#!/usr/bin/env python3
"""Local preview of a Slides deck: renders each slide at 1920x1080 and builds a contact sheet.
Usage: python3 render.py <deck_root> <out_prefix> [slide_id ...]
"""
import json, sys, os, re, asyncio
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw

root, out = sys.argv[1], sys.argv[2]
only = sys.argv[3:]
idx = json.load(open(os.path.join(root, 'project/deck.json')))
css = open(os.path.join(root, 'project/deck.css')).read()
order = [s for s in idx['order'] if (not only or s in only)]
links = ''.join(f'<link rel="stylesheet" href="{f["href"]}">' for f in idx.get('faces', {}).values() if 'href' in f)
secs = []
for sid in order:
    p = os.path.join(root, 'project/slides', sid + '.html')
    if os.path.exists(p):
        h = open(p).read()
        h = re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)
        bm = os.path.join(root, 'blobmap.json')
        if os.path.exists(bm):
            for k, v in json.load(open(bm)).items():
                v = v if os.path.isabs(v) else os.path.abspath(os.path.join(root, v))
                h = h.replace(k, 'file://' + v)
        secs.append((sid, h))
harness = """
body{margin:0;counter-reset:page;}
section{width:1920px;height:1080px;position:relative;overflow:hidden;}
x-icon{display:inline-block;width:48px;height:48px;background:rgba(252,160,16,.35);border-radius:10px;}
x-shape{display:block;}
.wrap{width:1920px;height:1080px;position:relative;overflow:hidden;}
.wrap::after{content:'';position:absolute;left:0;top:920px;width:1920px;height:1px;background:rgba(255,0,0,.5);}
"""
html = '<!doctype html><html><head><meta charset="utf-8">' + links + '<style>' + css + harness + '</style></head><body>'
for sid, h in secs:
    html += f'<div class="wrap" id="w-{sid}">{h}</div>'
html += '</body></html>'
open(out + '.html', 'w').write(html)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=0.5)
        await pg.goto('file://' + os.path.abspath(out + '.html'))
        await pg.wait_for_timeout(2500)
        files = []
        for sid, _ in secs:
            el = await pg.query_selector(f'#w-{sid}')
            f = f'{out}-{sid}.png'
            await el.screenshot(path=f)
            # overflow check: content bottom of flow children
            info = await pg.evaluate("""(sid)=>{const s=document.querySelector('#w-'+sid+' section');
              let maxB=0; const r0=s.getBoundingClientRect();
              s.querySelectorAll('*').forEach(e=>{const st=getComputedStyle(e); if(e.closest('.footer')||e.closest('svg')) return;
                const r=e.getBoundingClientRect(); if(r.width>0&&r.height>0) maxB=Math.max(maxB,r.bottom-r0.top);});
              return {maxBottom: Math.round(maxB), sw: s.scrollWidth, sh: s.scrollHeight};}""", sid)
            print(sid, info)
            files.append(f)
        await b.close()
    ims = [Image.open(f) for f in files]
    w, h = ims[0].size
    cols = 3
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (w + 8), rows * (h + 8)), 'white')
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * (w + 8), (i // cols) * (h + 8)))
    sheet.save(out + '-sheet.png')
    print('sheet', sheet.size)

asyncio.run(main())

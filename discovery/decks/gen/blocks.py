# Slide builders shared by the BRG and Toho Gas decks.
# Every builder returns one <section> string. Connectors are always flow boxes.
import re
from lib import ic, head, section, hdrow, arrow, vtimeline, shot


def chk(text, cls='cap', icon='CheckCircle'):
    return ('<div class="hd" style="gap:12px;align-items:flex-start"><x-icon name="%s" style="width:30px;height:30px;'
            'color:#A85A00;flex:none"></x-icon><p class="%s" style="flex:1;color:#14203C">%s</p></div>') % (icon, cls, text)


def overview_slide(sid, eyebrow, title, lead, questions, flows_label, flows, aside, foot, phases=None):
    """questions: 4 x (icon, question, answer). flows: list of (num, name, tag, roles, desc)."""
    q = []
    for i, (icon, ques, ans) in enumerate(questions):
        if i:
            q.append(arrow('arrow-s', style='align-self:center'))
        q.append('<div class="card" style="flex:1;gap:10px;padding:22px 24px">%s<h3 class="h3">%s</h3><p class="t">%s</p></div>' % (ic(icon), ques, ans))
    cols = len(flows)
    f = []
    if phases:  # header cells that span the flow columns of each phase
        col = 1
        for label, span in phases:
            f.append('<div style="grid-column:%d / %d;border-bottom:3px solid #FCA010;padding-bottom:6px"><p class="lbl">%s</p></div>' % (col, col + span, label))
            col += span
    h3 = ' style="font-size:34px"' if cols > 3 else ''
    for num, name, tag, roles, desc in flows:
        tg = ('<p class="pill soft" style="align-self:flex-start;padding:4px 14px">%s</p>' % tag) if tag else ''
        f.append('<div class="card navy" style="gap:8px;padding:22px 24px">%s<div class="hd"><p class="num">%s</p><h3 class="h3"%s>%s</h3></div>'
                 '<p class="k">%s</p><p class="t">%s</p></div>' % (tg, num, h3, name, roles, desc))
    inner = head(eyebrow, title, lead) + '''<div class="content">
<div class="row" style="gap:12px;align-items:stretch">
%s
</div>
%s
<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:20px;row-gap:12px">
%s
</div>
</div>
''' % ('\n'.join(q), ('<p class="lbl">%s</p>' % flows_label) if flows_label else '', cols, '\n'.join(f))
    return section(sid, inner, aside, foot)


def roles_slide(sid, eyebrow, title, shot_html, roles, aside, foot):
    """roles: list of (icon, name, desc, navy_bool)."""
    tiles = []
    for icon, name, desc, navy in roles:
        tiles.append('<div class="role%s">%s<div class="rt"><p class="tb">%s</p><p class="cap">%s</p></div></div>' % (
            ' navy' if navy else '', ic(icon, 'sm'), name, desc))
    inner = head(eyebrow, title) + '''<div class="content">
<div class="row" style="gap:40px;align-items:flex-start">
%s
<div class="roles" style="flex:1">
%s
</div>
</div>
</div>
''' % (shot_html, '\n'.join(tiles))
    return section(sid, inner, aside, foot)


def flow_slide(sid, eyebrow, title, shot_html, steps, legend, aside, foot, extra_left=''):
    """steps: list of (name, who, approval_bool)."""
    inner = head(eyebrow, title) + '''<div class="content">
<div class="row" style="gap:56px;align-items:flex-start">
<div class="col" style="width:860px;flex:none;gap:20px">
%s
%s
</div>
<div class="col" style="flex:1;gap:4px">
%s
<p class="cap">%s</p>
</div>
</div>
</div>
''' % (shot_html, extra_left, vtimeline(steps), legend)
    return section(sid, inner, aside, foot)


def arch_slide(sid, eyebrow, title, rows, gov_title, gov_items, aside, foot):
    """rows: 5 x (label, sub, nodes, kind) with kind in ('', 'core');
    a node is 'text', ('text', 'x') for the core extension, or ('text', 'o') for a tinted node.
    gov_items: list of (icon, text) for the cross-cutting governance column."""
    bands = []
    for label, sub, nodes, kind in rows:
        core = kind == 'core'
        nd = []
        for n in nodes:
            if isinstance(n, tuple):
                nd.append('<p class="nd %s">%s</p>' % (n[1], n[0]))
            else:
                nd.append('<p class="nd">%s</p>' % n)
        bands.append('<div class="ly%s"><div class="ly-t"><p class="lbl">%s</p><p class="cap">%s</p></div><div class="ly-n">%s</div></div>' % (
            ' core' if core else '', label, sub, ''.join(nd)))
    gov = ''.join(chk(t, icon=i) for i, t in gov_items)
    link = ('<div class="lyc">%s%s</div>' % (arrow('lya', 'arrow-up'), arrow('lya', 'arrow-down')))
    inner = head(eyebrow, title) + '''<div class="content">
<div class="row" style="gap:16px;align-items:stretch">
<div class="col" style="flex:1;gap:0">
%s
</div>
<div class="gov"><div><p class="lbl">%s</p><p class="cap">Áp dụng cho mọi lớp</p></div>%s</div>
</div>
</div>
''' % (('\n' + link + '\n').join(bands), gov_title, gov)
    return section(sid, inner, aside, foot)


def _df_box(n, name, desc, kind):
    cls = ' ' + kind if kind else ''
    return ('<div class="df-box%s"><div class="hd" style="gap:12px"><p class="df-n">%d</p><p class="tb">%s</p></div>'
            '<p class="cap">%s</p></div>') % (cls, n, name, desc)


def _df_row(boxes):
    out = []
    for i, b in enumerate(boxes):
        if i:
            out.append('<div class="df-gap">%s</div>' % arrow('arrow-s'))
        out.append(b)
    return '<div class="df-row">%s</div>' % ''.join(out)


def _bend_svg(x1, x2, h, color, label, up=False, dash=False):
    """In-flow return line in its own strip: from x1 (top edge) to x2, rounded corners.
    up=False: starts at the top edge at x1, ends with a head at the bottom edge at x2.
    up=True : starts at the top edge at x1 and comes back up into the top edge at x2."""
    r = 14
    y = h / 2.0
    s = -1 if x2 < x1 else 1
    da = ' stroke-dasharray="10 8"' if dash else ''
    head_len = 9
    if not up:
        d = 'M%d 0 V%g Q%d %g %g %g H%g Q%d %g %d %g V%g' % (x1, y - r, x1, y, x1 + s * r, y, x2 - s * r, x2, y, x2, y + r, h - head_len)
        tip = 'M%d %d L%d %d L%d %d Z' % (x2 - 8, h - head_len, x2 + 8, h - head_len, x2, h)
    else:
        d = 'M%d 0 V%g Q%d %g %g %g H%g Q%d %g %d %g V%d' % (x1, y - r, x1, y, x1 + s * r, y, x2 - s * r, x2, y, x2, y - r, head_len)
        tip = 'M%d %d L%d %d L%d %d Z' % (x2 - 8, head_len, x2 + 8, head_len, x2, 0)
    return ('<svg width="1664" height="%d" viewBox="0 0 1664 %d" aria-label="%s"><path d="%s" fill="none" stroke="%s" '
            'stroke-width="3" stroke-linejoin="round"%s/><path d="%s" fill="%s"/></svg>') % (h, h, label, d, color, da, tip, color)


def dataflow_slide(sid, eyebrow, title, stages, loop_label, band, aside, foot):
    """stages: 8 x (name, desc, kind) with kind in ('', 'ap', 'core'). Two rows of four,
    joined by a return strip; a feedback strip runs from stage 8 back to stage 6."""
    boxes = [_df_box(i + 1, n, d, k) for i, (n, d, k) in enumerate(stages)]
    cx = [187, 617, 1047, 1477]
    inner = head(eyebrow, title) + '''<div class="content" style="gap:16px">
<div class="df">
%s
%s
%s
%s
</div>
<div class="row" style="gap:0"><div style="width:617px;flex:none"></div><p class="cap" style="width:860px;flex:none;text-align:center;color:#A85A00;font-weight:600">%s</p></div>
<div class="band" style="padding:20px 28px"><div class="hd"><p class="lbl">NGUYÊN TẮC</p><p class="t" style="flex:1">%s</p></div></div>
</div>
''' % (_df_row(boxes[:4]),
       _bend_svg(cx[3], cx[0], 48, '#8A93A6', 'Chặng 4 nối sang chặng 5'),
       _df_row(boxes[4:]),
       _bend_svg(cx[3], cx[1], 48, '#FCA010', 'Phản hồi từ chặng 8 về chặng 6', up=True, dash=True),
       loop_label, band)
    return section(sid, inner, aside, foot)


def ai_slide(sid, eyebrow, title, chain, principles, band_label, band, aside, foot):
    """chain: 4 x (text, navy_bool). principles: 5 x (icon, title, desc)."""
    c = []
    for i, (t, navy) in enumerate(chain):
        if i:
            c.append(arrow('arrow-s', style='align-self:center'))
        c.append('<div class="card%s" style="flex:1;padding:18px 22px"><div class="hd"><p class="num%s">%d</p><p class="tb"%s>%s</p></div></div>' % (
            ' navy' if navy else '', '', i + 1, ' style="color:#F3F4F7"' if navy else '', t))
    p = ''.join('<div class="card" style="gap:12px">%s<p class="tb">%s</p><p class="cap">%s</p></div>' % (ic(i), t, d) for i, t, d in principles)
    inner = head(eyebrow, title) + '''<div class="content">
<div class="row" style="gap:12px;align-items:stretch">
%s
</div>
<p class="lbl">NĂM NGUYÊN TẮC</p>
<div class="g5">
%s
</div>
<div class="band" style="padding:20px 28px"><div class="hd"><p class="lbl">%s</p><p class="t" style="flex:1">%s</p></div></div>
</div>
''' % ('\n'.join(c), p, band_label, band)
    return section(sid, inner, aside, foot)




def compliance_slide(sid, eyebrow, title, cols, note, aside, foot, feat_h=216):
    """cols: 3 x dict(icon, theme, laws[list], req, visual(html or ''), feats[list]).
    The requirement grows to fill, so the arrows and feature boxes line up across columns."""
    out = []
    for c in cols:
        laws = ''.join('<p class="lawtag">%s</p>' % l for l in c['laws'])
        feats = ''.join(chk(f) for f in c['feats'])
        out.append('''<div class="law">
<div class="hd">%s<h3 class="h3">%s</h3></div>
<div class="col" style="gap:8px">%s</div>
<p class="t" style="flex:1">%s</p>
%s
<div class="feat" style="min-height:%dpx"><p class="lbl">TRONG TALENT FLOW</p>%s%s</div>
</div>''' % (ic(c['icon'], 'sm'), c['theme'], laws, c['req'], arrow('arrow-d', 'arrow-down'), feat_h, c.get('visual', ''), feats))
    inner = head(eyebrow, title) + '''<div class="content" style="gap:20px">
<div class="g3" style="align-items:stretch">
%s
</div>
<p class="note">%s</p>
</div>
''' % ('\n'.join(out), note)
    return section(sid, inner, aside, foot)


def problems_slide(sid, eyebrow, title, rows, note, aside, foot):
    """rows: 7 x (code, name, evidence, level)."""
    tr = ['<tr class="h"><th style="width:6%">#</th><th style="width:30%">Vấn đề</th><th style="width:50%">Biểu hiện, bằng chứng hiện có</th><th style="width:14%">Mức chắc chắn</th></tr>']
    for i, (code, name, ev, lv) in enumerate(rows):
        tr.append('<tr%s><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (' class="z"' if i % 2 else '', code, name, ev, lv))
    inner = head(eyebrow, title) + '''<div class="content">
<table class="tbl tight">
%s
</table>
<p class="note">%s</p>
</div>
''' % ('\n'.join(tr), note)
    return section(sid, inner, aside, foot)


def migrate(old_dir, old_id, new_id, eyebrow=None, title=None):
    """Re-use an existing slide file under a new id; optionally replace its eyebrow and title."""
    h = open('%s/%s.html' % (old_dir, old_id), encoding='utf-8').read()
    h = h.replace('<section id="%s"' % old_id, '<section id="%s"' % new_id, 1)
    if eyebrow:
        h = re.sub(r'<p class="eyebrow">.*?</p>', '<p class="eyebrow">%s</p>' % eyebrow, h, count=1)
    if title:
        h = re.sub(r'<h2 class="title">.*?</h2>', '<h2 class="title">%s</h2>' % title, h, count=1)
    return h


def system_arch_slide(sid, eyebrow, title, users, channels, modules, ai, data, integ, systems, gov, infra, aside, foot):
    """Overall architecture: users -> Talent Flow (modules, AI, data, integration) -> existing systems,
    plus governance and infrastructure bands. Items: 'text' or ('text', cls) with cls in o/k."""
    def chips(items):
        out = []
        for it in items:
            if isinstance(it, tuple):
                out.append('<p class="nd %s">%s</p>' % (it[1], it[0]))
            else:
                out.append('<p class="nd">%s</p>' % it)
        return ''.join(out)
    link = '<div class="lyc">%s%s</div>' % (arrow('lya', 'arrow-up'), arrow('lya', 'arrow-down'))
    mods = ''.join('<p class="nd o">%s</p>' % m for m in modules)
    inner = head(eyebrow, title) + '''<div class="content" style="gap:0">
<div class="sa-band"><p class="lbl sa-l">NGƯỜI DÙNG</p>%s%s</div>
%s
<div class="sa-plat">
<div class="sa-tab"><p class="lbl">TALENT FLOW</p><p class="cap">Nền tảng đề xuất</p></div>
<div class="col" style="flex:1;gap:8px">
<div class="sa-row"><p class="sa-rl">NGHIỆP VỤ</p><div class="sa-mods">%s</div></div>
<div class="sa-row"><p class="sa-rl">DỊCH VỤ AI</p><div class="sa-chips">%s</div></div>
<div class="sa-row"><p class="sa-rl">DỮ LIỆU</p><div class="sa-chips">%s</div></div>
<div class="sa-row"><p class="sa-rl">TÍCH HỢP</p><div class="sa-chips">%s</div></div>
</div>
</div>
%s
<div class="sa-band"><p class="lbl sa-l">HỆ THỐNG HIỆN CÓ</p>%s</div>
<div class="g2" style="margin-top:12px">
<div class="band" style="padding:14px 22px;gap:4px"><p class="lbl">QUẢN TRỊ VÀ BẢO MẬT</p><p class="t">%s</p></div>
<div class="band" style="padding:14px 22px;gap:4px"><p class="lbl">HẠ TẦNG</p><p class="t">%s</p></div>
</div>
</div>
''' % (chips(users), chips([(c, 'o') for c in channels]), link, mods, chips(ai), chips(data), chips(integ),
       link, chips(systems), gov, infra)
    return section(sid, inner, aside, foot)


# Cover art: four input bubbles on the upper orbit flow into the skill core; two output bubbles below.
# Labels sit inside the bubbles. Inside the single backdrop <svg> the paint order is ring, streams, bubbles,
# so no stroke is drawn over a bubble; label <p>s are pinned on top, centred in each bubble.
import math as _m
_CV_O = (960, 120)                 # svg origin (canvas px), size 832 x 780
_CV_C = (1376, 510)                # core centre (canvas px)
_CV_R_CORE, _CV_R_IN, _CV_R_OUT = 88, 95, 110
_CV_IN_ANG = [-150, -110, -70, -30]
_CV_OUT_ANG = [120, 60]


def _cv_pt(ang, dist):
    return (_CV_C[0] + dist * _m.cos(_m.radians(ang)), _CV_C[1] + dist * _m.sin(_m.radians(ang)))


def _cv_stream(a, b, bend):
    """Cubic from a to b with a gentle sideways bend; returns (d, approx length)."""
    ux, uy = b[0] - a[0], b[1] - a[1]
    L = (ux * ux + uy * uy) ** 0.5
    px, py = -uy / L * bend, ux / L * bend
    p1 = (a[0] + ux * 0.35 + px, a[1] + uy * 0.35 + py)
    p2 = (a[0] + ux * 0.65 + px, a[1] + uy * 0.65 + py)
    d = 'M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f' % (a[0], a[1], p1[0], p1[1], p2[0], p2[1], b[0], b[1])
    return d, L + abs(bend)


def cover_slide(sid, eyebrow, title_html, sub, inputs, outputs, foot_left, aside, core_label='Kỹ năng'):
    """inputs: 4 labels (use <br> for two lines); outputs: 2 labels. Text sits inside the circles."""
    ox, oy = _CV_O
    S = lambda p: (p[0] - ox, p[1] - oy)
    C = S(_CV_C)
    nin = [S(_cv_pt(a, 300)) for a in _CV_IN_ANG]
    nout = [S(_cv_pt(a, 290)) for a in _CV_OUT_ANG]
    defs = ('<defs><radialGradient id="halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FCA010" stop-opacity="0.20"/>'
            '<stop offset="1" stop-color="#FCA010" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="core" cx="0.5" cy="0.4" r="0.6"><stop offset="0" stop-color="#2C3E6B"/><stop offset="1" stop-color="#14203C"/></radialGradient>'
            '<radialGradient id="bub" cx="0.5" cy="0.35" r="0.65"><stop offset="0" stop-color="#2C3E6B"/><stop offset="1" stop-color="#1A2850"/></radialGradient>'
            '<radialGradient id="obub" cx="0.5" cy="0.35" r="0.65"><stop offset="0" stop-color="#FFB733"/><stop offset="1" stop-color="#F29400"/></radialGradient>'
            '</defs>')
    back = ('<circle cx="%.1f" cy="%.1f" r="250" fill="url(#halo)"/>'
            '<circle cx="%.1f" cy="%.1f" r="300" fill="none" stroke="#3A4C7A" stroke-opacity="0.7" stroke-width="1.5" stroke-dasharray="3 9"/>') % (C + C)
    streams = []
    for n in nin:
        ux, uy = C[0] - n[0], C[1] - n[1]
        L = (ux * ux + uy * uy) ** 0.5
        ux, uy = ux / L, uy / L
        a = (n[0] + ux * _CV_R_IN, n[1] + uy * _CV_R_IN)
        b = (C[0] - ux * _CV_R_CORE, C[1] - uy * _CV_R_CORE)
        d, ln = _cv_stream(a, b, 16 if n[0] < C[0] else -16)
        k = int(ln) + 12
        streams.append('<path d="%s" fill="none" stroke="#6F82B0" stroke-opacity="0.2" stroke-width="12" stroke-linecap="round"/>'
                       '<path d="%s" fill="none" stroke="#9AAAD0" stroke-width="3" stroke-linecap="round" stroke-dasharray="%d">'
                       '<animate attributeName="stroke-dashoffset" values="%d;0" dur="0.9s" begin="0s"/></path>' % (d, d, k, k))
    for n in nout:
        ux, uy = n[0] - C[0], n[1] - C[1]
        L = (ux * ux + uy * uy) ** 0.5
        ux, uy = ux / L, uy / L
        a = (C[0] + ux * _CV_R_CORE, C[1] + uy * _CV_R_CORE)
        b = (n[0] - ux * _CV_R_OUT, n[1] - uy * _CV_R_OUT)
        d, ln = _cv_stream(a, b, 14 if n[0] < C[0] else -14)
        k = int(ln) + 12
        streams.append('<path d="%s" fill="none" stroke="#FCA010" stroke-opacity="0.18" stroke-width="16" stroke-linecap="round"/>'
                       '<path d="%s" fill="none" stroke="#FCA010" stroke-width="4" stroke-linecap="round" stroke-dasharray="%d">'
                       '<animate attributeName="stroke-dashoffset" values="%d;%d;0" dur="1.6s" begin="0s"/></path>' % (d, d, k, k, k))
    core = ('<circle cx="%.1f" cy="%.1f" r="%d" fill="url(#core)" stroke="#FCA010" stroke-width="5"/>'
            '<circle cx="%.1f" cy="%.1f" r="74" fill="none" stroke="#FCA010" stroke-opacity="0.35" stroke-width="1.5"/>') % (
        C[0], C[1], _CV_R_CORE, C[0], C[1])
    bubbles = ''.join('<circle cx="%.1f" cy="%.1f" r="%d" fill="none" stroke="#6F82B0" stroke-opacity="0.3" stroke-width="2"/>'
                      '<circle cx="%.1f" cy="%.1f" r="%d" fill="url(#bub)" stroke="#6F82B0" stroke-width="2"/>' % (
                          n[0], n[1], _CV_R_IN + 6, n[0], n[1], _CV_R_IN) for n in nin)
    bubbles += ''.join('<circle cx="%.1f" cy="%.1f" r="%d" fill="none" stroke="#FCA010" stroke-opacity="0.35" stroke-width="2"/>'
                       '<circle cx="%.1f" cy="%.1f" r="%d" fill="url(#obub)"/>' % (
                           n[0], n[1], _CV_R_OUT + 12, n[0], n[1], _CV_R_OUT) for n in nout)
    sparks = ''.join('<circle cx="%.1f" cy="%.1f" r="%s" fill="#BFC8DA" fill-opacity="%s"/>' % (C[0] + dx, C[1] + dy, r, o) for dx, dy, r, o in [
        (-205, -40, '2.5', '0.5'), (205, -40, '2.5', '0.5'), (-150, 120, '2', '0.4'), (150, 120, '2', '0.4'), (0, -170, '2', '0.45'), (0, 170, '2', '0.4')])
    svg = ('<svg style="position:absolute;left:%dpx;top:%dpx" width="832" height="780" viewBox="0 0 832 780" '
           'aria-label="Bốn thành phần nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp và AI hội về kỹ năng, '
           'tạo ra phát triển nghề nghiệp và điều chuyển nhân lực nội bộ">%s%s%s%s%s%s</svg>') % (
        ox, oy, defs, back, ''.join(streams), core, bubbles, sparks)
    labs = []
    for i, (a, lab) in enumerate(zip(_CV_IN_ANG, inputs)):
        x, y = _cv_pt(a, 300)
        lines = lab.count('<br>') + 1
        labs.append('<p class="cv-in" style="left:%dpx;top:%dpx;animation-delay:%dms">%s</p>' % (
            round(x) - 87, round(y - lines * 15), 150 + 120 * i, lab))
    labs.append('<p class="cv-core" style="left:%dpx;top:%dpx;animation-delay:650ms">%s</p>' % (_CV_C[0] - 80, _CV_C[1] - 20, core_label))
    for i, (a, lab) in enumerate(zip(_CV_OUT_ANG, outputs)):
        x, y = _cv_pt(a, 290)
        lines = lab.count('<br>') + 1
        labs.append('<p class="cv-out" style="left:%dpx;top:%dpx;animation-delay:%dms">%s</p>' % (
            round(x) - 102, round(y - lines * 15), 1000 + 150 * i, lab))
    inner = '''%s
<div class="cv-text" style="width:800px">
<p class="eyebrow">%s</p>
<h1 class="cv-title">%s</h1>
<div class="bar"></div>
<p class="cv-sub">%s</p>
</div>
%s
''' % (svg, eyebrow, title_html, sub, '\n'.join(labs))
    return section(sid, inner, aside, '<div class="footer"><p class="fl">%s</p><p class="fr"></p></div>' % foot_left,
                   cls='dark cover', attrs='data-transition="fade"')

# Helpers to generate Slides-type slide files (one <section> per file).
# Rule for every diagram here: connectors are flow boxes (div lines or in-flow <svg>)
# that sit BETWEEN components. Nothing is pinned over a component.
import os, html

SVG_ICONS = {
    'bank': '<path d="M3 10h18M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18M12 3l9 5H3z"/>',
    'cart': '<path d="M3 4h2.5l2.2 10.5h10.6L20.5 7H7"/><circle cx="10" cy="19" r="1.6"/><circle cx="17" cy="19" r="1.6"/>',
    'golf': '<path d="M7 21V3l10 4-10 4"/><path d="M4 21h9"/>',
    'city': '<path d="M3 21h18M5 21V9l5-3v15M10 21V4l6 3v14M16 21v-8h3v8"/>',
    'flame': '<path d="M12 3c.8 3.8 6 5.8 6 11a6 6 0 0 1-12 0c0-2.8 1.6-4.1 2.2-6.4 1.6 1 2.6 2.6 3.2 4.4.9-2.8.6-5.9.6-9z"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'leaf': '<path d="M5 19C5 10 11 5 20 5c0 9-5 15-14 15"/><path d="M5 19l7-7"/>',
    'headset': '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1"/><rect x="17" y="14" width="4" height="6" rx="1"/>',
    'gauge': '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/>',
    'helmet': '<path d="M3 17h18M5 17a7 7 0 0 1 14 0M12 7v4"/>',
    'ban': '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
    'scale': '<path d="M12 3v18M5 7h14M8 21h8M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
    'graph': '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="7" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M8.4 6.4l7.2.4M7.1 8.3l3.8 7.5M17 9.3l-3.9 6.4"/>',
    'swap': '<path d="M4 8h15l-4-4M20 16H5l4 4"/>',
    'flag': '<path d="M5 21V4h11l-2 4 2 4H5"/>',
    'chip': '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    'route': '<circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H15a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h6.5"/>',
}


def ic(name, cls='', label=''):
    """Orange round icon chip. name: x-icon name, or 'svg:<key>' for custom icons."""
    c = ('ic ' + cls).strip()
    if name.startswith('svg:'):
        key = name[4:]
        lab = html.escape(label or key)
        inner = ('<svg viewBox="0 0 24 24" width="24" height="24" aria-label="%s"><g fill="none" stroke="#14203C" stroke-width="2" '
                 'stroke-linecap="round" stroke-linejoin="round">%s</g></svg>') % (lab, SVG_ICONS[key])
    else:
        inner = '<x-icon name="%s"></x-icon>' % name
    return '<div class="%s">%s</div>' % (c, inner)


def footer(left):
    return '<div class="footer"><p class="fl">%s</p><p class="fr"></p></div>' % left


def head(eyebrow, title, lead=None):
    h = '<p class="eyebrow">%s</p>\n<h2 class="title">%s</h2>\n<div class="bar"></div>\n' % (eyebrow, title)
    if lead:
        h += '<p class="lead">%s</p>\n' % lead
    return h


def section(sid, inner, aside, foot, cls='', attrs=''):
    c = (' class="%s"' % cls) if cls else ''
    a = (' ' + attrs) if attrs else ''
    return '<section id="%s"%s%s>\n%s%s\n<aside>%s</aside>\n</section>\n' % (sid, c, a, inner, foot, aside)


def hdrow(icon, text, cls='t', label='', icls='sm'):
    return '<div class="hd">%s<p class="%s" style="flex:1">%s</p></div>' % (ic(icon, icls, label), cls, text)


def arrow(cls='arrow-s', kind='arrow-right', style=''):
    st = (' style="%s"' % style) if style else ''
    return '<x-shape kind="%s" class="%s"%s></x-shape>' % (kind, cls, st)


def timeline(steps):
    """Horizontal timeline. steps: list of (dot_text, name, desc, approval_bool).
    Each step owns the line to its left and right; lines end at the dot's edge."""
    n = len(steps)
    out = ['<div class="tl">']
    for i, (dot, name, desc, ap) in enumerate(steps):
        lft = 'tl-ln off' if i == 0 else 'tl-ln'
        rgt = 'tl-ln off' if i == n - 1 else 'tl-ln'
        out.append('<div class="tl-step"><div class="tl-top"><div class="%s"></div><p class="tl-dot%s">%s</p>'
                   '<div class="%s"></div></div><p class="tl-name">%s</p>%s</div>' % (
                       lft, ' ap' if ap else '', dot, rgt, name, ('<p class="tl-desc">%s</p>' % desc) if desc else ''))
    out.append('</div>')
    return '\n'.join(out)


def vtimeline(steps):
    """Vertical timeline. steps: list of (name, who, approval_bool).
    The rail segment is a flow box under each dot, inside the same row."""
    n = len(steps)
    out = ['<div class="vt">']
    for i, (name, who, ap) in enumerate(steps):
        ln = '<div class="vt-ln"></div>' if i < n - 1 else ''
        out.append('<div class="vt-step"><div class="vt-rail"><p class="vt-dot%s">%d</p>%s</div>'
                   '<div class="vt-body"><p class="vt-name">%s</p><p class="vt-who">%s</p></div></div>' % (
                       ' ap' if ap else '', i + 1, ln, name, who))
    out.append('</div>')
    return '\n'.join(out)


def shot(src, alt, w, h, cap):
    return ('<div class="col" style="width:%dpx;flex:none;gap:12px"><img class="shot" src="%s" alt="%s" '
            'style="width:%dpx;height:%dpx"><p class="cap">%s</p></div>') % (w, src, html.escape(alt), w, h, cap)


def rounded_bus(w, h, ends, side, color='#FCA010', sw=3, label='Đường nối'):
    """In-flow SVG that joins several edge points into one point with rounded elbows.
    side='left': lines start at x=0 (y in ends) and meet at (w, h/2).
    side='right': lines start at (0, h/2) and end at x=w (y in ends).
    The box sits in its own grid cell, so no line can cross a component."""
    m = h / 2.0
    xm = w / 2.0
    r = 12
    paths = []
    for y in ends:
        if abs(y - m) < 1:
            paths.append('M0 %g H%g' % (m, w))
            continue
        s = 1 if m > y else -1  # direction from y towards m
        if side == 'left':
            paths.append('M0 %g H%g Q%g %g %g %g V%g Q%g %g %g %g H%g' % (
                y, xm - r, xm, y, xm, y + s * r, m - s * r, xm, m, xm + r, m, w))
        else:
            paths.append('M0 %g H%g Q%g %g %g %g V%g Q%g %g %g %g H%g' % (
                m, xm - r, xm, m, xm, m - s * r, y + s * r, xm, y, xm + r, y, w))
    body = ''.join('<path d="%s"/>' % p for p in paths)
    return ('<svg width="%d" height="%d" viewBox="0 0 %d %d" aria-label="%s"><g fill="none" stroke="%s" '
            'stroke-width="%d" stroke-linecap="butt" stroke-linejoin="round">%s</g></svg>') % (
                w, h, w, h, html.escape(label), color, sw, body)


def write(root, sid, content):
    p = os.path.join(root, 'project', 'slides', sid + '.html')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    return p

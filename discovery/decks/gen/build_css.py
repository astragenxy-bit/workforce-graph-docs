# Rebuild project/deck.css = base rules (before the visual-components marker) + gen/visual.css
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for root in sys.argv[1:]:
    p = root + '/project/deck.css'
    s = open(p, encoding='utf-8').read()
    i = s.find('/* ===== Visual components')
    base = s[:i].rstrip() + '\n' if i >= 0 else s
    vis = open(os.path.join(HERE, 'visual.css'), encoding='utf-8').read()
    open(p, 'w', encoding='utf-8').write(base + vis)
    print(p, len(base), len(vis))

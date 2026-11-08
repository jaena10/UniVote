with open('build_full_univote.py', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find("localStorage.getItem('univote_has_voted')")
while idx != -1:
    print(c[max(0, idx-50):min(len(c), idx+350)])
    print('==============================')
    idx = c.find("localStorage.getItem('univote_has_voted')", idx+1)

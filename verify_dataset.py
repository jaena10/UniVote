import os
import json

base = r'D:\CODINGS\univote'

with open(r'build_full_univote.py', 'r', encoding='utf-8') as f:
    code = f.read()

start = code.find('candidates_data = [')
pos = start + len('candidates_data = ')
bracket_count = 0
end = -1
for i in range(pos, len(code)):
    if code[i] == '[':
        bracket_count += 1
    elif code[i] == ']':
        bracket_count -= 1
        if bracket_count == 0:
            end = i + 1
            break

candidates_data = json.loads(code[pos:end])
print(f"Total candidates in build_full_univote.py: {len(candidates_data)}")

missing_photos = []
unique_photos = set()
duplicates = []

for c in candidates_data:
    p = c['photo']
    if p in unique_photos:
        duplicates.append((c['id'], c['name'], p))
    unique_photos.add(p)
    
    full_p = os.path.join(base, p.lstrip('/'))
    if not os.path.exists(full_p):
        missing_photos.append((c['id'], c['name'], full_p))

if duplicates:
    print(f"ERROR: {len(duplicates)} duplicated photos found!")
    for d in duplicates[:5]:
        print(" ", d)
else:
    print("SUCCESS: Zero duplicate photos found across all candidates!")

if missing_photos:
    print(f"ERROR: {len(missing_photos)} missing photos!")
    for m in missing_photos[:5]:
        print(" ", m)
else:
    print(f"SUCCESS: ALL {len(candidates_data)} CANDIDATE PHOTOS VERIFIED TO EXIST ON DISK!")

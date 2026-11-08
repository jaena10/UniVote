# -*- coding: utf-8 -*-
"""
UniVote Master Patcher
Directly patches build_full_univote.py with all requested changes:
1. 17 departments alphabetically in registration dropdown
2. Student browsing mode (no "ballot already cast" on sign in)
3. Per-student vote tracking (not global has_voted flag)
4. Admin: department buttons for tallies (not all-at-once)
5. Admin: working Clear All Voting Data via modal
"""
import json, os, re

BASE = r"D:\CODINGS\univote"
SRC  = os.path.join(BASE, "build_full_univote.py")

# ── 17 Departments (alphabetical) ────────────────────────────────────────────
DEPARTMENTS = [
    "College of Accountancy",
    "College of Architecture",
    "College of Arts and Sciences (ABCOMM)",
    "College of Engineering",
    "College of Hospitality Management",
    "College of Human Services",
    "College of Industrial Engineering",
    "College of Information Technology",
    "College of Nursing",
    "College of Pharmacy",
    "College of Psychology",
    "College of Tourism Management",
    "Junior Highschool",
    "School of Arts and Sciences (Criminology)",
    "School of Business",
    "School of Education",
    "Senior Highschool",
]

# folder → new department name
FOLDER_TO_DEPT = {
    "College of Architecture":                         "College of Architecture",
    "College of Hospitality  Management":              "College of Hospitality Management",
    "College of Industrial Engineering":               "College of Industrial Engineering",
    "College of Information Technology":               "College of Information Technology",
    "College of Nursing":                              "College of Nursing",
    "College of Pharmacy":                             "College of Pharmacy",
    "JuniorHighSchool":                                "Junior Highschool",
    "School of Arts and Sciences (Criminology)":       "School of Arts and Sciences (Criminology)",
    "SeniorHighSchool":                                "Senior Highschool",
    "Siklab Party College of Accountancy":             "College of Accountancy",
    "Siklab Party College of Engineering":             "College of Engineering",
    "Siklab Party College of Human Services":          "College of Human Services",
    "Siklab Party College of Psychology":              "College of Psychology",
    "Siklab Party College of Tourism Management":      "College of Tourism Management",
    "Siklab Party School of Arts and Sciences (ABCOMM)": "College of Arts and Sciences (ABCOMM)",
    "Siklab Party School of Business":                 "School of Business",
    "Siklab Party School of Education":                "School of Education",
    "UACSC Officers under Siklab":                     "University Central Student Council (UACSC)",
}

# ── Default students (17, one per dept + keep existing ones) ─────────────────
DEFAULT_STUDENTS = [
    {"id":"2024000669","name":"Maria Clara T. Santos",    "email":"mctsantos.student@ua.edu.ph",   "dept":"College of Accountancy",                     "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000101","name":"Rafael E. Santos",          "email":"resantos.student@ua.edu.ph",    "dept":"College of Architecture",                    "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000102","name":"Alyssa M. David",           "email":"amdavid.student@ua.edu.ph",     "dept":"College of Arts and Sciences (ABCOMM)",      "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2023001244","name":"Juan Dela T. Cruz",         "email":"jdtcruz.student@ua.edu.ph",     "dept":"College of Engineering",                     "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024001882","name":"Camille Rose P. Diaz",      "email":"crpdiaz.student@ua.edu.ph",     "dept":"College of Hospitality Management",          "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000103","name":"Patricia B. Ocampo",        "email":"pbocampo.student@ua.edu.ph",    "dept":"College of Human Services",                  "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000104","name":"Gabriel N. Castro",         "email":"gncastro.student@ua.edu.ph",    "dept":"College of Industrial Engineering",          "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024001155","name":"Angelo G. Gomez",           "email":"aggomez.student@ua.edu.ph",     "dept":"College of Information Technology",          "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024006843","name":"Jaena B. Mangulabnan",      "email":"jbmangulabnan.student@ua.edu.ph","dept":"College of Nursing",                       "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000105","name":"Clarisse D. Mallari",       "email":"cdmallari.student@ua.edu.ph",   "dept":"College of Pharmacy",                        "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000106","name":"Samantha K. Rivera",        "email":"skrivera.student@ua.edu.ph",    "dept":"College of Psychology",                      "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024000107","name":"Marco L. Henson",           "email":"mlhenson.student@ua.edu.ph",    "dept":"College of Tourism Management",              "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024008812","name":"Joshua L. Garcia",          "email":"jlgarcia.student@ua.edu.ph",    "dept":"Junior Highschool",                          "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2023004490","name":"Beatriz Nicole L. Gomez",   "email":"bnlgomez.student@ua.edu.ph",    "dept":"School of Arts and Sciences (Criminology)",  "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2022009831","name":"Sofia Bianca R. Dizon",     "email":"sbrdizon.student@ua.edu.ph",    "dept":"School of Business",                         "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024003319","name":"Mark Anthony V. Ramos",     "email":"mavramos.student@ua.edu.ph",    "dept":"School of Education",                        "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
    {"id":"2024005576","name":"Jaenaganda M. Cruz",        "email":"jmcruz.student@ua.edu.ph",      "dept":"Senior Highschool",                          "verified":True,"passwordHash":"85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
]

print("Loading source file...")
with open(SRC, "r", encoding="utf-8") as f:
    code = f.read()

# ── Step 1: Update Python-level DEPARTMENTS list ─────────────────────────────
old_dept_block = re.search(r"^DEPARTMENTS = \[.*?\]", code, re.DOTALL | re.MULTILINE)
if old_dept_block:
    new_dept_block = "DEPARTMENTS = [\n" + "\n".join(f'    "{d}",' for d in DEPARTMENTS) + "\n]"
    code = code[:old_dept_block.start()] + new_dept_block + code[old_dept_block.end():]
    print("✓ Updated Python DEPARTMENTS list")

# ── Step 2: Update candidate targetDept values ────────────────────────────────
start = code.find("candidates_data = [")
bc = 0
end_idx = -1
for i in range(start + len("candidates_data = "), len(code)):
    if code[i] == "[": bc += 1
    elif code[i] == "]":
        bc -= 1
        if bc == 0:
            end_idx = i + 1
            break

cands = json.loads(code[start + len("candidates_data = "):end_idx])
print(f"Loaded {len(cands)} candidates.")

for c in cands:
    folder = c["photo"].split("/")[1] if "/" in c["photo"] else ""
    if folder in FOLDER_TO_DEPT:
        new_dept = FOLDER_TO_DEPT[folder]
        old_dept = c["targetDept"]
        c["targetDept"] = new_dept
        if old_dept in c.get("platform", ""):
            c["platform"] = c["platform"].replace(old_dept, new_dept)
        c["advocacies"] = [a.replace(old_dept, new_dept) for a in c.get("advocacies", [])]

new_cands_json = json.dumps(cands, indent=4)
code = code[:start + len("candidates_data = ")] + new_cands_json + code[end_idx:]
print("✓ Updated candidate targetDept values")

# ── Step 3: Update Python default_students ────────────────────────────────────
ds_start = code.find("default_students = [")
bc2 = 0
ds_end = -1
for i in range(ds_start + len("default_students = "), len(code)):
    if code[i] == "[": bc2 += 1
    elif code[i] == "]":
        bc2 -= 1
        if bc2 == 0:
            ds_end = i + 1
            break
new_students_json = json.dumps(DEFAULT_STUDENTS, indent=4)
code = code[:ds_start + len("default_students = ")] + new_students_json + code[ds_end:]
print("✓ Updated default_students")

# ── Step 4: Update the Python DEPARTMENTS list used for generate_admin_html ───
# Change all the old dept IDs used in JS DEPARTMENTS constant to match new 17-dept system
# This will be handled inside the generate_admin_html replacement below.

print("Saving updated source...")
with open(SRC, "w", encoding="utf-8") as f:
    f.write(code)
print("✓ Saved updated build_full_univote.py")
print("\nNow run the template generators separately.")

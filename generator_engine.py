# -*- coding: utf-8 -*-
"""
UniVote HTML Generator Engine
Builds the complete generate_student_html() and generate_admin_html() functions
and generates the full build_full_univote.py script.
"""
import json
import os

def get_dept_options_html(departments):
    return "\n".join([f'                        <option value="{d}">{d}</option>' for d in departments])

def build_generator_script():
    base_dir = r"D:\CODINGS\univote"
    
    # 17 Departments in exact alphabetical order
    departments = [
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
        "Senior Highschool"
    ]
    
    positions = [
        {"id": "pres", "name": "President"},
        {"id": "vp", "name": "Vice President"},
        {"id": "sec", "name": "Secretary"},
        {"id": "tres", "name": "Treasurer"},
        {"id": "aud", "name": "Auditor"},
        {"id": "pro", "name": "Public Relations Officer (PRO)"}
    ]

    dept_options = get_dept_options_html(departments)
    
    # Load candidate data from source
    with open(os.path.join(base_dir, 'build_full_univote.py'), 'r', encoding='utf-8') as f:
        source = f.read()

    start = source.find('candidates_data = [') + len('candidates_data = ')
    bracket_count = 0
    for i in range(start, len(source)):
        if source[i] == '[': bracket_count += 1
        elif source[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end = i + 1
                break
    candidates = json.loads(source[start:end])

    dept_map = {
        'College of Architecture': 'College of Architecture',
        'College of Hospitality  Management': 'College of Hospitality Management',
        'College of Industrial Engineering': 'College of Industrial Engineering',
        'College of Information Technology': 'College of Information Technology',
        'College of Nursing': 'College of Nursing',
        'College of Pharmacy': 'College of Pharmacy',
        'JuniorHighSchool': 'Junior Highschool',
        'School of Arts and Sciences (Criminology)': 'School of Arts and Sciences (Criminology)',
        'SeniorHighSchool': 'Senior Highschool',
        'Siklab Party College of Accountancy': 'College of Accountancy',
        'Siklab Party College of Engineering': 'College of Engineering',
        'Siklab Party College of Human Services': 'College of Human Services',
        'Siklab Party College of Psychology': 'College of Psychology',
        'Siklab Party College of Tourism Management': 'College of Tourism Management',
        'Siklab Party School of Arts and Sciences (ABCOMM)': 'College of Arts and Sciences (ABCOMM)',
        'Siklab Party School of Business': 'School of Business',
        'Siklab Party School of Education': 'School of Education',
        'UACSC Officers under Siklab': 'University Central Student Council (UACSC)'
    }

    for c in candidates:
        folder = c['photo'].split('/')[1]
        if folder in dept_map:
            new_dept = dept_map[folder]
            old_dept = c['targetDept']
            c['targetDept'] = new_dept
            if old_dept in c.get('platform', ''):
                c['platform'] = c['platform'].replace(old_dept, new_dept)
            if 'advocacies' in c and isinstance(c['advocacies'], list):
                c['advocacies'] = [adv.replace(old_dept, new_dept) for adv in c['advocacies']]

    default_students = [
        {"id": "2024000669", "name": "Maria Clara T. Santos", "email": "mctsantos.student@ua.edu.ph", "dept": "College of Accountancy", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000101", "name": "Rafael E. Santos", "email": "resantos.student@ua.edu.ph", "dept": "College of Architecture", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000102", "name": "Alyssa M. David", "email": "amdavid.student@ua.edu.ph", "dept": "College of Arts and Sciences (ABCOMM)", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2023001244", "name": "Juan Dela T. Cruz", "email": "jdtcruz.student@ua.edu.ph", "dept": "College of Engineering", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024001882", "name": "Camille Rose P. Diaz", "email": "crpdiaz.student@ua.edu.ph", "dept": "College of Hospitality Management", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000103", "name": "Patricia B. Ocampo", "email": "pbocampo.student@ua.edu.ph", "dept": "College of Human Services", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000104", "name": "Gabriel N. Castro", "email": "gncastro.student@ua.edu.ph", "dept": "College of Industrial Engineering", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024001155", "name": "Angelo G. Gomez", "email": "aggomez.student@ua.edu.ph", "dept": "College of Information Technology", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024006843", "name": "Jaena B. Mangulabnan", "email": "jbmangulabnan.student@ua.edu.ph", "dept": "College of Nursing", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000105", "name": "Clarisse D. Mallari", "email": "cdmallari.student@ua.edu.ph", "dept": "College of Pharmacy", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000106", "name": "Samantha K. Rivera", "email": "skrivera.student@ua.edu.ph", "dept": "College of Psychology", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024000107", "name": "Marco L. Henson", "email": "mlhenson.student@ua.edu.ph", "dept": "College of Tourism Management", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024008812", "name": "Joshua L. Garcia", "email": "jlgarcia.student@ua.edu.ph", "dept": "Junior Highschool", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2023004490", "name": "Beatriz Nicole L. Gomez", "email": "bnlgomez.student@ua.edu.ph", "dept": "School of Arts and Sciences (Criminology)", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2022009831", "name": "Sofia Bianca R. Dizon", "email": "sbrdizon.student@ua.edu.ph", "dept": "School of Business", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024003319", "name": "Mark Anthony V. Ramos", "email": "mavramos.student@ua.edu.ph", "dept": "School of Education", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"},
        {"id": "2024005576", "name": "Jaenaganda M. Cruz", "email": "jmcruz.student@ua.edu.ph", "dept": "Senior Highschool", "verified": True, "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"}
    ]

    print("Data structures prepared.")
    return departments, positions, candidates, default_students, dept_options

if __name__ == '__main__':
    depts, positions, candidates, students, dept_options = build_generator_script()
    print(f"Verified: {len(depts)} departments, {len(positions)} positions, {len(candidates)} candidates, {len(students)} students.")

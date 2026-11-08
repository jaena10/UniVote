# -*- coding: utf-8 -*-
"""
UniVote Builder - University of the Assumption
Generates studentweb.html and adminweb.html with:
1. College of Information Technology restored (10 total departments)
2. Admin Console using exact full department names without abbreviations
3. Studentweb:
   - "Full Student Name *" without "(Firstnames + Middle Initial + Lastname)"
   - "UA Institutional Email *" without "(Derived: ...)"
   - Separate Sign In and First-Time Registration modals
   - Registration success modal prompting student to sign in
   - Password show/hide toggle on all password fields
   - Sign in modal closes automatically upon authentication
   - Top banner (#lockedAccountBanner) completely removed after login
"""
import json
import os

DEPARTMENTS = [
    "College of Accountancy",
    "College of Engineering and Architecture",
    "College of Hospitality and Tourism Management",
    "College of Nursing and Pharmacy",
    "School of Arts and Sciences",
    "School of Business and Public Administration",
    "School of Education",
    "College of Information Technology",
    "Senior High School",
    "Junior High School"
]

POSITIONS = [
    {"id": "pres", "name": "President"},
    {"id": "vp", "name": "Vice President"},
    {"id": "sec", "name": "Secretary"},
    {"id": "tres", "name": "Treasurer"},
    {"id": "aud", "name": "Auditor"},
    {"id": "pro", "name": "Public Relations Officer (PRO)"}
]

print("Departments configured:", len(DEPARTMENTS))

candidates_data = [
    {
        "id": "ca_vp_1",
        "posId": "vp",
        "targetDept": "College of Accountancy",
        "name": "C.J Anthony Flores",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Membership",
        "photo": "/Siklab Party College of Accountancy/C.J Anthony Flores (Vice President for Membership).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Membership Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_vp_2",
        "posId": "vp",
        "targetDept": "College of Accountancy",
        "name": "Charlemagne Hipolito",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Non-Academics",
        "photo": "/Siklab Party College of Accountancy/Charlemagne Hipolito (Vice President for Non-Academics).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Non-Academics Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_pro_1",
        "posId": "pro",
        "targetDept": "College of Accountancy",
        "name": "Daniella Alsaybar",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Media",
        "photo": "/Siklab Party College of Accountancy/Daniella Alsaybar (Vice President for Media).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Media Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_aud_1",
        "posId": "aud",
        "targetDept": "College of Accountancy",
        "name": "France Marcelino",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Audit",
        "photo": "/Siklab Party College of Accountancy/France Marcelino (Vice President for Audit).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Audit Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_pres_1",
        "posId": "pres",
        "targetDept": "College of Accountancy",
        "name": "Jedidiah Laxamana",
        "party": "SIKLAB",
        "dept": "BS Accountancy - President",
        "photo": "/Siklab Party College of Accountancy/Jedidiah Laxamana (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_sec_1",
        "posId": "sec",
        "targetDept": "College of Accountancy",
        "name": "Jerica Paule",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Communications",
        "photo": "/Siklab Party College of Accountancy/Jerica Paule (Vice President for Communications).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Communications Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_tres_1",
        "posId": "tres",
        "targetDept": "College of Accountancy",
        "name": "John Ray Manio",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Finance",
        "photo": "/Siklab Party College of Accountancy/John Ray Manio (Vice President for Finance).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Finance Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "ca_vp_3",
        "posId": "vp",
        "targetDept": "College of Accountancy",
        "name": "Yvonne Cortez",
        "party": "SIKLAB",
        "dept": "BS Accountancy - Vice President for Academics",
        "photo": "/Siklab Party College of Accountancy/Yvonne Cortez (Vice President for Academics).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Accountancy students.",
        "advocacies": [
            "Vice President for Academics Student Initiatives",
            "Transparent College of Accountancy Representation"
        ]
    },
    {
        "id": "cea_pro_1",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Aaron John Garcia",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Technical Support",
        "photo": "/College of Architecture/Aaron John Garcia (Chairperson for Technical Support).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Technical Support Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_2",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Aldrin Isaac H. Lacanlale",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Graphic & Publication",
        "photo": "/College of Architecture/Aldrin Isaac H. Lacanlale (Chairperson for Graphic & Publication).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Graphic & Publication Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_3",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Andrei Magcalas",
        "party": "Independent",
        "dept": "BS Architecture - 2nd Year Representative",
        "photo": "/College of Architecture/Andrei Magcalas (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_1",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Angelica Solomon",
        "party": "Independent",
        "dept": "BS Architecture - Asst. Secretarty",
        "photo": "/College of Architecture/Angelica Solomon (Asst. Secretarty).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Asst. Secretarty Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_2",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Angelika Nuguid",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Documents",
        "photo": "/College of Architecture/Angelika Nuguid (Chairperson for Documents).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Documents Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_4",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Ashley Jae-hwa V. Soriano",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Graphics & Publication",
        "photo": "/College of Architecture/Ashley Jae-hwa V. Soriano (Chairperson for Graphics & Publication).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Graphics & Publication Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pres_1",
        "posId": "pres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Aviane May A. Del Rosario",
        "party": "Independent",
        "dept": "BS Architecture - President",
        "photo": "/College of Architecture/Aviane May A. Del Rosario (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_5",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Chester John Javier",
        "party": "Independent",
        "dept": "BS Architecture - 4th Year Representative",
        "photo": "/College of Architecture/Chester John Javier (4th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "4th Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_3",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Christel Loraine Lapuz",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Documents",
        "photo": "/College of Architecture/Christel Loraine Lapuz (Chairperson for Documents).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Documents Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_6",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Christen Joline Ramos",
        "party": "Independent",
        "dept": "BS Architecture - 1st Year Representative",
        "photo": "/College of Architecture/Christen Joline Ramos (1st Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "1st Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_4",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Christoph Jacq P. Mangune",
        "party": "Independent",
        "dept": "BS Architecture - Secretary",
        "photo": "/College of Architecture/Christoph Jacq P. Mangune (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_7",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Franzen Ivan Salunga",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Communications",
        "photo": "/College of Architecture/Franzen Ivan Salunga (Chairperson for Communications).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Communications Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_vp_1",
        "posId": "vp",
        "targetDept": "College of Engineering and Architecture",
        "name": "Jasmine S. Rubio",
        "party": "Independent",
        "dept": "BS Architecture - Vice President",
        "photo": "/College of Architecture/Jasmine S. Rubio (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_aud_1",
        "posId": "aud",
        "targetDept": "College of Engineering and Architecture",
        "name": "Kenreds L. Cabigting",
        "party": "Independent",
        "dept": "BS Architecture - Auditor",
        "photo": "/College of Architecture/Kenreds L. Cabigting (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_8",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Maria Felicity Espinoza",
        "party": "Independent",
        "dept": "BS Architecture - 3rd Year Representative",
        "photo": "/College of Architecture/Maria Felicity Espinoza (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_1",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Mark Anthony Canlas",
        "party": "Independent",
        "dept": "BS Architecture - Asst. Treasurer",
        "photo": "/College of Architecture/Mark Anthony Canlas (Asst. Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Asst. Treasurer Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_9",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Rein Pacia",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Technical Support",
        "photo": "/College of Architecture/Rein Pacia (Chairperson for Technical Support).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Technical Support Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_10",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Ron Maynard Clamor",
        "party": "Independent",
        "dept": "BS Architecture - 5th Year Representative",
        "photo": "/College of Architecture/Ron Maynard Clamor (5th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "5th Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_11",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Samleigh Del Rosario",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Public Relations",
        "photo": "/College of Architecture/Samleigh Del Rosario (Chairperson for Public Relations).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Public Relations Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_5",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Sean Patrick Manarang",
        "party": "Independent",
        "dept": "BS Architecture - Chairperson for Records",
        "photo": "/College of Architecture/Sean Patrick Manarang (Chairperson for Records).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Chairperson for Records Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_2",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Simone Gabriel Toledo",
        "party": "Independent",
        "dept": "BS Architecture - Treasurer",
        "photo": "/College of Architecture/Simone Gabriel Toledo (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_6",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Aileen Faye P. Nabong",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Secretary",
        "photo": "/College of Industrial Engineering/Aileen Faye P. Nabong (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_vp_2",
        "posId": "vp",
        "targetDept": "College of Engineering and Architecture",
        "name": "Arabella Francesca P. David",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Vice President for Internal Affairs",
        "photo": "/College of Industrial Engineering/Arabella Francesca P. David (Vice President for Internal Affairs).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Vice President for Internal Affairs Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_12",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Christian Andrei B. Sicat",
        "party": "Independent",
        "dept": "BS Industrial Engineering - 2nd Year Representative",
        "photo": "/College of Industrial Engineering/Christian Andrei B. Sicat (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_13",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Irish Ann I. Turla",
        "party": "Independent",
        "dept": "BS Industrial Engineering - P.I.O",
        "photo": "/College of Industrial Engineering/Irish Ann I. Turla (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_3",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Kevin Llyod C. Macaraeg",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Treasurer",
        "photo": "/College of Industrial Engineering/Kevin Llyod C. Macaraeg (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_4",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Maiko Dovan E. Alfonso",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Business Manager",
        "photo": "/College of Industrial Engineering/Maiko Dovan E. Alfonso (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_aud_2",
        "posId": "aud",
        "targetDept": "College of Engineering and Architecture",
        "name": "Matthew G. Landayan",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Auditor",
        "photo": "/College of Industrial Engineering/Matthew G. Landayan (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_14",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Matthew Gabriel R. Guevarra",
        "party": "Independent",
        "dept": "BS Industrial Engineering - 4th Year Representative",
        "photo": "/College of Industrial Engineering/Matthew Gabriel R. Guevarra (4th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "4th Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pres_2",
        "posId": "pres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Paul Ian S. Arcega",
        "party": "Independent",
        "dept": "BS Industrial Engineering - President",
        "photo": "/College of Industrial Engineering/Paul Ian S. Arcega (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_7",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Rhian Denise C. Guerta",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Asst. Secretary",
        "photo": "/College of Industrial Engineering/Rhian Denise C. Guerta (Asst. Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Asst. Secretary Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_15",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Roland S. Falcon Jr,",
        "party": "Independent",
        "dept": "BS Industrial Engineering - 3rd Year Representative",
        "photo": "/College of Industrial Engineering/Roland S. Falcon Jr, (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_vp_3",
        "posId": "vp",
        "targetDept": "College of Engineering and Architecture",
        "name": "Shamel Marie S. Dantes",
        "party": "Independent",
        "dept": "BS Industrial Engineering - Vice President for External Affairs",
        "photo": "/College of Industrial Engineering/Shamel Marie S. Dantes (Vice President for External Affairs).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Vice President for External Affairs Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_vp_4",
        "posId": "vp",
        "targetDept": "College of Engineering and Architecture",
        "name": "Adam Zachary Samia",
        "party": "SIKLAB",
        "dept": "College of Engineering - Vice President",
        "photo": "/Siklab Party College of Engineering/Adam Zachary Samia (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pres_3",
        "posId": "pres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Aislahandear Alfonso",
        "party": "SIKLAB",
        "dept": "College of Engineering - President",
        "photo": "/Siklab Party College of Engineering/Aislahandear Alfonso (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_5",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Caryll Sofia Discartin",
        "party": "SIKLAB",
        "dept": "College of Engineering - Treasurer",
        "photo": "/Siklab Party College of Engineering/Caryll Sofia Discartin (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_16",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Jhenel John Navarro",
        "party": "SIKLAB",
        "dept": "College of Engineering - 3rd Year Representative",
        "photo": "/Siklab Party College of Engineering/Jhenel John Navarro (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_sec_8",
        "posId": "sec",
        "targetDept": "College of Engineering and Architecture",
        "name": "Joshuane Talao",
        "party": "SIKLAB",
        "dept": "College of Engineering - Secretary",
        "photo": "/Siklab Party College of Engineering/Joshuane Talao (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_17",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Ken Louise Espiritu",
        "party": "SIKLAB",
        "dept": "College of Engineering - P.I.O",
        "photo": "/Siklab Party College of Engineering/Ken Louise Espiritu (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_aud_3",
        "posId": "aud",
        "targetDept": "College of Engineering and Architecture",
        "name": "Mary Joyce Pangilinan",
        "party": "SIKLAB",
        "dept": "College of Engineering - Auditor",
        "photo": "/Siklab Party College of Engineering/Mary Joyce Pangilinan (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_18",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Mary Jullien Tan",
        "party": "SIKLAB",
        "dept": "College of Engineering - 4th Year Representative",
        "photo": "/Siklab Party College of Engineering/Mary Jullien Tan (4th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "4th Year Representative Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_pro_19",
        "posId": "pro",
        "targetDept": "College of Engineering and Architecture",
        "name": "Melangie Tendero",
        "party": "SIKLAB",
        "dept": "College of Engineering - P.R.O",
        "photo": "/Siklab Party College of Engineering/Melangie Tendero (P.R.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "P.R.O Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "cea_tres_6",
        "posId": "tres",
        "targetDept": "College of Engineering and Architecture",
        "name": "Zedrich Tolentino",
        "party": "SIKLAB",
        "dept": "College of Engineering - Business Manager",
        "photo": "/Siklab Party College of Engineering/Zedrich Tolentino (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Engineering and Architecture students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Engineering and Architecture Representation"
        ]
    },
    {
        "id": "chtm_pro_1",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Anazawa Aira Y.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 4th Year Representative",
        "photo": "/College of Hospitality  Management/Anazawa Aira Y. (4th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "4th Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_2",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Calara Casseyrhine Louie C.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 3rd Year Representative",
        "photo": "/College of Hospitality  Management/Calara Casseyrhine Louie C. (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_tres_1",
        "posId": "tres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Isip Mark Andrei M.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Business Manager",
        "photo": "/College of Hospitality  Management/Isip Mark Andrei M. (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_3",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Maliwat Riahyana Venice R.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 1st Year Representative",
        "photo": "/College of Hospitality  Management/Maliwat Riahyana Venice R. (1st Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "1st Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_4",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Mallari Mikaela Marie A.",
        "party": "Independent",
        "dept": "BS Hospitality Management - P.I.O",
        "photo": "/College of Hospitality  Management/Mallari Mikaela Marie A. (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_vp_1",
        "posId": "vp",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Manalastas Angel Therese R.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Vice President",
        "photo": "/College of Hospitality  Management/Manalastas Angel Therese R. (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_5",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Nario Khyle Anklet F.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Executive Asst.",
        "photo": "/College of Hospitality  Management/Nario Khyle Anklet F. (Executive Asst.).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Executive Asst. Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_aud_1",
        "posId": "aud",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Pineda Ailey C.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Auditor",
        "photo": "/College of Hospitality  Management/Pineda Ailey C. (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_tres_2",
        "posId": "tres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Ponce Mary Marjoie V.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Treasurer",
        "photo": "/College of Hospitality  Management/Ponce Mary Marjoie V. (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_6",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Punzalan Mary Grace A.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 2nd Year Representative",
        "photo": "/College of Hospitality  Management/Punzalan Mary Grace A. (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_tres_3",
        "posId": "tres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Ramos Jema S.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Business Manager",
        "photo": "/College of Hospitality  Management/Ramos Jema S. (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_7",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Reginaldo Mary Alexine R.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 3rd Year Reprentative",
        "photo": "/College of Hospitality  Management/Reginaldo Mary Alexine R. (3rd Year Reprentative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "3rd Year Reprentative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_8",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Santos Jan Eugene T.",
        "party": "Independent",
        "dept": "BS Hospitality Management - P.I.O",
        "photo": "/College of Hospitality  Management/Santos Jan Eugene T. (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_9",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Santos Pia Charlotte P.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Excecutive Asst.",
        "photo": "/College of Hospitality  Management/Santos Pia Charlotte P. (Excecutive Asst.).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Excecutive Asst. Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_sec_1",
        "posId": "sec",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Sotto Marielle S.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Secretary",
        "photo": "/College of Hospitality  Management/Sotto Marielle S. (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_10",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Tan Mark Angelo",
        "party": "Independent",
        "dept": "BS Hospitality Management - 1st Year Representative",
        "photo": "/College of Hospitality  Management/Tan Mark Angelo (1st Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "1st Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_11",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Tango Aerhon C.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Creative Director",
        "photo": "/College of Hospitality  Management/Tango Aerhon C. (Creative Director).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Creative Director Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_12",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Velasquez Kristine Noielle B.",
        "party": "Independent",
        "dept": "BS Hospitality Management - 2nd Year Representative",
        "photo": "/College of Hospitality  Management/Velasquez Kristine Noielle B. (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_13",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Viray Javen Chloe A.",
        "party": "Independent",
        "dept": "BS Hospitality Management - Creative Director",
        "photo": "/College of Hospitality  Management/Viray Javen Chloe A. (Creative Director).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Creative Director Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pres_1",
        "posId": "pres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Vitanggul Justin Luigi G.",
        "party": "Independent",
        "dept": "BS Hospitality Management - President",
        "photo": "/College of Hospitality  Management/Vitanggul Justin Luigi G. (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_sec_2",
        "posId": "sec",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Angel Clemente",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Secretary",
        "photo": "/Siklab Party College of Tourism Management/Angel Clemente (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_14",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Ashlie Sicat",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Creative Staff",
        "photo": "/Siklab Party College of Tourism Management/Ashlie Sicat (Creative Staff).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Creative Staff Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pres_2",
        "posId": "pres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Jeaanelle Bianca Dionicio",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - President",
        "photo": "/Siklab Party College of Tourism Management/Jeaanelle Bianca Dionicio (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_vp_2",
        "posId": "vp",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Kathrain Galang",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Vice President For Internal Affair",
        "photo": "/Siklab Party College of Tourism Management/Kathrain Galang (Vice President For Internal Affair).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Vice President For Internal Affair Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_aud_2",
        "posId": "aud",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Keith Aubrey Digneneng",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Auditor",
        "photo": "/Siklab Party College of Tourism Management/Keith Aubrey Digneneng (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_tres_4",
        "posId": "tres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Kyle Geoff Garcia",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Business Manager",
        "photo": "/Siklab Party College of Tourism Management/Kyle Geoff Garcia (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_sec_3",
        "posId": "sec",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Lanalyn Medina",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Assistant Secretary",
        "photo": "/Siklab Party College of Tourism Management/Lanalyn Medina (Assistant Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Assistant Secretary Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_15",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Lyranhezka Jeorgina Alibo",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - 2nd Year Representative",
        "photo": "/Siklab Party College of Tourism Management/Lyranhezka Jeorgina Alibo (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_16",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Naome Jorlin Razal",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Creative Staff",
        "photo": "/Siklab Party College of Tourism Management/Naome Jorlin Razal (Creative Staff).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Creative Staff Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_17",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Nariena Micaela Quiambao",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Creative Staff",
        "photo": "/Siklab Party College of Tourism Management/Nariena Micaela Quiambao (Creative Staff).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Creative Staff Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_pro_18",
        "posId": "pro",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Niel Jayson Siaton",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Public Information Officer",
        "photo": "/Siklab Party College of Tourism Management/Niel Jayson Siaton (Public Information Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Public Information Officer Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_vp_3",
        "posId": "vp",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Queen Adelita Galang",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Vice President For External Affair",
        "photo": "/Siklab Party College of Tourism Management/Queen Adelita Galang (Vice President For External Affair).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Vice President For External Affair Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "chtm_tres_5",
        "posId": "tres",
        "targetDept": "College of Hospitality and Tourism Management",
        "name": "Ryza Reyes",
        "party": "SIKLAB",
        "dept": "BS Tourism Management - Treasurer",
        "photo": "/Siklab Party College of Tourism Management/Ryza Reyes (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Hospitality and Tourism Management students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Hospitality and Tourism Management Representation"
        ]
    },
    {
        "id": "cnp_pres_1",
        "posId": "pres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Aiona Mungcal",
        "party": "Independent",
        "dept": "BS Nursing - President",
        "photo": "/College of Nursing/Aiona Mungcal (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_vp_1",
        "posId": "vp",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Aletheia Polintan",
        "party": "Independent",
        "dept": "BS Nursing - Vice President",
        "photo": "/College of Nursing/Aletheia Polintan (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_1",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Ayumid Mae Cortez",
        "party": "Independent",
        "dept": "BS Nursing - Business Manager",
        "photo": "/College of Nursing/Ayumid Mae Cortez (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_1",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Hannah Thea Agajona",
        "party": "Independent",
        "dept": "BS Nursing - P.I.O",
        "photo": "/College of Nursing/Hannah Thea Agajona (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_2",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Janella Klarisse Andan",
        "party": "Independent",
        "dept": "BS Nursing - Asst. Creative Director",
        "photo": "/College of Nursing/Janella Klarisse Andan (Asst. Creative Director).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Creative Director Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_sec_1",
        "posId": "sec",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Josephine Ann Nunag",
        "party": "Independent",
        "dept": "BS Nursing - Asst. Secretary",
        "photo": "/College of Nursing/Josephine Ann Nunag (Asst. Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Secretary Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_aud_1",
        "posId": "aud",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Jumile Ivan Castro",
        "party": "Independent",
        "dept": "BS Nursing - Auditor",
        "photo": "/College of Nursing/Jumile Ivan Castro (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_3",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Kirzten Nicole Alcoy",
        "party": "Independent",
        "dept": "BS Nursing - Executive Assitant",
        "photo": "/College of Nursing/Kirzten Nicole Alcoy (Executive Assitant).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Executive Assitant Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_sec_2",
        "posId": "sec",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Louise Lhane Kabigting",
        "party": "Independent",
        "dept": "BS Nursing - Secretary",
        "photo": "/College of Nursing/Louise Lhane Kabigting (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_4",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Mandy Manalastas",
        "party": "Independent",
        "dept": "BS Nursing - Creative Director",
        "photo": "/College of Nursing/Mandy Manalastas (Creative Director).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Creative Director Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_2",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Raymond Rivera",
        "party": "Independent",
        "dept": "BS Nursing - Assist.Treasurer",
        "photo": "/College of Nursing/Raymond Rivera (Assist.Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Assist.Treasurer Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_3",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Shane Simon",
        "party": "Independent",
        "dept": "BS Nursing - Treasurer",
        "photo": "/College of Nursing/Shane Simon (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_4",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "April Joy Dampil",
        "party": "Independent",
        "dept": "BS Pharmacy - Asst. Business Manager",
        "photo": "/College of Pharmacy/April Joy Dampil (Asst. Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Business Manager Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_5",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Arianne Jaeda Quiambao",
        "party": "Independent",
        "dept": "BS Pharmacy - Asst. P.I.O",
        "photo": "/College of Pharmacy/Arianne Jaeda Quiambao (Asst. P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. P.I.O Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_vp_2",
        "posId": "vp",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Ashantee Pelayo",
        "party": "Independent",
        "dept": "BS Pharmacy - Vice President",
        "photo": "/College of Pharmacy/Ashantee Pelayo (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_6",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Austen Jenn Luriz",
        "party": "Independent",
        "dept": "BS Pharmacy - Level 2 Coordinator",
        "photo": "/College of Pharmacy/Austen Jenn Luriz (Level 2 Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Level 2 Coordinator Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_aud_2",
        "posId": "aud",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Deziree Inocendio",
        "party": "Independent",
        "dept": "BS Pharmacy - Asst. Auditor",
        "photo": "/College of Pharmacy/Deziree Inocendio (Asst. Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Auditor Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_5",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Erica Danielle Quinol",
        "party": "Independent",
        "dept": "BS Pharmacy - Business Manager",
        "photo": "/College of Pharmacy/Erica Danielle Quinol (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_7",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Erris John Punzalan",
        "party": "Independent",
        "dept": "BS Pharmacy - Level 1 Coordinator",
        "photo": "/College of Pharmacy/Erris John Punzalan (Level 1 Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Level 1 Coordinator Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_sec_3",
        "posId": "sec",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Geebee II Garcia",
        "party": "Independent",
        "dept": "BS Pharmacy - Asst. Secretary",
        "photo": "/College of Pharmacy/Geebee II Garcia (Asst. Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Secretary Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_8",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Henry Cunanan Jr.",
        "party": "Independent",
        "dept": "BS Pharmacy - Level 3 Coordinator",
        "photo": "/College of Pharmacy/Henry Cunanan Jr. (Level 3 Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Level 3 Coordinator Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_sec_4",
        "posId": "sec",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Jammeah Colis",
        "party": "Independent",
        "dept": "BS Pharmacy - Secretary",
        "photo": "/College of Pharmacy/Jammeah Colis (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_aud_3",
        "posId": "aud",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Jessalyn Licu",
        "party": "Independent",
        "dept": "BS Pharmacy - Auditor",
        "photo": "/College of Pharmacy/Jessalyn Licu (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_9",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Joella Diane Sablan",
        "party": "Independent",
        "dept": "BS Pharmacy - P.I.O",
        "photo": "/College of Pharmacy/Joella Diane Sablan (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pro_10",
        "posId": "pro",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Maria Shamel Munoz",
        "party": "Independent",
        "dept": "BS Pharmacy - Level 4 Coordinator",
        "photo": "/College of Pharmacy/Maria Shamel Munoz (Level 4 Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Level 4 Coordinator Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_6",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Marinelle Dela Pena",
        "party": "Independent",
        "dept": "BS Pharmacy - Asst. Treasurer",
        "photo": "/College of Pharmacy/Marinelle Dela Pena (Asst. Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Asst. Treasurer Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_tres_7",
        "posId": "tres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Shanen Ann Canlas",
        "party": "Independent",
        "dept": "BS Pharmacy - Treasurer",
        "photo": "/College of Pharmacy/Shanen Ann Canlas (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "cnp_pres_2",
        "posId": "pres",
        "targetDept": "College of Nursing and Pharmacy",
        "name": "Venice Krystel Punla",
        "party": "Independent",
        "dept": "BS Pharmacy - President",
        "photo": "/College of Pharmacy/Venice Krystel Punla (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Nursing and Pharmacy students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Nursing and Pharmacy Representation"
        ]
    },
    {
        "id": "sas_tres_1",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Bianca Talavera",
        "party": "SIKLAB",
        "dept": "AB Communication - Treasurer",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Bianca Talavera (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_sec_1",
        "posId": "sec",
        "targetDept": "School of Arts and Sciences",
        "name": "Jasmine Mercado",
        "party": "SIKLAB",
        "dept": "AB Communication - Secretary",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Jasmine Mercado (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_2",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Joshua Gonzales",
        "party": "SIKLAB",
        "dept": "AB Communication - Business Manager",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Joshua Gonzales (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_vp_1",
        "posId": "vp",
        "targetDept": "School of Arts and Sciences",
        "name": "Juliana Palao",
        "party": "SIKLAB",
        "dept": "AB Communication - Vice President",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Juliana Palao (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_aud_1",
        "posId": "aud",
        "targetDept": "School of Arts and Sciences",
        "name": "Kevin Panoy",
        "party": "SIKLAB",
        "dept": "AB Communication - Auditor",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Kevin Panoy (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_1",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Miriam Cruz",
        "party": "SIKLAB",
        "dept": "AB Communication - P.I.O",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Miriam Cruz (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pres_1",
        "posId": "pres",
        "targetDept": "School of Arts and Sciences",
        "name": "Yshine Mapilisan",
        "party": "SIKLAB",
        "dept": "AB Communication - President",
        "photo": "/Siklab Party School of Arts and Sciences (ABCOMM)/Yshine Mapilisan (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_vp_2",
        "posId": "vp",
        "targetDept": "School of Arts and Sciences",
        "name": "Aika Hernandez",
        "party": "Independent",
        "dept": "BS Criminology - Vice President",
        "photo": "/School of Arts and Sciences (Criminology)/Aika Hernandez (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_2",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Airine Pineda",
        "party": "Independent",
        "dept": "BS Criminology - P.R.O",
        "photo": "/School of Arts and Sciences (Criminology)/Airine Pineda (P.R.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "P.R.O Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pres_2",
        "posId": "pres",
        "targetDept": "School of Arts and Sciences",
        "name": "Arnold Medina",
        "party": "Independent",
        "dept": "BS Criminology - President",
        "photo": "/School of Arts and Sciences (Criminology)/Arnold Medina (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_sec_2",
        "posId": "sec",
        "targetDept": "School of Arts and Sciences",
        "name": "Blue Macapagal",
        "party": "Independent",
        "dept": "BS Criminology - Secretary",
        "photo": "/School of Arts and Sciences (Criminology)/Blue Macapagal (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_3",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Carlo Decena",
        "party": "Independent",
        "dept": "BS Criminology - Treasurer",
        "photo": "/School of Arts and Sciences (Criminology)/Carlo Decena (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_4",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Faith Liwanag",
        "party": "Independent",
        "dept": "BS Criminology - Business Manager",
        "photo": "/School of Arts and Sciences (Criminology)/Faith Liwanag (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_3",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Kenxin Dela Torre",
        "party": "Independent",
        "dept": "BS Criminology - Protocol Officer",
        "photo": "/School of Arts and Sciences (Criminology)/Kenxin Dela Torre (Protocol Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Protocol Officer Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_4",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Leslie Lao",
        "party": "Independent",
        "dept": "BS Criminology - Creative Director",
        "photo": "/School of Arts and Sciences (Criminology)/Leslie Lao (Creative Director).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Creative Director Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_5",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Mark Lara",
        "party": "Independent",
        "dept": "BS Criminology - Creative Staff",
        "photo": "/School of Arts and Sciences (Criminology)/Mark Lara (Creative Staff).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Creative Staff Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_6",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Ruel Arga",
        "party": "Independent",
        "dept": "BS Criminology - 1st Year Representative",
        "photo": "/School of Arts and Sciences (Criminology)/Ruel Arga (1st Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "1st Year Representative Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_vp_3",
        "posId": "vp",
        "targetDept": "School of Arts and Sciences",
        "name": "Aien Phoebe C. Sonza",
        "party": "SIKLAB",
        "dept": "BS Psychology - Vice President",
        "photo": "/Siklab Party College of Psychology/Aien Phoebe C. Sonza (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_aud_2",
        "posId": "aud",
        "targetDept": "School of Arts and Sciences",
        "name": "Erica Ghin L. Martinez",
        "party": "SIKLAB",
        "dept": "BS Psychology - Auditor",
        "photo": "/Siklab Party College of Psychology/Erica Ghin L. Martinez (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_7",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Ieasha Azrielle Ann L. Manimbo",
        "party": "SIKLAB",
        "dept": "BS Psychology - P.I.O",
        "photo": "/Siklab Party College of Psychology/Ieasha Azrielle Ann L. Manimbo (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_5",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Jioff Troy B. Yambao",
        "party": "SIKLAB",
        "dept": "BS Psychology - Business Manager",
        "photo": "/Siklab Party College of Psychology/Jioff Troy B. Yambao (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_sec_3",
        "posId": "sec",
        "targetDept": "School of Arts and Sciences",
        "name": "Patricia Mae V. Corral",
        "party": "SIKLAB",
        "dept": "BS Psychology - Secretary",
        "photo": "/Siklab Party College of Psychology/Patricia Mae V. Corral (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pres_3",
        "posId": "pres",
        "targetDept": "School of Arts and Sciences",
        "name": "Steiven Codie p. Gonzales",
        "party": "SIKLAB",
        "dept": "BS Psychology - President",
        "photo": "/Siklab Party College of Psychology/Steiven Codie p. Gonzales (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_6",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Therese Claire B. Marquez",
        "party": "SIKLAB",
        "dept": "BS Psychology - Treasurer",
        "photo": "/Siklab Party College of Psychology/Therese Claire B. Marquez (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_8",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Atheena Denise M. Viray",
        "party": "SIKLAB",
        "dept": "BS Human Services - 2nd Year Representative",
        "photo": "/Siklab Party College of Human Services/Atheena Denise M. Viray (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_aud_3",
        "posId": "aud",
        "targetDept": "School of Arts and Sciences",
        "name": "Erdelyn T. Ladrillo",
        "party": "SIKLAB",
        "dept": "BS Human Services - Auditor",
        "photo": "/Siklab Party College of Human Services/Erdelyn T. Ladrillo (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_9",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Keirsten Mary C. Manalese",
        "party": "SIKLAB",
        "dept": "BS Human Services - 3rd Year Representative",
        "photo": "/Siklab Party College of Human Services/Keirsten Mary C. Manalese (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_10",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Maann Sofia V. Roxas",
        "party": "SIKLAB",
        "dept": "BS Human Services - P.I.O",
        "photo": "/Siklab Party College of Human Services/Maann Sofia V. Roxas (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_sec_4",
        "posId": "sec",
        "targetDept": "School of Arts and Sciences",
        "name": "Marie Anne Clarrise C. Dizon",
        "party": "SIKLAB",
        "dept": "BS Human Services - Secretary",
        "photo": "/Siklab Party College of Human Services/Marie Anne Clarrise C. Dizon (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_tres_7",
        "posId": "tres",
        "targetDept": "School of Arts and Sciences",
        "name": "Mary Hannah Sofia J. Castro",
        "party": "SIKLAB",
        "dept": "BS Human Services - Treasurer",
        "photo": "/Siklab Party College of Human Services/Mary Hannah Sofia J. Castro (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_vp_4",
        "posId": "vp",
        "targetDept": "School of Arts and Sciences",
        "name": "Reigniel Carl B. Dantes",
        "party": "SIKLAB",
        "dept": "BS Human Services - Vice President",
        "photo": "/Siklab Party College of Human Services/Reigniel Carl B. Dantes (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pro_11",
        "posId": "pro",
        "targetDept": "School of Arts and Sciences",
        "name": "Sheanjay Justine A. Billedo",
        "party": "SIKLAB",
        "dept": "BS Human Services - 4th Year Representative",
        "photo": "/Siklab Party College of Human Services/Sheanjay Justine A. Billedo (4th Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "4th Year Representative Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sas_pres_4",
        "posId": "pres",
        "targetDept": "School of Arts and Sciences",
        "name": "Steve Jake M. Regala",
        "party": "SIKLAB",
        "dept": "BS Human Services - President",
        "photo": "/Siklab Party College of Human Services/Steve Jake M. Regala (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Arts and Sciences students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Arts and Sciences Representation"
        ]
    },
    {
        "id": "sbpa_pro_1",
        "posId": "pro",
        "targetDept": "School of Business and Public Administration",
        "name": "Alejo Ruui L. Bautista",
        "party": "SIKLAB",
        "dept": "BS Business Administration - P.I.O",
        "photo": "/Siklab Party School of Business/Alejo Ruui L. Bautista (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_tres_1",
        "posId": "tres",
        "targetDept": "School of Business and Public Administration",
        "name": "Arcel Joshua L. Navarro",
        "party": "SIKLAB",
        "dept": "BS Business Administration - Treasurer",
        "photo": "/Siklab Party School of Business/Arcel Joshua L. Navarro (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_sec_1",
        "posId": "sec",
        "targetDept": "School of Business and Public Administration",
        "name": "Denise Marielle M. Austria",
        "party": "SIKLAB",
        "dept": "BS Business Administration - Secretary",
        "photo": "/Siklab Party School of Business/Denise Marielle M. Austria (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_vp_1",
        "posId": "vp",
        "targetDept": "School of Business and Public Administration",
        "name": "Elaine B. Agustin",
        "party": "SIKLAB",
        "dept": "BS Business Administration - 2nd Year Representative",
        "photo": "/Siklab Party School of Business/Elaine B. Agustin (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_vp_2",
        "posId": "vp",
        "targetDept": "School of Business and Public Administration",
        "name": "Gian Marcus V. Garcia",
        "party": "SIKLAB",
        "dept": "BS Business Administration - Vice President",
        "photo": "/Siklab Party School of Business/Gian Marcus V. Garcia (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_pres_1",
        "posId": "pres",
        "targetDept": "School of Business and Public Administration",
        "name": "Marian Alexis C. Mercado",
        "party": "SIKLAB",
        "dept": "BS Business Administration - President",
        "photo": "/Siklab Party School of Business/Marian Alexis C. Mercado (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_aud_1",
        "posId": "aud",
        "targetDept": "School of Business and Public Administration",
        "name": "Michael S. Ramos Jr.",
        "party": "SIKLAB",
        "dept": "BS Business Administration - 3rd Year Representative",
        "photo": "/Siklab Party School of Business/Michael S. Ramos Jr. (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "sbpa_pro_2",
        "posId": "pro",
        "targetDept": "School of Business and Public Administration",
        "name": "Princess Giren P. Cabaya",
        "party": "SIKLAB",
        "dept": "BS Business Administration - Director for Sports",
        "photo": "/Siklab Party School of Business/Princess Giren P. Cabaya (Director for Sports).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Business and Public Administration students.",
        "advocacies": [
            "Director for Sports Student Initiatives",
            "Transparent School of Business and Public Administration Representation"
        ]
    },
    {
        "id": "se_pro_1",
        "posId": "pro",
        "targetDept": "School of Education",
        "name": "Angel Mallari",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - 3rd Year Representative",
        "photo": "/Siklab Party School of Education/Angel Mallari (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_pres_1",
        "posId": "pres",
        "targetDept": "School of Education",
        "name": "Carl Angelo Dela Cruz",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - President",
        "photo": "/Siklab Party School of Education/Carl Angelo Dela Cruz (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_sec_1",
        "posId": "sec",
        "targetDept": "School of Education",
        "name": "Gabriel Angelo Paguinto",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - Secretary",
        "photo": "/Siklab Party School of Education/Gabriel Angelo Paguinto (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_pro_2",
        "posId": "pro",
        "targetDept": "School of Education",
        "name": "Jerald Caballero",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - P.I.O",
        "photo": "/Siklab Party School of Education/Jerald Caballero (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_tres_1",
        "posId": "tres",
        "targetDept": "School of Education",
        "name": "Joisaiah Gabriel Quiambao",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - Business Manager",
        "photo": "/Siklab Party School of Education/Joisaiah Gabriel Quiambao (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_vp_1",
        "posId": "vp",
        "targetDept": "School of Education",
        "name": "Paul Ricci Basa",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - 2nd Year Representative",
        "photo": "/Siklab Party School of Education/Paul Ricci Basa (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_aud_1",
        "posId": "aud",
        "targetDept": "School of Education",
        "name": "Randel Pacia",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - Auditor",
        "photo": "/Siklab Party School of Education/Randel Pacia (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "se_vp_2",
        "posId": "vp",
        "targetDept": "School of Education",
        "name": "Rodeline De Guzman",
        "party": "SIKLAB",
        "dept": "Bachelor of Education - Vice President",
        "photo": "/Siklab Party School of Education/Rodeline De Guzman (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for School of Education students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent School of Education Representation"
        ]
    },
    {
        "id": "cit_pro_1",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Alejos Theeanna Jether",
        "party": "Independent",
        "dept": "BS Information Technology - Director for Creative Media",
        "photo": "/College of Information Technology/Alejos Theeanna Jether (Director for Creative Media).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Director for Creative Media Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_tres_1",
        "posId": "tres",
        "targetDept": "College of Information Technology",
        "name": "Bondoc Kirby Joshua",
        "party": "Independent",
        "dept": "BS Information Technology - Business Development Coordinator",
        "photo": "/College of Information Technology/Bondoc Kirby Joshua (Business Development Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Business Development Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_2",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Carlos Llwelyn Jade",
        "party": "Independent",
        "dept": "BS Information Technology - Visual Design Coordinator",
        "photo": "/College of Information Technology/Carlos Llwelyn Jade (Visual Design Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Visual Design Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_3",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Dela Cruz Kelvin Rhay",
        "party": "Independent",
        "dept": "BS Information Technology - Information Communication Officer",
        "photo": "/College of Information Technology/Dela Cruz Kelvin Rhay (Information Communication Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Information Communication Officer Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_4",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Dela Pena Stephany Ann",
        "party": "Independent",
        "dept": "BS Information Technology - Digital Communications Officer",
        "photo": "/College of Information Technology/Dela Pena Stephany Ann (Digital Communications Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Digital Communications Officer Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_vp_1",
        "posId": "vp",
        "targetDept": "College of Information Technology",
        "name": "Garcia Aian Jae",
        "party": "Independent",
        "dept": "BS Information Technology - Vice President",
        "photo": "/College of Information Technology/Garcia Aian Jae (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_5",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Garcia Jose Miguel",
        "party": "Independent",
        "dept": "BS Information Technology - Sports Coordinator",
        "photo": "/College of Information Technology/Garcia Jose Miguel (Sports Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Sports Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_vp_2",
        "posId": "vp",
        "targetDept": "College of Information Technology",
        "name": "Guevarra Yaslee GJ",
        "party": "Independent",
        "dept": "BS Information Technology - VP-External Affairs",
        "photo": "/College of Information Technology/Guevarra Yaslee GJ (VP-External Affairs).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "VP-External Affairs Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_tres_2",
        "posId": "tres",
        "targetDept": "College of Information Technology",
        "name": "Henson Patricia Alizah",
        "party": "Independent",
        "dept": "BS Information Technology - Treasurer",
        "photo": "/College of Information Technology/Henson Patricia Alizah (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_6",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Infante James March",
        "party": "Independent",
        "dept": "BS Information Technology - External Relations Communication Officer",
        "photo": "/College of Information Technology/Infante James March (External Relations Communication Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "External Relations Communication Officer Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_sec_1",
        "posId": "sec",
        "targetDept": "College of Information Technology",
        "name": "Judilla Cj Kyle",
        "party": "Independent",
        "dept": "BS Information Technology - Secretary",
        "photo": "/College of Information Technology/Judilla Cj Kyle (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_vp_3",
        "posId": "vp",
        "targetDept": "College of Information Technology",
        "name": "Lasig Anele Pelagia",
        "party": "Independent",
        "dept": "BS Information Technology - VP-Internal Affairs",
        "photo": "/College of Information Technology/Lasig Anele Pelagia (VP-Internal Affairs).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "VP-Internal Affairs Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_7",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Layug Abrham Beaver",
        "party": "Independent",
        "dept": "BS Information Technology - Student Development Coordinator",
        "photo": "/College of Information Technology/Layug Abrham Beaver (Student Development Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Student Development Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pres_1",
        "posId": "pres",
        "targetDept": "College of Information Technology",
        "name": "Lising Hanna Samantha",
        "party": "Independent",
        "dept": "BS Information Technology - President",
        "photo": "/College of Information Technology/Lising Hanna Samantha (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_8",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Nanola Darlene Jade",
        "party": "Independent",
        "dept": "BS Information Technology - 1st Year Representative",
        "photo": "/College of Information Technology/Nanola Darlene Jade (1st Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "1st Year Representative Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_9",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Pacleb Roi Vince",
        "party": "Independent",
        "dept": "BS Information Technology - 2nd Year Representative",
        "photo": "/College of Information Technology/Pacleb Roi Vince (2nd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "2nd Year Representative Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_10",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Pastoral Graciella",
        "party": "Independent",
        "dept": "BS Information Technology - Director For Communications",
        "photo": "/College of Information Technology/Pastoral Graciella (Director For Communications).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Director For Communications Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_tres_3",
        "posId": "tres",
        "targetDept": "College of Information Technology",
        "name": "Pena Glenn",
        "party": "Independent",
        "dept": "BS Information Technology - Business Manager",
        "photo": "/College of Information Technology/Pena Glenn (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_11",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Pineda Siegfrid",
        "party": "Independent",
        "dept": "BS Information Technology - Administrative Coordinator",
        "photo": "/College of Information Technology/Pineda Siegfrid (Administrative Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Administrative Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_12",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Punzalan Nickern John",
        "party": "Independent",
        "dept": "BS Information Technology - Assistang Representative",
        "photo": "/College of Information Technology/Punzalan Nickern John (Assistang Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Assistang Representative Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_13",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Sambo Juan Paolo",
        "party": "Independent",
        "dept": "BS Information Technology - AudioTechnical Media Coordinator",
        "photo": "/College of Information Technology/Sambo Juan Paolo (AudioTechnical Media Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "AudioTechnical Media Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_tres_4",
        "posId": "tres",
        "targetDept": "College of Information Technology",
        "name": "Serrano Markevin",
        "party": "Independent",
        "dept": "BS Information Technology - Finance Coordinator",
        "photo": "/College of Information Technology/Serrano Markevin (Finance Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Finance Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_aud_1",
        "posId": "aud",
        "targetDept": "College of Information Technology",
        "name": "Sunga Justin Vince",
        "party": "Independent",
        "dept": "BS Information Technology - Auditor",
        "photo": "/College of Information Technology/Sunga Justin Vince (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_14",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Teresa Jan Andrei",
        "party": "Independent",
        "dept": "BS Information Technology - 3rd Year Representative",
        "photo": "/College of Information Technology/Teresa Jan Andrei (3rd Year Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "3rd Year Representative Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_15",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Tolentino Kurt Laurence",
        "party": "Independent",
        "dept": "BS Information Technology - Media Staff",
        "photo": "/College of Information Technology/Tolentino Kurt Laurence (Media Staff).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Media Staff Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "cit_pro_16",
        "posId": "pro",
        "targetDept": "College of Information Technology",
        "name": "Yutuc Benedict",
        "party": "Independent",
        "dept": "BS Information Technology - Video Production Coordinator",
        "photo": "/College of Information Technology/Yutuc Benedict (Video Production Coordinator).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for College of Information Technology students.",
        "advocacies": [
            "Video Production Coordinator Student Initiatives",
            "Transparent College of Information Technology Representation"
        ]
    },
    {
        "id": "shs_tres_1",
        "posId": "tres",
        "targetDept": "Senior High School",
        "name": "Andrei D. Cabrera",
        "party": "Independent",
        "dept": "Senior High School - Treasurer",
        "photo": "/SeniorHighSchool/Andrei D. Cabrera (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_1",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Carlo Nathaniel Q. Perez",
        "party": "Independent",
        "dept": "Senior High School - Assistant to the Council",
        "photo": "/SeniorHighSchool/Carlo Nathaniel Q. Perez (Assistant to the Council).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Assistant to the Council Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_vp_1",
        "posId": "vp",
        "targetDept": "Senior High School",
        "name": "Florence Joy M. Manalo",
        "party": "Independent",
        "dept": "Senior High School - Vice President",
        "photo": "/SeniorHighSchool/Florence Joy M. Manalo (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_2",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Hailey Chad M. Reyes",
        "party": "Independent",
        "dept": "Senior High School - Internal Public Information Officer",
        "photo": "/SeniorHighSchool/Hailey Chad M. Reyes (Internal Public Information Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Internal Public Information Officer Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_3",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Isla Guenevere F. Banzuelo",
        "party": "Independent",
        "dept": "Senior High School - Grade 12 Humss Gas Representative",
        "photo": "/SeniorHighSchool/Isla Guenevere F. Banzuelo (Grade 12 Humss Gas Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 12 Humss Gas Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_4",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Jade Rhian C. Viray",
        "party": "Independent",
        "dept": "Senior High School - Grade 12 Stem Representative",
        "photo": "/SeniorHighSchool/Jade Rhian C. Viray (Grade 12 Stem Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 12 Stem Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_5",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Jaden McKenzie C. Alfonso",
        "party": "Independent",
        "dept": "Senior High School - Grade 11 Stem Representative",
        "photo": "/SeniorHighSchool/Jaden McKenzie C. Alfonso (Grade 11 Stem Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 11 Stem Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_6",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Jaycel Karla C. Zapata",
        "party": "Independent",
        "dept": "Senior High School - Grade 11 Abm Representative",
        "photo": "/SeniorHighSchool/Jaycel Karla C. Zapata (Grade 11 Abm Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 11 Abm Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_aud_1",
        "posId": "aud",
        "targetDept": "Senior High School",
        "name": "Lychelle Narisse C. Garcia",
        "party": "Independent",
        "dept": "Senior High School - Auditor",
        "photo": "/SeniorHighSchool/Lychelle Narisse C. Garcia (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_sec_1",
        "posId": "sec",
        "targetDept": "Senior High School",
        "name": "Myca Ella M. Dimitui",
        "party": "Independent",
        "dept": "Senior High School - Secretary",
        "photo": "/SeniorHighSchool/Myca Ella M. Dimitui (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pres_1",
        "posId": "pres",
        "targetDept": "Senior High School",
        "name": "Raika Angelene D. Sadac",
        "party": "Independent",
        "dept": "Senior High School - President",
        "photo": "/SeniorHighSchool/Raika Angelene D. Sadac (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_7",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Railey Joshan R. Sotto",
        "party": "Independent",
        "dept": "Senior High School - External Public Information Officer",
        "photo": "/SeniorHighSchool/Railey Joshan R. Sotto (External Public Information Officer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "External Public Information Officer Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_tres_2",
        "posId": "tres",
        "targetDept": "Senior High School",
        "name": "Rajja C. Pamintuan",
        "party": "Independent",
        "dept": "Senior High School - Business Manager",
        "photo": "/SeniorHighSchool/Rajja C. Pamintuan (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_8",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Rays Draven R. Dizon",
        "party": "Independent",
        "dept": "Senior High School - Grade 12 Abm Representative",
        "photo": "/SeniorHighSchool/Rays Draven R. Dizon (Grade 12 Abm Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 12 Abm Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "shs_pro_9",
        "posId": "pro",
        "targetDept": "Senior High School",
        "name": "Zara Elisha S. Tolentino",
        "party": "Independent",
        "dept": "Senior High School - Grade 11 Humss Gas Representative",
        "photo": "/SeniorHighSchool/Zara Elisha S. Tolentino (Grade 11 Humss Gas Representative).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Senior High School students.",
        "advocacies": [
            "Grade 11 Humss Gas Representative Student Initiatives",
            "Transparent Senior High School Representation"
        ]
    },
    {
        "id": "jhs_sec_1",
        "posId": "sec",
        "targetDept": "Junior High School",
        "name": "Bethia Reiko D. Dizon",
        "party": "Independent",
        "dept": "Junior High School - Secretary",
        "photo": "/JuniorHighSchool/Bethia Reiko D. Dizon (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "jhs_tres_1",
        "posId": "tres",
        "targetDept": "Junior High School",
        "name": "Jazzy C. Miranda",
        "party": "Independent",
        "dept": "Junior High School - Treasurer",
        "photo": "/JuniorHighSchool/Jazzy C. Miranda (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "jhs_pres_1",
        "posId": "pres",
        "targetDept": "Junior High School",
        "name": "Juliana Isabella D. Dizon",
        "party": "Independent",
        "dept": "Junior High School - President",
        "photo": "/JuniorHighSchool/Juliana Isabella D. Dizon (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "jhs_vp_1",
        "posId": "vp",
        "targetDept": "Junior High School",
        "name": "Khristen John L. Escoto",
        "party": "Independent",
        "dept": "Junior High School - Vice President",
        "photo": "/JuniorHighSchool/Khristen John L. Escoto (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "jhs_aud_1",
        "posId": "aud",
        "targetDept": "Junior High School",
        "name": "Paul Vince C. Asuncion",
        "party": "Independent",
        "dept": "Junior High School - Auditor",
        "photo": "/JuniorHighSchool/Paul Vince C. Asuncion (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "jhs_pro_1",
        "posId": "pro",
        "targetDept": "Junior High School",
        "name": "Yvonne Sarah F. Garcia",
        "party": "Independent",
        "dept": "Junior High School - P.R.O",
        "photo": "/JuniorHighSchool/Yvonne Sarah F. Garcia (P.R.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for Junior High School students.",
        "advocacies": [
            "P.R.O Student Initiatives",
            "Transparent Junior High School Representation"
        ]
    },
    {
        "id": "ucscu_tres_1",
        "posId": "tres",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Alaina Gracie Macapagal",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - Treasurer",
        "photo": "/UACSC Officers under Siklab/Alaina Gracie Macapagal (Treasurer).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "Treasurer Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_aud_1",
        "posId": "aud",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Althea Jodie Zerna",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - Auditor",
        "photo": "/UACSC Officers under Siklab/Althea Jodie Zerna (Auditor).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "Auditor Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_sec_1",
        "posId": "sec",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Eushobelle David",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - Secretary",
        "photo": "/UACSC Officers under Siklab/Eushobelle David (Secretary).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "Secretary Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_pro_1",
        "posId": "pro",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Gabriell Joie Pineda",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - P.I.O",
        "photo": "/UACSC Officers under Siklab/Gabriell Joie Pineda (P.I.O).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "P.I.O Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_pres_1",
        "posId": "pres",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Garnett Tolentino",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - President",
        "photo": "/UACSC Officers under Siklab/Garnett Tolentino (President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "President Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_vp_1",
        "posId": "vp",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "James Marc Infante",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - Vice President",
        "photo": "/UACSC Officers under Siklab/James Marc Infante (Vice President).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "Vice President Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    },
    {
        "id": "ucscu_tres_2",
        "posId": "tres",
        "targetDept": "University Central Student Council (UACSC)",
        "name": "Ralph Lauren Batac",
        "party": "SIKLAB",
        "dept": "UA Central Student Council - Business Manager",
        "photo": "/UACSC Officers under Siklab/Ralph Lauren Batac (Business Manager).png",
        "platform": "Dedicated leadership, transparent student governance, and active representation for University Central Student Council (UACSC) students.",
        "advocacies": [
            "Business Manager Student Initiatives",
            "Transparent University Central Student Council (UACSC) Representation"
        ]
    }
]

default_students = [
    {
        "id": "2024000669",
        "name": "Maria Clara T. Santos",
        "email": "mctsantos.student@ua.edu.ph",
        "dept": "College of Accountancy",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2023001244",
        "name": "Juan Dela T. Cruz",
        "email": "jdtcruz.student@ua.edu.ph",
        "dept": "College of Engineering and Architecture",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024001882",
        "name": "Camille Rose P. Diaz",
        "email": "crpdiaz.student@ua.edu.ph",
        "dept": "College of Hospitality and Tourism Management",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024006843",
        "name": "Jaena B. Mangulabnan",
        "email": "jbmangulabnan.student@ua.edu.ph",
        "dept": "College of Nursing and Pharmacy",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2023004490",
        "name": "Beatriz Nicole L. Gomez",
        "email": "bnlgomez.student@ua.edu.ph",
        "dept": "School of Arts and Sciences",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2022009831",
        "name": "Sofia Bianca R. Dizon",
        "email": "sbrdizon.student@ua.edu.ph",
        "dept": "School of Business and Public Administration",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024003319",
        "name": "Mark Anthony V. Ramos",
        "email": "mavramos.student@ua.edu.ph",
        "dept": "School of Education",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024001155",
        "name": "Angelo G. Gomez",
        "email": "aggomez.student@ua.edu.ph",
        "dept": "College of Information Technology",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024005576",
        "name": "Jaenaganda M. Cruz",
        "email": "jmcruz.student@ua.edu.ph",
        "dept": "Senior High School",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    },
    {
        "id": "2024008812",
        "name": "Joshua L. Garcia",
        "email": "jlgarcia.student@ua.edu.ph",
        "dept": "Junior High School",
        "verified": True,
        "passwordHash": "85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b"
    }
]
print(f"Candidates: {len(candidates_data)}, Students: {len(default_students)}")

def generate_student_html():
    candidates_json = json.dumps(candidates_data)
    students_json = json.dumps(default_students)
    depts_json = json.dumps(DEPARTMENTS)
    positions_json = json.dumps(POSITIONS)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniVote - University of the Assumption Student Portal</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- CryptoJS for AES-256 and SHA-256 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Canvas Confetti -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <!-- QR Code Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <!-- Font Family -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- External CSS -->
    <link rel="stylesheet" href="/static/css/student.css">
    <style>
        @media print {{
            body * {{ visibility: hidden !important; }}
            #receiptModal, #receiptModal * {{ visibility: visible !important; }}
            #receiptModal {{
                position: fixed !important;
                left: 0 !important;
                top: 0 !important;
                width: 100vw !important;
                height: 100vh !important;
                background: white !important;
                padding: 15px !important;
                margin: 0 !important;
                display: flex !important;
                justify-content: center !important;
                align-items: flex-start !important;
                z-index: 999999 !important;
            }}
            #receiptModal > div {{
                max-width: 100% !important;
                width: 100% !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }}
            .no-print, button, nav {{ display: none !important; }}
        }}
    </style>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Plus Jakarta Sans', 'sans-serif'],
                    }},
                    colors: {{
                        ua: {{
                            navy: '#020381',
                            royal: '#1e3a8a',
                            gold: '#d97706',
                            goldlight: '#fef3c7',
                            red: '#cf2e2e',
                            ice: '#f0f4ff'
                        }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col selection:bg-blue-600 selection:text-white">

    <!-- Top Navigation Bar -->
    <nav class="bg-white/95 backdrop-blur-md border-b border-slate-200/80 sticky top-0 z-40 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                
                <!-- UA & UniVote Brand Logo with Official Seal -->
                <div class="flex items-center space-x-3 cursor-pointer" onclick="switchMainTab('ballot')">
                    <img src="/templates/ua-logo.png" alt="University of the Assumption Seal" class="w-12 h-12 object-contain drop-shadow" onerror="this.onerror=null; this.src='/ua-logo.png';">
                    <div>
                        <div class="flex items-center space-x-2">
                            <span class="text-2xl font-black text-slate-900 tracking-tight">Uni<span class="text-blue-700">Vote</span></span>
                            <span class="bg-amber-100 text-amber-800 text-[10px] font-bold px-2.5 py-0.5 rounded-full border border-amber-200">UA PAMPANGA</span>
                        </div>
                        <p class="text-[11px] text-slate-500 font-semibold">Virtus • Scientia • Communitas</p>
                    </div>
                </div>

                <!-- Modern Segmented Pill Nav Tabs -->
                <div class="hidden lg:flex items-center bg-slate-100/90 p-1.5 rounded-2xl border border-slate-200/80 shadow-inner">
                    <button onclick="switchMainTab('ballot')" id="tab-nav-ballot" class="nav-tab-btn px-5 py-2.5 rounded-xl text-xs font-extrabold transition-all duration-200 flex items-center space-x-2 bg-blue-700 text-white shadow-md shadow-blue-700/20">
                        <i data-lucide="vote" class="w-4 h-4"></i>
                        <span>Voting Portal</span>
                    </button>
                    <button onclick="switchMainTab('results')" id="tab-nav-results" class="nav-tab-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 flex items-center space-x-2 text-slate-600 hover:text-blue-700 hover:bg-white/60">
                        <i data-lucide="trophy" class="w-4 h-4"></i>
                        <span>Official Results</span>
                    </button>
                    <button onclick="switchMainTab('partylists')" id="tab-nav-partylists" class="nav-tab-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all duration-200 flex items-center space-x-2 text-slate-600 hover:text-blue-700 hover:bg-white/60">
                        <i data-lucide="flag" class="w-4 h-4"></i>
                        <span>Partylists &amp; Advocacies</span>
                    </button>
                </div>

                <!-- Student Status / Verification / Auth Control -->
                <div class="flex items-center space-x-2.5">
                    <div id="voterBadge" class="hidden flex items-center space-x-2 bg-blue-50 border border-blue-200 px-3 py-1.5 rounded-full text-xs text-blue-800 font-medium shadow-sm">
                        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        <i data-lucide="user-check" class="w-4 h-4 text-blue-700"></i>
                        <span id="voterIdentityDisplay" class="font-bold">Student Active</span>
                    </div>

                    <!-- Separate Sign In and Registration Nav Buttons (Distinct and not mixed) -->
                    <div id="unauthNavGroup" class="flex items-center space-x-2">
                        <button onclick="openSignInModal()" class="flex items-center space-x-1.5 bg-ua-navy hover:bg-blue-800 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition shadow-md">
                            <i data-lucide="log-in" class="w-4 h-4 text-amber-400"></i>
                            <span>Sign In</span>
                        </button>
                        <button onclick="openRegisterModal()" class="flex items-center space-x-1.5 bg-white hover:bg-slate-50 text-blue-800 border border-slate-300 font-bold text-xs px-3.5 py-2.5 rounded-xl transition shadow-sm">
                            <i data-lucide="user-plus" class="w-4 h-4 text-blue-700"></i>
                            <span>Register</span>
                        </button>
                    </div>

                    <button id="logoutBtn" onclick="handleStudentLogout()" class="hidden bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold text-xs px-3 py-2.5 rounded-xl transition flex items-center space-x-1.5">
                        <i data-lucide="log-out" class="w-4 h-4 text-slate-500"></i>
                        <span>Log Out</span>
                    </button>
                </div>

            </div>
        </div>

        <!-- Mobile Nav Bar Tabs -->
        <div class="lg:hidden flex border-t border-slate-200 bg-slate-100 p-2 space-x-1.5 overflow-x-auto custom-scrollbar">
            <button onclick="switchMainTab('ballot')" id="mob-tab-nav-ballot" class="mob-nav-tab-btn flex-1 py-2 px-3 text-xs font-bold rounded-xl bg-blue-700 text-white whitespace-nowrap transition-all shadow-sm">Voting Portal</button>
            <button onclick="switchMainTab('results')" id="mob-tab-nav-results" class="mob-nav-tab-btn flex-1 py-2 px-3 text-xs font-bold rounded-xl bg-white text-slate-600 whitespace-nowrap transition-all border border-slate-200">Official Results</button>
            <button onclick="switchMainTab('partylists')" id="mob-tab-nav-partylists" class="mob-nav-tab-btn flex-1 py-2 px-3 text-xs font-bold rounded-xl bg-white text-slate-600 whitespace-nowrap transition-all border border-slate-200">Partylists</button>
        </div>
    </nav>

    <!-- Main Content Container -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">

        <!-- ================= PAGE 1: VOTING PORTAL ================= -->
        <div id="page-ballot" class="main-page-section space-y-8">
            
            <!-- Simplified Header Banner (Dynamic Election Schedule Retained) -->
            <div class="ua-hero-bg rounded-3xl p-8 md:p-10 text-white shadow-xl shadow-blue-900/15 relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 w-72 h-72 bg-blue-400/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="relative z-10 max-w-3xl space-y-4">
                    <div class="inline-flex items-center space-x-2 bg-white/10 backdrop-blur-md px-3.5 py-1.5 rounded-full text-xs font-medium border border-white/20">
                        <i data-lucide="shield" class="w-3.5 h-3.5 text-amber-300"></i>
                        <span id="activeElectionBannerTitle">University of the Assumption Elections</span>
                    </div>
                    <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight leading-tight">
                        Cast Your Vote with Absolute Secrecy &amp; Integrity
                    </h1>
                    
                    <!-- Clean Official Election Schedule Badge -->
                    <div class="inline-flex items-center space-x-3 bg-white/10 backdrop-blur-md px-4 py-2 rounded-2xl border border-white/15">
                        <i data-lucide="calendar" class="w-4 h-4 text-amber-300 shrink-0"></i>
                        <div>
                            <p class="text-[10px] text-blue-200 uppercase font-bold tracking-wider">Official Election Schedule</p>
                            <p class="text-xs sm:text-sm font-bold text-white mt-0.5" id="electionScheduleDisplay">2026-10-01 to 2026-11-30</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sign-in Prompt Notice -->
            <div id="unauthNotice" class="bg-amber-50 border-2 border-amber-300 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center shrink-0">
                        <i data-lucide="lock" class="w-6 h-6 text-amber-700"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Department-Locked Access: Sign In to Unlock Ballot</h3>
                        <p class="text-slate-600 text-xs mt-0.5">Under UA Election Commission policy, student council positions and candidate slates are restricted strictly to your enrolled department. Sign in or register with your institutional <strong>@ua.edu.ph</strong> email to access your official ballot.</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2 shrink-0">
                    <button onclick="openSignInModal()" class="bg-ua-navy hover:bg-blue-800 text-white font-bold text-xs px-5 py-3 rounded-2xl transition shadow-md flex items-center space-x-1.5">
                        <i data-lucide="log-in" class="w-4 h-4 text-amber-400"></i>
                        <span>Sign In</span>
                    </button>
                    <button onclick="openRegisterModal()" class="bg-white hover:bg-slate-50 text-blue-800 border border-slate-300 font-bold text-xs px-4 py-3 rounded-2xl transition shadow-sm flex items-center space-x-1.5">
                        <i data-lucide="user-plus" class="w-4 h-4 text-blue-700"></i>
                        <span>Register</span>
                    </button>
                </div>
            </div>

            <!-- Election Inactive Notice Banner -->
            <div id="electionInactiveBanner" class="hidden bg-slate-800 text-amber-300 border border-amber-500/30 p-4 rounded-2xl text-xs font-bold flex items-center space-x-3">
                <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-400 shrink-0"></i>
                <span>Notice: Voting is currently closed or deactivated by the UA Election Commission. Ballots cannot be submitted at this time.</span>
            </div>

            <!-- Full-Width Candidate Slate Container -->
            <div class="space-y-6">
                
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-5 rounded-3xl border border-blue-100 shadow-sm">
                    <div>
                        <h2 class="text-xl font-extrabold text-slate-900 flex items-center space-x-2">
                            <i data-lucide="users" class="w-5 h-5 text-blue-700"></i>
                            <span id="candidateSectionTitle">Official Candidate Slate</span>
                        </h2>
                        <p class="text-xs text-slate-500" id="candidateSectionSub">Sign in with your UA account to view candidates for your department</p>
                    </div>
                    
                    <div class="flex items-center space-x-2">
                        <div class="relative">
                            <input type="text" id="candidateSearch" onkeyup="renderCandidateCards()" placeholder="Search candidate or party..." class="pl-9 pr-4 py-2.5 text-xs border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none w-56">
                            <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-3"></i>
                        </div>
                    </div>
                </div>

                <!-- Position Filter Tabs -->
                <div class="flex items-center space-x-2 overflow-x-auto pb-1 custom-scrollbar" id="positionTabs">
                    <!-- Dynamic Position Tabs -->
                </div>

                <!-- Candidate Cards Container -->
                <div id="candidateCardsContainer" class="space-y-4">
                    <!-- Dynamic Candidates -->
                </div>

            </div>

            <!-- Sleek Ballot Review & Action Bar -->
            <div id="ballotActionBar" class="sticky bottom-6 z-30 bg-white/95 backdrop-blur-md rounded-3xl p-4 sm:p-5 border border-blue-200 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="flex items-center space-x-3.5">
                    <div class="w-11 h-11 rounded-2xl bg-blue-100 text-blue-700 flex items-center justify-center shrink-0">
                        <i data-lucide="check-circle-2" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h4 class="font-bold text-slate-900 text-sm" id="ballotSelectionSummaryTitle">Official Ballot Selections</h4>
                            <span id="ballotCountBadge" class="bg-blue-100 text-blue-800 text-[10px] font-extrabold px-2 py-0.5 rounded-full border border-blue-200">0 of 6 Selected</span>
                        </div>
                        <p class="text-xs text-slate-500" id="ballotSelectionSummarySub">Select candidates across your department council positions to cast your vote</p>
                    </div>
                </div>

                <div class="flex items-center space-x-3 w-full sm:w-auto">
                    <button id="reviewBallotBtn" onclick="openReviewModal()" class="w-full sm:w-auto bg-ua-navy hover:bg-blue-800 disabled:bg-slate-200 disabled:text-slate-400 disabled:cursor-not-allowed text-white font-bold py-3.5 px-6 rounded-2xl transition shadow-lg flex items-center justify-center space-x-2 text-xs">
                        <i data-lucide="check-square" class="w-4 h-4 text-amber-400"></i>
                        <span id="reviewBallotBtnText">Sign In to Cast Vote</span>
                    </button>
                </div>
            </div>

        </div>

        <!-- ================= PAGE 2: OFFICIAL RESULTS & WINNERS (ALL 10 DEPARTMENTS) ================= -->
        <div id="page-results" class="main-page-section hidden space-y-8">
            <div class="bg-gradient-to-r from-blue-900 via-blue-800 to-slate-900 text-white rounded-3xl p-8 shadow-xl space-y-3">
                <span class="bg-amber-400 text-slate-950 text-[10px] font-black px-2.5 py-1 rounded-full uppercase tracking-wider">Official Election Outcomes</span>
                <h2 class="text-3xl font-extrabold">Department Election Results &amp; Certified Winners</h2>
                <p class="text-blue-100 text-sm">Official tallied results published by the University of the Assumption Election Commission.</p>
                
                <!-- Department Selector on Results Page -->
                <div class="pt-2 flex flex-wrap items-center gap-2" id="resultsDeptSelectorContainer">
                    <span class="text-xs text-blue-200 font-bold uppercase tracking-wider mr-2">Filter Department:</span>
                    <button onclick="switchResultsDept('College of Accountancy')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-blue-700 text-white border border-blue-500" data-dept="College of Accountancy">College of Accountancy</button>
                    <button onclick="switchResultsDept('College of Engineering and Architecture')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="College of Engineering and Architecture">College of Engineering and Architecture</button>
                    <button onclick="switchResultsDept('College of Hospitality and Tourism Management')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="College of Hospitality and Tourism Management">College of Hospitality and Tourism Management</button>
                    <button onclick="switchResultsDept('College of Nursing and Pharmacy')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="College of Nursing and Pharmacy">College of Nursing and Pharmacy</button>
                    <button onclick="switchResultsDept('School of Arts and Sciences')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="School of Arts and Sciences">School of Arts and Sciences</button>
                    <button onclick="switchResultsDept('School of Business and Public Administration')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="School of Business and Public Administration">School of Business and Public Administration</button>
                    <button onclick="switchResultsDept('School of Education')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="School of Education">School of Education</button>
                    <button onclick="switchResultsDept('College of Information Technology')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="College of Information Technology">College of Information Technology</button>
                    <button onclick="switchResultsDept('Senior High School')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="Senior High School">Senior High School</button>
                    <button onclick="switchResultsDept('Junior High School')" class="res-dept-btn px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white/10 text-white hover:bg-white/20 border border-white/20" data-dept="Junior High School">Junior High School</button>
                </div>
            </div>

            <!-- Results Content Area -->
            <div id="resultsContentArea" class="space-y-6">
                <!-- Dynamic Content injected in JS -->
            </div>
        </div>

        <!-- ================= PAGE 3: DEPARTMENT PARTYLISTS & ADVOCACIES (ALL 10 DEPTS) ================= -->
        <div id="page-partylists" class="main-page-section hidden space-y-8">
            
            <div class="relative rounded-3xl overflow-hidden shadow-xl bg-slate-900 text-white">
                <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&q=80&w=1200" alt="UA Campus Life" class="w-full h-64 object-cover opacity-35">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-900/60 to-transparent flex flex-col justify-end p-8">
                    <div class="max-w-3xl space-y-2">
                        <span class="bg-amber-500 text-slate-950 text-xs font-black px-3 py-1 rounded-full uppercase tracking-wider">OFFICIAL PARTYLIST DIRECTORY</span>
                        <h2 class="text-3xl md:text-4xl font-extrabold text-white">Department Partylists, Platforms &amp; Advocacies</h2>
                        <p class="text-blue-100 text-sm">Explore student political parties across university departments and councils.</p>
                    </div>
                </div>
            </div>

            <div class="flex items-center justify-between bg-white p-4 rounded-3xl border border-blue-100 shadow-sm flex-wrap gap-3">
                <span class="text-xs font-bold text-slate-700 uppercase tracking-wider">Select Department:</span>
                <div class="flex items-center space-x-2 overflow-x-auto pb-1" id="partylistFilterTabs">
                    <button onclick="filterPartylists('College of Accountancy')" id="btn-partylist-acc" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition bg-blue-700 text-white whitespace-nowrap">College of Accountancy</button>
                    <button onclick="filterPartylists('College of Engineering and Architecture')" id="btn-partylist-cea" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">College of Engineering and Architecture</button>
                    <button onclick="filterPartylists('College of Hospitality and Tourism Management')" id="btn-partylist-chtm" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">College of Hospitality and Tourism Management</button>
                    <button onclick="filterPartylists('College of Nursing and Pharmacy')" id="btn-partylist-cnp" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">College of Nursing and Pharmacy</button>
                    <button onclick="filterPartylists('School of Arts and Sciences')" id="btn-partylist-sas" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">School of Arts and Sciences</button>
                    <button onclick="filterPartylists('School of Business and Public Administration')" id="btn-partylist-sbpa" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">School of Business and Public Administration</button>
                    <button onclick="filterPartylists('School of Education')" id="btn-partylist-sed" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">School of Education</button>
                    <button onclick="filterPartylists('College of Information Technology')" id="btn-partylist-it" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">College of Information Technology</button>
                    <button onclick="filterPartylists('Senior High School')" id="btn-partylist-shs" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">Senior High School</button>
                    <button onclick="filterPartylists('Junior High School')" id="btn-partylist-jhs" class="partylist-dept-btn px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-600 hover:bg-slate-100 whitespace-nowrap">Junior High School</button>
                </div>
            </div>

            <div id="partylistsContainer" class="space-y-6"></div>

        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 py-6 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500">
            <div class="flex items-center space-x-2">
                <i data-lucide="shield" class="w-4 h-4 text-blue-700"></i>
                <span class="font-bold text-slate-800">University of the Assumption UniVote System</span>
                <span>• Official Commission Certified Portal</span>
            </div>
            <div>
                © 2026 University of the Assumption. All rights reserved.
            </div>
        </div>
    </footer>

    <!-- Review Choices Modal -->
    <div id="reviewChoicesModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-5 shadow-2xl border border-blue-100">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <h3 class="font-extrabold text-slate-900 text-base flex items-center space-x-2">
                    <i data-lucide="check-square" class="w-5 h-5 text-blue-700"></i>
                    <span>Review Your Selections</span>
                </h3>
                <button onclick="closeReviewModal()" type="button" class="text-slate-400 hover:text-slate-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <p class="text-xs text-slate-600">Please carefully verify your chosen candidates for your department before submitting your official ballot.</p>

            <div id="reviewChoicesList" class="space-y-2 max-h-64 overflow-y-auto custom-scrollbar border-y py-3">
                <!-- Dynamically injected choices -->
            </div>

            <div class="bg-blue-50 border border-blue-200 p-3.5 rounded-2xl text-[11px] text-blue-900 space-y-1">
                <p class="font-bold flex items-center space-x-1.5 text-blue-950">
                    <i data-lucide="shield-check" class="w-4 h-4 text-blue-700"></i>
                    <span>Official Submission Notice</span>
                </p>
                <p>Once cast, your ballot is cryptographically recorded in the Commission audit registry and cannot be altered or re-voted.</p>
            </div>

            <div class="flex space-x-3 pt-2">
                <button onclick="closeReviewModal()" class="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3 rounded-xl text-xs transition">Modify Choices</button>
                <button onclick="submitBallot()" class="flex-1 bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 rounded-xl text-xs shadow-md transition">Confirm &amp; Cast Ballot</button>
            </div>
        </div>
    </div>

    <!-- ================= MODAL 1: DEDICATED SIGN IN MODAL ================= -->
    <div id="signInModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-5 border border-blue-100 shadow-2xl relative">
            <div class="flex items-center justify-between border-b pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-ua-navy flex items-center justify-center text-white shadow-sm">
                        <i data-lucide="log-in" class="w-5 h-5 text-amber-400"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Student Sign In</h3>
                        <p class="text-[11px] text-slate-500">Access your department official ballot</p>
                    </div>
                </div>
                <button onclick="closeSignInModal()" type="button" class="text-slate-400 hover:text-slate-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <!-- Inline Alert Message Box -->
            <div id="signInAlertBox" class="hidden text-xs p-3 rounded-2xl border font-semibold"></div>

            <form id="formStudentLogin" onsubmit="handleAuthenticate(event)" class="space-y-4 text-xs">
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        UA Student ID <span class="text-rose-500">*</span>
                        <span class="text-[10px] text-slate-400 font-normal">(10 digits, year 2010–2026)</span>
                    </label>
                    <input type="text" id="authStudentId" required maxlength="10" placeholder="e.g. 2024000669" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none font-mono">
                </div>
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        UA Institutional Email <span class="text-rose-500">*</span>
                    </label>
                    <input type="email" id="authStudentEmail" required placeholder="e.g. jdtcruz.student@ua.edu.ph" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        Account Password <span class="text-rose-500">*</span>
                    </label>
                    <div class="relative">
                        <input type="password" id="authPassword" required placeholder="Enter your password" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility('authPassword', 'eyeAuthPassword')" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-700 focus:outline-none">
                            <i data-lucide="eye" id="eyeAuthPassword" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                <button type="submit" class="w-full bg-ua-navy text-white font-bold py-3 rounded-xl hover:bg-blue-800 transition shadow-md flex items-center justify-center space-x-2">
                    <i data-lucide="log-in" class="w-4 h-4 text-amber-400"></i>
                    <span>Authenticate &amp; Access Department Ballot</span>
                </button>
            </form>

            <div class="border-t pt-3 text-center">
                <p class="text-xs text-slate-600">
                    Don't have an account yet? 
                    <button onclick="switchToRegisterModal()" class="font-bold text-blue-700 hover:underline">First-Time Registration</button>
                </p>
            </div>
        </div>
    </div>

    <!-- ================= MODAL 2: DEDICATED FIRST-TIME REGISTRATION MODAL ================= -->
    <div id="registerModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 border border-blue-100 shadow-2xl relative max-h-[95vh] overflow-y-auto custom-scrollbar">
            <div class="flex items-center justify-between border-b pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-emerald-700 flex items-center justify-center text-white shadow-sm">
                        <i data-lucide="user-plus" class="w-5 h-5 text-emerald-200"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">First-Time Registration</h3>
                        <p class="text-[11px] text-slate-500">Enroll your student voter account</p>
                    </div>
                </div>
                <button onclick="closeRegisterModal()" type="button" class="text-slate-400 hover:text-slate-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <!-- Inline Alert Message Box -->
            <div id="registerAlertBox" class="hidden text-xs p-3 rounded-2xl border font-semibold"></div>

            <form id="formStudentRegister" onsubmit="handleStudentRegistration(event)" class="space-y-3.5 text-xs">
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        UA Student ID <span class="text-rose-500">*</span>
                        <span class="text-[10px] text-slate-400 font-normal">(10 digits, year 2010–2026)</span>
                    </label>
                    <input type="text" id="regStudentId" required maxlength="10" placeholder="e.g. 2024000669" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none font-mono">
                </div>
                <div>
                    <!-- Requested: Label is strictly 'Full Student Name *' without extra notes -->
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        Full Student Name <span class="text-rose-500">*</span>
                    </label>
                    <input type="text" id="regStudentName" oninput="updateDerivedEmailSuggestion()" required placeholder="e.g. Juan Dela T. Cruz" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>
                <div>
                    <!-- Requested: Label is strictly 'UA Institutional Email *' without extra notes -->
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        UA Institutional Email <span class="text-rose-500">*</span>
                    </label>
                    <input type="email" id="regStudentEmail" required placeholder="e.g. jdtcruz.student@ua.edu.ph" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>
                <div>
                    <!-- Department dropdown with all 8 colleges + Senior High + Junior High -->
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Department <span class="text-rose-500">*</span></label>
                    <select id="regDepartment" required class="w-full px-4 py-2.5 border border-slate-200 rounded-xl bg-white focus:ring-2 focus:ring-blue-600 focus:outline-none font-semibold text-slate-800">
                        <option value="College of Accountancy">College of Accountancy</option>
                        <option value="College of Engineering and Architecture">College of Engineering and Architecture</option>
                        <option value="College of Hospitality and Tourism Management">College of Hospitality and Tourism Management</option>
                        <option value="College of Nursing and Pharmacy">College of Nursing and Pharmacy</option>
                        <option value="School of Arts and Sciences">School of Arts and Sciences</option>
                        <option value="School of Business and Public Administration">School of Business and Public Administration</option>
                        <option value="School of Education">School of Education</option>
                        <option value="College of Information Technology">College of Information Technology</option>
                        <option value="Senior High School">Senior High School</option>
                        <option value="Junior High School">Junior High School</option>
                    </select>
                </div>
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">
                        Create Account Password <span class="text-rose-500">*</span>
                        <span class="text-[10px] text-slate-400 font-normal">(Min 8 chars, must contain special char: *, _, +, @, #, !)</span>
                    </label>
                    <div class="relative">
                        <input type="password" id="regPassword" required minlength="8" placeholder="Must include special character (*, _, +, @, #, !)" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility('regPassword', 'eyeRegPassword')" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-700 focus:outline-none">
                            <i data-lucide="eye" id="eyeRegPassword" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Confirm Account Password <span class="text-rose-500">*</span></label>
                    <div class="relative">
                        <input type="password" id="regConfirmPassword" required minlength="8" placeholder="Re-enter password" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility('regConfirmPassword', 'eyeRegConfirmPassword')" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-700 focus:outline-none">
                            <i data-lucide="eye" id="eyeRegConfirmPassword" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                <button type="submit" class="w-full bg-emerald-700 text-white font-bold py-3 rounded-xl hover:bg-emerald-800 transition shadow-md flex items-center justify-center space-x-2">
                    <i data-lucide="user-plus" class="w-4 h-4 text-emerald-200"></i>
                    <span>Register Account</span>
                </button>
            </form>

            <div class="border-t pt-3 text-center">
                <p class="text-xs text-slate-600">
                    Already have an account? 
                    <button onclick="switchToSignInModal()" class="font-bold text-blue-700 hover:underline">Sign In here</button>
                </p>
            </div>
        </div>
    </div>

    <!-- ================= MODAL 3: REGISTRATION SUCCESSFUL MODAL ================= -->
    <div id="regSuccessModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 text-center space-y-4 border border-blue-100 shadow-2xl">
            <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center shadow-inner">
                <i data-lucide="check-circle" class="w-10 h-10"></i>
            </div>
            <div class="space-y-1">
                <h3 class="text-xl font-extrabold text-slate-900">Registration Successful!</h3>
                <p class="text-xs text-slate-600 leading-relaxed" id="regSuccessMessage">
                    Your student account is now registered in the UniVote system. Please sign in with your credentials to access your official department ballot.
                </p>
            </div>
            <div class="bg-slate-50 border border-slate-200 p-3 rounded-2xl text-xs font-mono text-slate-700 text-left space-y-1" id="regSuccessSummary">
                <!-- Injected in JS -->
            </div>
            <button onclick="proceedFromRegSuccessToSignIn()" class="w-full bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 rounded-xl transition shadow-md flex items-center justify-center space-x-2 text-xs">
                <i data-lucide="log-in" class="w-4 h-4 text-amber-400"></i>
                <span>Proceed to Sign In</span>
            </button>
        </div>
    </div>

    <!-- Digital Voting Receipt Modal with Permanent QR Code -->
    <div id="receiptModal" class="fixed inset-0 bg-slate-900/75 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-xl w-full p-6 space-y-5 shadow-2xl border border-blue-100 max-h-[92vh] overflow-y-auto">
            
            <div class="text-center space-y-1.5 no-print">
                <div class="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center shadow-inner">
                    <i data-lucide="check-circle-2" class="w-8 h-8"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-900">Ballot Cast Successfully!</h3>
                <p class="text-xs text-slate-500">Your official electronic ballot has been cryptographically recorded and verified by the UA Election Commission.</p>
            </div>

            <!-- Printable Official Digital Receipt Card -->
            <div id="printableReceipt" class="bg-slate-50 border border-slate-200 rounded-3xl p-5 space-y-4 font-mono text-xs shadow-sm">
                
                <!-- Receipt Card Header with UA Seal -->
                <div class="flex justify-between items-center border-b border-slate-200 pb-3 font-sans">
                    <div class="flex items-center space-x-3">
                        <img src="/templates/ua-logo.png" alt="University of the Assumption Seal" class="w-12 h-12 object-contain" onerror="this.onerror=null; this.src='/ua-logo.png';">
                        <div>
                            <span class="font-black text-blue-950 text-base block leading-tight">UniVote Official Digital Receipt</span>
                            <p class="text-[10px] text-slate-500 font-semibold">University of the Assumption • Pampanga</p>
                        </div>
                    </div>
                    <span class="text-emerald-700 text-[10px] font-black bg-emerald-100 px-3 py-1 rounded-full border border-emerald-300 uppercase tracking-wider">
                        VERIFIED BALLOT ✓
                    </span>
                </div>

                <!-- Timestamp & Department Metadata -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-sans">
                    <div class="bg-white p-2.5 rounded-xl border border-slate-200">
                        <span class="text-slate-400 block text-[9px] uppercase tracking-wider font-extrabold">VOTING TIMESTAMP</span>
                        <span id="receiptTimestamp" class="font-extrabold text-slate-900 text-xs"></span>
                    </div>
                    <div class="bg-white p-2.5 rounded-xl border border-slate-200">
                        <span class="text-slate-400 block text-[9px] uppercase tracking-wider font-extrabold">ACADEMIC DEPARTMENT</span>
                        <span id="receiptDept" class="font-extrabold text-blue-800 text-xs"></span>
                    </div>
                </div>

                <!-- Verified Student Details -->
                <div class="space-y-1.5 font-sans bg-white p-3 rounded-2xl border border-slate-200 text-[11px]">
                    <div class="flex justify-between items-center py-0.5">
                        <span class="text-slate-500 font-bold">Student ID:</span>
                        <span id="receiptStudentId" class="font-extrabold text-slate-900 font-mono text-xs"></span>
                    </div>
                    <div class="flex justify-between items-center py-0.5">
                        <span class="text-slate-500 font-bold">Voter Name:</span>
                        <span id="receiptStudentName" class="font-extrabold text-slate-900"></span>
                    </div>
                    <div class="flex justify-between items-center py-0.5">
                        <span class="text-slate-500 font-bold">Institutional Email:</span>
                        <span id="receiptStudentEmail" class="font-semibold text-slate-700 font-mono text-[10px]"></span>
                    </div>
                    <div class="flex justify-between items-center pt-1 border-t border-slate-100">
                        <span class="text-slate-500 font-bold">Voter Security Token:</span>
                        <span id="receiptToken" class="text-blue-700 font-bold break-all font-mono text-[9px] max-w-[260px] text-right"></span>
                    </div>
                </div>

                <!-- Official Recorded Ballot Selections -->
                <div class="font-sans space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-[10px] uppercase font-black text-slate-500 tracking-wider">OFFICIAL CANDIDATE CHOICES RECORDED (6 OF 6 RACES)</span>
                        <span class="text-[10px] font-bold text-blue-700">6 / 6 Complete</span>
                    </div>
                    <div id="receiptChoicesList" class="space-y-1.5">
                        <!-- Injected via JavaScript -->
                    </div>
                </div>

                <!-- Ballot Audit Trail Cipher -->
                <div class="font-sans space-y-1">
                    <span class="text-slate-400 block text-[9px] uppercase tracking-wider font-extrabold">AES-256 AUDIT TRAIL CIPHER PAYLOAD</span>
                    <span id="receiptCipherHash" class="text-slate-600 break-all text-[9px] bg-white p-2.5 rounded-xl border border-slate-200 font-mono block max-h-16 overflow-y-auto leading-relaxed"></span>
                </div>

                <!-- Scannable Digital Receipt QR Code Card -->
                <div class="flex flex-col items-center justify-center pt-2 font-sans space-y-2 border-t border-slate-200">
                    <div class="p-3 bg-white rounded-2xl border-2 border-slate-300 shadow-sm inline-flex items-center justify-center">
                        <div id="qrcodeCanvas" class="flex items-center justify-center min-w-[140px] min-h-[140px]"></div>
                    </div>
                    <p class="text-[10px] text-slate-500 font-bold text-center">
                        Official Scannable Verification QR Code • Encodes permanent payload with voting timestamp, student ID &amp; votes
                    </p>
                </div>
            </div>

            <!-- Modal Action Buttons -->
            <div class="flex flex-wrap items-center gap-2 pt-1 no-print">
                <button type="button" onclick="window.print()" class="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-700 font-black py-3 px-3 rounded-2xl transition text-xs flex items-center justify-center space-x-1.5 border border-slate-200 shadow-xs">
                    <i data-lucide="printer" class="w-4 h-4"></i>
                    <span>Print Receipt</span>
                </button>
                <button type="button" onclick="downloadDigitalReceipt()" class="flex-1 bg-amber-500 hover:bg-amber-600 text-slate-900 font-black py-3 px-3 rounded-2xl transition text-xs flex items-center justify-center space-x-1.5 shadow-sm">
                    <i data-lucide="download" class="w-4 h-4"></i>
                    <span>Download Receipt</span>
                </button>
                <button type="button" onclick="closeReceiptModal()" class="flex-1 bg-ua-navy hover:bg-blue-800 text-white font-black py-3 px-3 rounded-2xl transition text-xs flex items-center justify-center space-x-1.5 shadow-md">
                    <i data-lucide="check" class="w-4 h-4"></i>
                    <span>Done</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Application Script -->
    <script>
        const DEFAULT_POSITIONS = {positions_json};
        const DEFAULT_DEPARTMENTS = {depts_json};
        const DEFAULT_CANDIDATES = {candidates_json};
        const DEFAULT_STUDENTS = {students_json};

        let currentUser = null;
        let selectedChoices = {{}};
        let activePositionTab = 'all';
        let activePartylistDept = 'College of Accountancy';
        let activeResultsDept = 'College of Accountancy';
        const AES_SECRET_KEY = 'UniVote-UA-2026';

        // ================= PARTY-LIST & AFFILIATION RESOLUTION =================
        function getCandidateParty(c) {{
            if (!c) return 'Independent';
            const dept = (c.dept || c.targetDept || '').toLowerCase();
            const photo = (c.photo || '').toLowerCase();
            
            // Strict Independent departments per institutional guidelines:
            if (
                dept.includes('architecture') ||
                dept.includes('industrial engineering') ||
                dept.includes('information technology') ||
                dept.includes('nursing') ||
                dept.includes('pharmacy') ||
                dept.includes('criminology') ||
                photo.includes('college of architecture') ||
                photo.includes('college of industrial engineering') ||
                photo.includes('college of information technology') ||
                photo.includes('college of nursing') ||
                photo.includes('college of pharmacy') ||
                photo.includes('criminology')
            ) {{
                return 'Independent';
            }}

            if (c.party && c.party.trim() !== '') {{
                const p = c.party.trim();
                if (p.toLowerCase() === 'siklab' || p.toLowerCase().includes('siklab')) {{
                    return 'SIKLAB';
                }}
                return p;
            }}
            return 'Independent';
        }}

        function renderPartyBadge(c) {{
            const party = getCandidateParty(c);
            if (party === 'SIKLAB') {{
                return `<span class="text-[10px] font-black text-amber-800 bg-amber-100 px-2.5 py-0.5 rounded-full border border-amber-300 uppercase tracking-wider inline-flex items-center gap-1 shadow-xs"><span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>SIKLAB</span>`;
            }}
            return `<span class="text-[10px] font-bold text-slate-700 bg-slate-100 px-2.5 py-0.5 rounded-full border border-slate-300 uppercase tracking-wider inline-flex items-center gap-1 shadow-xs"><span class="w-1.5 h-1.5 rounded-full bg-slate-400"></span>Independent</span>`;
        }}


        // PASSWORD VISIBILITY TOGGLE (See / Hide password)
        function togglePasswordVisibility(inputId, eyeIconId) {{
            const input = document.getElementById(inputId);
            const eye = document.getElementById(eyeIconId);
            if (!input) return;
            if (input.type === 'password') {{
                input.type = 'text';
                if (eye) eye.setAttribute('data-lucide', 'eye-off');
            }} else {{
                input.type = 'password';
                if (eye) eye.setAttribute('data-lucide', 'eye');
            }}
            lucide.createIcons();
        }}

        // SEPARATE MODAL CONTROLLERS
        function openSignInModal(prefillId = '', prefillEmail = '') {{
            if (currentUser) {{
                alert(`Your account is already signed in for ${{currentUser.dept}}.`);
                return;
            }}
            closeRegisterModal();
            closeRegSuccessModal();
            const modal = document.getElementById('signInModal');
            if (modal) modal.classList.remove('hidden');
            hideSignInAlert();

            if (prefillId) document.getElementById('authStudentId').value = prefillId;
            if (prefillEmail) document.getElementById('authStudentEmail').value = prefillEmail;
        }}

        function closeSignInModal() {{
            const modal = document.getElementById('signInModal');
            if (modal) modal.classList.add('hidden');
            hideSignInAlert();
        }}

        function openRegisterModal() {{
            if (currentUser) {{
                alert(`Your account is already signed in for ${{currentUser.dept}}.`);
                return;
            }}
            closeSignInModal();
            closeRegSuccessModal();
            const modal = document.getElementById('registerModal');
            if (modal) modal.classList.remove('hidden');
            hideRegisterAlert();
        }}

        function closeRegisterModal() {{
            const modal = document.getElementById('registerModal');
            if (modal) modal.classList.add('hidden');
            hideRegisterAlert();
        }}

        function switchToRegisterModal() {{
            closeSignInModal();
            openRegisterModal();
        }}

        function switchToSignInModal() {{
            closeRegisterModal();
            openSignInModal();
        }}

        function closeRegSuccessModal() {{
            const modal = document.getElementById('regSuccessModal');
            if (modal) modal.classList.add('hidden');
        }}

        let registeredCache = null;
        function proceedFromRegSuccessToSignIn() {{
            closeRegSuccessModal();
            if (registeredCache) {{
                openSignInModal(registeredCache.id, registeredCache.email);
            }} else {{
                openSignInModal();
            }}
        }}

        function showSignInAlert(msg) {{
            const el = document.getElementById('signInAlertBox');
            if (!el) return;
            el.innerText = msg;
            el.className = 'text-xs p-3 rounded-2xl border font-semibold bg-rose-50 text-rose-700 border-rose-200 block';
        }}

        function hideSignInAlert() {{
            const el = document.getElementById('signInAlertBox');
            if (el) {{
                el.className = 'hidden';
                el.innerText = '';
            }}
        }}

        function showRegisterAlert(msg) {{
            const el = document.getElementById('registerAlertBox');
            if (!el) return;
            el.innerText = msg;
            el.className = 'text-xs p-3 rounded-2xl border font-semibold bg-rose-50 text-rose-700 border-rose-200 block';
        }}

        function hideRegisterAlert() {{
            const el = document.getElementById('registerAlertBox');
            if (el) {{
                el.className = 'hidden';
                el.innerText = '';
            }}
        }}

        // STRICT VALIDATION: Student ID strictly 10 digits with admission years between 2010 and 2026
        function isValidStudentId(id) {{
            return /^(201[0-9]|202[0-6])\d{{6}}$/.test(id.trim());
        }}

        // MANDATORY INITIAL FORMAT RULE: (firstnames + middleinitial + lastname resulting in initials + lastname.student@ua.edu.ph)
        // e.g. "Juan Dela T. Cruz" -> "jdtcruz.student@ua.edu.ph"
        function deriveOfficialUaEmail(fullName) {{
            if (!fullName) return '';
            const parts = fullName.trim().split(/\\s+/).filter(Boolean);
            if (parts.length < 2) return '';
            
            const rawLast = parts[parts.length - 1];
            const lastname = rawLast.replace(/[^a-zA-Z]/g, '').toLowerCase();
            
            const firstAndMiddle = parts.slice(0, parts.length - 1);
            const initials = firstAndMiddle.map(p => {{
                const cleaned = p.replace(/[^a-zA-Z]/g, '');
                return cleaned.length > 0 ? cleaned[0].toLowerCase() : '';
            }}).join('');

            if (!initials || !lastname) return '';
            return `${{initials}}${{lastname}}.student@ua.edu.ph`;
        }}

        // General validation checking if email has valid @ua.edu.ph domain
        function isValidUaEmailGeneral(email) {{
            return /^[a-zA-Z0-9._%+-]+@ua\\.edu\\.ph$/i.test(email.trim());
        }}

        // STRICT PASSWORD COMPLEXITY VALIDATION
        function validatePasswordComplexity(password, studentName = '', studentId = '') {{
            if (!password || password.length < 8) {{
                return {{ valid: false, message: "Password must be at least 8 characters long." }};
            }}
            
            const specialCharRegex = /[*_+@#!$%^&()\\-=~`\\[\\]{{}};'",.<>?\\\\|\\/]/;
            if (!specialCharRegex.test(password)) {{
                return {{ valid: false, message: "Password must contain at least one special character (e.g., *, _, +, @, #, !)." }};
            }}

            const lower = password.toLowerCase();

            const sequentialPatterns = [
                "0123", "1234", "2345", "3456", "4567", "5678", "6789", "7890",
                "9876", "8765", "7654", "6543", "5432", "4321", "3210",
                "abcd", "bcde", "cdef", "defg", "efgh", "qwerty", "asdfgh"
            ];
            for (const seq of sequentialPatterns) {{
                if (lower.includes(seq)) {{
                    return {{ valid: false, message: "Password contains weak sequential or keyboard patterns (e.g. 1234, qwerty)." }};
                }}
            }}

            const commonWeak = ["password", "123456", "12345678", "admin", "univote", "welcome", "student"];
            for (const w of commonWeak) {{
                if (lower === w || lower.startsWith(w) || lower.endsWith(w)) {{
                    return {{ valid: false, message: "Common, easily guessable passwords are not permitted." }};
                }}
            }}

            if (/(?:19[5-9]\\d|20[0-2]\\d)/.test(password)) {{
                if (commonWeak.some(w => lower.includes(w))) {{
                    return {{ valid: false, message: "Passwords combining common words with birth years or dates are not permitted." }};
                }}
            }}

            if (studentName) {{
                const nameParts = studentName.toLowerCase().split(/\\s+/).filter(p => p.length >= 3);
                for (const part of nameParts) {{
                    const cleanedPart = part.replace(/[^a-zA-Z]/g, '');
                    if (cleanedPart.length >= 3 && lower.includes(cleanedPart)) {{
                        return {{ valid: false, message: "Password cannot contain parts of your name." }};
                    }}
                }}
            }}

            if (studentId && lower.includes(studentId.toLowerCase())) {{
                return {{ valid: false, message: "Password cannot contain your Student ID." }};
            }}

            return {{ valid: true }};
        }}

        // Helper to update email field automatically as student types full name
        function updateDerivedEmailSuggestion() {{
            const name = document.getElementById('regStudentName').value;
            const derived = deriveOfficialUaEmail(name);
            const emailInput = document.getElementById('regStudentEmail');
            if (derived && (!emailInput.value || emailInput.value.endsWith('@ua.edu.ph'))) {{
                emailInput.value = derived;
            }}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            initializeDatabaseDefaults();
            lucide.createIcons();
            checkSessionLock();
            renderPositionTabs();
            renderCandidateCards();
            renderPartylists();
            updateBallotVisualizer();
            checkElectionActiveState();
        }});

        // Version stamp — bump this string whenever candidates or schema changes to force a fresh reseed
        const UNIVOTE_DATA_VERSION = 'univote_v5_2026_11_08';

        function initializeDatabaseDefaults() {{
            // FORCE RESEED: if data version doesn't match (old data), wipe candidates and reload
            if (localStorage.getItem('univote_data_version') !== UNIVOTE_DATA_VERSION) {{
                localStorage.setItem('univote_db_candidates', JSON.stringify(DEFAULT_CANDIDATES));
                localStorage.setItem('univote_data_version', UNIVOTE_DATA_VERSION);
            }} else {{
                const existingCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
                if (existingCandidates.length < 126) {{
                    localStorage.setItem('univote_db_candidates', JSON.stringify(DEFAULT_CANDIDATES));
                }}
            }}
            if (!localStorage.getItem('univote_db_students')) {{
                localStorage.setItem('univote_db_students', JSON.stringify(DEFAULT_STUDENTS));
            }}
            if (!localStorage.getItem('univote_db_elections')) {{
                const defaultElection = {{
                    title: 'UA University Student Council Elections 2026',
                    startDate: '2026-10-01',
                    endDate: '2026-11-30',
                    active: true,
                    published: true
                }};
                localStorage.setItem('univote_db_elections', JSON.stringify(defaultElection));
            }}
            if (!localStorage.getItem('univote_encrypted_ballots_db')) {{
                localStorage.setItem('univote_encrypted_ballots_db', JSON.stringify([]));
            }}
        }}

        function checkElectionActiveState() {{
            const elec = JSON.parse(localStorage.getItem('univote_db_elections'));
            if (elec) {{
                const bannerTitle = document.getElementById('activeElectionBannerTitle');
                if (bannerTitle) bannerTitle.innerText = elec.title;
                const scheduleEl = document.getElementById('electionScheduleDisplay');
                if (scheduleEl) scheduleEl.innerText = `${{elec.startDate}} to ${{elec.endDate}}`;
                
                const inactiveBanner = document.getElementById('electionInactiveBanner');
                if (inactiveBanner) {{
                    if (!elec.active) {{
                        inactiveBanner.classList.remove('hidden');
                    }} else {{
                        inactiveBanner.classList.add('hidden');
                    }}
                }}
            }}
            renderResultsPage();
        }}

        function checkSessionLock() {{
            const savedSession = sessionStorage.getItem('univote_locked_session');
            if (savedSession) {{
                currentUser = JSON.parse(savedSession);
                activeResultsDept = currentUser.dept;
                activePartylistDept = currentUser.dept;
                applySessionLockUI();
            }}

            if (localStorage.getItem('univote_has_voted') === 'true') {{
                const savedVotes = localStorage.getItem('univote_saved_choices');
                if (savedVotes) {{
                    selectedChoices = JSON.parse(savedVotes);
                }}
                const reviewBtn = document.getElementById('reviewBallotBtn');
                if (reviewBtn) reviewBtn.disabled = true;
                const reviewBtnText = document.getElementById('reviewBallotBtnText');
                if (reviewBtnText) reviewBtnText.innerText = "Ballot Already Cast";
            }} else {{
                selectedChoices = {{}};
                localStorage.removeItem('univote_saved_choices');
            }}
        }}

        function applySessionLockUI() {{
            const voterDisplay = document.getElementById('voterIdentityDisplay');
            if (voterDisplay) voterDisplay.innerText = `${{currentUser.name}} (${{currentUser.dept}})`;
            const voterBadge = document.getElementById('voterBadge');
            if (voterBadge) voterBadge.classList.remove('hidden');
            const logoutBtn = document.getElementById('logoutBtn');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            
            const unauthNavGroup = document.getElementById('unauthNavGroup');
            if (unauthNavGroup) unauthNavGroup.classList.add('hidden');

            const unauthNotice = document.getElementById('unauthNotice');
            if (unauthNotice) unauthNotice.classList.add('hidden');

            const candTitle = document.getElementById('candidateSectionTitle');
            if (candTitle) candTitle.innerText = `${{currentUser.dept}} Candidate Slate`;
            const candSub = document.getElementById('candidateSectionSub');
            if (candSub) candSub.innerText = `Displaying official council positions and candidates running strictly for ${{currentUser.dept}}`;

            lucide.createIcons();
        }}

        function handleStudentLogout() {{
            sessionStorage.removeItem('univote_locked_session');
            localStorage.removeItem('univote_saved_choices');
            localStorage.removeItem('univote_has_voted');
            selectedChoices = {{}};
            location.reload();
        }}

        function switchMainTab(tabKey) {{
            document.querySelectorAll('.main-page-section').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.nav-tab-btn').forEach(el => {{
                el.classList.remove('bg-blue-700', 'text-white', 'shadow-md');
                el.classList.add('text-slate-600');
            }});
            document.querySelectorAll('.mob-nav-tab-btn').forEach(el => {{
                el.classList.remove('bg-blue-700', 'text-white');
                el.classList.add('bg-white', 'text-slate-600');
            }});

            const targetSection = document.getElementById(`page-${{tabKey}}`);
            if (targetSection) targetSection.classList.remove('hidden');

            const btn = document.getElementById(`tab-nav-${{tabKey}}`);
            if (btn) {{
                btn.classList.remove('text-slate-600');
                btn.classList.add('bg-blue-700', 'text-white', 'shadow-md');
            }}

            const mobBtn = document.getElementById(`mob-tab-nav-${{tabKey}}`);
            if (mobBtn) {{
                mobBtn.classList.remove('bg-white', 'text-slate-600');
                mobBtn.classList.add('bg-blue-700', 'text-white');
            }}

            if (tabKey === 'results') {{
                renderResultsPage();
            }}
        }}

        // AUTHENTICATION: LOGIN HANDLER (Closes automatically upon signing in)
        function handleAuthenticate(e) {{
            e.preventDefault();
            hideSignInAlert();

            const studentId = document.getElementById('authStudentId').value.trim();
            const studentEmail = document.getElementById('authStudentEmail').value.trim().toLowerCase();
            const password = document.getElementById('authPassword').value;

            // 1. Strict Student ID Validation
            if (!isValidStudentId(studentId)) {{
                showSignInAlert("Invalid Student ID! Must be strictly 10 digits with admission year between 2010 and 2026 (e.g., 2024000669).");
                return;
            }}

            // 2. Strict @ua.edu.ph institutional email validation
            if (!isValidUaEmailGeneral(studentEmail)) {{
                showSignInAlert("Invalid Email! Institutional email must end with @ua.edu.ph (e.g., jdtcruz.student@ua.edu.ph).");
                return;
            }}

            // 3. Lookup in Student Database
            const students = JSON.parse(localStorage.getItem('univote_db_students')) || [];
            const foundStudent = students.find(s => s.id === studentId);

            if (!foundStudent) {{
                showSignInAlert("Student account not found in roster! Please click 'First-Time Registration' below to register.");
                return;
            }}

            if (foundStudent.email && foundStudent.email.toLowerCase() !== studentEmail) {{
                showSignInAlert("Institutional email does not match the registered record for this Student ID.");
                return;
            }}

            const passwordHash = CryptoJS.SHA256(password).toString();
            if (!foundStudent.passwordHash) {{
                showSignInAlert("Your account password has not been established. Please register first.");
                return;
            }}

            if (foundStudent.passwordHash !== passwordHash) {{
                showSignInAlert("Incorrect account password! Please verify your password and try again.");
                return;
            }}

            if (!foundStudent.verified) {{
                showSignInAlert("Your student enrollment status is currently unverified by the registrar. Please contact the UA Election Commission.");
                return;
            }}

            // Login Success: Create session token & lock session
            const userSession = {{
                id: foundStudent.id,
                name: foundStudent.name,
                email: foundStudent.email,
                dept: foundStudent.dept,
                token: CryptoJS.SHA256(foundStudent.id + foundStudent.email + Date.now()).toString()
            }};

            sessionStorage.setItem('univote_locked_session', JSON.stringify(userSession));
            currentUser = userSession;
            activeResultsDept = currentUser.dept;
            activePartylistDept = currentUser.dept;

            // AUTO-CLOSE MODAL AFTER SIGNING IN
            closeSignInModal();

            applySessionLockUI();
            renderPositionTabs();
            renderCandidateCards();
            updateBallotVisualizer();
            renderResultsPage();
        }}

        // REGISTRATION WORKFLOW: Shows Success Modal and asks student to Sign In
        function handleStudentRegistration(e) {{
            e.preventDefault();
            hideRegisterAlert();

            const studentId = document.getElementById('regStudentId').value.trim();
            const studentName = document.getElementById('regStudentName').value.trim();
            const studentEmail = document.getElementById('regStudentEmail').value.trim().toLowerCase();
            const dept = document.getElementById('regDepartment').value;
            const password = document.getElementById('regPassword').value;
            const confirmPassword = document.getElementById('regConfirmPassword').value;

            // 1. Strict Student ID Validation
            if (!isValidStudentId(studentId)) {{
                showRegisterAlert("Invalid Student ID! Must be strictly 10 digits with admission year between 2010 and 2026 (e.g., 2024000669).");
                return;
            }}

            // 2. Strict Derived Institutional Email Format Rule
            const expectedEmail = deriveOfficialUaEmail(studentName);
            if (!expectedEmail) {{
                showRegisterAlert("Please enter a valid full name with first name(s), middle initial, and last name (e.g. Juan Dela T. Cruz).");
                return;
            }}

            if (studentEmail !== expectedEmail) {{
                showRegisterAlert(`Institutional email must strictly match your official name format: initials + lastname.student@ua.edu.ph (Expected: ${{expectedEmail}})`);
                return;
            }}

            // 3. Strict Password Complexity Validation
            const pwdCheck = validatePasswordComplexity(password, studentName, studentId);
            if (!pwdCheck.valid) {{
                showRegisterAlert(pwdCheck.message);
                return;
            }}

            if (password !== confirmPassword) {{
                showRegisterAlert("Passwords do not match! Please re-type your confirm password.");
                return;
            }}

            let students = JSON.parse(localStorage.getItem('univote_db_students')) || [];

            // ---- STRICT DUPLICATE PREVENTION ----
            // Block: Same Student ID already registered
            const idExists = students.find(s => s.id === studentId);
            if (idExists) {{
                showRegisterAlert(
                    `Student ID ${{studentId}} is already registered in the UniVote system. If this is your account, please Sign In instead. If you believe this is an error, contact the UA Election Commission.`
                );
                return;
            }}

            // Block: Same name already registered (case-insensitive, trimmed)
            const normalizedName = studentName.trim().toLowerCase().replace(/\s+/g, ' ');
            const nameExists = students.find(s => s.name.trim().toLowerCase().replace(/\s+/g, ' ') === normalizedName);
            if (nameExists) {{
                showRegisterAlert(
                    `The name "${{studentName}}" is already registered to another student account (ID: ${{nameExists.id.substring(0,4)}}XXXXXX). Each student must register with their own unique full name.`
                );
                return;
            }}

            // Block: Same email already registered
            const emailExists = students.find(s => s.email && s.email.toLowerCase() === studentEmail);
            if (emailExists) {{
                showRegisterAlert(
                    `The institutional email "${{studentEmail}}" is already linked to an existing account. Each student must use their own unique UA email address.`
                );
                return;
            }}

            // Block: Password reuse — another student already uses this same password hash
            const passwordHash = CryptoJS.SHA256(password).toString();
            const passwordTaken = students.find(s => s.passwordHash === passwordHash);
            if (passwordTaken) {{
                showRegisterAlert(
                    `This password is already in use by another registered student. For security and uniqueness, every student account must have its own distinct password.`
                );
                return;
            }}

            // All uniqueness checks passed — create the new student account
            const newStudent = {{
                id: studentId,
                name: studentName,
                email: studentEmail,
                dept: dept,
                verified: true,
                passwordHash: passwordHash
            }};
            students.push(newStudent);

            localStorage.setItem('univote_db_students', JSON.stringify(students));

            // Cache credentials for sign-in pre-fill
            registeredCache = {{
                id: studentId,
                email: studentEmail
            }};

            // CLOSE REGISTRATION MODAL
            closeRegisterModal();

            // OPEN REGISTRATION SUCCESS MODAL ASKING STUDENT TO SIGN IN
            const summaryBox = document.getElementById('regSuccessSummary');
            if (summaryBox) {{
                summaryBox.innerHTML = `
                    <p><strong>Student ID:</strong> ${{studentId}}</p>
                    <p><strong>Full Name:</strong> ${{studentName}}</p>
                    <p><strong>Department:</strong> ${{dept}}</p>
                    <p><strong>Institutional Email:</strong> ${{studentEmail}}</p>
                `;
            }}

            const successModal = document.getElementById('regSuccessModal');
            if (successModal) successModal.classList.remove('hidden');

            confetti({{ particleCount: 75, spread: 60, origin: {{ y: 0.7 }} }});
        }}

        // POSITION FILTER TABS: Pres, VP, Sec, Treas, Aud, PRO (WITH SELECTION TRACKING)
        function renderPositionTabs() {{
            const container = document.getElementById('positionTabs');
            if (!container) return;
            const totalRaces = DEFAULT_POSITIONS.length;
            const completedCount = Object.keys(selectedChoices).length;
            
            let tabsHtml = `
                <button onclick="filterPositionTab('all')" id="btn-pos-all" class="pos-tab-btn px-4 py-2 rounded-xl text-xs font-bold transition whitespace-nowrap flex items-center space-x-1.5 ${{activePositionTab === 'all' ? 'bg-blue-700 text-white shadow-sm' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'}}">
                    <span>All Races</span>
                    <span class="text-[10px] px-1.5 py-0.5 rounded-full ${{completedCount === totalRaces ? 'bg-emerald-500 text-white' : 'bg-slate-100 text-slate-700'}}">${{completedCount}}/${{totalRaces}}</span>
                </button>
            `;

            DEFAULT_POSITIONS.forEach(pos => {{
                const isActive = activePositionTab === pos.id;
                const isChosen = !!selectedChoices[pos.id];
                tabsHtml += `
                    <button onclick="filterPositionTab('${{pos.id}}')" id="btn-pos-${{pos.id}}" class="pos-tab-btn px-4 py-2 rounded-xl text-xs font-bold transition whitespace-nowrap flex items-center space-x-1.5 ${{isActive ? 'bg-blue-700 text-white shadow-sm' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'}}">
                        <span>${{pos.name}}</span>
                        ${{isChosen 
                            ? '<span class="text-[10px] bg-emerald-100 text-emerald-800 font-black px-1.5 py-0.2 rounded-md">✓</span>' 
                            : '<span class="text-[9px] bg-rose-50 text-rose-600 font-bold px-1 rounded border border-rose-200">0/1</span>'}}
                    </button>
                `;
            }});

            container.innerHTML = tabsHtml;
        }}

        function filterPositionTab(posId) {{
            activePositionTab = posId;
            renderPositionTabs();
            renderCandidateCards();
        }}

        // CANDIDATE DIRECTORY RENDERING (STRICT DEPARTMENT-BASED ACCESS CONTROL)
        function renderCandidateCards() {{
            const container = document.getElementById('candidateCardsContainer');
            const search = document.getElementById('candidateSearch').value.toLowerCase();
            const isVoted = localStorage.getItem('univote_has_voted') === 'true';

            // IF NOT LOGGED IN: STRICT ACCESS CONTROL
            if (!currentUser) {{
                container.innerHTML = `
                    <div class="bg-white rounded-3xl p-10 text-center border-2 border-dashed border-blue-200 shadow-sm space-y-4">
                        <div class="w-16 h-16 rounded-2xl bg-blue-50 text-blue-700 flex items-center justify-center mx-auto shadow-inner">
                            <i data-lucide="lock" class="w-8 h-8 text-blue-600"></i>
                        </div>
                        <div class="max-w-md mx-auto space-y-1">
                            <h3 class="text-lg font-black text-slate-900">Department Authorization Required</h3>
                            <p class="text-xs text-slate-500 leading-relaxed">
                                Candidates and ballot choices are restricted strictly by academic department. Please sign in with your UA Student ID and password to access your department's candidates.
                            </p>
                        </div>
                        <div class="flex items-center justify-center space-x-2 pt-2">
                            <button onclick="openSignInModal()" class="bg-ua-navy hover:bg-blue-800 text-white text-xs font-bold px-6 py-3 rounded-xl transition shadow-md inline-flex items-center space-x-1.5">
                                <i data-lucide="log-in" class="w-4 h-4 text-amber-400"></i>
                                <span>Sign In</span>
                            </button>
                            <button onclick="openRegisterModal()" class="bg-white hover:bg-slate-50 text-blue-800 border border-slate-300 text-xs font-bold px-5 py-3 rounded-xl transition shadow-sm inline-flex items-center space-x-1.5">
                                <i data-lucide="user-plus" class="w-4 h-4 text-blue-700"></i>
                                <span>First-Time Registration</span>
                            </button>
                        </div>
                    </div>
                `;
                lucide.createIcons();
                return;
            }}

            const allCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || DEFAULT_CANDIDATES;

            // STRICT DEPARTMENT ACCESS CONTROL
            const filtered = allCandidates.filter(c => {{
                const matchesDept = (c.targetDept === currentUser.dept);
                const matchesPos = (activePositionTab === 'all' || c.posId === activePositionTab);
                const matchesSearch = c.name.toLowerCase().includes(search) || c.party.toLowerCase().includes(search) || (c.dept && c.dept.toLowerCase().includes(search));
                return matchesDept && matchesPos && matchesSearch;
            }});

            if (filtered.length === 0) {{
                container.innerHTML = `
                    <div class="bg-white rounded-3xl p-8 text-center text-slate-400 border border-slate-200 space-y-2">
                        <i data-lucide="search-x" class="w-10 h-10 mx-auto text-slate-300"></i>
                        <p class="text-sm font-semibold text-slate-600">No Candidates Found</p>
                        <p class="text-xs text-slate-400">
                            There are currently no candidates matching your filter in <strong>${{currentUser.dept}}</strong>.
                        </p>
                    </div>
                `;
                lucide.createIcons();
                return;
            }}

            container.innerHTML = filtered.map(c => {{
                const isSelected = selectedChoices[c.posId] === c.id;
                const posObj = DEFAULT_POSITIONS.find(p => p.id === c.posId);
                const posName = posObj ? posObj.name : 'Candidate';

                const buttonDisabled = isVoted ? 'disabled' : '';
                const buttonStyle = isVoted 
                    ? (isSelected ? 'bg-blue-800 text-white opacity-80 cursor-not-allowed' : 'bg-slate-100 text-slate-400 opacity-50 cursor-not-allowed')
                    : (isSelected ? 'bg-blue-700 text-white shadow-md' : 'bg-slate-100 text-slate-700 hover:bg-slate-200');

                return `
                    <div class="bg-white rounded-3xl p-5 border transition-all duration-200 shadow-sm hover:shadow-md ${{isSelected ? 'border-2 border-blue-700 bg-blue-50/20' : 'border-slate-200'}}">
                        <div class="flex flex-col sm:flex-row gap-5 items-start sm:items-center">
                            <img src="${{c.photo || '/templates/ua-logo.png'}}" alt="${{c.name}}" class="w-20 h-20 rounded-2xl object-cover object-center border-2 border-white shadow-md shrink-0" style="object-fit: cover; object-position: center;" onerror="this.onerror=null; this.src='/templates/ua-logo.png';">
                            
                            <div class="flex-1 space-y-2">
                                <div class="flex flex-wrap items-center gap-1.5">
                                    <span class="text-[10px] font-extrabold text-blue-800 bg-blue-100 px-2.5 py-0.5 rounded-full border border-blue-200 uppercase">${{posName}}</span>
                                    <span class="text-[10px] font-bold text-amber-800 bg-amber-100 px-2.5 py-0.5 rounded-full border border-amber-200">${{c.targetDept}}</span>
                                    <span class="text-xs text-slate-500 font-medium">${{c.dept || ''}}</span>
                                </div>
                                <h4 class="text-lg font-bold text-slate-900">${{c.name}}</h4>
                                <div class="pt-0.5">${{renderPartyBadge(c)}}</div>
                                <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-3 rounded-2xl border border-slate-100">${{c.platform}}</p>
                                ${{c.advocacies && c.advocacies.length > 0 ? `
                                    <div class="flex flex-wrap gap-1 pt-1">
                                        ${{c.advocacies.map(a => `<span class="text-[10px] bg-slate-100 text-slate-600 px-2 py-0.5 rounded-md font-semibold"># ${{a}}</span>`).join('')}}
                                    </div>
                                ` : ''}}
                            </div>

                            <button onclick="toggleSelectCandidate('${{c.posId}}', '${{c.id}}')" ${{buttonDisabled}} class="shrink-0 w-full sm:w-auto px-5 py-2.5 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-2 ${{buttonStyle}}">
                                <i data-lucide="${{isSelected ? 'check-circle' : 'circle'}}" class="w-4 h-4"></i>
                                <span>${{isSelected ? (isVoted ? 'Selected & Locked' : 'Selected') : 'Select Candidate'}}</span>
                            </button>
                        </div>
                    </div>
                `;
            }}).join('');

            lucide.createIcons();
        }}

        function toggleSelectCandidate(posId, candidateId) {{
            if (localStorage.getItem('univote_has_voted') === 'true') return;
            if (!currentUser) {{
                openSignInModal();
                return;
            }}

            if (selectedChoices[posId] === candidateId) {{
                delete selectedChoices[posId];
            }} else {{
                selectedChoices[posId] = candidateId;
            }}
            renderCandidateCards();
            updateBallotVisualizer();
        }}

        function updateBallotVisualizer() {{
            const reviewBtn = document.getElementById('reviewBallotBtn');
            const reviewBtnText = document.getElementById('reviewBallotBtnText');
            const countBadge = document.getElementById('ballotCountBadge');
            const summarySub = document.getElementById('ballotSelectionSummarySub');
            const hasVoted = localStorage.getItem('univote_has_voted') === 'true';

            const keys = Object.keys(selectedChoices);
            const totalRaces = DEFAULT_POSITIONS.length;

            if (hasVoted) {{
                if (countBadge) {{
                    countBadge.className = "bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2.5 py-0.5 rounded-full border border-emerald-300";
                    countBadge.innerText = "Official Ballot Cast ✓";
                }}
                if (reviewBtn) {{
                    reviewBtn.disabled = true;
                    reviewBtn.className = "w-full sm:w-auto bg-slate-200 text-slate-400 font-bold py-3.5 px-6 rounded-2xl cursor-not-allowed flex items-center justify-center space-x-2 text-xs";
                }}
                if (reviewBtnText) reviewBtnText.innerText = "Ballot Already Cast";
                if (summarySub) summarySub.innerHTML = '<span class="text-emerald-700 font-semibold">Your official ballot has been cast and committed to the audit trail.</span>';
                return;
            }}

            if (!currentUser) {{
                if (countBadge) {{
                    countBadge.className = "bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-slate-200";
                    countBadge.innerText = `0 of ${{totalRaces}} Selected`;
                }}
                if (reviewBtn) {{
                    reviewBtn.disabled = false;
                    reviewBtn.className = "w-full sm:w-auto bg-ua-navy hover:bg-blue-800 text-white font-bold py-3.5 px-6 rounded-2xl transition shadow-lg flex items-center justify-center space-x-2 text-xs";
                }}
                if (reviewBtnText) reviewBtnText.innerText = "Sign In to Cast Vote";
                if (summarySub) summarySub.innerText = "Please sign in or register to unlock and select candidate choices.";
            }} else {{
                const elec = JSON.parse(localStorage.getItem('univote_db_elections'));
                const isElecActive = elec ? elec.active : true;

                // STRICT ENFORCEMENT: MUST SELECT ALL 6 POSITIONS (6/6)
                if (keys.length < totalRaces) {{
                    const remaining = totalRaces - keys.length;
                    if (countBadge) {{
                        countBadge.className = "bg-amber-100 text-amber-800 text-[10px] font-extrabold px-2.5 py-0.5 rounded-full border border-amber-300";
                        countBadge.innerText = `${{keys.length}} of ${{totalRaces}} Selected (Incomplete)`;
                    }}
                    if (reviewBtn) {{
                        reviewBtn.disabled = true;
                        reviewBtn.className = "w-full sm:w-auto bg-slate-200 text-slate-400 font-bold py-3.5 px-6 rounded-2xl cursor-not-allowed flex items-center justify-center space-x-2 text-xs transition";
                    }}
                    if (reviewBtnText) reviewBtnText.innerText = `Complete All 6 Selections (${{keys.length}}/${{totalRaces}} Selected)`;
                    if (summarySub) summarySub.innerHTML = `<span class="text-amber-800 font-semibold">Under UA election guidelines, you must select one candidate for each of the 6 student council positions. (${{remaining}} position${{remaining > 1 ? 's' : ''}} remaining)</span>`;
                }} else {{
                    if (countBadge) {{
                        countBadge.className = "bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2.5 py-0.5 rounded-full border border-emerald-300";
                        countBadge.innerText = `6 of 6 Complete ✓`;
                    }}
                    if (reviewBtn) {{
                        reviewBtn.disabled = !isElecActive;
                        reviewBtn.className = "w-full sm:w-auto bg-ua-navy hover:bg-blue-800 text-white font-bold py-3.5 px-6 rounded-2xl transition shadow-lg shadow-blue-900/20 flex items-center justify-center space-x-2 text-xs";
                    }}
                    if (reviewBtnText) reviewBtnText.innerText = `Review Complete Ballot (6/6 Selected) & Cast Vote`;
                    if (summarySub) summarySub.innerHTML = `<span class="text-emerald-700 font-semibold">All 6 student council positions selected! You are ready to review and cast your encrypted ballot.</span>`;
                }}
            }}
        }}

        function openReviewModal() {{
            if (!currentUser) {{
                openSignInModal();
                return;
            }}

            const keys = Object.keys(selectedChoices);
            const totalRaces = DEFAULT_POSITIONS.length;

            // STRICT GUARD: CANNOT VOTE WITH ONLY 1 OR PARTIAL SELECTION
            if (keys.length < totalRaces) {{
                const missing = totalRaces - keys.length;
                alert(`Incomplete Ballot (${{keys.length}}/${{totalRaces}} Selected):\n\nUnder University of the Assumption election rules, you must select 1 candidate for each of the 6 student council positions (President, Vice President, Secretary, Treasurer, Auditor, and PRO) before submitting.\n\nYou cannot cast a ballot with only ${{keys.length}} candidate${{keys.length === 1 ? '' : 's'}}. Please select the remaining ${{missing}} position${{missing > 1 ? 's' : ''}}.`);
                return;
            }}

            const list = document.getElementById('reviewChoicesList');
            const allCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || DEFAULT_CANDIDATES;

            list.innerHTML = Object.keys(selectedChoices).map(posId => {{
                const posObj = DEFAULT_POSITIONS.find(p => p.id === posId);
                const candObj = allCandidates.find(c => c.id === selectedChoices[posId]);
                return `
                    <div class="flex justify-between items-center text-xs p-3 bg-slate-50 rounded-2xl border">
                        <div>
                            <span class="font-bold text-slate-500 uppercase text-[10px] block">${{posObj?.name}}:</span>
                            <span class="text-blue-900 font-extrabold text-sm">${{candObj?.name || 'Selected Candidate'}}</span>
                        </div>
                        ${{renderPartyBadge(candObj)}}
                    </div>
                `;
            }}).join('');

            document.getElementById('reviewChoicesModal').classList.remove('hidden');
        }}

        function closeReviewModal() {{
            document.getElementById('reviewChoicesModal').classList.add('hidden');
        }}

        function submitBallot() {{
            const keys = Object.keys(selectedChoices);
            const totalRaces = DEFAULT_POSITIONS.length;
            if (keys.length < totalRaces) {{
                alert(`Cannot submit incomplete ballot. You must complete all 6 candidate positions to cast your vote.`);
                return;
            }}

            closeReviewModal();

            const payload = {{
                voterToken: currentUser.token,
                department: currentUser.dept,
                votes: selectedChoices,
                timestamp: new Date().toISOString()
            }};

            const cipher = CryptoJS.AES.encrypt(JSON.stringify(payload), AES_SECRET_KEY).toString();

            // Save encrypted payload into Database
            let ballotsDb = JSON.parse(localStorage.getItem('univote_encrypted_ballots_db')) || [];
            ballotsDb.push({{
                voterToken: currentUser.token,
                department: currentUser.dept,
                cipherPayload: cipher,
                timestamp: new Date().toLocaleString()
            }});
            localStorage.setItem('univote_encrypted_ballots_db', JSON.stringify(ballotsDb));

            localStorage.setItem('univote_has_voted', 'true');
            localStorage.setItem('univote_saved_choices', JSON.stringify(selectedChoices));

            document.getElementById('reviewBallotBtn').disabled = true;
            document.getElementById('reviewBallotBtnText').innerText = "Ballot Already Cast";

            renderCandidateCards();
            updateBallotVisualizer();

            confetti({{ particleCount: 120, spread: 80, origin: {{ y: 0.6 }} }});

            // Populate Digital Receipt Fields
            const exactTimestamp = new Date().toLocaleString('en-US', {{ dateStyle: 'full', timeStyle: 'medium' }});
            document.getElementById('receiptTimestamp').innerText = exactTimestamp;
            document.getElementById('receiptDept').innerText = currentUser.dept;
            document.getElementById('receiptStudentId').innerText = currentUser.id;
            document.getElementById('receiptStudentName').innerText = currentUser.name;
            document.getElementById('receiptStudentEmail').innerText = currentUser.email || 'institutional.account@ua.edu.ph';
            document.getElementById('receiptToken').innerText = currentUser.token;
            document.getElementById('receiptCipherHash').innerText = cipher;

            const allCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || DEFAULT_CANDIDATES;
            
            // Build dynamic Choices List on Receipt Card
            const choicesContainer = document.getElementById('receiptChoicesList');
            let qrSummaryLines = [];
            qrSummaryLines.push(`=== UNIVOTE OFFICIAL VOTING RECEIPT ===`);
            qrSummaryLines.push(`Institution: University of the Assumption`);
            qrSummaryLines.push(`Timestamp: ${{exactTimestamp}}`);
            qrSummaryLines.push(`Student ID: ${{currentUser.id}}`);
            qrSummaryLines.push(`Student: ${{currentUser.name}}`);
            qrSummaryLines.push(`Department: ${{currentUser.dept}}`);
            qrSummaryLines.push(`Security Token: ${{currentUser.token}}`);
            qrSummaryLines.push(`\n--- OFFICIAL VOTES CAST ---`);

            choicesContainer.innerHTML = DEFAULT_POSITIONS.map(pos => {{
                const candId = selectedChoices[pos.id];
                const cand = allCandidates.find(c => c.id === candId);
                const candName = cand ? cand.name : 'Unknown Candidate';
                const partyName = cand ? getCandidateParty(cand) : 'Independent';
                
                qrSummaryLines.push(`• ${{pos.name}}: ${{candName}} (${{partyName}})`);

                return `
                    <div class="flex items-center justify-between p-2.5 bg-white rounded-xl border border-slate-200 text-xs">
                        <div class="flex items-center space-x-2.5">
                            <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 font-black text-[10px] flex items-center justify-center shrink-0">✓</span>
                            <div>
                                <span class="font-extrabold text-[9px] text-slate-400 uppercase tracking-wider block">${{pos.name}}</span>
                                <span class="font-black text-slate-900">${{candName}}</span>
                            </div>
                        </div>
                        <div>${{renderPartyBadge(cand)}}</div>
                    </div>
                `;
            }}).join('');

            qrSummaryLines.push(`\nCipher: ${{cipher.substring(0, 48)}}...`);
            qrSummaryLines.push(`Status: VERIFIED & TAMPER-PROOF`);

            const fullQrPayload = qrSummaryLines.join('\\n');

            // Dynamic permanent QR code generation with fallback
            const qrCanvas = document.getElementById('qrcodeCanvas');
            qrCanvas.innerHTML = '';
            try {{
                if (typeof QRCode !== 'undefined') {{
                    new QRCode(qrCanvas, {{
                        text: fullQrPayload,
                        width: 140,
                        height: 140,
                        colorDark: "#020381",
                        colorLight: "#ffffff",
                        correctLevel: QRCode.CorrectLevel.M
                    }});
                }} else {{
                    throw new Error("QRCode library not loaded");
                }}
            }} catch (err) {{
                const encodedPayload = encodeURIComponent(fullQrPayload);
                qrCanvas.innerHTML = `<img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&color=020381&data=${{encodedPayload}}" alt="UniVote Ballot QR" class="w-[140px] h-[140px] rounded-lg">`;
            }}

            document.getElementById('receiptModal').classList.remove('hidden');
        }}

        function downloadDigitalReceipt() {{
            if (!currentUser) return;
            const allCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || DEFAULT_CANDIDATES;
            let text = "==========================================================\\n";
            text += "         UNIVERSITY OF THE ASSUMPTION - UNIVOTE          \\n";
            text += "             OFFICIAL DIGITAL VOTING RECEIPT             \\n";
            text += "==========================================================\\n\\n";
            text += `STATUS             : OFFICIAL BALLOT CAST & AUDITED [VERIFIED]\\n`;
            text += `TIMESTAMP          : ${{document.getElementById('receiptTimestamp').innerText}}\\n`;
            text += `STUDENT ID         : ${{currentUser.id}}\\n`;
            text += `VOTER NAME         : ${{currentUser.name}}\\n`;
            text += `INSTITUTIONAL EMAIL: ${{currentUser.email || 'N/A'}}\\n`;
            text += `ACADEMIC DEPARTMENT: ${{currentUser.dept}}\\n`;
            text += `VOTER TOKEN        : ${{currentUser.token}}\\n\\n`;
            text += "----------------------------------------------------------\\n";
            text += "                      VOTES RECORDED                      \\n";
            text += "----------------------------------------------------------\\n";
            DEFAULT_POSITIONS.forEach(pos => {{
                const candId = selectedChoices[pos.id];
                const cand = allCandidates.find(c => c.id === candId);
                const candName = cand ? cand.name : 'Unknown Candidate';
                const partyName = cand ? getCandidateParty(cand) : 'Independent';
                text += `${{pos.name.padEnd(32)}}: ${{candName}} (${{partyName}})\\n`;
            }});
            text += "----------------------------------------------------------\\n";
            text += `AES-256 AUDIT CIPHER HASH:\\n${{document.getElementById('receiptCipherHash').innerText}}\\n`;
            text += "==========================================================\\n";
            text += "This digital receipt is authenticated by the UA Election Commission.\\n";

            const blob = new Blob([text], {{ type: 'text/plain;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `UniVote_Receipt_${{currentUser.id}}_${{Date.now()}}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
function closeReceiptModal() {{
            document.getElementById('receiptModal').classList.add('hidden');
        }}

        // ================= OFFICIAL RESULTS PAGE =================
        function switchResultsDept(dept) {{
            activeResultsDept = dept;
            document.querySelectorAll('.res-dept-btn').forEach(b => {{
                if (b.getAttribute('data-dept') === dept) {{
                    b.classList.remove('bg-white/10', 'text-white', 'hover:bg-white/20');
                    b.classList.add('bg-blue-700', 'text-white', 'border-blue-500');
                }} else {{
                    b.classList.remove('bg-blue-700', 'border-blue-500');
                    b.classList.add('bg-white/10', 'text-white', 'hover:bg-white/20');
                }}
            }});
            renderResultsPage();
        }}

        function renderResultsPage() {{
            const container = document.getElementById('resultsContentArea');
            if (!container) return;

            const elec = JSON.parse(localStorage.getItem('univote_db_elections'));

            if (!elec || !elec.published) {{
                container.innerHTML = `
                    <div class="bg-white rounded-3xl p-10 text-center border border-slate-200 shadow-sm space-y-3">
                        <i data-lucide="lock" class="w-12 h-12 text-slate-300 mx-auto"></i>
                        <h3 class="font-extrabold text-lg text-slate-800">Official Results Sealed</h3>
                        <p class="text-xs text-slate-500 max-w-md mx-auto">Official election tallies and winner designations will be made viewable here immediately following Commission publication.</p>
                    </div>
                `;
                lucide.createIcons();
                return;
            }}

            const targetDept = currentUser ? currentUser.dept : activeResultsDept;
            const ballots = JSON.parse(localStorage.getItem('univote_encrypted_ballots_db')) || [];
            const candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
            
            const deptBallots = ballots.filter(b => b.department === targetDept);

            const tallies = {{}};
            deptBallots.forEach(b => {{
                try {{
                    const bytes = CryptoJS.AES.decrypt(b.cipherPayload, AES_SECRET_KEY);
                    const payload = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));
                    const votes = payload.votes || {{}};

                    Object.keys(votes).forEach(posId => {{
                        const candId = votes[posId];
                        if (!tallies[posId]) tallies[posId] = {{}};
                        tallies[posId][candId] = (tallies[posId][candId] || 0) + 1;
                    }});
                }} catch (e) {{}}
            }});

            const deptCandidates = candidates.filter(c => c.targetDept === targetDept);

            let htmlContent = `
                <div class="bg-emerald-50 border border-emerald-200 rounded-3xl p-6 text-emerald-900 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold uppercase bg-emerald-200 text-emerald-900 px-3 py-1 rounded-full">OFFICIAL COMMISSION PUBLICATION</span>
                        <span class="text-xs font-extrabold bg-white text-emerald-800 px-3 py-1 rounded-full border border-emerald-300">${{targetDept}}</span>
                    </div>
                    <h3 class="text-xl font-extrabold">Certified Winners &amp; Tally Standings</h3>
                    <p class="text-xs">Results certified by the UA Commission on Elections (${{deptBallots.length}} total encrypted ballots cast for ${{targetDept}}).</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            `;

            if (deptCandidates.length === 0) {{
                htmlContent += `
                    <div class="col-span-2 bg-white rounded-3xl p-8 text-center text-slate-400 border">
                        No official candidate tallies recorded for ${{targetDept}}.
                    </div>
                `;
            }} else {{
                htmlContent += DEFAULT_POSITIONS.map(pos => {{
                    const posCands = deptCandidates.filter(c => c.posId === pos.id);
                    if (posCands.length === 0) return '';

                    let maxVotes = -1;
                    let winnerId = null;

                    posCands.forEach(c => {{
                        const count = (tallies[pos.id] && tallies[pos.id][c.id]) ? tallies[pos.id][c.id] : 0;
                        if (count > maxVotes) {{
                            maxVotes = count;
                            winnerId = c.id;
                        }}
                    }});

                    return `
                        <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm space-y-4">
                            <div class="flex justify-between items-center border-b pb-3">
                                <span class="font-extrabold text-sm text-slate-900">${{pos.name}}</span>
                                <span class="text-[10px] font-bold bg-blue-50 text-blue-700 px-2.5 py-0.5 rounded-full border border-blue-100">${{targetDept}}</span>
                            </div>

                            <div class="space-y-3">
                                ${{posCands.map(c => {{
                                    const count = (tallies[pos.id] && tallies[pos.id][c.id]) ? tallies[pos.id][c.id] : 0;
                                    const isWinner = (c.id === winnerId && count > 0);
                                    const percentage = deptBallots.length > 0 ? ((count / deptBallots.length) * 100).toFixed(1) : '0.0';

                                    return `
                                        <div class="p-3.5 rounded-2xl border ${{isWinner ? 'border-amber-400 bg-amber-50/50 shadow-sm' : 'border-slate-100 bg-slate-50'}} flex items-center justify-between">
                                            <div class="flex items-center space-x-3">
                                                <img src="${{c.photo || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=300'}}" class="w-11 h-11 rounded-xl object-cover shrink-0 border">
                                                <div>
                                                    <div class="flex items-center space-x-2">
                                                        <h4 class="font-bold text-sm text-slate-900">${{c.name}}</h4>
                                                        ${{isWinner ? '<span class="bg-amber-500 text-slate-950 font-black text-[9px] px-2 py-0.5 rounded-full uppercase">WINNER</span>' : ''}}
                                                    </div>
                                                    <p class="text-xs font-bold text-blue-700">${{c.party}}</p>
                                                </div>
                                            </div>

                                            <div class="text-right">
                                                <span class="text-xl font-black text-slate-900">${{count}}</span>
                                                <span class="text-xs text-slate-400 font-normal"> votes (${{percentage}}%)</span>
                                            </div>
                                        </div>
                                    `;
                                }}).join('')}}
                            </div>
                        </div>
                    `;
                }}).join('');
            }}

            htmlContent += `</div>`;
            container.innerHTML = htmlContent;
            lucide.createIcons();
        }}

        // ================= PARTYLISTS PAGE (ALL 10 DEPARTMENTS) =================
        function filterPartylists(dept) {{
            activePartylistDept = dept;
            document.querySelectorAll('.partylist-dept-btn').forEach(el => {{
                el.classList.remove('bg-blue-700', 'text-white');
                el.classList.add('text-slate-600');
            }});
            const deptBtnMap = {{
                'College of Accountancy': 'btn-partylist-acc',
                'College of Engineering and Architecture': 'btn-partylist-cea',
                'College of Hospitality and Tourism Management': 'btn-partylist-chtm',
                'College of Nursing and Pharmacy': 'btn-partylist-cnp',
                'School of Arts and Sciences': 'btn-partylist-sas',
                'School of Business and Public Administration': 'btn-partylist-sbpa',
                'School of Education': 'btn-partylist-sed',
                'College of Information Technology': 'btn-partylist-it',
                'Senior High School': 'btn-partylist-shs',
                'Junior High School': 'btn-partylist-jhs'
            }};
            const activeBtn = document.getElementById(deptBtnMap[dept]);
            if (activeBtn) {{
                activeBtn.classList.remove('text-slate-600');
                activeBtn.classList.add('bg-blue-700', 'text-white');
            }}
            renderPartylists();
        }}

        function renderPartylists() {{
            const container = document.getElementById('partylistsContainer');
            const dept = activePartylistDept;
            const allCandidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || DEFAULT_CANDIDATES;
            const deptCandidates = allCandidates.filter(c => c.targetDept === dept);

            const siklabCandidates = deptCandidates.filter(c => getCandidateParty(c) === 'SIKLAB');
            const indepCandidates = deptCandidates.filter(c => getCandidateParty(c) === 'Independent');

            let cardsHtml = '';

            // SIKLAB Party Card (if any candidates in dept)
            if (siklabCandidates.length > 0) {{
                cardsHtml += `
                    <div class="bg-white rounded-3xl p-6 border-2 border-amber-200 shadow-sm space-y-4">
                        <div class="flex items-center justify-between border-b border-amber-100 pb-3">
                            <div class="flex items-center space-x-3">
                                <div class="w-10 h-10 rounded-2xl bg-amber-500 text-white font-black flex items-center justify-center shadow-md">
                                    S
                                </div>
                                <div>
                                    <h4 class="text-base font-extrabold text-slate-900">SIKLAB Party-List</h4>
                                    <p class="text-[11px] text-amber-800 font-bold">Alyansang Siklab • Serbisyong Tapat at Inklusibo</p>
                                </div>
                            </div>
                            <span class="text-[10px] font-black text-amber-800 bg-amber-100 px-3 py-1 rounded-full border border-amber-300 uppercase tracking-wider">
                                SIKLAB PARTY
                            </span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed bg-amber-50/50 p-3.5 rounded-2xl border border-amber-100">
                            Dedicated to participatory governance, student welfare advocacy, financial openness, and progressive student empowerment across all university faculties.
                        </p>
                        <div>
                            <span class="text-[10px] uppercase font-black text-slate-400 tracking-wider block mb-2">OFFICIAL CANDIDATE SLATE (${{siklabCandidates.length}} CANDIDATES)</span>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                ${{siklabCandidates.map(c => {{
                                    const posObj = DEFAULT_POSITIONS.find(p => p.id === c.posId);
                                    return `
                                        <div class="flex items-center space-x-2.5 p-2 rounded-xl bg-slate-50 border border-slate-200">
                                            <img src="${{c.photo || '/templates/ua-logo.png'}}" class="w-9 h-9 rounded-xl object-cover object-center border shrink-0" style="object-fit: cover; object-position: center;" onerror="this.onerror=null; this.src='/templates/ua-logo.png';">
                                            <div class="truncate">
                                                <span class="font-extrabold text-xs text-slate-900 block truncate">${{c.name}}</span>
                                                <span class="text-[10px] text-amber-700 font-bold uppercase">${{posObj ? posObj.name : c.posId}}</span>
                                            </div>
                                        </div>
                                    `;
                                }}).join('')}}
                            </div>
                        </div>
                    </div>
                `;
            }}

            // Independent / Non-Partisan Candidates Card
            if (indepCandidates.length > 0) {{
                cardsHtml += `
                    <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                            <div class="flex items-center space-x-3">
                                <div class="w-10 h-10 rounded-2xl bg-slate-800 text-white font-black flex items-center justify-center shadow-md">
                                    I
                                </div>
                                <div>
                                    <h4 class="text-base font-extrabold text-slate-900">Independent Candidates</h4>
                                    <p class="text-[11px] text-slate-500 font-bold">Non-Partisan Academic Student Advocates</p>
                                </div>
                            </div>
                            <span class="text-[10px] font-bold text-slate-700 bg-slate-100 px-3 py-1 rounded-full border border-slate-300 uppercase tracking-wider">
                                INDEPENDENT
                            </span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-3.5 rounded-2xl border border-slate-100">
                            Independent student council candidates serving with institutional integrity, academic dedication, and non-partisan commitment to fellow Asuncionistas.
                        </p>
                        <div>
                            <span class="text-[10px] uppercase font-black text-slate-400 tracking-wider block mb-2">INDEPENDENT CANDIDATES (${{indepCandidates.length}} CANDIDATES)</span>
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                ${{indepCandidates.map(c => {{
                                    const posObj = DEFAULT_POSITIONS.find(p => p.id === c.posId);
                                    return `
                                        <div class="flex items-center space-x-2.5 p-2 rounded-xl bg-slate-50 border border-slate-200">
                                            <img src="${{c.photo || '/templates/ua-logo.png'}}" class="w-9 h-9 rounded-xl object-cover object-center border shrink-0" style="object-fit: cover; object-position: center;" onerror="this.onerror=null; this.src='/templates/ua-logo.png';">
                                            <div class="truncate">
                                                <span class="font-extrabold text-xs text-slate-900 block truncate">${{c.name}}</span>
                                                <span class="text-[10px] text-slate-600 font-bold uppercase">${{posObj ? posObj.name : c.posId}}</span>
                                            </div>
                                        </div>
                                    `;
                                }}).join('')}}
                            </div>
                        </div>
                    </div>
                `;
            }}

            if (!cardsHtml) {{
                cardsHtml = `<div class="p-8 text-center text-slate-400 bg-white rounded-3xl border border-slate-200">No registered candidate slates found for this department.</div>`;
            }}

            container.innerHTML = cardsHtml;
            lucide.createIcons();
        }}
    </script>
</body>
</html>'''

print("Student HTML generator ready.")

def generate_admin_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniVote Admin Console - University of the Assumption</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- CryptoJS for AES-256 and SHA-256 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Font Family -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- External CSS -->
    <link rel="stylesheet" href="/static/css/admin.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Plus Jakarta Sans', 'sans-serif'] },
                    colors: { ua: { navy: '#020381', royal: '#1e3a8a', gold: '#d97706' } }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-100 text-slate-800 font-sans antialiased min-h-screen flex flex-col">

    <!-- Login Modal overlay if unauthenticated -->
    <div id="adminLoginModal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-8 space-y-6 shadow-2xl border border-slate-200">
            <div class="text-center space-y-2">
                <div class="w-14 h-14 rounded-2xl bg-blue-900 text-amber-400 mx-auto flex items-center justify-center shadow-lg">
                    <i data-lucide="shield-check" class="w-8 h-8"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-900">Administrator Access</h3>
                <p class="text-xs text-slate-500">University of the Assumption Election Commission</p>
            </div>

            <div id="loginErrorMsg" class="hidden text-rose-600 font-bold text-xs bg-rose-50 p-3 rounded-xl border border-rose-200 text-center"></div>

            <form onsubmit="handleAdminLogin(event)" class="space-y-4 text-xs">
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Admin Username</label>
                    <input type="text" id="adminUsername" required value="admin" class="w-full px-4 py-2.5 border rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Admin Password</label>
                    <input type="password" id="adminPassword" required value="ua2026admin" class="w-full px-4 py-2.5 border rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>
                <button type="submit" id="adminLoginSubmitBtn" class="w-full bg-blue-700 hover:bg-blue-800 text-white font-bold py-3 rounded-xl transition shadow-md text-xs">Log In as Administrator</button>
            </form>
        </div>
    </div>

    <!-- Top Navigation Header -->
    <header class="bg-[#0B1528] text-white sticky top-0 z-40 border-b border-slate-800 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                
                <!-- Glowing Shield Icon & Brand -->
                <div class="flex items-center space-x-3.5">
                    <div class="relative flex items-center justify-center">
                        <div class="absolute inset-0 bg-blue-500/40 rounded-2xl blur-md"></div>
                        <div class="relative w-11 h-11 rounded-2xl bg-gradient-to-tr from-blue-700 to-indigo-600 flex items-center justify-center text-amber-300 shadow-[0_0_18px_rgba(59,130,246,0.55)] border border-blue-400/40">
                            <i data-lucide="shield-check" class="w-6 h-6 text-white drop-shadow"></i>
                        </div>
                    </div>
                    <div class="flex items-center space-x-2.5">
                        <span class="text-xl font-black tracking-tight text-white">Uni<span class="text-blue-400">Vote</span></span>
                        <span class="text-slate-500 text-sm font-semibold">|</span>
                        <span class="text-sm font-bold text-slate-200 tracking-wide">Admin Dashboard</span>
                    </div>
                </div>

                <!-- Log Out Admin Button -->
                <div class="flex items-center">
                    <button onclick="handleAdminLogout()" class="bg-slate-800/90 hover:bg-slate-700 text-slate-200 font-bold text-xs px-4 py-2.5 rounded-xl transition flex items-center space-x-2 border border-slate-700 shadow-sm">
                        <i data-lucide="log-out" class="w-4 h-4 text-slate-400"></i>
                        <span>Log Out Admin</span>
                    </button>
                </div>

            </div>
        </div>
    </header>

    <!-- Main Content Tabs Container -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 bg-slate-100">

        <!-- Horizontal Tab Navigation Bar with Pill-Shaped Tabs -->
        <div class="flex items-center space-x-2 bg-white/90 backdrop-blur-sm p-1.5 rounded-full border border-slate-200 shadow-sm w-fit max-w-full overflow-x-auto">
            <button onclick="switchAdminSection('results')" id="admin-tab-results" class="admin-tab-btn px-5 py-2.5 rounded-full text-xs font-bold bg-blue-600 text-white shadow-md shadow-blue-500/25 flex items-center space-x-2 transition whitespace-nowrap">
                <i data-lucide="trophy" class="w-4 h-4"></i>
                <span>Department Winners &amp; Tallies</span>
            </button>
            <button onclick="switchAdminSection('students')" id="admin-tab-students" class="admin-tab-btn px-5 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center space-x-2 transition whitespace-nowrap">
                <i data-lucide="users" class="w-4 h-4 text-slate-400"></i>
                <span>Student Management</span>
            </button>
            <button onclick="switchAdminSection('candidates')" id="admin-tab-candidates" class="admin-tab-btn px-5 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center space-x-2 transition whitespace-nowrap">
                <i data-lucide="user-plus" class="w-4 h-4 text-slate-400"></i>
                <span>Candidate Management</span>
            </button>
            <button onclick="switchAdminSection('elections')" id="admin-tab-elections" class="admin-tab-btn px-5 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center space-x-2 transition whitespace-nowrap">
                <i data-lucide="calendar" class="w-4 h-4 text-slate-400"></i>
                <span>Election Settings</span>
            </button>
            <button onclick="switchAdminSection('audit')" id="admin-tab-audit" class="admin-tab-btn px-5 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center space-x-2 transition whitespace-nowrap">
                <i data-lucide="database" class="w-4 h-4 text-slate-400"></i>
                <span>Audit Registry</span>
            </button>
        </div>

        <!-- SECTION 1: LIVE TALLIES — ALL 10 DEPARTMENTS & 6 POSITIONS (EXACT NAMES WITHOUT ABBREVIATIONS) -->
        <div id="admin-section-results" class="admin-section space-y-6">

            <!-- Summary Stats Bar -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 space-y-1">
                    <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Total Ballots Cast</p>
                    <p class="text-2xl font-black text-slate-900" id="statTotalBallots">0</p>
                </div>
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 space-y-1">
                    <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Total Candidates</p>
                    <p class="text-2xl font-black text-slate-900" id="statTotalCandidates">0</p>
                </div>
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 space-y-1">
                    <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Positions per Dept</p>
                    <p class="text-2xl font-black text-blue-700">6 Races</p>
                </div>
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4 space-y-1">
                    <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Results Status</p>
                    <p class="text-sm font-black" id="statPublicationBadge">Sealed / Private</p>
                </div>
            </div>

            <!-- Section Header + Refresh -->
            <div class="flex items-center justify-between">
                <h2 class="text-base font-extrabold text-slate-800 flex items-center space-x-2">
                    <i data-lucide="bar-chart-2" class="w-5 h-5 text-blue-600"></i>
                    <span>Live Candidate Tallies — All 6 Positions Across Departments</span>
                </h2>
                <button onclick="loadWinnersAndTallies()" class="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2 rounded-xl shadow transition">
                    <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                    <span>Refresh Tallies</span>
                </button>
            </div>

            <!-- Dynamic Department Columns -->
            <div id="allDeptContainer" class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6 items-start">
                <div class="col-span-3 text-center text-slate-400 py-12 text-sm">Loading tallies...</div>
            </div>
        </div>

        <!-- SECTION 2: STUDENT ENROLLMENT ROSTER -->
        <div id="admin-section-students" class="admin-section hidden space-y-6">
            <div class="flex justify-between items-center bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-extrabold text-slate-900">UA Student Enrollment Roster</h3>
                    <p class="text-xs text-slate-500">Add, edit, verify, or remove enrolled students across academic departments</p>
                </div>
                <button onclick="openStudentModal()" class="bg-blue-700 hover:bg-blue-800 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-md flex items-center space-x-2">
                    <i data-lucide="plus" class="w-4 h-4"></i>
                    <span>Add New Student</span>
                </button>
            </div>

            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                <table class="w-full text-left text-xs text-slate-600">
                    <thead class="bg-slate-50 text-slate-400 font-bold uppercase text-[10px] border-b">
                        <tr>
                            <th class="p-4">Student ID (10 Digits)</th>
                            <th class="p-4">Full Student Name</th>
                            <th class="p-4">UA Institutional Email</th>
                            <th class="p-4">Department</th>
                            <th class="p-4">Status</th>
                            <th class="p-4 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody id="studentTableBody" class="divide-y divide-slate-100">
                        <!-- Injected JS -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- SECTION 3: CANDIDATE MANAGEMENT -->
        <div id="admin-section-candidates" class="admin-section hidden space-y-6">
            <div class="flex justify-between items-center bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-extrabold text-slate-900">Election Candidate Directory</h3>
                    <p class="text-xs text-slate-500">Manage candidates across President, VP, Secretary, Treasurer, Auditor, and PRO</p>
                </div>
                <button onclick="openCandidateModal()" class="bg-blue-700 hover:bg-blue-800 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow-md flex items-center space-x-2">
                    <i data-lucide="plus" class="w-4 h-4"></i>
                    <span>Add Candidate</span>
                </button>
            </div>

            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                <table class="w-full text-left text-xs text-slate-600">
                    <thead class="bg-slate-50 text-slate-400 font-bold uppercase text-[10px] border-b">
                        <tr>
                            <th class="p-4">Candidate Name</th>
                            <th class="p-4">Race / Position</th>
                            <th class="p-4">Target Department</th>
                            <th class="p-4">Partylist</th>
                            <th class="p-4 text-right">Actions</th>
                        </tr>
                    </thead>
                    <tbody id="candidateTableBody" class="divide-y divide-slate-100">
                        <!-- Injected JS -->
                    </tbody>
                </table>
            </div>
        </div>

        <!-- SECTION 4: ELECTION MANAGEMENT -->
        <div id="admin-section-elections" class="admin-section hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-6">
                <div>
                    <h3 class="text-xl font-extrabold text-slate-900">Election Controls &amp; Schedule</h3>
                    <p class="text-xs text-slate-500">Set opening and closing dates, activate/deactivate elections, and publish official results to students</p>
                </div>

                <form onsubmit="handleSaveElection(event)" class="space-y-4 max-w-xl text-xs">
                    <div>
                        <label class="block font-bold text-slate-700 mb-1">Election Title</label>
                        <input type="text" id="elecTitle" required class="w-full px-4 py-2.5 border rounded-xl focus:outline-none">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block font-bold text-slate-700 mb-1">Opening Date</label>
                            <input type="date" id="elecStartDate" required class="w-full px-4 py-2.5 border rounded-xl focus:outline-none">
                        </div>
                        <div>
                            <label class="block font-bold text-slate-700 mb-1">Closing Date</label>
                            <input type="date" id="elecEndDate" required class="w-full px-4 py-2.5 border rounded-xl focus:outline-none">
                        </div>
                    </div>
                    <div class="flex items-center space-x-6 pt-2">
                        <label class="flex items-center space-x-2 font-bold cursor-pointer">
                            <input type="checkbox" id="elecActive" class="w-4 h-4 rounded text-blue-600">
                            <span>Election Activated (Voting Enabled)</span>
                        </label>
                        <label class="flex items-center space-x-2 font-bold cursor-pointer">
                            <input type="checkbox" id="elecPublished" class="w-4 h-4 rounded text-blue-600">
                            <span>Publish Official Results to Students</span>
                        </label>
                    </div>
                    <button type="submit" class="bg-blue-700 hover:bg-blue-800 text-white font-bold px-6 py-3 rounded-xl transition shadow-md">
                        Save Election Configuration
                    </button>
                </form>

                <!-- DANGER ZONE: CLEAR ALL VOTING DATA -->
                <div class="mt-8 pt-6 border-t border-rose-200">
                    <div class="p-5 rounded-2xl bg-rose-50/80 border border-rose-300 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                        <div class="space-y-1">
                            <div class="flex items-center space-x-2">
                                <div class="w-8 h-8 rounded-lg bg-rose-100 text-rose-700 flex items-center justify-center shrink-0">
                                    <i data-lucide="alert-octagon" class="w-5 h-5"></i>
                                </div>
                                <h4 class="font-extrabold text-sm text-rose-900">Administrative Danger Zone: Clear All Voting Data</h4>
                            </div>
                            <p class="text-xs text-rose-700 max-w-xl leading-relaxed">
                                Completely wipes all stored encrypted ballot databases, live voter tallies, submitted vote history, and active sessions from browser storage.
                            </p>
                            <p class="text-[11px] font-bold text-emerald-800">
                                ✓ Candidate profiles and student enrollment rosters are strictly preserved.
                            </p>
                        </div>
                        <button type="button" onclick="confirmClearAllVotingData()" class="px-5 py-3 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-black text-xs transition shadow-md flex items-center space-x-2 shrink-0">
                            <i data-lucide="trash-2" class="w-4 h-4"></i>
                            <span>Clear All Voting Data</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- SECTION 5: AUDIT LOG -->
        <div id="admin-section-audit" class="admin-section hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <div class="flex justify-between items-center border-b pb-4">
                    <div>
                        <h3 class="text-xl font-extrabold text-slate-900">Encrypted Ballot Audit Registry</h3>
                        <p class="text-xs text-slate-500">Cryptographically secured audit log of all cast ballots</p>
                    </div>
                    <span class="text-xs font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">Commission Certified</span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs text-slate-600">
                        <thead class="bg-slate-50 text-slate-400 font-bold uppercase text-[10px] border-b">
                            <tr>
                                <th class="p-4">Timestamp</th>
                                <th class="p-4">Voter Token (SHA-256)</th>
                                <th class="p-4">Department</th>
                                <th class="p-4">Audit Cipher Record</th>
                            </tr>
                        </thead>
                        <tbody id="encryptedBallotsTableBody" class="divide-y divide-slate-100 font-mono text-[11px]">
                            <!-- Injected JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </main>

    <!-- Modal: Add/Edit Student -->
    <div id="studentEditModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 border shadow-2xl">
            <h3 class="font-bold text-base text-slate-900" id="studentModalTitle">Add UA Student</h3>
            <div id="adminStudentError" class="hidden text-rose-600 text-xs bg-rose-50 p-2.5 rounded-xl border border-rose-200 font-semibold"></div>
            <form onsubmit="handleSaveStudent(event)" class="space-y-3 text-xs">
                <input type="hidden" id="studentEditIndex" value="-1">
                <div>
                    <label class="block font-bold mb-1">
                        Student ID <span class="text-rose-500">*</span>
                        <span class="text-[10px] font-normal text-slate-400">(10 digits, year 2010–2026)</span>
                    </label>
                    <input type="text" id="modalStudentId" required maxlength="10" placeholder="e.g. 2024000669" class="w-full px-4 py-2 border rounded-xl font-mono">
                </div>
                <div>
                    <label class="block font-bold mb-1">Full Student Name <span class="text-rose-500">*</span></label>
                    <input type="text" id="modalStudentName" required placeholder="e.g. Juan Dela T. Cruz" class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">
                        UA Institutional Email <span class="text-rose-500">*</span>
                        <span class="text-[10px] font-normal text-slate-400">(@ua.edu.ph required)</span>
                    </label>
                    <input type="email" id="modalStudentEmail" required placeholder="e.g. jdtcruz.student@ua.edu.ph" class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">Department</label>
                    <select id="modalStudentDept" required class="w-full px-4 py-2 border rounded-xl bg-white font-medium">
                        <option value="College of Accountancy">College of Accountancy</option>
                        <option value="College of Engineering and Architecture">College of Engineering and Architecture</option>
                        <option value="College of Hospitality and Tourism Management">College of Hospitality and Tourism Management</option>
                        <option value="College of Nursing and Pharmacy">College of Nursing and Pharmacy</option>
                        <option value="School of Arts and Sciences">School of Arts and Sciences</option>
                        <option value="School of Business and Public Administration">School of Business and Public Administration</option>
                        <option value="School of Education">School of Education</option>
                        <option value="College of Information Technology">College of Information Technology</option>
                        <option value="Senior High School">Senior High School</option>
                        <option value="Junior High School">Junior High School</option>
                    </select>
                </div>
                <div class="flex items-center space-x-2 pt-1">
                    <input type="checkbox" id="modalStudentVerified" class="w-4 h-4 rounded text-blue-600">
                    <label for="modalStudentVerified" class="font-bold">UA Enrolled Verified</label>
                </div>
                <div class="flex space-x-2 pt-2">
                    <button type="button" onclick="closeStudentModal()" class="flex-1 bg-slate-100 py-2.5 rounded-xl font-bold">Cancel</button>
                    <button type="submit" class="flex-1 bg-blue-700 text-white py-2.5 rounded-xl font-bold">Save Student</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Modal: Add/Edit Candidate (Expanded to 6 Positions & 10 Depts) -->
    <div id="candidateEditModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 border shadow-2xl">
            <h3 class="font-bold text-base text-slate-900" id="candidateModalTitle">Add Candidate</h3>
            <form onsubmit="handleSaveCandidate(event)" class="space-y-3 text-xs">
                <input type="hidden" id="candidateEditIndex" value="-1">
                <div>
                    <label class="block font-bold mb-1">Candidate Name</label>
                    <input type="text" id="modalCandName" required class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">Position / Office</label>
                    <select id="modalCandPos" required class="w-full px-4 py-2 border rounded-xl bg-white font-bold text-blue-800">
                        <option value="pres">President</option>
                        <option value="vp">Vice President</option>
                        <option value="sec">Secretary</option>
                        <option value="tres">Treasurer</option>
                        <option value="aud">Auditor</option>
                        <option value="pro">Public Relations Officer (PRO)</option>
                    </select>
                </div>
                <div>
                    <label class="block font-bold mb-1">Target Department</label>
                    <select id="modalCandDept" required class="w-full px-4 py-2 border rounded-xl bg-white font-medium">
                        <option value="College of Accountancy">College of Accountancy</option>
                        <option value="College of Engineering and Architecture">College of Engineering and Architecture</option>
                        <option value="College of Hospitality and Tourism Management">College of Hospitality and Tourism Management</option>
                        <option value="College of Nursing and Pharmacy">College of Nursing and Pharmacy</option>
                        <option value="School of Arts and Sciences">School of Arts and Sciences</option>
                        <option value="School of Business and Public Administration">School of Business and Public Administration</option>
                        <option value="School of Education">School of Education</option>
                        <option value="College of Information Technology">College of Information Technology</option>
                        <option value="Senior High School">Senior High School</option>
                        <option value="Junior High School">Junior High School</option>
                    </select>
                </div>
                <div>
                    <label class="block font-bold mb-1">Partylist</label>
                    <input type="text" id="modalCandParty" required class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">Candidate Photo URL</label>
                    <input type="text" id="modalCandPhoto" placeholder="https://images.unsplash.com/..." class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold mb-1">Platform Summary</label>
                    <textarea id="modalCandPlatform" rows="2" class="w-full px-4 py-2 border rounded-xl" placeholder="Key platform points..."></textarea>
                </div>
                <div class="flex space-x-2 pt-2">
                    <button type="button" onclick="closeCandidateModal()" class="flex-1 bg-slate-100 py-2.5 rounded-xl font-bold">Cancel</button>
                    <button type="submit" class="flex-1 bg-blue-700 text-white py-2.5 rounded-xl font-bold">Save Candidate</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Application Script -->
    <script>
        const AES_SECRET_KEY = 'UniVote-UA-2026';
        // ================= UNIVERSAL PARTY RESOLUTION =================
        function getCandidateParty(c) {
            if (!c) return 'Independent';
            const dept = (c.dept || c.targetDept || '').toLowerCase();
            const photo = (c.photo || '').toLowerCase();
            
            if (
                dept.includes('architecture') ||
                dept.includes('industrial engineering') ||
                dept.includes('information technology') ||
                dept.includes('nursing') ||
                dept.includes('pharmacy') ||
                dept.includes('criminology') ||
                photo.includes('college of architecture') ||
                photo.includes('college of industrial engineering') ||
                photo.includes('college of information technology') ||
                photo.includes('college of nursing') ||
                photo.includes('college of pharmacy') ||
                photo.includes('criminology')
            ) {
                return 'Independent';
            }

            if (c.party && c.party.trim() !== '') {
                const p = c.party.trim();
                if (p.toLowerCase() === 'siklab' || p.toLowerCase().includes('siklab')) {
                    return 'SIKLAB';
                }
                return p;
            }
            return 'Independent';
        }

        // ================= CLEAR ALL VOTING DATA ADMINISTRATIVE FUNCTION =================
        function confirmClearAllVotingData() {
            const userConfirm = prompt(
                "WARNING: CLEAR ALL VOTING DATA\\n\\n" +
                "This administrative action will:\\n" +
                "1. Wipe all encrypted ballots from localStorage (univote_encrypted_ballots_db)\\n" +
                "2. Reset all departmental vote tallies and winner leaderboards to 0\\n" +
                "3. Clear student vote submission histories (univote_has_voted, univote_saved_choices)\\n" +
                "4. Clear any active student voting sessions\\n\\n" +
                "Candidate profiles and student rosters will NOT be touched.\\n\\n" +
                "Type 'CLEAR' to confirm and execute:"
            );

            if (userConfirm === 'CLEAR' || userConfirm === 'clear') {
                clearAllVotingData();
            } else if (userConfirm !== null) {
                alert("Operation canceled: Confirmation word did not match 'CLEAR'.");
            }
        }

        function clearAllVotingData() {
            // 1. Wipe encrypted ballots database
            localStorage.setItem('univote_encrypted_ballots_db', JSON.stringify([]));

            // 2. Wipe vote histories and flags
            localStorage.removeItem('univote_has_voted');
            localStorage.removeItem('univote_saved_choices');

            // 3. Wipe active student voter session
            sessionStorage.removeItem('univote_locked_session');

            // Note: Candidate profiles (univote_db_candidates) and student rosters (univote_db_students) are strictly preserved!

            // 4. Refresh admin tallies, winner boards, and audit log immediately
            loadWinnersAndTallies();
            loadAuditTable();

            alert(
                "SUCCESS: Voting data wiped completely!\\n\\n" +
                "• Encrypted ballots database cleared.\\n" +
                "• All departmental tallies reset to zero.\\n" +
                "• Student voting history flags reset.\\n" +
                "• Candidate profiles and student rosters preserved."
            );
        }


        // ALL 6 POSITIONS
        const POSITIONS = [
            { id: 'pres', name: 'President' },
            { id: 'vp', name: 'Vice President' },
            { id: 'sec', name: 'Secretary' },
            { id: 'tres', name: 'Treasurer' },
            { id: 'aud', name: 'Auditor' },
            { id: 'pro', name: 'Public Relations Officer (PRO)' }
        ];

        // ALL 10 ACADEMIC DEPARTMENTS WITH HARMONIOUS, NON-EYESORE COLORS
        const DEPARTMENTS = [
            { 
                id: 'College of Accountancy', 
                label: 'College of Accountancy', 
                cardBorder: 'border-indigo-200/90',
                headerBg: 'bg-gradient-to-r from-indigo-50 to-blue-50/70 border-b border-indigo-100',
                titleColor: 'text-indigo-950',
                subColor: 'text-indigo-600',
                badgeClass: 'bg-indigo-100 text-indigo-900 border border-indigo-200',
                accentBg: 'bg-indigo-50/20',
                barColor: 'bg-indigo-600',
                dot: 'bg-indigo-600'
            },
            { 
                id: 'College of Engineering and Architecture', 
                label: 'College of Engineering and Architecture', 
                cardBorder: 'border-amber-200/90',
                headerBg: 'bg-gradient-to-r from-amber-50 to-orange-50/60 border-b border-amber-100',
                titleColor: 'text-amber-950',
                subColor: 'text-amber-700',
                badgeClass: 'bg-amber-100 text-amber-900 border border-amber-200',
                accentBg: 'bg-amber-50/20',
                barColor: 'bg-amber-600',
                dot: 'bg-amber-600'
            },
            { 
                id: 'College of Hospitality and Tourism Management', 
                label: 'College of Hospitality and Tourism Management', 
                cardBorder: 'border-emerald-200/90',
                headerBg: 'bg-gradient-to-r from-emerald-50 to-teal-50/60 border-b border-emerald-100',
                titleColor: 'text-emerald-950',
                subColor: 'text-emerald-700',
                badgeClass: 'bg-emerald-100 text-emerald-900 border border-emerald-200',
                accentBg: 'bg-emerald-50/20',
                barColor: 'bg-emerald-600',
                dot: 'bg-emerald-600'
            },
            { 
                id: 'College of Nursing and Pharmacy', 
                label: 'College of Nursing and Pharmacy', 
                cardBorder: 'border-rose-200/90',
                headerBg: 'bg-gradient-to-r from-rose-50 to-pink-50/60 border-b border-rose-100',
                titleColor: 'text-rose-950',
                subColor: 'text-rose-700',
                badgeClass: 'bg-rose-100 text-rose-900 border border-rose-200',
                accentBg: 'bg-rose-50/20',
                barColor: 'bg-rose-600',
                dot: 'bg-rose-600'
            },
            { 
                id: 'School of Arts and Sciences', 
                label: 'School of Arts and Sciences', 
                cardBorder: 'border-purple-200/90',
                headerBg: 'bg-gradient-to-r from-purple-50 to-violet-50/60 border-b border-purple-100',
                titleColor: 'text-purple-950',
                subColor: 'text-purple-700',
                badgeClass: 'bg-purple-100 text-purple-900 border border-purple-200',
                accentBg: 'bg-purple-50/20',
                barColor: 'bg-purple-600',
                dot: 'bg-purple-600'
            },
            { 
                id: 'School of Business and Public Administration', 
                label: 'School of Business and Public Administration', 
                cardBorder: 'border-sky-200/90',
                headerBg: 'bg-gradient-to-r from-sky-50 to-blue-50/60 border-b border-sky-100',
                titleColor: 'text-sky-950',
                subColor: 'text-sky-700',
                badgeClass: 'bg-sky-100 text-sky-900 border border-sky-200',
                accentBg: 'bg-sky-50/20',
                barColor: 'bg-sky-600',
                dot: 'bg-sky-600'
            },
            { 
                id: 'School of Education', 
                label: 'School of Education', 
                cardBorder: 'border-teal-200/90',
                headerBg: 'bg-gradient-to-r from-teal-50 to-emerald-50/60 border-b border-teal-100',
                titleColor: 'text-teal-950',
                subColor: 'text-teal-700',
                badgeClass: 'bg-teal-100 text-teal-900 border border-teal-200',
                accentBg: 'bg-teal-50/20',
                barColor: 'bg-teal-600',
                dot: 'bg-teal-600'
            },
            { 
                id: 'College of Information Technology', 
                label: 'College of Information Technology', 
                cardBorder: 'border-blue-300',
                headerBg: 'bg-gradient-to-r from-blue-50 to-indigo-50/60 border-b border-blue-200',
                titleColor: 'text-blue-950',
                subColor: 'text-blue-700',
                badgeClass: 'bg-blue-100 text-blue-900 border border-blue-300',
                accentBg: 'bg-blue-50/25',
                barColor: 'bg-blue-600',
                dot: 'bg-blue-600'
            },
            { 
                id: 'Senior High School', 
                label: 'Senior High School', 
                cardBorder: 'border-orange-200/90',
                headerBg: 'bg-gradient-to-r from-orange-50 to-amber-50/60 border-b border-orange-100',
                titleColor: 'text-orange-950',
                subColor: 'text-orange-700',
                badgeClass: 'bg-orange-100 text-orange-900 border border-orange-200',
                accentBg: 'bg-orange-50/20',
                barColor: 'bg-orange-600',
                dot: 'bg-orange-600'
            },
            { 
                id: 'Junior High School', 
                label: 'Junior High School', 
                cardBorder: 'border-cyan-200/90',
                headerBg: 'bg-gradient-to-r from-cyan-50 to-teal-50/60 border-b border-cyan-100',
                titleColor: 'text-cyan-950',
                subColor: 'text-cyan-700',
                badgeClass: 'bg-cyan-100 text-cyan-900 border border-cyan-200',
                accentBg: 'bg-cyan-50/20',
                barColor: 'bg-cyan-600',
                dot: 'bg-cyan-600'
            }
        ];

        document.addEventListener('DOMContentLoaded', () => {
            lucide.createIcons();
            checkAdminAuth();
            loadWinnersAndTallies();
            loadStudentTable();
            loadCandidateTable();
            loadElectionConfig();
            loadAuditTable();
        });

        function checkAdminAuth() {
            const modal = document.getElementById('adminLoginModal');
            if (sessionStorage.getItem('univote_admin_authenticated') === 'true') {
                if (modal) {
                    modal.classList.add('hidden');
                    modal.classList.remove('flex');
                    modal.style.display = 'none';
                }
            } else {
                if (modal) {
                    modal.classList.remove('hidden');
                    modal.classList.add('flex');
                    modal.style.display = 'flex';
                }
            }
        }

        function handleAdminLogin(e) {
            if (e && e.preventDefault) e.preventDefault();
            const u = document.getElementById('adminUsername').value.trim();
            const p = document.getElementById('adminPassword').value.trim();
            const errEl = document.getElementById('loginErrorMsg');

            if (u === 'admin' && p === 'ua2026admin') {
                sessionStorage.setItem('univote_admin_authenticated', 'true');
                const modal = document.getElementById('adminLoginModal');
                if (modal) {
                    modal.classList.add('hidden');
                    modal.classList.remove('flex');
                    modal.style.display = 'none';
                }
                if (errEl) errEl.classList.add('hidden');
            } else {
                if (errEl) {
                    errEl.textContent = "Invalid Administrator credentials!";
                    errEl.classList.remove('hidden');
                } else {
                    alert("Invalid Administrator credentials!");
                }
            }
        }

        function handleAdminLogout() {
            sessionStorage.removeItem('univote_admin_authenticated');
            location.reload();
        }

        function switchAdminSection(sectionKey) {
            document.querySelectorAll('.admin-section').forEach(e => e.classList.add('hidden'));
            document.querySelectorAll('.admin-tab-btn').forEach(e => {
                e.classList.remove('bg-blue-600', 'bg-blue-700', 'text-white', 'shadow-md', 'shadow-blue-500/25');
                e.classList.add('text-slate-600');
            });

            const targetSection = document.getElementById(`admin-section-${sectionKey}`);
            if (targetSection) targetSection.classList.remove('hidden');

            const btn = document.getElementById(`admin-tab-${sectionKey}`);
            if (btn) {
                btn.classList.remove('text-slate-600');
                btn.classList.add('bg-blue-600', 'text-white', 'shadow-md', 'shadow-blue-500/25');
            }
        }

        // --- SECTION 1: LIVE TALLIES ACROSS ALL 6 POSITIONS & 10 DEPARTMENTS ---
        function buildTalliesForDept(ballots, deptId) {
            const tallies = {};
            const deptBallots = ballots.filter(b => b.department === deptId);
            deptBallots.forEach(b => {
                try {
                    const bytes = CryptoJS.AES.decrypt(b.cipherPayload, AES_SECRET_KEY);
                    const payload = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));
                    const votes = payload.votes || {};
                    Object.keys(votes).forEach(posId => {
                        const candId = votes[posId];
                        if (!tallies[posId]) tallies[posId] = {};
                        tallies[posId][candId] = (tallies[posId][candId] || 0) + 1;
                    });
                } catch (e) {}
            });
            return { tallies, deptBallots };
        }

        function renderDeptColumn(dept, candidates, ballots) {
            const { tallies, deptBallots } = buildTalliesForDept(ballots, dept.id);
            const totalVotes = deptBallots.length;
            const deptCandidates = candidates.filter(c => c.targetDept === dept.id);

            const positionCards = POSITIONS.map(pos => {
                const posCands = deptCandidates.filter(c => c.posId === pos.id);
                if (posCands.length === 0) return '';

                let maxVotes = 0;
                let leaderId = null;
                posCands.forEach(c => {
                    const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                    if (count > maxVotes) { maxVotes = count; leaderId = c.id; }
                });

                const candidateRows = posCands.map(c => {
                    const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                    const pct = totalVotes > 0 ? ((count / totalVotes) * 100).toFixed(1) : '0.0';
                    const isLeading = c.id === leaderId && count > 0;
                    const barWidth = totalVotes > 0 ? Math.round((count / totalVotes) * 100) : 0;

                    return `
                        <div class="rounded-xl border ${isLeading ? 'border-amber-300 bg-amber-50' : 'border-slate-100 bg-slate-50'} p-3 space-y-1.5">
                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="flex items-center space-x-1.5">
                                        <img src="${c.photo || '/templates/ua-logo.png'}" class="w-6 h-6 rounded-md object-cover object-center border shrink-0 inline-block mr-1" style="object-fit: cover; object-position: center;" onerror="this.onerror=null; this.src='/templates/ua-logo.png';"><h4 class="font-bold text-xs text-slate-900 inline-block align-middle">${c.name}</h4>
                                        ${isLeading ? '<span class="bg-amber-500 text-white font-black text-[8px] px-1.5 py-0.5 rounded-full uppercase">LEAD</span>' : ''}
                                    </div>
                                    <p class="text-[10px] font-semibold text-blue-600 truncate max-w-[150px]">${getCandidateParty(c)}</p>
                                </div>
                                <div class="text-right">
                                    <span class="text-base font-black text-slate-900">${count}</span>
                                    <span class="text-[10px] text-slate-400"> votes</span>
                                </div>
                            </div>
                            <div class="w-full bg-slate-200/80 rounded-full h-1.5 overflow-hidden">
                                <div class="${isLeading ? 'bg-amber-500' : dept.barColor} h-1.5 rounded-full transition-all duration-300" style="width:${barWidth}%"></div>
                            </div>
                            <div class="flex justify-between text-[9px] font-bold">
                                <span class="text-slate-500">${pct}%</span>
                                <span class="${isLeading ? 'text-amber-600' : 'text-slate-400'}">${barWidth}% share</span>
                            </div>
                        </div>
                    `;
                }).join('');

                return `
                    <div class="bg-white/95 rounded-2xl border ${dept.cardBorder}/60 p-3.5 space-y-2 shadow-xs">
                        <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                            <span class="text-[10px] font-extrabold text-slate-700 uppercase tracking-wider">${pos.name}</span>
                            <span class="text-[9px] font-bold ${dept.badgeClass} px-2 py-0.5 rounded-md">${posCands.length} candidate${posCands.length !== 1 ? 's' : ''}</span>
                        </div>
                        <div class="space-y-2">
                            ${candidateRows}
                        </div>
                    </div>
                `;
            }).join('');

            const noCandidates = deptCandidates.length === 0;

            return `
                <div class="bg-white rounded-3xl border ${dept.cardBorder} shadow-sm overflow-hidden hover:shadow-md transition">
                    <div class="${dept.headerBg} p-5 space-y-1">
                        <div class="flex items-center justify-between">
                            <h3 class="font-extrabold text-xs tracking-wider uppercase ${dept.titleColor} flex items-center space-x-2">
                                <span class="w-3 h-3 rounded-full ${dept.dot} shadow-xs"></span>
                                <span>${dept.label}</span>
                            </h3>
                            <span class="text-[10px] font-bold ${dept.badgeClass} px-2.5 py-0.5 rounded-full">${totalVotes} Ballots</span>
                        </div>
                        <p class="text-[11px] ${dept.subColor} font-semibold">${deptCandidates.length} Candidates across 6 positions</p>
                    </div>

                    <div class="p-5 space-y-3 ${dept.accentBg}">
                        ${noCandidates
                            ? `<div class="rounded-2xl border border-dashed border-slate-200 p-6 text-center text-slate-400 text-xs bg-white">
                                    No candidates registered for ${dept.label}.
                               </div>`
                            : positionCards
                        }
                    </div>
                </div>
            `;
        }

        function loadWinnersAndTallies() {
            const mainContainer = document.getElementById('allDeptContainer');
            const statTotal = document.getElementById('statTotalBallots');
            const statCands = document.getElementById('statTotalCandidates');
            const badge = document.getElementById('statPublicationBadge');

            const ballots = JSON.parse(localStorage.getItem('univote_encrypted_ballots_db')) || [];
            const candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
            const elec = JSON.parse(localStorage.getItem('univote_db_elections')) || { published: false };

            if (statTotal) statTotal.textContent = ballots.length;
            if (statCands) statCands.textContent = candidates.length;
            if (badge) {
                if (elec.published) {
                    badge.textContent = 'Published to Students';
                    badge.className = 'text-sm font-black text-emerald-600';
                } else {
                    badge.textContent = 'Sealed / Private';
                    badge.className = 'text-sm font-black text-amber-600';
                }
            }

            if (mainContainer) {
                mainContainer.innerHTML = DEPARTMENTS.map(dept =>
                    renderDeptColumn(dept, candidates, ballots)
                ).join('');
            }

            lucide.createIcons();
        }

        // --- SECTION 2: STUDENT MANAGEMENT ---
        function loadStudentTable() {
            const students = JSON.parse(localStorage.getItem('univote_db_students')) || [];
            const tbody = document.getElementById('studentTableBody');

            tbody.innerHTML = students.map((s, idx) => `
                <tr class="hover:bg-slate-50 border-b">
                    <td class="p-4 font-bold text-slate-900 font-mono">${s.id}</td>
                    <td class="p-4 font-semibold">${s.name}</td>
                    <td class="p-4 font-mono text-[11px] text-slate-600">${s.email || '<span class="text-slate-400">Not set</span>'}</td>
                    <td class="p-4"><span class="bg-blue-50 text-blue-800 font-bold px-2 py-0.5 rounded border border-blue-100">${s.dept}</span></td>
                    <td class="p-4">
                        <button onclick="toggleVerifyStudent(${idx})" class="px-2.5 py-1 rounded-full text-[10px] font-bold ${s.verified ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
                            ${s.verified ? 'UA Verified' : 'Unverified'}
                        </button>
                    </td>
                    <td class="p-4 text-right space-x-2">
                        <button onclick="editStudent(${idx})" class="text-blue-600 hover:text-blue-800 font-bold">Edit</button>
                        <button onclick="deleteStudent(${idx})" class="text-rose-600 hover:text-rose-800 font-bold">Delete</button>
                    </td>
                </tr>
            `).join('');
        }

        function toggleVerifyStudent(idx) {
            let students = JSON.parse(localStorage.getItem('univote_db_students')) || [];
            students[idx].verified = !students[idx].verified;
            localStorage.setItem('univote_db_students', JSON.stringify(students));
            loadStudentTable();
        }

        function openStudentModal() {
            document.getElementById('studentEditIndex').value = "-1";
            document.getElementById('modalStudentId').value = "";
            document.getElementById('modalStudentName').value = "";
            document.getElementById('modalStudentEmail').value = "";
            document.getElementById('modalStudentDept').value = "College of Accountancy";
            document.getElementById('modalStudentVerified').checked = true;
            document.getElementById('adminStudentError').classList.add('hidden');
            document.getElementById('studentEditModal').classList.remove('hidden');
        }

        function closeStudentModal() {
            document.getElementById('studentEditModal').classList.add('hidden');
        }

        function editStudent(idx) {
            const students = JSON.parse(localStorage.getItem('univote_db_students')) || [];
            const s = students[idx];
            document.getElementById('studentEditIndex').value = idx;
            document.getElementById('modalStudentId').value = s.id;
            document.getElementById('modalStudentName').value = s.name;
            document.getElementById('modalStudentEmail').value = s.email || "";
            document.getElementById('modalStudentDept').value = s.dept;
            document.getElementById('modalStudentVerified').checked = s.verified;
            document.getElementById('adminStudentError').classList.add('hidden');
            document.getElementById('studentEditModal').classList.remove('hidden');
        }

        function handleSaveStudent(e) {
            e.preventDefault();
            const errBox = document.getElementById('adminStudentError');
            errBox.classList.add('hidden');

            const id = document.getElementById('modalStudentId').value.trim();
            const name = document.getElementById('modalStudentName').value.trim();
            const email = document.getElementById('modalStudentEmail').value.trim().toLowerCase();
            const dept = document.getElementById('modalStudentDept').value;
            const verified = document.getElementById('modalStudentVerified').checked;

            if (!/^(201[0-9]|202[0-6])\d{6}$/.test(id)) {
                errBox.innerText = "Student ID must strictly be 10 digits with admission year between 2010 and 2026 (e.g. 2024000669).";
                errBox.classList.remove('hidden');
                return;
            }

            if (!/^[a-zA-Z0-9._%+-]+@ua\.edu\.ph$/i.test(email)) {
                errBox.innerText = "Institutional email must be a valid @ua.edu.ph address (e.g. student@ua.edu.ph).";
                errBox.classList.remove('hidden');
                return;
            }

            const idx = parseInt(document.getElementById('studentEditIndex').value);
            let students = JSON.parse(localStorage.getItem('univote_db_students')) || [];

            const studentObj = {
                id,
                name,
                email,
                dept,
                verified,
                passwordHash: (idx !== -1 && students[idx].passwordHash) ? students[idx].passwordHash : CryptoJS.SHA256('UaVote2026*!').toString()
            };

            if (idx === -1) {
                students.push(studentObj);
            } else {
                students[idx] = studentObj;
            }

            localStorage.setItem('univote_db_students', JSON.stringify(students));
            closeStudentModal();
            loadStudentTable();
        }

        function deleteStudent(idx) {
            if (confirm("Delete this student record from system database?")) {
                let students = JSON.parse(localStorage.getItem('univote_db_students')) || [];
                students.splice(idx, 1);
                localStorage.setItem('univote_db_students', JSON.stringify(students));
                loadStudentTable();
            }
        }

        // --- SECTION 3: CANDIDATE MANAGEMENT ---
        function loadCandidateTable() {
            const candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
            const tbody = document.getElementById('candidateTableBody');

            tbody.innerHTML = candidates.map((c, idx) => {
                const posObj = POSITIONS.find(p => p.id === c.posId);
                const posName = posObj ? posObj.name : c.posId;

                return `
                    <tr class="hover:bg-slate-50 border-b">
                        <td class="p-4 font-bold text-slate-900 flex items-center space-x-2.5">
                            <img src="${c.photo || '/templates/ua-logo.png'}" class="w-8 h-8 rounded-xl object-cover object-center border shrink-0" style="object-fit: cover; object-position: center;" onerror="this.onerror=null; this.src='/templates/ua-logo.png';">
                            <span>${c.name}</span>
                        </td>
                        <td class="p-4"><span class="bg-blue-50 text-blue-800 font-extrabold px-2 py-0.5 rounded border border-blue-100 uppercase">${posName}</span></td>
                        <td class="p-4"><span class="bg-amber-50 text-amber-800 font-bold px-2 py-0.5 rounded border border-amber-100">${c.targetDept}</span></td>
                        <td class="p-4 font-semibold"><span class="px-2.5 py-0.5 rounded-full text-xs font-bold ${getCandidateParty(c) === 'SIKLAB' ? 'bg-amber-100 text-amber-800 border border-amber-200' : 'bg-slate-100 text-slate-700 border border-slate-200'}">${getCandidateParty(c)}</span></td>
                        <td class="p-4 text-right space-x-2">
                            <button onclick="editCandidate(${idx})" class="text-blue-600 hover:text-blue-800 font-bold">Edit</button>
                            <button onclick="deleteCandidate(${idx})" class="text-rose-600 hover:text-rose-800 font-bold">Delete</button>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function openCandidateModal() {
            document.getElementById('candidateEditIndex').value = "-1";
            document.getElementById('modalCandName').value = "";
            document.getElementById('modalCandPos').value = "pres";
            document.getElementById('modalCandDept').value = "College of Accountancy";
            document.getElementById('modalCandParty').value = "";
            document.getElementById('modalCandPhoto').value = "";
            document.getElementById('modalCandPlatform').value = "";
            document.getElementById('candidateEditModal').classList.remove('hidden');
        }

        function closeCandidateModal() {
            document.getElementById('candidateEditModal').classList.add('hidden');
        }

        function editCandidate(idx) {
            const candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
            const c = candidates[idx];
            document.getElementById('candidateEditIndex').value = idx;
            document.getElementById('modalCandName').value = c.name;
            document.getElementById('modalCandPos').value = c.posId;
            document.getElementById('modalCandDept').value = c.targetDept;
            document.getElementById('modalCandParty').value = c.party;
            document.getElementById('modalCandPhoto').value = c.photo || "";
            document.getElementById('modalCandPlatform').value = c.platform || "";
            document.getElementById('candidateEditModal').classList.remove('hidden');
        }

        function handleSaveCandidate(e) {
            e.preventDefault();
            const idx = parseInt(document.getElementById('candidateEditIndex').value);
            let candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];

            const candObj = {
                id: (idx !== -1 && candidates[idx].id) ? candidates[idx].id : 'cand_' + Date.now(),
                name: document.getElementById('modalCandName').value.trim(),
                posId: document.getElementById('modalCandPos').value,
                targetDept: document.getElementById('modalCandDept').value,
                party: document.getElementById('modalCandParty').value.trim(),
                dept: document.getElementById('modalCandDept').value,
                photo: document.getElementById('modalCandPhoto').value.trim() || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=300',
                platform: document.getElementById('modalCandPlatform').value.trim() || 'Platform dedicated to student service.',
                advocacies: ['Student Service']
            };

            if (idx === -1) {
                candidates.push(candObj);
            } else {
                candidates[idx] = candObj;
            }

            localStorage.setItem('univote_db_candidates', JSON.stringify(candidates));
            closeCandidateModal();
            loadCandidateTable();
            loadWinnersAndTallies();
        }

        function deleteCandidate(idx) {
            if (confirm("Delete this candidate?")) {
                let candidates = JSON.parse(localStorage.getItem('univote_db_candidates')) || [];
                candidates.splice(idx, 1);
                localStorage.setItem('univote_db_candidates', JSON.stringify(candidates));
                loadCandidateTable();
                loadWinnersAndTallies();
            }
        }

        // --- SECTION 4: ELECTION CONFIGURATION ---
        function loadElectionConfig() {
            const elec = JSON.parse(localStorage.getItem('univote_db_elections')) || {
                title: 'UA University Student Council Elections 2026',
                startDate: '2026-10-01',
                endDate: '2026-11-30',
                active: true,
                published: true
            };

            document.getElementById('elecTitle').value = elec.title;
            document.getElementById('elecStartDate').value = elec.startDate;
            document.getElementById('elecEndDate').value = elec.endDate;
            document.getElementById('elecActive').checked = elec.active;
            document.getElementById('elecPublished').checked = elec.published;
        }

        function handleSaveElection(e) {
            e.preventDefault();
            const elecObj = {
                title: document.getElementById('elecTitle').value.trim(),
                startDate: document.getElementById('elecStartDate').value,
                endDate: document.getElementById('elecEndDate').value,
                active: document.getElementById('elecActive').checked,
                published: document.getElementById('elecPublished').checked
            };

            localStorage.setItem('univote_db_elections', JSON.stringify(elecObj));
            alert("Election configuration updated successfully!");
            loadWinnersAndTallies();
        }

        // --- SECTION 5: AUDIT LOG ---
        function loadAuditTable() {
            const ballots = JSON.parse(localStorage.getItem('univote_encrypted_ballots_db')) || [];
            const tbody = document.getElementById('encryptedBallotsTableBody');

            if (ballots.length === 0) {
                tbody.innerHTML = `<tr><td colspan="4" class="p-4 text-slate-400">No encrypted ballots recorded in database.</td></tr>`;
                return;
            }

            tbody.innerHTML = ballots.map(b => `
                <tr class="hover:bg-slate-50 border-b">
                    <td class="p-4">${b.timestamp}</td>
                    <td class="p-4 text-blue-700 font-bold">${b.voterToken}</td>
                    <td class="p-4 font-sans font-bold">${b.department}</td>
                    <td class="p-4 text-emerald-600 break-all max-w-xs">${b.cipherPayload}</td>
                </tr>
            `).join('');
        }
    </script>
</body>
</html>'''

student_html = generate_student_html()
admin_html = generate_admin_html()

with open(r'D:\CODINGS\univote\templates\studentweb.html', 'w', encoding='utf-8') as f:
    f.write(student_html)
print("Updated studentweb.html successfully!")

with open(r'D:\CODINGS\univote\templates\adminweb.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
print("Updated adminweb.html successfully!")

with open(r'D:\CODINGS\univote\update_univote.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\\n')
    f.write('import os\\n\\n')
    f.write('STUDENT_HTML = ' + repr(student_html) + '\\n\\n')
    f.write('ADMIN_HTML = ' + repr(admin_html) + '\\n\\n')
    f.write('with open(r"templates\\\\studentweb.html", "w", encoding="utf-8") as f:\\n')
    f.write('    f.write(STUDENT_HTML)\\n')
    f.write('with open(r"templates\\\\adminweb.html", "w", encoding="utf-8") as f:\\n')
    f.write('    f.write(ADMIN_HTML)\\n')
    f.write('print("Synced via update_univote.py")\\n')
print("Synchronized update_univote.py successfully!")

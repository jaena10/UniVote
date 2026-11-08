# -*- coding: utf-8 -*-
"""
UniVote Master Solution Script
Applies all fixes cleanly to templates/studentweb.html and templates/adminweb.html.
"""

import re
import json

DEPARTMENTS_17 = [
    "College of Accountancy",
    "College of Architecture",
    "College of Arts and Sciences (ABComm)",
    "College of Engineering",
    "College of Hospitality Management",
    "College of Human Services",
    "College of Industrial Engineering",
    "College of Information Technology",
    "College of Nursing",
    "College of Pharmacy",
    "College of Psychology",
    "College of Tourism Management",
    "Junior High School",
    "School of Arts and Sciences (Criminology)",
    "School of Business",
    "School of Education",
    "Senior High School"
]

folder_to_dept = {
    'Siklab Party College of Accountancy': 'College of Accountancy',
    'College of Architecture': 'College of Architecture',
    'Siklab Party School of Arts and Sciences (ABCOMM)': 'College of Arts and Sciences (ABComm)',
    'Siklab Party College of Engineering': 'College of Engineering',
    'College of Hospitality  Management': 'College of Hospitality Management',
    'Siklab Party College of Human Services': 'College of Human Services',
    'College of Industrial Engineering': 'College of Industrial Engineering',
    'College of Information Technology': 'College of Information Technology',
    'College of Nursing': 'College of Nursing',
    'College of Pharmacy': 'College of Pharmacy',
    'Siklab Party College of Psychology': 'College of Psychology',
    'Siklab Party College of Tourism Management': 'College of Tourism Management',
    'JuniorHighSchool': 'Junior High School',
    'School of Arts and Sciences (Criminology)': 'School of Arts and Sciences (Criminology)',
    'Siklab Party School of Business': 'School of Business',
    'Siklab Party School of Education': 'School of Education',
    'SeniorHighSchool': 'Senior High School',
}

DEPT_COLORS_17 = [
    {"id": "College of Accountancy", "label": "College of Accountancy", "cardBorder": "border-indigo-200/90", "headerBg": "bg-gradient-to-r from-indigo-50 to-blue-50/70 border-b border-indigo-100", "titleColor": "text-indigo-950", "subColor": "text-indigo-600", "badgeClass": "bg-indigo-100 text-indigo-900 border border-indigo-200", "accentBg": "bg-indigo-50/20", "barColor": "bg-indigo-600", "dot": "bg-indigo-600"},
    {"id": "College of Architecture", "label": "College of Architecture", "cardBorder": "border-amber-200/90", "headerBg": "bg-gradient-to-r from-amber-50 to-orange-50/60 border-b border-amber-100", "titleColor": "text-amber-950", "subColor": "text-amber-700", "badgeClass": "bg-amber-100 text-amber-900 border border-amber-200", "accentBg": "bg-amber-50/20", "barColor": "bg-amber-600", "dot": "bg-amber-600"},
    {"id": "College of Arts and Sciences (ABComm)", "label": "College of Arts and Sciences (ABComm)", "cardBorder": "border-purple-200/90", "headerBg": "bg-gradient-to-r from-purple-50 to-violet-50/60 border-b border-purple-100", "titleColor": "text-purple-950", "subColor": "text-purple-700", "badgeClass": "bg-purple-100 text-purple-900 border border-purple-200", "accentBg": "bg-purple-50/20", "barColor": "bg-purple-600", "dot": "bg-purple-600"},
    {"id": "College of Engineering", "label": "College of Engineering", "cardBorder": "border-blue-200/90", "headerBg": "bg-gradient-to-r from-blue-50 to-indigo-50/60 border-b border-blue-100", "titleColor": "text-blue-950", "subColor": "text-blue-700", "badgeClass": "bg-blue-100 text-blue-900 border border-blue-200", "accentBg": "bg-blue-50/20", "barColor": "bg-blue-600", "dot": "bg-blue-600"},
    {"id": "College of Hospitality Management", "label": "College of Hospitality Management", "cardBorder": "border-emerald-200/90", "headerBg": "bg-gradient-to-r from-emerald-50 to-teal-50/60 border-b border-emerald-100", "titleColor": "text-emerald-950", "subColor": "text-emerald-700", "badgeClass": "bg-emerald-100 text-emerald-900 border border-emerald-200", "accentBg": "bg-emerald-50/20", "barColor": "bg-emerald-600", "dot": "bg-emerald-600"},
    {"id": "College of Human Services", "label": "College of Human Services", "cardBorder": "border-rose-200/90", "headerBg": "bg-gradient-to-r from-rose-50 to-pink-50/60 border-b border-rose-100", "titleColor": "text-rose-950", "subColor": "text-rose-700", "badgeClass": "bg-rose-100 text-rose-900 border border-rose-200", "accentBg": "bg-rose-50/20", "barColor": "bg-rose-600", "dot": "bg-rose-600"},
    {"id": "College of Industrial Engineering", "label": "College of Industrial Engineering", "cardBorder": "border-orange-200/90", "headerBg": "bg-gradient-to-r from-orange-50 to-amber-50/60 border-b border-orange-100", "titleColor": "text-orange-950", "subColor": "text-orange-700", "badgeClass": "bg-orange-100 text-orange-900 border border-orange-200", "accentBg": "bg-orange-50/20", "barColor": "bg-orange-600", "dot": "bg-orange-600"},
    {"id": "College of Information Technology", "label": "College of Information Technology", "cardBorder": "border-sky-300", "headerBg": "bg-gradient-to-r from-sky-50 to-blue-50/60 border-b border-sky-200", "titleColor": "text-sky-950", "subColor": "text-sky-700", "badgeClass": "bg-sky-100 text-sky-900 border border-sky-300", "accentBg": "bg-sky-50/25", "barColor": "bg-sky-600", "dot": "bg-sky-600"},
    {"id": "College of Nursing", "label": "College of Nursing", "cardBorder": "border-red-200/90", "headerBg": "bg-gradient-to-r from-red-50 to-rose-50/60 border-b border-red-100", "titleColor": "text-red-950", "subColor": "text-red-700", "badgeClass": "bg-red-100 text-red-900 border border-red-200", "accentBg": "bg-red-50/20", "barColor": "bg-red-600", "dot": "bg-red-600"},
    {"id": "College of Pharmacy", "label": "College of Pharmacy", "cardBorder": "border-teal-200/90", "headerBg": "bg-gradient-to-r from-teal-50 to-emerald-50/60 border-b border-teal-100", "titleColor": "text-teal-950", "subColor": "text-teal-700", "badgeClass": "bg-teal-100 text-teal-900 border border-teal-200", "accentBg": "bg-teal-50/20", "barColor": "bg-teal-600", "dot": "bg-teal-600"},
    {"id": "College of Psychology", "label": "College of Psychology", "cardBorder": "border-violet-200/90", "headerBg": "bg-gradient-to-r from-violet-50 to-purple-50/60 border-b border-violet-100", "titleColor": "text-violet-950", "subColor": "text-violet-700", "badgeClass": "bg-violet-100 text-violet-900 border border-violet-200", "accentBg": "bg-violet-50/20", "barColor": "bg-violet-600", "dot": "bg-violet-600"},
    {"id": "College of Tourism Management", "label": "College of Tourism Management", "cardBorder": "border-cyan-200/90", "headerBg": "bg-gradient-to-r from-cyan-50 to-blue-50/60 border-b border-cyan-100", "titleColor": "text-cyan-950", "subColor": "text-cyan-700", "badgeClass": "bg-cyan-100 text-cyan-900 border border-cyan-200", "accentBg": "bg-cyan-50/20", "barColor": "bg-cyan-600", "dot": "bg-cyan-600"},
    {"id": "Junior High School", "label": "Junior High School", "cardBorder": "border-slate-300", "headerBg": "bg-gradient-to-r from-slate-100 to-blue-50/60 border-b border-slate-200", "titleColor": "text-slate-900", "subColor": "text-slate-600", "badgeClass": "bg-slate-200 text-slate-800 border border-slate-300", "accentBg": "bg-slate-50/20", "barColor": "bg-slate-600", "dot": "bg-slate-600"},
    {"id": "School of Arts and Sciences (Criminology)", "label": "School of Arts and Sciences (Criminology)", "cardBorder": "border-stone-300", "headerBg": "bg-gradient-to-r from-stone-100 to-amber-50/60 border-b border-stone-200", "titleColor": "text-stone-900", "subColor": "text-stone-600", "badgeClass": "bg-stone-200 text-stone-800 border border-stone-300", "accentBg": "bg-stone-50/20", "barColor": "bg-stone-700", "dot": "bg-stone-700"},
    {"id": "School of Business", "label": "School of Business", "cardBorder": "border-blue-300", "headerBg": "bg-gradient-to-r from-blue-50 to-sky-50/60 border-b border-blue-200", "titleColor": "text-blue-950", "subColor": "text-blue-700", "badgeClass": "bg-blue-100 text-blue-900 border border-blue-300", "accentBg": "bg-blue-50/20", "barColor": "bg-blue-600", "dot": "bg-blue-600"},
    {"id": "School of Education", "label": "School of Education", "cardBorder": "border-emerald-300", "headerBg": "bg-gradient-to-r from-emerald-50 to-green-50/60 border-b border-emerald-200", "titleColor": "text-emerald-950", "subColor": "text-emerald-700", "badgeClass": "bg-emerald-100 text-emerald-900 border border-emerald-300", "accentBg": "bg-emerald-50/20", "barColor": "bg-emerald-600", "dot": "bg-emerald-600"},
    {"id": "Senior High School", "label": "Senior High School", "cardBorder": "border-yellow-300", "headerBg": "bg-gradient-to-r from-yellow-50 to-amber-50/60 border-b border-yellow-200", "titleColor": "text-yellow-950", "subColor": "text-yellow-700", "badgeClass": "bg-yellow-100 text-yellow-900 border border-yellow-300", "accentBg": "bg-yellow-50/20", "barColor": "bg-amber-600", "dot": "bg-amber-600"},
]

print("Department metadata prepared.")

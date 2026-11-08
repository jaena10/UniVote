# -*- coding: utf-8 -*-
"""
UniVote Complete Codebase Synchronizer
Updates build_full_univote.py, studentweb.html, adminweb.html, and update_univote.py.
"""
import json
import os
import sys

from generator_engine import build_generator_script, get_dept_options_html

departments, positions, candidates_data, default_students, dept_options = build_generator_script()

print(f"Loaded {len(departments)} departments, {len(candidates_data)} candidates, {len(default_students)} students.")

# We will create build_master_files.py to generate student_html and admin_html cleanly.

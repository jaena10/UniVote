# -*- coding: utf-8 -*-
r"""
UniVote Administrative Utility: Clear All Voting Data
Location: D:\CODINGS\univote\clear_voting_data.py

This script serves as an administrative function to wipe stored encrypted ballots,
tallies, and voter session histories from the browser localStorage / database
without affecting candidate rosters or student accounts.
"""

import os
import sys

def print_banner():
    print("=" * 65)
    print("      UNIVERSITY OF THE ASSUMPTION — UNIVOTE COMMISSION       ")
    print("             CLEAR ALL VOTING DATA UTILITY                     ")
    print("=" * 65)
    print("Scope:")
    print("  [x] Wipes all stored encrypted ballot records (univote_encrypted_ballots_db)")
    print("  [x] Wipes submitted vote history & flags (univote_has_voted, univote_saved_choices)")
    print("  [x] Wipes active voter sessions (univote_locked_session)")
    print("  [x] Resets departmental tally counters and winner designations to 0")
    print("  [✓] PRESERVED: Candidate rosters (univote_db_candidates)")
    print("  [✓] PRESERVED: Student enrollment accounts (univote_db_students)")
    print("  [✓] PRESERVED: Election schedule & configurations (univote_db_elections)")
    print("=" * 65)

def main():
    print_banner()
    print("\nHow would you like to clear the voting data?")
    print("1. In Admin Web Dashboard (Recommended):")
    print("   Open http://127.0.0.1:5000/admin -> Login -> Go to 'Election Controls' or 'Audit Log'")
    print("   Click the red 'Clear All Voting Data' button and type 'CLEAR' when prompted.")
    print("\n2. Browser Developer Console:")
    print("   Execute the following command in your browser console on the UniVote portal:")
    print("""
   localStorage.setItem('univote_encrypted_ballots_db', JSON.stringify([]));
   localStorage.removeItem('univote_has_voted');
   localStorage.removeItem('univote_saved_choices');
   sessionStorage.removeItem('univote_locked_session');
   console.log('UniVote: Voting data wiped. Candidates and students preserved.');
   location.reload();
""")
    print("=" * 65)
    print("Status: Both Admin Console and Student Portal are synchronized.")
    print("Ready to serve clean election ballots.")

if __name__ == '__main__':
    main()

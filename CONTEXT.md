# UniVote — Project Context & Architecture
**Last Updated**: 2026-11-08 18:48 PHT  
**Institution**: University of the Assumption (UA Pampanga)  
**Working Directory**: `D:\CODINGS\univote`  
**Server Command**: `python server.py` → Port `5000`

| Portal | URL |
|---|---|
| Student Voting Portal | http://127.0.0.1:5000/ |
| Admin Console | http://127.0.0.1:5000/admin |
| Admin Credentials | Username: `admin` / Password: `ua2026admin` |

---

## 1. File Structure
```
D:\CODINGS\univote\
├── server.py                   # Python HTTP server routing / and /admin on port 5000
├── build_full_univote.py       # Master generator — run to rebuild both HTML files
├── update_univote.py           # Synchronized runner (synced by build_full_univote.py)
├── clear_voting_data.py        # Administrative CLI data wipe utility
├── CONTEXT.md                  # This file
├── ua-logo.png                 # Official University of the Assumption Seal Logo
└── templates\
    ├── studentweb.html         # Student Voting Portal (DO NOT edit directly)
    ├── adminweb.html           # Admin Console (DO NOT edit directly)
    └── ua-logo.png             # Official Seal Logo
```
> Always edit `build_full_univote.py` then run `python build_full_univote.py` to regenerate templates.

---

## 2. Academic Departments (10 Total — Exact Names, No Abbreviations)

| # | Department Name | Admin Card Color |
|---|---|---|
| 1 | College of Accountancy | Indigo |
| 2 | College of Engineering and Architecture | Amber |
| 3 | College of Hospitality and Tourism Management | Emerald |
| 4 | College of Nursing and Pharmacy | Rose |
| 5 | School of Arts and Sciences | Purple |
| 6 | School of Business and Public Administration | Sky Blue |
| 7 | School of Education | Teal |
| 8 | College of Information Technology | Blue |
| 9 | Senior High School | Orange |
| 10 | Junior High School | Cyan |

---

## 3. Student Council Positions (6 Races Per Department)
`pres` President · `vp` Vice President · `sec` Secretary · `tres` Treasurer · `aud` Auditor · `pro` PRO

---

## 4. Candidate Seed Data
- **Total**: 215 verified candidates across all academic departments
- **Asset Folders**: Real candidate portraits with format `Name (Position).png`
- **Party-list Affiliation Rules**:
  - `SIKLAB`: Alyansang Siklab party-list across participating collegiate faculties and UACSC
  - `Independent`: Automatically enforced for College of Architecture, College of Industrial Engineering, College of Information Technology, College of Nursing, College of Pharmacy, and School of Arts and Sciences (Criminology)
  - Zero duplicate photos and zero placeholder candidate names
- **Data Version Stamp**: `univote_v5_2026_11_08` — forces automatic localStorage candidate reseed on page load

---

## 5. Seed Test Students
| Student ID | Name | Department |
|---|---|---|
| 2024000669 | Maria Clara T. Santos | College of Accountancy |
| 2023001244 | Juan Dela T. Cruz | College of Engineering and Architecture |
| 2024001882 | Camille Rose P. Diaz | College of Hospitality and Tourism Management |
| 2024006843 | Jaena B. Mangulabnan | College of Nursing and Pharmacy |
| 2023004490 | Beatriz Nicole L. Gomez | School of Arts and Sciences |
| 2022009831 | Sofia Bianca R. Dizon | School of Business and Public Administration |
| 2024003319 | Mark Anthony V. Ramos | School of Education |
| 2024001155 | Angelo G. Gomez | College of Information Technology |
| 2024005576 | Jaenaganda M. Cruz | Senior High School |
| 2024008812 | Joshua L. Garcia | Junior High School |

> Default test password: `Password@2026` (SHA-256: `85750059f33b118b6e6c278064c519d08ba2ff23ef983818e69818ce3eb64f7b`)

---

## 6. Administrative Functions
- **Clear All Voting Data**:
  - Accessible via Admin Dashboard Section 4 & Section 5 danger control
  - Or via `python clear_voting_data.py`
  - Wipes `univote_encrypted_ballots_db`, `univote_has_voted`, `univote_saved_choices`, and active session
  - Strictly preserves candidate profiles (`univote_db_candidates`) and student enrollment rosters (`univote_db_students`)

---

## 7. Dynamic Digital Voting Receipt & QR Code
- Automatic display upon casting 6/6 complete ballot
- Contains voting timestamp, student ID, full name, institutional email, department, and token
- Lists all 6 selected candidates with official party badges
- Displays AES-256 encrypted audit trail cipher
- Generates permanent scannable QR Code (QRCode.js CDN + QR Server fallback)
- Features 1-click **Print Receipt** and **Download Receipt** card functions

---

## 6. Registration Validation Rules
- **Student ID**: 10 digits, year 2010–2026
- **Email**: `initials + lastname.student@ua.edu.ph` (e.g. `jdtcruz.student@ua.edu.ph`)
- **Password**: Min 8 chars, must include `* _ + @ # !`, rejects common words, name/ID patterns

### Duplicate Prevention (4 Strict Guards — no overwrite)
1. **Student ID** already registered → blocked
2. **Full Name** already registered → blocked (case-insensitive)
3. **Email** already linked → blocked
4. **Password hash** already used by another account → blocked

---

## 7. Voting — Strict 6/6 Complete Ballot
- Must select all 6 positions before submit button enables
- Position tabs show `✓` / `0/1` real-time indicators
- Both `openReviewModal()` and `submitBallot()` enforce the 6/6 guard

---

## 8. UI Architecture
- 3 fully separate modals: `#signInModal` (auto-closes on login) · `#registerModal` · `#regSuccessModal`
- Password show/hide toggle on all password fields
- Top locked banner (`#lockedAccountBanner`) removed after login
- UA Life / ads / promotional banners removed

---

## 9. Admin Console
- Soft pastel per-department card headers, leading candidate bar in gold `amber-500`
- Sections: Live Tallies · Student Management · Candidate Management · Election Settings · Audit Registry
- Exact unabbreviated department names everywhere

# UniVote — Project Context & Architecture
**Last Updated**: 2026-11-09 00:22 PHT  
**Institution**: University of the Assumption (UA Pampanga)  
**Working Directory**: `D:\CODINGS\univote`  
**GitHub Repository**: [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)  
**Render Deployment**: Configured via `render.yaml` (Free Tier)  

| Portal | URL | Description |
|---|---|---|
| Student Voting Portal | `http://127.0.0.1:5000/` | Student voting, candidate directory, partylists, results |
| Admin Management Console | `http://127.0.0.1:5000/admin` | Live tallies, winners by department, clear voting data, roster |
| Health Check Endpoint | `http://127.0.0.1:5000/healthz` | Zero-downtime healthcheck endpoint for Render |
| Default Admin Credentials | Username: `admin` / Password: `ua2026admin` | UA Election Commission administrative credentials |

---

## 1. Project File Structure
```
D:\CODINGS\univote\
├── server.py                   # High-performance multi-threaded Python HTTP server (Render ready)
├── app.py                      # Alternative Flask WSGI backend
├── render.yaml                 # Render Infrastructure-as-Code Blueprint configuration (Free Tier)
├── Dockerfile                  # Containerized deployment specification (python:3.11-slim)
├── requirements.txt            # Python dependencies (Standard Library native)
├── .gitignore                  # Git ignore rules (__pycache__, temporary caches, etc.)
├── CONTEXT.md                  # Comprehensive project context & architecture documentation
├── ua-logo.png                 # Official University of the Assumption Seal Logo
├── static/
│   ├── css/
│   │   ├── student.css         # Custom student styling
│   │   └── admin.css           # Custom admin console styling
│   └── ua-logo.png             # Static branding asset
├── templates/
│   ├── studentweb.html         # Complete Student Voting Portal with Browsing Mode
│   └── adminweb.html           # Administrator Console with per-dept buttons & Clear All
├── College of Architecture/    # Candidate portrait directory
├── College of Hospitality  Management/
├── College of Industrial Engineering/
├── College of Information Technology/
├── College of Nursing/
├── College of Pharmacy/
├── JuniorHighSchool/
├── School of Arts and Sciences (Criminology)/
├── SeniorHighSchool/
├── Siklab Party College of Accountancy/
├── Siklab Party College of Engineering/
├── Siklab Party College of Human Services/
├── Siklab Party College of Psychology/
├── Siklab Party College of Tourism Management/
├── Siklab Party School of Arts and Sciences (ABCOMM)/
├── Siklab Party School of Business/
├── Siklab Party School of Education/
└── UACSC Officers under Siklab/ # University Central Student Council candidates
```

---

## 2. Academic Departments (17 Total — Alphabetical Order)
All 17 university departments are strictly organized in alphabetical order across registration dropdowns, student filters, and admin tally selector buttons:

| # | Department Name | Student Council Status |
|---|---|---|
| 1 | College of Accountancy | 6 Positions Active |
| 2 | College of Architecture | 6 Positions Active |
| 3 | College of Arts and Sciences (ABComm) | 6 Positions Active |
| 4 | College of Engineering | 6 Positions Active |
| 5 | College of Hospitality Management | 6 Positions Active |
| 6 | College of Human Services | 6 Positions Active |
| 7 | College of Industrial Engineering | 6 Positions Active |
| 8 | College of Information Technology | 6 Positions Active |
| 9 | College of Nursing | 6 Positions Active |
| 10 | College of Pharmacy | 6 Positions Active |
| 11 | College of Psychology | 6 Positions Active |
| 12 | College of Tourism Management | 6 Positions Active |
| 13 | Junior High School | 6 Positions Active |
| 14 | School of Arts and Sciences (Criminology) | 6 Positions Active |
| 15 | School of Business | 6 Positions Active |
| 16 | School of Education | 6 Positions Active |
| 17 | Senior High School | 6 Positions Active |

---

## 3. Council Positions (6 Races Per Department)
Every department features the standard student council slate:
1. `pres` — President
2. `vp` — Vice President
3. `sec` — Secretary
4. `tres` — Treasurer
5. `aud` — Auditor
6. `pro` — Public Relations Officer (PRO)

---

## 4. Student Portal Workflow & Security Architecture

### A. Browsing Mode First (No Auto-Voting)
* **Zero Pre-Selection**: `selectedChoices` is initialized as `{}` (completely empty) upon opening the website, signing in, or registering. No candidate is ever automatically pre-selected.
* **Browsing Banner**: Upon sign-in, students land in **Browsing Mode**. A banner welcomes them, informs them of their department, and displays a prominent **"Start Voting"** button.
* **Uncluttered UI**: The bottom ballot review bar is hidden during Browsing Mode so students can comfortably read candidate platforms, view partylists, and check certified results without distraction.
* **Transition to Voting Mode**: Clicking **"Start Voting"** (or selecting any candidate) transitions the student into active voting mode, unhiding the bottom action bar with `0 of 6 Selected`.

### B. Per-Student Vote Tracking
* Votes are tracked per individual student ID (`univote_voted_student_ids`).
* A student is only locked as "Ballot Already Cast" if their specific student account has submitted a ballot.
* Other students on the same computer/browser start with an empty ballot.

### C. Strict 6/6 Ballot Enforcement
* Ballots can only be reviewed and submitted once all 6 council positions are selected.
* Modals display exact selections before final confirmation.
* Submission signs the ballot using **AES-256** and saves it to the encrypted audit log.
* Generates a digital receipt featuring an immutable scannable QR Code, Print, and Download card actions.

### D. Registration Validation Rules
* **Student ID**: Strictly 10 digits with admission years between 2010 and 2026.
* **Email Format**: Must follow institutional format `initials + lastname.student@ua.edu.ph`.
* **Password Complexity**: Minimum 8 characters, requiring at least one special character (`* _ + @ # !`), rejecting sequential keys and common dictionary patterns.
* **4 Duplicate Guards**: Rejects duplicate Student ID, duplicate Full Name, duplicate Institutional Email, and duplicate Password Hash.

---

## 5. Admin Management Console Architecture

### A. Department Winners & Tallies by Button
* Displays all 17 departments as individual filter buttons in alphabetical order.
* Clicking any department button isolates and displays only that department's winners, candidate vote tallies, percentage share, and lead indicators across all 6 positions.
* Avoids overwhelming the administrator by not displaying all departments simultaneously.

### B. Reliable "Clear All Voting Data"
* Accessible right on the **Department Winners & Tallies** action header as well as in the **Election Settings** Danger Zone.
* Uses a reliable native `confirm()` dialog with clear explanation (no typing friction).
* Thoroughly wipes:
  1. `univote_encrypted_ballots_db` (resets to `[]`)
  2. `univote_voted_student_ids` (resets to `[]`)
  3. `univote_has_voted`, `univote_saved_choices`, and all per-student vote keys
  4. Active student voter sessions
  5. Broadcasts `univote_reset_signal` so open student tabs reset in real-time
* Strictly preserves candidate rosters (`univote_db_candidates`) and student enrollment records (`univote_db_students`).

---

## 6. Technology Stack Overview

### Frontend
* **HTML5**: Semantic template structure for student and admin web portals.
* **JavaScript (ES6+)**: Core client-side business logic, reactive state, cryptography, and real-time computation.
* **CSS3**: Layout styling, `@media print` print-sheet optimization for digital receipts, custom scrollbars.
* **Tailwind CSS (v3)**: Utility-first CSS framework configured with custom UA brand colors (Navy `#020381`, Royal Blue `#1e3a8a`, Gold `#d97706`).
* **CryptoJS**: **AES-256** ballot encryption and **SHA-256** voter token and password hashing.
* **QRCode.js**: Scannable verification QR code generation.
* **Canvas Confetti**: Celebratory particle effects upon successful ballot casting.
* **Lucide Icons**: Comprehensive SVG icon set.

### Backend & DevOps
* **Python 3 (3.11+)**: Primary backend language.
* **`http.server.ThreadingHTTPServer`**: Multi-threaded concurrent HTTP request handling.
* **Flask**: Secondary WSGI backend (`app.py`).
* **Render YAML (`render.yaml`)**: Infrastructure-as-Code Blueprint for zero-cost free service deployment.
* **Dockerfile**: Containerized definition for standardized container environments.
* **Git & GitHub**: Version control and CI/CD repository at `https://github.com/jaena10/UniVote.git`.

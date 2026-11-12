# UniVote — Project Context & Architecture
**Last Updated**: 2026-11-12 22:36 PHT  
**Institution**: University of the Assumption (UA Pampanga)  
**Working Directory**: `D:\CODINGS\univote`  
**GitHub Repository**: [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)  
**Render Deployment**: Configured via `render.yaml` (Free Tier)  

| Portal | URL | Description |
|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|
| Student Voting Portal | `http://127.0.0.1:5000/` | Student voting, candidate directory, partylists, results |
| Admin Management Console | `http://127.0.0.1:5000/admin` | Live tallies, winners by department, clear voting data, roster |
| Health Check Endpoint | `http://127.0.0.1:5000/healthz` | Zero-downtime healthcheck endpoint for Render |
| Default Admin Credentials | Username: `admin` / Password: `ua2026admin` | UA Election Commission administrative credentials |

---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

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

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---

## 2. Academic Departments (17 Total — Alphabetical Order)
All 17 university departments are strictly organized in alphabetical order across registration dropdowns, student filters, and admin tally selector buttons:

| # | Department Name | Student Council Status |
|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---|
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

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

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

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

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

### C. Strict Ballot Completion, Universal "Abstain" Option & AES-256 Cryptographic Digital Receipt Card
* **Universal "Abstain" Button & Option Card**: Every election contest (Central Student Council / UACSC, all 17 department councils, Senior High School, Junior High School, and student organization elections) provides an explicit **"Abstain"** button in each race header and a dedicated **"Abstain from Voting"** card in the candidate grid. Students can choose to formally abstain from any position. Selecting Abstain satisfies the ballot completion requirement for that race.
* **Strict Complete Ballot Guard**: Ballots can only be reviewed and submitted once all eligible positions are decided (either by choosing a candidate or electing to abstain).
* **Review Modal**: Groups and previews exact candidate selections and formal abstentions for both Central Council (UACSC) and Department Council before final confirmation.
* **AES-256 Audit Signing**: Submission encrypts and signs the ballot using **AES-256** and records it to the cryptographic database, preserving both candidate votes and formal abstentions.
* **Streamlined Digital Receipt Card (PNG & Modal)**:
  * Contains official University of the Assumption branding and header, verification status badge, exact voting timestamp, academic department, and verified student credentials (ID, voter name, institutional email, voter token).
  * Lists all official recorded candidate choices and formal abstentions across all contested positions.
  * Bottom section features the authenticated **AES-256 AUDIT TRAIL CIPHER PAYLOAD** displaying the full cipher payload.
  * Omit scannable QR block and legacy security disclaimer texts for a clean, professional, and audit-ready receipt card.
* **Downloadable & Printable Digital Receipt Card**:
  1. **Download Card (PNG)**: Renders the high-resolution branded digital receipt card with official UA seal, student info, candidate table, and AES-256 cipher payload to HTML5 Canvas and exports `UniVote_Receipt_Card_[StudentID].png`.
  2. **Audit File (.txt)**: Downloads certified text audit log `UniVote_Receipt_[StudentID].txt`.
  3. **Print Receipt**: Uses optimized `@media print` styling to print an official paper voting receipt sheet.

### D. Registration Validation Rules
* **Student ID**: Strictly 10 digits with admission years between 2010 and 2026.
* **Email Format**: Must follow institutional format `initials + lastname.student@ua.edu.ph`.
* **Password Complexity**: Minimum 8 characters, requiring at least one special character (`* _ + @ # !`), rejecting sequential keys and common dictionary patterns.
* **4 Duplicate Guards**: Rejects duplicate Student ID, duplicate Full Name, duplicate Institutional Email, and duplicate Password Hash.

---

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

---

## 5. Admin Management Console Architecture

### A. Department Winners & Central Council Tallies by Button
* Displays **⭐ Central Student Council (UACSC)** along with all 17 departments as individual filter buttons.
* Clicking **⭐ Central Student Council (UACSC)** tallies and highlights winners for UACSC positions across all ballots cast university-wide.
* Clicking any department button isolates and displays that department's winners, candidate vote tallies, percentage share, lead indicators, and formal abstention counts across all positions.
* Avoids overwhelming the administrator by displaying clean, focused council tallies on demand.

### B. Student Management Full Records Display
* Displays authentic student enrollment records across all departments with full student names (e.g., *Maria Clara T. Santos*, *Juan Carlos D. Dela Cruz*) instead of academic program labels.
* Automatic data migration seamlessly upgrades legacy records to proper student names.

### C. Student Bulk Deletion ("Delete All")
* Accessible via the **"Delete All"** button on the Student Management roster toolbar.
* Equipped with a **Safety Confirmation Modal** requiring explicit `DELETE ALL` confirmation typing to prevent accidental data loss.
* Wipes `univote_db_students` to `[]`, invalidates active student sessions via `univote_reset_signal`, and maintains a clean zero-record state without auto-reseeding defaults.
* Dispatches a call to the backend API endpoint (`POST /api/admin/delete-all-students`) implemented in both [`server.py`](file:///D:/CODINGS/univote/server.py) and [`app.py`](file:///D:/CODINGS/univote/app.py).
* Strictly preserves candidate databases and cast ballot audit records.

### D. Reliable "Clear All Voting Data"
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

## 7. Changelog — Session History

### 2026-11-12 (Session)
**Feature Added: Universal Abstain Button**
- Added formal **"Abstain"** option to **every election race** across the entire UniVote system:
  - ✅ Central Student Council (UACSC) — all positions
  - ✅ All 17 departmental elections — all positions
  - ✅ Senior High School elections — all positions
  - ✅ Junior High School elections — all positions
  - ✅ Student organization elections (year reps, chairpersons, etc.)
- **Files Modified**:
  - `templates/studentweb.html` — Abstain UI cards, header buttons, review modal, receipt modal, PNG canvas, .txt audit
  - `templates/adminweb.html` — `abstainCounts` tally tracking, Formal Abstention row per position card
  - `CONTEXT.md` — Architecture documentation updated
- **Commit**: `9d006c4` pushed to `main` on [https://github.com/jaena10/UniVote.git](https://github.com/jaena10/UniVote.git)
- **Key implementation details**:
  - `selectedChoices[raceId] = 'ABSTAIN'` — sentinel value for abstentions in ballot payload
  - Abstain satisfies ballot completion count — enables "Review & Cast" when all races decided
  - `buildTalliesForDept` in adminweb splits `abstainCounts[posId]` from `candVoteCounts[candId]`
  - Race key parsing: `uacsc_<posId>` → UACSC abstain; `dept_<posId>` → Department abstain
  - All receipt outputs (modal, PNG, .txt) display abstentions cleanly with `⊘` icon and `ABSTAIN` label
  - Results page (student portal) shows Abstain row with vote count and grey progress bar per position

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

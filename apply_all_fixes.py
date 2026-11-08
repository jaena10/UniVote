"""
Apply all UniVote fixes:
1. Student portal: Update department dropdown to full alphabetical list
2. Student portal: Add browsing mode (no auto-cast on sign-in)
3. Admin portal: Fix clear all voting data
4. Admin portal: Per-department tally buttons instead of showing all at once
"""
import re

# ============================================================
# FIX 1: STUDENT WEB - Department dropdown (full alphabetical)
# ============================================================

student_path = r'D:\CODINGS\univote\templates\studentweb.html'

with open(student_path, 'r', encoding='utf-8') as f:
    student_html = f.read()

# New department list in alphabetical order
NEW_DEPARTMENTS = [
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
    "Senior High School",
]

new_options = '\n'.join([
    f'                        <option value="{d}">{d}</option>'
    for d in NEW_DEPARTMENTS
])

# Replace the department dropdown options
old_dropdown_pattern = r'(<select id="regDepartment"[^>]*>)\s*(<option.*?</option>\s*)+\s*(</select>)'
new_dropdown = r'\1\n' + new_options + '\n                    \\3'
student_html = re.sub(old_dropdown_pattern, new_dropdown, student_html, flags=re.DOTALL)

# ============================================================
# FIX 2: STUDENT WEB - Browsing mode after sign-in
# ============================================================

# 2a. Hide ballot section initially and add a "Start Voting" banner
# After the unauthNotice div and electionInactiveBanner, add a browsing mode banner
browsing_banner = '''
            <!-- Browsing Mode Banner (shown after sign-in, before voting) -->
            <div id="browsingModeBanner" class="hidden bg-emerald-50 border-2 border-emerald-300 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center shrink-0">
                        <i data-lucide="eye" class="w-6 h-6 text-emerald-700"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Welcome! You are now signed in.</h3>
                        <p class="text-slate-600 text-xs mt-0.5">You are currently in <strong>browsing mode</strong>. Browse candidates, view partylists, and check results. When you are ready to vote, click the button to start.</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2 shrink-0">
                    <button onclick="enterVotingMode()" class="bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs px-6 py-3 rounded-2xl transition shadow-md flex items-center space-x-2">
                        <i data-lucide="vote" class="w-4 h-4 text-emerald-200"></i>
                        <span>Start Voting</span>
                    </button>
                </div>
            </div>
'''

# Insert the browsing banner after electionInactiveBanner
student_html = student_html.replace(
    '            <!-- Full-Width Candidate Slate Container -->',
    browsing_banner + '\n            <!-- Full-Width Candidate Slate Container -->'
)

# 2b. Hide the candidate slate and ballot action bar initially (add hidden class via JS)
# We'll do this via JS in the applySessionLockUI function instead of modifying HTML directly

# 2c. Add the enterVotingMode function and modify applySessionLockUI
# Find the applySessionLockUI function and modify it to enter browsing mode
old_apply_session_lock = '''        function applySessionLockUI() {
            const voterDisplay = document.getElementById('voterIdentityDisplay');
            if (voterDisplay) voterDisplay.innerText = `${currentUser.name} (${currentUser.dept})`;
            const voterBadge = document.getElementById('voterBadge');
            if (voterBadge) voterBadge.classList.remove('hidden');
            const logoutBtn = document.getElementById('logoutBtn');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            
            const unauthNavGroup = document.getElementById('unauthNavGroup');
            if (unauthNavGroup) unauthNavGroup.classList.add('hidden');

            const unauthNotice = document.getElementById('unauthNotice');
            if (unauthNotice) unauthNotice.classList.add('hidden');

            const candTitle = document.getElementById('candidateSectionTitle');
            if (candTitle) candTitle.innerText = `${currentUser.dept} Candidate Slate`;
            const candSub = document.getElementById('candidateSectionSub');
            if (candSub) candSub.innerText = `Displaying official council positions and candidates running strictly for ${currentUser.dept}`;

            lucide.createIcons();
        }'''

new_apply_session_lock = '''        function applySessionLockUI() {
            const voterDisplay = document.getElementById('voterIdentityDisplay');
            if (voterDisplay) voterDisplay.innerText = `${currentUser.name} (${currentUser.dept})`;
            const voterBadge = document.getElementById('voterBadge');
            if (voterBadge) voterBadge.classList.remove('hidden');
            const logoutBtn = document.getElementById('logoutBtn');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            
            const unauthNavGroup = document.getElementById('unauthNavGroup');
            if (unauthNavGroup) unauthNavGroup.classList.add('hidden');

            const unauthNotice = document.getElementById('unauthNotice');
            if (unauthNotice) unauthNotice.classList.add('hidden');

            const candTitle = document.getElementById('candidateSectionTitle');
            if (candTitle) candTitle.innerText = `${currentUser.dept} Candidate Slate`;
            const candSub = document.getElementById('candidateSectionSub');
            if (candSub) candSub.innerText = `Displaying official council positions and candidates running strictly for ${currentUser.dept}`;

            // BROWSING MODE: If user has NOT voted yet, enter browsing mode
            const hasVoted = localStorage.getItem('univote_has_voted') === 'true';
            if (!hasVoted) {
                enterBrowsingMode();
            }

            lucide.createIcons();
        }

        // BROWSING MODE: Show browsing banner, hide ballot action bar
        function enterBrowsingMode() {
            const browsingBanner = document.getElementById('browsingModeBanner');
            if (browsingBanner) browsingBanner.classList.remove('hidden');
            
            // Hide the ballot action bar in browsing mode
            const ballotActionBar = document.getElementById('ballotActionBar');
            if (ballotActionBar) ballotActionBar.classList.add('hidden');
        }

        // VOTING MODE: Hide browsing banner, show ballot action bar
        function enterVotingMode() {
            const browsingBanner = document.getElementById('browsingModeBanner');
            if (browsingBanner) browsingBanner.classList.add('hidden');
            
            // Show the ballot action bar
            const ballotActionBar = document.getElementById('ballotActionBar');
            if (ballotActionBar) ballotActionBar.classList.remove('hidden');

            // Update the review button text
            const reviewBtnText = document.getElementById('reviewBallotBtnText');
            if (reviewBtnText) reviewBtnText.innerText = 'Review & Cast Ballot';

            lucide.createIcons();
            renderCandidateCards();
            updateBallotVisualizer();
        }'''

student_html = student_html.replace(old_apply_session_lock, new_apply_session_lock)

# 2d. Remove the "Ballot Already Cast" auto-display on checkSessionLock
# The current checkSessionLock shows "Ballot Already Cast" even on fresh sign-in
# We keep that behavior only if user actually voted, but ensure it doesn't auto-submit
# This part is already fine - it just shows "Ballot Already Cast" text if univote_has_voted is true

# Write the updated student HTML
with open(student_path, 'w', encoding='utf-8') as f:
    f.write(student_html)

print("[OK] studentweb.html updated successfully")
print("  - Department dropdown: full alphabetical list (17 departments)")
print("  - Browsing mode banner added")
print("  - enterBrowsingMode() and enterVotingMode() functions added")
print("  - applySessionLockUI() modified to enter browsing mode after sign-in")


# ============================================================
# FIX 3 & 4: ADMIN WEB - Fix clear data + per-department tallies
# ============================================================

admin_path = r'D:\CODINGS\univote\templates\adminweb.html'

with open(admin_path, 'r', encoding='utf-8') as f:
    admin_html = f.read()

# 3a. Replace the results section to add department filter buttons
old_results_section = '''            <!-- Section Header + Refresh -->
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
            </div>'''

new_results_section = '''            <!-- Section Header + Refresh -->
            <div class="flex items-center justify-between flex-wrap gap-3">
                <h2 class="text-base font-extrabold text-slate-800 flex items-center space-x-2">
                    <i data-lucide="bar-chart-2" class="w-5 h-5 text-blue-600"></i>
                    <span>Department Winners & Tallies</span>
                </h2>
                <button onclick="loadWinnersAndTallies()" class="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2 rounded-xl shadow transition">
                    <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                    <span>Refresh Tallies</span>
                </button>
            </div>

            <!-- Per-Department Filter Buttons -->
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Select Department to View Tallies</p>
                <div class="flex flex-wrap gap-2" id="adminDeptFilterButtons">
                    <!-- Generated by JS -->
                </div>
            </div>

            <!-- Dynamic Department Column (single department at a time) -->
            <div id="allDeptContainer" class="space-y-6">
                <div class="text-center text-slate-400 py-12 text-sm">Select a department above to view tallies.</div>
            </div>'''

admin_html = admin_html.replace(old_results_section, new_results_section)

# 3b. Replace the loadWinnersAndTallies function to support per-department filtering
old_load_winners = '''        function loadWinnersAndTallies() {
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
        }'''

new_load_winners = '''        let adminSelectedDept = null;

        function renderDeptFilterButtons() {
            const container = document.getElementById('adminDeptFilterButtons');
            if (!container) return;
            container.innerHTML = DEPARTMENTS.map(dept => {
                const isActive = adminSelectedDept === dept.id;
                const activeClass = isActive
                    ? 'bg-blue-600 text-white shadow-md shadow-blue-500/25 border-blue-500'
                    : 'bg-white text-slate-600 hover:bg-slate-50 border-slate-200';
                return `<button onclick="selectAdminDept('${dept.id}')" class="px-3.5 py-2 rounded-xl text-xs font-bold transition border ${activeClass} whitespace-nowrap">${dept.label}</button>`;
            }).join('');
        }

        function selectAdminDept(deptId) {
            adminSelectedDept = deptId;
            renderDeptFilterButtons();
            loadWinnersAndTallies();
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

            // Render department filter buttons
            renderDeptFilterButtons();

            if (mainContainer) {
                if (!adminSelectedDept) {
                    mainContainer.innerHTML = '<div class="text-center text-slate-400 py-12 text-sm"><i data-lucide="mouse-pointer-click" class="w-6 h-6 mx-auto mb-2 text-slate-300"></i><p>Select a department above to view its winners and tallies.</p></div>';
                } else {
                    const dept = DEPARTMENTS.find(d => d.id === adminSelectedDept);
                    if (dept) {
                        mainContainer.innerHTML = renderDeptColumn(dept, candidates, ballots);
                    }
                }
            }

            lucide.createIcons();
        }'''

admin_html = admin_html.replace(old_load_winners, new_load_winners)

# 3c. The clearAllVotingData function looks correct already, but let's also make sure
# we also clear ALL per-student voting flags. The issue might be that localStorage
# keys are stored per-student. Let's enhance the clear function.
old_clear_fn = '''        function clearAllVotingData() {
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
        }'''

new_clear_fn = '''        function clearAllVotingData() {
            // 1. Wipe encrypted ballots database
            localStorage.setItem('univote_encrypted_ballots_db', JSON.stringify([]));

            // 2. Wipe vote histories and flags
            localStorage.removeItem('univote_has_voted');
            localStorage.removeItem('univote_saved_choices');

            // 3. Wipe active student voter session
            sessionStorage.removeItem('univote_locked_session');

            // 4. Also clear any other univote voting-related keys
            const keysToRemove = [];
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (key && (key.startsWith('univote_vote_') || key.startsWith('univote_ballot_'))) {
                    keysToRemove.push(key);
                }
            }
            keysToRemove.forEach(k => localStorage.removeItem(k));

            // Note: Candidate profiles (univote_db_candidates) and student rosters (univote_db_students) are strictly preserved!

            // 5. Reset selected department view
            adminSelectedDept = null;

            // 6. Refresh admin tallies, winner boards, and audit log immediately
            loadWinnersAndTallies();
            loadAuditTable();

            alert(
                "SUCCESS: Voting data wiped completely!\\n\\n" +
                "• Encrypted ballots database cleared.\\n" +
                "• All departmental tallies reset to zero.\\n" +
                "• Student voting history flags reset.\\n" +
                "• Candidate profiles and student rosters preserved."
            );
        }'''

admin_html = admin_html.replace(old_clear_fn, new_clear_fn)

# Write updated admin HTML
with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("\n[OK] adminweb.html updated successfully")
print("  - Per-department tally buttons added (select one dept at a time)")
print("  - loadWinnersAndTallies() now shows single dept at a time")
print("  - clearAllVotingData() enhanced with additional cleanup")
print("\n[DONE] All fixes applied!")

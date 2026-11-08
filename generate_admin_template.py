# -*- coding: utf-8 -*-
"""
Generates adminweb.html content for UniVote.
"""

def generate_admin_html_code(dept_options_html):
    return f'''
def generate_admin_html():
    return \'\'\'<!DOCTYPE html>
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
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: [\'Plus Jakarta Sans\', \'sans-serif\'] }},
                    colors: {{ ua: {{ navy: \'#020381\', royal: \'#1e3a8a\', gold: \'#d97706\' }} }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-slate-100 text-slate-800 flex flex-col min-h-screen font-sans selection:bg-blue-900 selection:text-white">

    <!-- TOP ADMIN HEADER -->
    <header class="bg-slate-900 text-white sticky top-0 z-40 border-b border-slate-800 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex items-center space-x-3.5">
                    <img src="/templates/ua-logo.png" alt="University Seal" class="w-12 h-12 object-contain" onerror="this.onerror=null; this.src=\'/static/ua-logo.png\';">
                    <div>
                        <div class="flex items-center space-x-2">
                            <span class="font-extrabold text-2xl tracking-tight text-white">UniVote</span>
                            <span class="bg-blue-600 text-white text-[10px] font-black px-2.5 py-0.5 rounded-full uppercase tracking-wider">Admin Console</span>
                        </div>
                        <p class="text-xs text-slate-400">Institutional Election Commission &amp; Central Registry</p>
                    </div>
                </div>

                <div class="flex items-center space-x-4">
                    <div class="hidden sm:flex items-center space-x-2 bg-slate-800/80 px-3 py-1.5 rounded-xl border border-slate-700 text-xs">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        <span class="font-mono text-slate-300">ADMIN: COMMISSIONER ACTIVE</span>
                    </div>
                    <button type="button" onclick="handleAdminLogout()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-rose-600/80 hover:text-white text-slate-300 font-bold text-xs transition border border-slate-700 flex items-center space-x-1.5">
                        <i data-lucide="log-out" class="w-4 h-4"></i>
                        <span>Exit</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- ADMIN WORKSPACE BAR -->
    <div class="bg-white border-b border-slate-200 sticky top-20 z-30 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center space-x-2 overflow-x-auto py-2.5 no-scrollbar">
                <button type="button" onclick="switchAdminSection(\'results\')" id="tab-btn-results" class="admin-tab-btn px-4 py-2 rounded-xl text-xs font-bold transition flex items-center space-x-2 bg-blue-600 text-white shadow-md shadow-blue-500/25">
                    <i data-lucide="bar-chart-2" class="w-4 h-4"></i>
                    <span>Department Winners &amp; Tallies</span>
                </button>
                <button type="button" onclick="switchAdminSection(\'students\')" id="tab-btn-students" class="admin-tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition flex items-center space-x-2">
                    <i data-lucide="users" class="w-4 h-4"></i>
                    <span>Student Roster</span>
                </button>
                <button type="button" onclick="switchAdminSection(\'candidates\')" id="tab-btn-candidates" class="admin-tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition flex items-center space-x-2">
                    <i data-lucide="user-check" class="w-4 h-4"></i>
                    <span>Candidate Registry</span>
                </button>
                <button type="button" onclick="switchAdminSection(\'elections\')" id="tab-btn-elections" class="admin-tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition flex items-center space-x-2">
                    <i data-lucide="sliders" class="w-4 h-4"></i>
                    <span>Election Controls</span>
                </button>
                <button type="button" onclick="switchAdminSection(\'audit\')" id="tab-btn-audit" class="admin-tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 transition flex items-center space-x-2">
                    <i data-lucide="shield-check" class="w-4 h-4"></i>
                    <span>Encrypted Audit Log</span>
                </button>
            </div>
        </div>
    </div>

    <!-- MAIN ADMIN CONTENT -->
    <main class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-grow">

        <!-- ================= SECTION 1: DEPARTMENT WINNERS & TALLIES ================= -->
        <div id="admin-section-results" class="admin-section space-y-6">
            
            <!-- Top Controls & Action Bar -->
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                <div>
                    <h2 class="text-xl font-black text-slate-900">Department Winners &amp; Live Tallies</h2>
                    <p class="text-xs text-slate-500">Official encrypted ballot counts and real-time winner designations by department</p>
                </div>
                <div class="flex items-center space-x-2.5">
                    <button type="button" onclick="loadWinnersAndTallies()" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow transition flex items-center space-x-1.5">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                        <span>Refresh Tallies</span>
                    </button>
                    <button type="button" onclick="openClearDataModal()" class="bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow transition flex items-center space-x-1.5">
                        <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                        <span>Clear All Voting Data</span>
                    </button>
                </div>
            </div>

            <!-- Stats Overview Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-5">
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center font-bold">
                        <i data-lucide="archive" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <span class="text-xs text-slate-400 font-bold uppercase tracking-wider block">Total Encrypted Ballots</span>
                        <span id="statTotalBallots" class="text-2xl font-black text-slate-900">0</span>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
                        <i data-lucide="user-check" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <span class="text-xs text-slate-400 font-bold uppercase tracking-wider block">Official Candidates</span>
                        <span id="statTotalCandidates" class="text-2xl font-black text-slate-900">215</span>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
                        <i data-lucide="globe" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <span class="text-xs text-slate-400 font-bold uppercase tracking-wider block">Publication Status</span>
                        <span id="statPublicationBadge" class="text-sm font-black text-emerald-600">Published to Students</span>
                    </div>
                </div>
            </div>

            <!-- DEPARTMENT SELECTOR BUTTON BAR (17 Buttons in Alphabetical Order) -->
            <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3.5">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <div class="w-7 h-7 rounded-lg bg-ua-navy text-white flex items-center justify-center">
                            <i data-lucide="layers" class="w-4 h-4"></i>
                        </div>
                        <h3 class="font-extrabold text-sm text-slate-900">Select Academic Department (17 Total):</h3>
                    </div>
                    <span class="text-[11px] font-semibold text-slate-500">Click a department button to view its winners &amp; race tallies</span>
                </div>

                <!-- 17 Department Buttons -->
                <div id="adminDeptButtonsBar" class="flex flex-wrap gap-2 pt-1">
                    <!-- Dynamic Buttons Generated in loadWinnersAndTallies() -->
                </div>
            </div>

            <!-- SINGLE DEPARTMENT WINNERS & TALLIES DISPLAY CONTAINER -->
            <div id="singleDeptContainer" class="space-y-6">
                <!-- Rendered dynamically by renderSingleDeptView() -->
            </div>

        </div>

        <!-- ================= SECTION 2: STUDENT ENROLLMENT ROSTER ================= -->
        <div id="admin-section-students" class="admin-section hidden space-y-6">
            <div class="flex justify-between items-center bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                <div>
                    <h2 class="text-xl font-black text-slate-900">Student Enrollment Roster</h2>
                    <p class="text-xs text-slate-500">Official student registry and voter verification management</p>
                </div>
                <button type="button" onclick="openStudentModal()" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow transition flex items-center space-x-1.5">
                    <i data-lucide="user-plus" class="w-4 h-4"></i>
                    <span>Enroll Student</span>
                </button>
            </div>

            <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-slate-50 border-b font-extrabold text-slate-500 uppercase tracking-wider">
                            <tr>
                                <th class="p-4">Student ID</th>
                                <th class="p-4">Full Legal Name</th>
                                <th class="p-4">Institutional Email</th>
                                <th class="p-4">Department</th>
                                <th class="p-4">Status</th>
                                <th class="p-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="studentTableBody" class="divide-y divide-slate-100 font-medium">
                            <!-- Dynamic Students -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= SECTION 3: CANDIDATE REGISTRY ================= -->
        <div id="admin-section-candidates" class="admin-section hidden space-y-6">
            <div class="flex justify-between items-center bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                <div>
                    <h2 class="text-xl font-black text-slate-900">Candidate Registry</h2>
                    <p class="text-xs text-slate-500">Registered candidate profiles, positions, and affiliations</p>
                </div>
                <button type="button" onclick="openCandidateModal()" class="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow transition flex items-center space-x-1.5">
                    <i data-lucide="plus" class="w-4 h-4"></i>
                    <span>Add Candidate</span>
                </button>
            </div>

            <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-slate-50 border-b font-extrabold text-slate-500 uppercase tracking-wider">
                            <tr>
                                <th class="p-4">Photo</th>
                                <th class="p-4">Candidate Name</th>
                                <th class="p-4">Position</th>
                                <th class="p-4">Party List</th>
                                <th class="p-4">Department</th>
                                <th class="p-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="candidateTableBody" class="divide-y divide-slate-100 font-medium">
                            <!-- Dynamic Candidates -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= SECTION 4: ELECTION CONTROLS ================= -->
        <div id="admin-section-elections" class="admin-section hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-6">
                <div>
                    <h2 class="text-xl font-black text-slate-900">Election Configuration &amp; Schedule</h2>
                    <p class="text-xs text-slate-500">Manage voting windows, publication rules, and administrative controls</p>
                </div>

                <form id="electionConfigForm" onsubmit="handleSaveElection(event)" class="space-y-4 max-w-xl text-xs">
                    <div>
                        <label class="block font-bold text-slate-700 mb-1">Official Election Title *</label>
                        <input type="text" id="elecTitle" required class="w-full px-4 py-2.5 border rounded-xl font-semibold">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block font-bold text-slate-700 mb-1">Start Date *</label>
                            <input type="date" id="elecStart" required class="w-full px-4 py-2.5 border rounded-xl">
                        </div>
                        <div>
                            <label class="block font-bold text-slate-700 mb-1">End Date *</label>
                            <input type="date" id="elecEnd" required class="w-full px-4 py-2.5 border rounded-xl">
                        </div>
                    </div>
                    <div class="space-y-3 pt-2">
                        <label class="flex items-center space-x-2">
                            <input type="checkbox" id="elecActive" class="w-4 h-4 rounded text-blue-600 focus:ring-blue-500">
                            <span class="font-bold text-slate-800">Voting Portal Active (Allows student ballot submissions)</span>
                        </label>
                        <label class="flex items-center space-x-2">
                            <input type="checkbox" id="elecPublished" class="w-4 h-4 rounded text-blue-600 focus:ring-blue-500">
                            <span class="font-bold text-slate-800">Publish Tallies to Students (Unseals public live results)</span>
                        </label>
                    </div>
                    <button type="submit" class="px-5 py-2.5 rounded-xl bg-ua-navy hover:bg-blue-800 text-white font-bold transition shadow-sm">
                        Save Election Configuration
                    </button>
                </form>

                <!-- DANGER ZONE: CLEAR ALL VOTING DATA -->
                <div class="mt-8 pt-6 border-t border-rose-200">
                    <div class="p-5 rounded-2xl bg-rose-50/80 border border-rose-300 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                        <div class="space-y-1">
                            <div class="flex items-center space-x-2">
                                <div class="w-7 h-7 rounded-lg bg-rose-100 text-rose-700 flex items-center justify-center shrink-0">
                                    <i data-lucide="alert-octagon" class="w-4 h-4"></i>
                                </div>
                                <h4 class="font-extrabold text-sm text-rose-900">Administrative Danger Zone: Clear All Voting Data</h4>
                            </div>
                            <p class="text-xs text-rose-700 max-w-xl leading-relaxed">
                                Completely wipes all stored encrypted ballot databases, live voter tallies, submitted vote history, and active sessions. Candidate profiles and student enrollment rosters are strictly preserved.
                            </p>
                        </div>
                        <button type="button" onclick="openClearDataModal()" class="px-5 py-3 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-black text-xs transition shadow-md flex items-center space-x-2 shrink-0">
                            <i data-lucide="trash-2" class="w-4 h-4"></i>
                            <span>Clear All Voting Data</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- ================= SECTION 5: AUDIT LOG ================= -->
        <div id="admin-section-audit" class="admin-section hidden space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 class="text-xl font-black text-slate-900">Cryptographic Audit Trail</h2>
                    <p class="text-xs text-slate-500">Raw AES-256 encrypted voter payloads and verification tokens</p>
                </div>
                <button type="button" onclick="openClearDataModal()" class="px-4 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs transition shadow-sm flex items-center space-x-1.5 shrink-0">
                    <i data-lucide="trash-2" class="w-4 h-4"></i>
                    <span>Wipe All Ballot Data</span>
                </button>
            </div>

            <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs font-mono">
                        <thead class="bg-slate-50 border-b font-sans font-bold text-slate-500 uppercase">
                            <tr>
                                <th class="p-4">Timestamp</th>
                                <th class="p-4">Voter Token</th>
                                <th class="p-4">Department</th>
                                <th class="p-4">Encrypted Cipher Payload (AES-256)</th>
                            </tr>
                        </thead>
                        <tbody id="encryptedBallotsTableBody" class="divide-y divide-slate-100">
                            <!-- Dynamic Encrypted Ballots -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </main>

    <!-- ================= MODALS ================= -->

    <!-- DEDICATED CLEAR ALL VOTING DATA CONFIRMATION MODAL -->
    <div id="clearVotingDataModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 border border-rose-200 shadow-2xl relative">
            <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-rose-100 text-rose-700 flex items-center justify-center shrink-0 shadow-inner">
                    <i data-lucide="alert-octagon" class="w-6 h-6"></i>
                </div>
                <div>
                    <h3 class="font-extrabold text-slate-900 text-base">Clear All Voting Data</h3>
                    <p class="text-xs text-rose-600 font-semibold">Institutional Election Data Wipe</p>
                </div>
            </div>

            <p class="text-xs text-slate-600 leading-relaxed">
                Are you sure you want to completely wipe all voting data? This administrative reset action will:
            </p>

            <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 text-xs text-slate-600 space-y-1.5">
                <p class="font-bold text-slate-800">Scope of Action:</p>
                <div class="space-y-1 text-[11px]">
                    <div class="flex items-center space-x-1.5 text-rose-700">
                        <i data-lucide="trash" class="w-3.5 h-3.5"></i>
                        <span>Wipes all encrypted ballots database (univote_encrypted_ballots_db)</span>
                    </div>
                    <div class="flex items-center space-x-1.5 text-rose-700">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                        <span>Resets all departmental tallies and leaderboards to zero</span>
                    </div>
                    <div class="flex items-center space-x-1.5 text-rose-700">
                        <i data-lucide="unlock" class="w-3.5 h-3.5"></i>
                        <span>Clears student vote submission histories (allows students to vote anew)</span>
                    </div>
                    <div class="flex items-center space-x-1.5 text-emerald-700 font-bold">
                        <i data-lucide="check" class="w-3.5 h-3.5"></i>
                        <span>Strictly preserves candidate profiles and student enrollment accounts</span>
                    </div>
                </div>
            </div>

            <div class="flex items-center justify-end space-x-2 pt-2 border-t">
                <button type="button" onclick="closeClearDataModal()" class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-50 font-bold text-xs transition">
                    Cancel
                </button>
                <button type="button" onclick="executeClearAllVotingData()" class="px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-extrabold text-xs transition shadow-md flex items-center space-x-1.5">
                    <i data-lucide="trash-2" class="w-4 h-4"></i>
                    <span>Yes, Clear All Voting Data</span>
                </button>
            </div>
        </div>
    </div>

    <!-- STUDENT MODAL -->
    <div id="studentModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 shadow-2xl border border-slate-200">
            <h3 id="studentModalTitle" class="text-base font-extrabold text-slate-900">Enroll Student</h3>
            <form id="formAdminStudent" onsubmit="handleSaveStudent(event)" class="space-y-3 text-xs">
                <input type="hidden" id="modalStudentOriginalId">
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Student ID (10 digits) *</label>
                    <input type="text" id="modalStudentId" required placeholder="2024000669" class="w-full px-4 py-2 border rounded-xl font-mono">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Legal Full Name *</label>
                    <input type="text" id="modalStudentName" required placeholder="Maria Clara T. Santos" class="w-full px-4 py-2 border rounded-xl font-semibold">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">UA Institutional Email *</label>
                    <input type="email" id="modalStudentEmail" required placeholder="mctsantos.student@ua.edu.ph" class="w-full px-4 py-2 border rounded-xl">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Academic Department *</label>
                    <select id="modalStudentDept" required class="w-full px-4 py-2 border rounded-xl bg-white font-medium">
{dept_options_html}
                    </select>
                </div>
                <div class="flex items-center space-x-2 pt-1">
                    <input type="checkbox" id="modalStudentVerified" class="w-4 h-4 rounded text-blue-600">
                    <label for="modalStudentVerified" class="font-bold text-slate-700">Verified Enrollment Status</label>
                </div>
                <div class="flex justify-end space-x-2 pt-3 border-t">
                    <button type="button" onclick="closeStudentModal()" class="px-4 py-2 border rounded-xl font-bold">Cancel</button>
                    <button type="submit" class="px-5 py-2 bg-emerald-600 text-white rounded-xl font-bold shadow">Save Student</button>
                </div>
            </form>
        </div>
    </div>

    <!-- CANDIDATE MODAL -->
    <div id="candidateModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 shadow-2xl border border-slate-200">
            <h3 id="candidateModalTitle" class="text-base font-extrabold text-slate-900">Add Candidate</h3>
            <form id="formAdminCandidate" onsubmit="handleSaveCandidate(event)" class="space-y-3 text-xs">
                <input type="hidden" id="modalCandId">
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Candidate Legal Name *</label>
                    <input type="text" id="modalCandName" required class="w-full px-4 py-2 border rounded-xl font-bold">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Council Position *</label>
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
                    <label class="block font-bold text-slate-700 mb-1">Party List Affiliation *</label>
                    <input type="text" id="modalCandParty" required placeholder="SIKLAB or Independent" class="w-full px-4 py-2 border rounded-xl font-semibold">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Academic Department *</label>
                    <select id="modalCandDept" required class="w-full px-4 py-2 border rounded-xl bg-white font-medium">
{dept_options_html}
                    </select>
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Photo Path *</label>
                    <input type="text" id="modalCandPhoto" required placeholder="/templates/ua-logo.png" class="w-full px-4 py-2 border rounded-xl font-mono text-[11px]">
                </div>
                <div class="flex justify-end space-x-2 pt-3 border-t">
                    <button type="button" onclick="closeCandidateModal()" class="px-4 py-2 border rounded-xl font-bold">Cancel</button>
                    <button type="submit" class="px-5 py-2 bg-blue-600 text-white rounded-xl font-bold shadow">Save Profile</button>
                </div>
            </form>
        </div>
    </div>

    <!-- ADMIN LOGIN MODAL -->
    <div id="adminLoginModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-sm w-full p-6 text-center space-y-5 shadow-2xl border border-slate-200">
            <div class="w-14 h-14 rounded-2xl bg-slate-900 text-white mx-auto flex items-center justify-center shadow-md">
                <i data-lucide="shield" class="w-8 h-8 text-amber-400"></i>
            </div>
            <div>
                <h3 class="text-xl font-extrabold text-slate-900">Administrator Login</h3>
                <p class="text-xs text-slate-500 mt-1">UniVote Election Commission Terminal</p>
            </div>
            <div id="loginErrorMsg" class="hidden text-xs bg-rose-50 text-rose-700 p-3 rounded-xl border border-rose-200 font-bold"></div>
            <form onsubmit="handleAdminLogin(event)" class="space-y-3.5 text-xs text-left">
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Username</label>
                    <input type="text" id="adminUsername" required value="admin" class="w-full px-4 py-2.5 border rounded-xl font-semibold">
                </div>
                <div>
                    <label class="block font-bold text-slate-700 mb-1">Password</label>
                    <input type="password" id="adminPassword" required value="ua2026admin" class="w-full px-4 py-2.5 border rounded-xl font-mono">
                </div>
                <button type="submit" class="w-full bg-slate-900 hover:bg-black text-white font-bold py-3 rounded-xl transition shadow-md">
                    Access Console
                </button>
            </form>
        </div>
    </div>

    <!-- ADMIN SCRIPTS -->
    <script>
        const AES_SECRET_KEY = \'UniVote-UA-2026\';

        // 17 Academic Departments in Alphabetical Order
        const DEPARTMENTS = [
            {{ id: \'College of Accountancy\', label: \'College of Accountancy\', color: \'indigo\' }},
            {{ id: \'College of Architecture\', label: \'College of Architecture\', color: \'amber\' }},
            {{ id: \'College of Arts and Sciences (ABCOMM)\', label: \'College of Arts and Sciences (ABCOMM)\', color: \'purple\' }},
            {{ id: \'College of Engineering\', label: \'College of Engineering\', color: \'blue\' }},
            {{ id: \'College of Hospitality Management\', label: \'College of Hospitality Management\', color: \'emerald\' }},
            {{ id: \'College of Human Services\', label: \'College of Human Services\', color: \'rose\' }},
            {{ id: \'College of Industrial Engineering\', label: \'College of Industrial Engineering\', color: \'orange\' }},
            {{ id: \'College of Information Technology\', label: \'College of Information Technology\', color: \'sky\' }},
            {{ id: \'College of Nursing\', label: \'College of Nursing\', color: \'teal\' }},
            {{ id: \'College of Pharmacy\', label: \'College of Pharmacy\', color: \'violet\' }},
            {{ id: \'College of Psychology\', label: \'College of Psychology\', color: \'fuchsia\' }},
            {{ id: \'College of Tourism Management\', label: \'College of Tourism Management\', color: \'cyan\' }},
            {{ id: \'Junior Highschool\', label: \'Junior Highschool\', color: \'slate\' }},
            {{ id: \'School of Arts and Sciences (Criminology)\', label: \'School of Arts and Sciences (Criminology)\', color: \'red\' }},
            {{ id: \'School of Business\', label: \'School of Business\', color: \'amber\' }},
            {{ id: \'School of Education\', label: \'School of Education\', color: \'teal\' }},
            {{ id: \'Senior Highschool\', label: \'Senior Highschool\', color: \'emerald\' }}
        ];

        const POSITIONS = [
            {{ id: \'pres\', name: \'President\' }},
            {{ id: \'vp\', name: \'Vice President\' }},
            {{ id: \'sec\', name: \'Secretary\' }},
            {{ id: \'tres\', name: \'Treasurer\' }},
            {{ id: \'aud\', name: \'Auditor\' }},
            {{ id: \'pro\', name: \'Public Relations Officer (PRO)\' }}
        ];

        // Active Selected Department for Section 1 View (Defaults to first department)
        let activeAdminDeptId = \'College of Accountancy\';

        function normalizeDept(name) {{
            if (!name) return \'\';
            let n = name.trim();
            if (n === \'Junior High School\') return \'Junior Highschool\';
            if (n === \'Senior High School\') return \'Senior Highschool\';
            if (n.toLowerCase() === \'college of hospitality managemet\') return \'College of Hospitality Management\';
            return n;
        }}

        document.addEventListener(\'DOMContentLoaded\', () => {{
            lucide.createIcons();
            checkAdminAuth();
            loadWinnersAndTallies();
            loadStudentTable();
            loadCandidateTable();
            loadElectionConfig();
            loadAuditTable();
        }});

        function checkAdminAuth() {{
            const modal = document.getElementById(\'adminLoginModal\');
            if (sessionStorage.getItem(\'univote_admin_authenticated\') === \'true\') {{
                if (modal) modal.classList.add(\'hidden\');
            }} else {{
                if (modal) modal.classList.remove(\'hidden\');
            }}
        }}

        function handleAdminLogin(e) {{
            if (e && e.preventDefault) e.preventDefault();
            const u = document.getElementById(\'adminUsername\').value.trim();
            const p = document.getElementById(\'adminPassword\').value.trim();
            const errEl = document.getElementById(\'loginErrorMsg\');

            if (u === \'admin\' && p === \'ua2026admin\') {{
                sessionStorage.setItem(\'univote_admin_authenticated\', \'true\');
                const modal = document.getElementById(\'adminLoginModal\');
                if (modal) modal.classList.add(\'hidden\');
                if (errEl) errEl.classList.add(\'hidden\');
            }} else {{
                if (errEl) {{
                    errEl.textContent = "Invalid Administrator credentials!";
                    errEl.classList.remove(\'hidden\');
                }} else {{
                    alert("Invalid Administrator credentials!");
                }}
            }}
        }}

        function handleAdminLogout() {{
            sessionStorage.removeItem(\'univote_admin_authenticated\');
            location.reload();
        }}

        function switchAdminSection(sectionKey) {{
            document.querySelectorAll(\'.admin-section\').forEach(e => e.classList.add(\'hidden\'));
            document.querySelectorAll(\'.admin-tab-btn\').forEach(e => {{
                e.classList.remove(\'bg-blue-600\', \'bg-blue-700\', \'text-white\', \'shadow-md\', \'shadow-blue-500/25\');
                e.classList.add(\'text-slate-600\');
            }});

            const sec = document.getElementById(`admin-section-${{sectionKey}}`);
            const btn = document.getElementById(`tab-btn-${{sectionKey}}`);
            if (sec) sec.classList.remove(\'hidden\');
            if (btn) {{
                btn.classList.add(\'bg-blue-600\', \'text-white\', \'shadow-md\', \'shadow-blue-500/25\');
                btn.classList.remove(\'text-slate-600\');
            }}
            lucide.createIcons();
        }}

        function getCandidateParty(c) {{
            if (!c) return \'Independent\';
            const dept = (c.dept || c.targetDept || \'\').toLowerCase();
            const photo = (c.photo || \'\').toLowerCase();
            
            if (
                dept.includes(\'architecture\') ||
                dept.includes(\'industrial engineering\') ||
                dept.includes(\'information technology\') ||
                dept.includes(\'nursing\') ||
                dept.includes(\'pharmacy\') ||
                dept.includes(\'criminology\') ||
                photo.includes(\'college of architecture\') ||
                photo.includes(\'college of industrial engineering\') ||
                photo.includes(\'college of information technology\') ||
                photo.includes(\'college of nursing\') ||
                photo.includes(\'college of pharmacy\') ||
                photo.includes(\'criminology\')
            ) {{
                return \'Independent\';
            }}

            if (c.party && c.party.trim() !== \'\') {{
                const p = c.party.trim();
                if (p.toLowerCase() === \'siklab\' || p.toLowerCase().includes(\'siklab\')) {{
                    return \'SIKLAB\';
                }}
                return p;
            }}
            return \'Independent\';
        }}

        // ================= CLEAR ALL VOTING DATA =================
        function openClearDataModal() {{
            document.getElementById(\'clearVotingDataModal\').classList.remove(\'hidden\');
            lucide.createIcons();
        }}

        function closeClearDataModal() {{
            document.getElementById(\'clearVotingDataModal\').classList.add(\'hidden\');
        }}

        function confirmClearAllVotingData() {{
            openClearDataModal();
        }}

        function executeClearAllVotingData() {{
            // 1. Wipe encrypted ballots database
            localStorage.setItem(\'univote_encrypted_ballots_db\', JSON.stringify([]));

            // 2. Wipe vote histories and flags
            localStorage.setItem(\'univote_voted_students\', JSON.stringify({{}}));
            localStorage.setItem(\'univote_student_choices\', JSON.stringify({{}}));
            localStorage.removeItem(\'univote_has_voted\');
            localStorage.removeItem(\'univote_saved_choices\');

            // 3. Wipe active student voter session
            sessionStorage.removeItem(\'univote_locked_session\');

            // 4. Reset any hasVoted flags in student roster
            const students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            let updated = false;
            students.forEach(s => {{
                if (s.hasVoted) {{ s.hasVoted = false; updated = true; }}
            }});
            if (updated) {{
                localStorage.setItem(\'univote_db_students\', JSON.stringify(students));
            }}

            // 5. Broadcast real-time wipe to any open studentweb tabs
            localStorage.setItem(\'univote_voting_reset_trigger\', Date.now().toString());

            closeClearDataModal();

            // 6. Refresh admin tallies, winner boards, and audit log immediately
            loadWinnersAndTallies();
            loadAuditTable();
            loadStudentTable();

            alert(
                "SUCCESS: Voting data wiped completely!\\n\\n" +
                "• All encrypted ballots cleared.\\n" +
                "• All departmental tallies reset to zero.\\n" +
                "• Student voting history flags reset.\\n" +
                "• Candidate profiles and student rosters preserved."
            );
        }}

        // ================= DEPARTMENT WINNERS & TALLIES (BUTTON-BY-DEPARTMENT) =================
        function buildTalliesForDept(ballots, deptId) {{
            const tallies = {{}};
            const target = normalizeDept(deptId);
            const deptBallots = ballots.filter(b => normalizeDept(b.department) === target);
            
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
            return {{ tallies, deptBallots }};
        }}

        function switchAdminDept(deptId) {{
            activeAdminDeptId = deptId;
            loadWinnersAndTallies();
        }}

        function loadWinnersAndTallies() {{
            const statTotal = document.getElementById(\'statTotalBallots\');
            const statCands = document.getElementById(\'statTotalCandidates\');
            const badge = document.getElementById(\'statPublicationBadge\');

            const ballots = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\')) || [];
            const candidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || [];
            const students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const elec = JSON.parse(localStorage.getItem(\'univote_db_elections\')) || {{ published: false }};

            if (statTotal) statTotal.textContent = ballots.length;
            if (statCands) statCands.textContent = candidates.length;
            if (badge) {{
                if (elec.published) {{
                    badge.textContent = \'Published to Students\';
                    badge.className = \'text-sm font-black text-emerald-600\';
                }} else {{
                    badge.textContent = \'Sealed / Private\';
                    badge.className = \'text-sm font-black text-amber-600\';
                }}
            }}

            // Render the 17 Department Buttons
            renderDepartmentButtons(ballots);

            // Render Single Selected Department
            renderSingleDepartmentView(activeAdminDeptId, candidates, ballots, students);

            lucide.createIcons();
        }}

        function renderDepartmentButtons(ballots) {{
            const bar = document.getElementById(\'adminDeptButtonsBar\');
            if (!bar) return;

            // Compute vote counts for all 17 departments
            const counts = {{}};
            ballots.forEach(b => {{
                const d = normalizeDept(b.department);
                counts[d] = (counts[d] || 0) + 1;
            }});

            bar.innerHTML = DEPARTMENTS.map(dept => {{
                const isActive = (dept.id === activeAdminDeptId);
                const count = counts[normalizeDept(dept.id)] || 0;

                return `
                    <button 
                        type="button" 
                        onclick="switchAdminDept(\'${{dept.id}}\')" 
                        class="px-3.5 py-2 rounded-xl text-xs font-bold transition flex items-center space-x-2 shrink-0 ${{
                            isActive 
                                ? \'bg-ua-navy text-white shadow-md ring-2 ring-ua-navy ring-offset-2 ring-offset-white font-extrabold\' 
                                : \'bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 shadow-sm\'
                        }}">
                        <span>${{dept.label}}</span>
                        <span class="text-[10px] px-2 py-0.5 rounded-full font-black ${{
                            isActive 
                                ? \'bg-white/20 text-white\' 
                                : (count > 0 ? \'bg-blue-100 text-blue-900\' : \'bg-slate-100 text-slate-400\')
                        }}">
                            ${{count}} vote${{count === 1 ? \'\' : \'s\'}}
                        </span>
                    </button>
                `;
            }}).join(\'\');
        }}

        function renderSingleDepartmentView(deptId, candidates, ballots, students) {{
            const container = document.getElementById(\'singleDeptContainer\');
            if (!container) return;

            const deptObj = DEPARTMENTS.find(d => d.id === deptId) || DEPARTMENTS[0];
            const target = normalizeDept(deptObj.id);

            const { tallies, deptBallots } = buildTalliesForDept(ballots, deptObj.id);
            const totalDeptVotes = deptBallots.length;

            const deptCandidates = candidates.filter(c => normalizeDept(c.targetDept) === target);
            const deptStudents = students.filter(s => normalizeDept(s.dept) === target);
            const turnoutPct = deptStudents.length > 0 ? ((totalDeptVotes / deptStudents.length) * 100).toFixed(1) : \'0.0\';

            // Find leaders/winners for each position in this department
            const winners = [];
            POSITIONS.forEach(pos => {{
                const posCands = deptCandidates.filter(c => c.posId === pos.id);
                if (posCands.length > 0) {{
                    let maxVotes = -1;
                    let leader = null;
                    posCands.forEach(c => {{
                        const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                        if (count > maxVotes) {{
                            maxVotes = count;
                            leader = c;
                        }}
                    }});
                    if (leader) {{
                        winners.push({{ pos, candidate: leader, votes: Math.max(0, maxVotes) }});
                    }}
                }}
            }});

            let html = `
                <!-- Department Overview Card -->
                <div class="bg-gradient-to-r from-slate-900 to-blue-950 text-white rounded-3xl p-6 sm:p-8 shadow-xl relative overflow-hidden">
                    <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div>
                            <div class="inline-flex items-center space-x-2 bg-white/10 px-3 py-1 rounded-full text-xs font-semibold mb-2 border border-white/20">
                                <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-amber-300"></i>
                                <span>Official Department Slate</span>
                            </div>
                            <h2 class="text-2xl sm:text-3xl font-black tracking-tight">${{deptObj.label}}</h2>
                            <p class="text-xs text-blue-200 mt-1">Official real-time race tallies, voter turnout, and winning designations</p>
                        </div>
                        <div class="flex items-center space-x-4 bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/15">
                            <div class="text-center px-2">
                                <span class="text-[10px] text-blue-200 font-bold uppercase block">Ballots Cast</span>
                                <span class="text-2xl font-black text-amber-300">${{totalDeptVotes}}</span>
                            </div>
                            <div class="h-8 w-px bg-white/20"></div>
                            <div class="text-center px-2">
                                <span class="text-[10px] text-blue-200 font-bold uppercase block">Enrolled Voters</span>
                                <span class="text-2xl font-black text-white">${{deptStudents.length}}</span>
                            </div>
                            <div class="h-8 w-px bg-white/20"></div>
                            <div class="text-center px-2">
                                <span class="text-[10px] text-blue-200 font-bold uppercase block">Voter Turnout</span>
                                <span class="text-2xl font-black text-emerald-400">${{turnoutPct}}%</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- COUNCIL WINNERS / LEADERS SHOWCASE -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                    <div class="flex items-center justify-between border-b pb-3">
                        <div class="flex items-center space-x-2">
                            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center font-bold">
                                <i data-lucide="award" class="w-4 h-4"></i>
                            </div>
                            <h3 class="font-black text-sm text-slate-900">Current Council Leadership &amp; Race Leaders (${{deptObj.label}})</h3>
                        </div>
                        <span class="text-[10px] font-bold text-slate-400">Determined by live encrypted vote count</span>
                    </div>

                    ${{winners.length === 0 ? `
                        <div class="text-center py-8 text-slate-400 text-xs">No registered candidates for this department.</div>
                    ` : `
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
                            ${{winners.map(w => `
                                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3 text-center space-y-2 hover:shadow-md transition">
                                    <span class="text-[9px] font-black uppercase tracking-wider text-slate-400 block">${{w.pos.name}}</span>
                                    <div class="relative w-14 h-14 mx-auto">
                                        <img src="${{w.candidate.photo || \'/templates/ua-logo.png\'}}" class="w-14 h-14 rounded-xl object-cover border border-slate-200 shadow-sm" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                        <span class="absolute -top-1.5 -right-1.5 bg-amber-500 text-white text-[9px] font-black px-1.5 py-0.2 rounded-full shadow">#1</span>
                                    </div>
                                    <div>
                                        <h4 class="font-extrabold text-xs text-slate-900 truncate">${{w.candidate.name}}</h4>
                                        <p class="text-[10px] font-bold text-blue-700">${{getCandidateParty(w.candidate)}}</p>
                                    </div>
                                    <div class="pt-1 border-t border-slate-200 text-xs font-black text-slate-800">
                                        ${{w.votes}} vote${{w.votes === 1 ? \'\' : \'s\'}}
                                    </div>
                                </div>
                            `).join(\'\')}}
                        </div>
                    `}}
                </div>

                <!-- POSITION-BY-POSITION DETAILED TALLIES -->
                <div class="space-y-4">
                    <div class="flex items-center space-x-2">
                        <div class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold">
                            <i data-lucide="list-ordered" class="w-4 h-4"></i>
                        </div>
                        <h3 class="font-black text-sm text-slate-900">Comprehensive Race-by-Race Tallies (${{deptObj.label}})</h3>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            `;

            POSITIONS.forEach(pos => {{
                const posCands = deptCandidates.filter(c => c.posId === pos.id);
                if (posCands.length === 0) return;

                let maxVotes = 0;
                let leaderId = null;
                posCands.forEach(c => {{
                    const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                    if (count > maxVotes) {{
                        maxVotes = count;
                        leaderId = c.id;
                    }}
                }});

                html += `
                    <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-sm hover:border-slate-300 transition">
                        <div class="flex items-center justify-between border-b pb-2.5">
                            <h4 class="font-black text-xs text-slate-900 uppercase tracking-wider">${{pos.name}}</h4>
                            <span class="text-[10px] font-bold text-slate-400 bg-slate-50 px-2 py-0.5 rounded-full border">${{posCands.length}} Cand.</span>
                        </div>
                        <div class="space-y-2.5">
                            ${{posCands.map(c => {{
                                const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                                const pct = totalDeptVotes > 0 ? ((count / totalDeptVotes) * 100).toFixed(1) : \'0.0\';
                                const isLead = c.id === leaderId && count > 0;
                                return `
                                    <div class="rounded-xl border ${{isLead ? \'border-amber-300 bg-amber-50/60\' : \'border-slate-100 bg-slate-50\'}} p-3 space-y-1.5">
                                        <div class="flex items-center justify-between">
                                            <div class="flex items-center space-x-2 truncate">
                                                <img src="${{c.photo || \'/templates/ua-logo.png\'}}" class="w-7 h-7 rounded-lg object-cover border shrink-0" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                                <div class="min-w-0">
                                                    <div class="flex items-center space-x-1">
                                                        <h5 class="font-extrabold text-xs text-slate-900 truncate">${{c.name}}</h5>
                                                        ${{isLead ? \'<span class="bg-amber-500 text-white font-black text-[8px] px-1.5 py-0.2 rounded-full uppercase">LEAD</span>\' : \'\'}}
                                                    </div>
                                                    <p class="text-[10px] font-semibold text-blue-600 truncate">${{getCandidateParty(c)}}</p>
                                                </div>
                                            </div>
                                            <div class="text-right shrink-0 ml-2">
                                                <span class="text-sm font-black text-slate-900">${{count}}</span>
                                                <span class="text-[10px] text-slate-400 font-bold block">${{pct}}%</span>
                                            </div>
                                        </div>
                                        <div class="w-full bg-slate-200 rounded-full h-1.5 overflow-hidden">
                                            <div class="bg-blue-600 h-1.5 rounded-full" style="width: ${{pct}}%"></div>
                                        </div>
                                    </div>
                                `;
                            }}).join(\'\')}}
                        </div>
                    </div>
                `;
            }});

            html += `</div></div>`;
            container.innerHTML = html;
        }}

        // ================= STUDENT ROSTER MANAGEMENT =================
        function loadStudentTable() {{
            const students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const tbody = document.getElementById(\'studentTableBody\');
            if (!tbody) return;

            tbody.innerHTML = students.map(s => `
                <tr class="hover:bg-slate-50 border-b">
                    <td class="p-4 font-mono font-bold text-blue-700">${{s.id}}</td>
                    <td class="p-4 font-bold text-slate-900">${{s.name}}</td>
                    <td class="p-4 text-slate-600">${{s.email || \'--\'}}</td>
                    <td class="p-4 font-medium text-slate-800">${{s.dept}}</td>
                    <td class="p-4">
                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold ${{s.verified ? \'bg-emerald-100 text-emerald-800\' : \'bg-amber-100 text-amber-800\'}}">
                            ${{s.verified ? \'Verified\' : \'Unverified\'}}
                        </span>
                    </td>
                    <td class="p-4 text-right space-x-2">
                        <button onclick="toggleVerifyStudent(\'${{s.id}}\')" class="text-blue-600 hover:text-blue-800 font-bold">Verify</button>
                        <button onclick="editStudent(\'${{s.id}}\')" class="text-slate-600 hover:text-slate-800 font-bold">Edit</button>
                        <button onclick="deleteStudent(\'${{s.id}}\')" class="text-rose-600 hover:text-rose-800 font-bold">Delete</button>
                    </td>
                </tr>
            `).join(\'\');
        }}

        function openStudentModal() {{
            document.getElementById(\'modalStudentOriginalId\').value = \'\';
            document.getElementById(\'modalStudentId\').value = \'\';
            document.getElementById(\'modalStudentName\').value = \'\';
            document.getElementById(\'modalStudentEmail\').value = \'\';
            document.getElementById(\'modalStudentVerified\').checked = true;
            document.getElementById(\'studentModalTitle\').innerText = "Enroll Student";
            document.getElementById(\'studentModal\').classList.remove(\'hidden\');
        }}

        function closeStudentModal() {{
            document.getElementById(\'studentModal\').classList.add(\'hidden\');
        }}

        function editStudent(id) {{
            const students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const s = students.find(x => x.id === id);
            if (!s) return;

            document.getElementById(\'modalStudentOriginalId\').value = s.id;
            document.getElementById(\'modalStudentId\').value = s.id;
            document.getElementById(\'modalStudentName\').value = s.name;
            document.getElementById(\'modalStudentEmail\').value = s.email;
            document.getElementById(\'modalStudentDept\').value = s.dept;
            document.getElementById(\'modalStudentVerified\').checked = s.verified;
            document.getElementById(\'studentModalTitle\').innerText = "Edit Student";
            document.getElementById(\'studentModal\').classList.remove(\'hidden\');
        }}

        function handleSaveStudent(e) {{
            e.preventDefault();
            const origId = document.getElementById(\'modalStudentOriginalId\').value;
            const id = document.getElementById(\'modalStudentId\').value.trim();
            const name = document.getElementById(\'modalStudentName\').value.trim();
            const email = document.getElementById(\'modalStudentEmail\').value.trim();
            const dept = document.getElementById(\'modalStudentDept\').value;
            const verified = document.getElementById(\'modalStudentVerified\').checked;

            let students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];

            if (origId) {{
                const idx = students.findIndex(x => x.id === origId);
                if (idx !== -1) {{
                    students[idx] = {{ ...students[idx], id, name, email, dept, verified }};
                }}
            }} else {{
                students.push({{
                    id, name, email, dept, verified,
                    passwordHash: CryptoJS.SHA256(\'Password@2026\').toString()
                }});
            }}

            localStorage.setItem(\'univote_db_students\', JSON.stringify(students));
            closeStudentModal();
            loadStudentTable();
        }}

        function toggleVerifyStudent(id) {{
            let students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const idx = students.findIndex(x => x.id === id);
            if (idx !== -1) {{
                students[idx].verified = !students[idx].verified;
                localStorage.setItem(\'univote_db_students\', JSON.stringify(students));
                loadStudentTable();
            }}
        }}

        function deleteStudent(id) {{
            if (!confirm(`Delete student record ${{id}}?`)) return;
            let students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            students = students.filter(x => x.id !== id);
            localStorage.setItem(\'univote_db_students\', JSON.stringify(students));
            loadStudentTable();
        }}

        // ================= CANDIDATE MANAGEMENT =================
        function loadCandidateTable() {{
            const candidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || [];
            const tbody = document.getElementById(\'candidateTableBody\');
            if (!tbody) return;

            tbody.innerHTML = candidates.map(c => `
                <tr class="hover:bg-slate-50 border-b">
                    <td class="p-4">
                        <img src="${{c.photo || \'/templates/ua-logo.png\'}}" class="w-8 h-8 rounded-lg object-cover border" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                    </td>
                    <td class="p-4 font-bold text-slate-900">${{c.name}}</td>
                    <td class="p-4 font-bold text-blue-700">${{POSITIONS.find(p => p.id === c.posId)?.name || c.posId}}</td>
                    <td class="p-4">${{renderPartyBadge(c)}}</td>
                    <td class="p-4 text-slate-700">${{c.targetDept}}</td>
                    <td class="p-4 text-right space-x-2">
                        <button onclick="editCandidate(\'${{c.id}}\')" class="text-blue-600 hover:text-blue-800 font-bold">Edit</button>
                        <button onclick="deleteCandidate(\'${{c.id}}\')" class="text-rose-600 hover:text-rose-800 font-bold">Delete</button>
                    </td>
                </tr>
            `).join(\'\');
        }}

        function renderPartyBadge(c) {{
            const party = getCandidateParty(c);
            if (party === \'SIKLAB\') {{
                return `<span class="bg-amber-100 text-amber-900 font-black text-[10px] px-2 py-0.5 rounded-full border border-amber-300">SIKLAB</span>`;
            }} else {{
                return `<span class="bg-slate-100 text-slate-700 font-bold text-[10px] px-2 py-0.5 rounded-full border border-slate-200">Independent</span>`;
            }}
        }}

        function openCandidateModal() {{
            document.getElementById(\'modalCandId\').value = \'\';
            document.getElementById(\'modalCandName\').value = \'\';
            document.getElementById(\'modalCandParty\').value = \'SIKLAB\';
            document.getElementById(\'modalCandPhoto\').value = \'/templates/ua-logo.png\';
            document.getElementById(\'candidateModalTitle\').innerText = "Add Candidate";
            document.getElementById(\'candidateModal\').classList.remove(\'hidden\');
        }}

        function closeCandidateModal() {{
            document.getElementById(\'candidateModal\').classList.add(\'hidden\');
        }}

        function editCandidate(id) {{
            const candidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || [];
            const c = candidates.find(x => x.id === id);
            if (!c) return;

            document.getElementById(\'modalCandId\').value = c.id;
            document.getElementById(\'modalCandName\').value = c.name;
            document.getElementById(\'modalCandPos\').value = c.posId;
            document.getElementById(\'modalCandParty\').value = c.party;
            document.getElementById(\'modalCandDept\').value = c.targetDept;
            document.getElementById(\'modalCandPhoto\').value = c.photo;
            document.getElementById(\'candidateModalTitle\').innerText = "Edit Candidate";
            document.getElementById(\'candidateModal\').classList.remove(\'hidden\');
        }}

        function handleSaveCandidate(e) {{
            e.preventDefault();
            const id = document.getElementById(\'modalCandId\').value;
            const name = document.getElementById(\'modalCandName\').value.trim();
            const posId = document.getElementById(\'modalCandPos\').value;
            const party = document.getElementById(\'modalCandParty\').value.trim();
            const targetDept = document.getElementById(\'modalCandDept\').value;
            const photo = document.getElementById(\'modalCandPhoto\').value.trim();

            let candidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || [];

            if (id) {{
                const idx = candidates.findIndex(x => x.id === id);
                if (idx !== -1) {{
                    candidates[idx] = {{ ...candidates[idx], name, posId, party, targetDept, photo }};
                }}
            }} else {{
                const newId = \'cand_\' + Date.now();
                candidates.push({{
                    id: newId,
                    name, posId, party, targetDept, photo,
                    platform: `Dedicated leadership and representation for ${{targetDept}} students.`,
                    advocacies: [\'Student-Centered Leadership\', \'Integrity and Excellence\']
                }});
            }}

            localStorage.setItem(\'univote_db_candidates\', JSON.stringify(candidates));
            closeCandidateModal();
            loadCandidateTable();
            loadWinnersAndTallies();
        }}

        function deleteCandidate(id) {{
            if (!confirm("Are you sure you want to delete this candidate?")) return;
            let candidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || [];
            candidates = candidates.filter(x => x.id !== id);
            localStorage.setItem(\'univote_db_candidates\', JSON.stringify(candidates));
            loadCandidateTable();
            loadWinnersAndTallies();
        }}

        // ================= ELECTION CONFIGURATION =================
        function loadElectionConfig() {{
            const elec = JSON.parse(localStorage.getItem(\'univote_db_elections\')) || {{
                title: \'UA University Student Council Elections 2026\',
                startDate: \'2026-10-01\',
                endDate: \'2026-11-30\',
                active: true,
                published: true
            }};

            document.getElementById(\'elecTitle\').value = elec.title;
            document.getElementById(\'elecStart\').value = elec.startDate;
            document.getElementById(\'elecEnd\').value = elec.endDate;
            document.getElementById(\'elecActive\').checked = elec.active;
            document.getElementById(\'elecPublished\').checked = elec.published;
        }}

        function handleSaveElection(e) {{
            e.preventDefault();
            const updated = {{
                title: document.getElementById(\'elecTitle\').value.trim(),
                startDate: document.getElementById(\'elecStart\').value,
                endDate: document.getElementById(\'elecEnd\').value,
                active: document.getElementById(\'elecActive\').checked,
                published: document.getElementById(\'elecPublished\').checked
            }};
            localStorage.setItem(\'univote_db_elections\', JSON.stringify(updated));
            loadWinnersAndTallies();
            alert("Election configuration saved successfully!");
        }}

        // ================= AUDIT LOG =================
        function loadAuditTable() {{
            const ballots = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\')) || [];
            const tbody = document.getElementById(\'encryptedBallotsTableBody\');
            if (!tbody) return;

            if (ballots.length === 0) {{
                tbody.innerHTML = `<tr><td colspan="4" class="p-6 text-center text-slate-400">No encrypted ballots recorded in database. All tallies are clean.</td></tr>`;
                return;
            }}

            tbody.innerHTML = ballots.map(b => `
                <tr class="hover:bg-slate-50 border-b">
                    <td class="p-4">${{b.timestamp}}</td>
                    <td class="p-4 text-blue-700 font-bold">${{b.voterToken}}</td>
                    <td class="p-4 font-sans font-bold text-slate-800">${{b.department}}</td>
                    <td class="p-4 text-emerald-600 break-all max-w-xs font-mono text-[11px]">${{b.cipherPayload}}</td>
                </tr>
            `).join(\'\');
        }}
    </script>
</body>
</html>\'\'\'
'''

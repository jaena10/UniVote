# -*- coding: utf-8 -*-
"""
Generates studentweb.html content for UniVote.
"""

def generate_student_html_code(dept_options_html):
    # Notice: we escape double braces {{ and }} for python formatting if needed,
    # or return a clean function string that takes (candidates_json, students_json, depts_json, positions_json).
    return f'''
def generate_student_html():
    candidates_json = json.dumps(candidates_data)
    students_json = json.dumps(default_students)
    depts_json = json.dumps(DEPARTMENTS)
    positions_json = json.dumps(POSITIONS)

    return f\'\'\'<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniVote - University of the Assumption Student Voting Portal</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- CryptoJS for AES-256 and SHA-256 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>
    <!-- QRCode.js Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/static/css/student.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: [\'Plus Jakarta Sans\', \'sans-serif\'],
                        mono: [\'JetBrains Mono\', \'monospace\'],
                    }},
                    colors: {{
                        ua: {{
                            navy: \'#020381\',
                            gold: \'#d97706\',
                            emerald: \'#059669\',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .custom-scrollbar::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #f1f5f9;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #94a3b8;
        }}
        .ua-hero-bg {{
            background: linear-gradient(135deg, #020381 0%, #1e3a8a 50%, #0369a1 100%);
        }}
        @media print {{
            body * {{
                visibility: hidden;
            }}
            #printableReceipt, #printableReceipt * {{
                visibility: visible;
            }}
            #printableReceipt {{
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                border: none;
                box-shadow: none;
                padding: 0;
                margin: 0;
            }}
            .no-print {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 flex flex-col min-h-screen font-sans selection:bg-blue-900 selection:text-white">

    <!-- TOP NAVIGATION BAR -->
    <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40 transition-all">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Brand / Logo -->
                <div class="flex items-center space-x-3.5">
                    <img src="/templates/ua-logo.png" alt="University of the Assumption Seal Logo" class="w-12 h-12 object-contain filter drop-shadow-sm" onerror="this.onerror=null; this.src=\'/static/ua-logo.png\';">
                    <div>
                        <div class="flex items-center space-x-2">
                            <span class="font-extrabold text-2xl tracking-tight text-ua-navy">UniVote</span>
                            <span class="bg-amber-100 text-amber-900 text-[10px] font-black px-2 py-0.5 rounded-full border border-amber-200 uppercase tracking-wide">Pampanga</span>
                        </div>
                        <p class="text-xs font-semibold text-slate-500">University of the Assumption Student Voting Portal</p>
                    </div>
                </div>

                <!-- Navigation Tabs -->
                <nav class="hidden md:flex items-center space-x-1">
                    <button onclick="switchMainTab(\'ballot\')" id="nav-btn-ballot" class="main-nav-btn px-4 py-2 rounded-xl text-xs font-bold transition flex items-center space-x-2 bg-blue-50 text-ua-navy">
                        <i data-lucide="vote" class="w-4 h-4"></i>
                        <span>Ballot Slate</span>
                    </button>
                    <button onclick="switchMainTab(\'partylists\')" id="nav-btn-partylists" class="main-nav-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition flex items-center space-x-2">
                        <i data-lucide="users" class="w-4 h-4"></i>
                        <span>Official Partylists</span>
                    </button>
                    <button onclick="switchMainTab(\'results\')" id="nav-btn-results" class="main-nav-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition flex items-center space-x-2">
                        <i data-lucide="bar-chart-3" class="w-4 h-4"></i>
                        <span>Live Results</span>
                    </button>
                </nav>

                <!-- Authentication Group -->
                <div class="flex items-center space-x-3">
                    <div id="unauthNavGroup" class="flex items-center space-x-2">
                        <button onclick="openSignInModal()" class="bg-ua-navy hover:bg-blue-800 text-white text-xs font-bold px-4 py-2.5 rounded-xl transition shadow-md shadow-blue-900/15 flex items-center space-x-1.5">
                            <i data-lucide="log-in" class="w-4 h-4 text-amber-300"></i>
                            <span>Sign In</span>
                        </button>
                        <button onclick="openRegisterModal()" class="bg-white hover:bg-slate-50 text-blue-900 border border-slate-300 text-xs font-bold px-3.5 py-2.5 rounded-xl transition shadow-sm flex items-center space-x-1.5">
                            <i data-lucide="user-plus" class="w-4 h-4 text-emerald-600"></i>
                            <span class="hidden sm:inline">First-Time Registration</span>
                            <span class="sm:hidden">Register</span>
                        </button>
                    </div>

                    <!-- Authenticated Identity Badge -->
                    <div id="voterBadge" class="hidden flex items-center space-x-2 bg-slate-100 border border-slate-200 pl-3 pr-2 py-1.5 rounded-2xl shadow-sm">
                        <div class="w-7 h-7 rounded-full bg-ua-navy text-white flex items-center justify-center font-bold text-xs shadow-inner">
                            <i data-lucide="user-check" class="w-3.5 h-3.5 text-emerald-400"></i>
                        </div>
                        <span id="voterIdentityDisplay" class="text-xs font-black text-slate-800 max-w-[200px] truncate">Student Name</span>
                        <button onclick="handleStudentLogout()" title="Sign Out" class="text-slate-400 hover:text-rose-600 transition p-1 rounded-lg hover:bg-white">
                            <i data-lucide="log-out" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- MAIN WRAPPER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">

        <!-- ================= PAGE 1: VOTING PORTAL ================= -->
        <div id="page-ballot" class="main-page-section space-y-8">
            
            <!-- Hero Header Banner -->
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
                        <i data-lucide="calendar" class="w-4 h-4 text-amber-300"></i>
                        <div class="text-xs">
                            <span class="text-blue-100">Official Election Schedule: </span>
                            <span id="electionScheduleDisplay" class="font-bold text-white tracking-wide">2026-10-01 to 2026-11-30</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Election Inactive Alert Banner -->
            <div id="electionInactiveBanner" class="hidden bg-rose-50 border-2 border-rose-300 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-2xl bg-rose-100 text-rose-800 flex items-center justify-center shrink-0">
                        <i data-lucide="alert-triangle" class="w-6 h-6 text-rose-700"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Voting Portal Currently Closed</h3>
                        <p id="electionInactiveNotice" class="text-xs text-slate-600 mt-0.5">The election period has either ended or has not yet commenced. Ballot submissions are sealed.</p>
                    </div>
                </div>
            </div>

            <!-- BROWSING MODE BANNER (Visible when NOT logged in) -->
            <div id="browsingModeBanner" class="bg-gradient-to-r from-blue-50 to-indigo-50/80 border-2 border-blue-200 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-2xl bg-ua-navy text-white flex items-center justify-center shrink-0 shadow-md">
                        <i data-lucide="compass" class="w-6 h-6 text-amber-300"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h3 class="font-black text-slate-900 text-base">Candidate Slate Browsing Mode</h3>
                            <span class="bg-blue-100 text-blue-800 text-[10px] font-black px-2 py-0.5 rounded-full border border-blue-200">BROWSING ACTIVE</span>
                        </div>
                        <p class="text-xs text-slate-600 mt-0.5 max-w-2xl">
                            You are exploring candidate profiles, platforms, and advocacies across UA departments. Select any department from the dropdown below to preview their slate. Sign in with your UA Student ID when you are ready to vote.
                        </p>
                    </div>
                </div>
                <div class="flex items-center space-x-2.5 shrink-0">
                    <button onclick="openSignInModal()" class="bg-ua-navy hover:bg-blue-800 text-white text-xs font-bold px-5 py-2.5 rounded-xl transition shadow-md flex items-center space-x-1.5">
                        <i data-lucide="log-in" class="w-4 h-4 text-amber-300"></i>
                        <span>Sign In to Vote</span>
                    </button>
                    <button onclick="openRegisterModal()" class="bg-white hover:bg-slate-50 text-blue-900 border border-slate-300 text-xs font-bold px-4 py-2.5 rounded-xl transition shadow-sm flex items-center space-x-1.5">
                        <i data-lucide="user-plus" class="w-4 h-4 text-emerald-600"></i>
                        <span>Register</span>
                    </button>
                </div>
            </div>

            <!-- VOTED CONFIRMATION BANNER (Visible when logged in and HAS voted) -->
            <div id="votedConfirmedBanner" class="hidden bg-emerald-50 border-2 border-emerald-300 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
                <div class="flex items-center space-x-4">
                    <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 shadow-inner">
                        <i data-lucide="check-circle-2" class="w-6 h-6"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Ballot Officially Cast &amp; Cryptographically Sealed</h3>
                        <p class="text-xs text-slate-600 mt-0.5">Your official ballot choices for this election have been recorded and securely signed in the institutional audit registry.</p>
                    </div>
                </div>
                <button onclick="openReceiptModal()" class="bg-emerald-700 hover:bg-emerald-800 text-white text-xs font-bold px-5 py-2.5 rounded-xl transition shadow-md flex items-center space-x-1.5 shrink-0">
                    <i data-lucide="file-text" class="w-4 h-4 text-emerald-200"></i>
                    <span>View Digital Receipt</span>
                </button>
            </div>

            <!-- Candidate Slate Explorer Section -->
            <div class="space-y-6">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-2 border-b border-slate-100">
                    <div>
                        <div class="flex items-center space-x-2.5">
                            <h2 id="candidateSectionTitle" class="text-xl font-extrabold text-slate-900">College of Accountancy Candidates</h2>
                            <span id="browsingModeBadge" class="bg-blue-100 text-blue-800 text-[10px] font-black px-2 py-0.5 rounded-full border border-blue-200">BROWSING</span>
                        </div>
                        <p id="candidateSectionSub" class="text-xs text-slate-500">Previewing council positions and official candidate platforms</p>
                    </div>
                    
                    <div class="flex flex-wrap items-center gap-2.5">
                        <!-- Browsing Mode Department Selector -->
                        <div id="browsingDeptSelectorContainer" class="flex items-center space-x-1.5 bg-white p-1 rounded-xl border border-blue-200 shadow-sm">
                            <label class="text-[11px] font-bold text-slate-600 pl-2 shrink-0">Department:</label>
                            <select id="browsingDeptSelect" onchange="switchBrowsingDept(this.value)" class="text-xs font-bold border-0 rounded-lg px-2 py-1.5 bg-transparent text-ua-navy focus:ring-0 focus:outline-none">
{dept_options_html}
                            </select>
                        </div>

                        <!-- Candidate Search -->
                        <div class="relative">
                            <input type="text" id="candidateSearch" onkeyup="renderCandidateCards()" placeholder="Search candidate or party..." class="pl-9 pr-4 py-2.5 text-xs border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none w-52 bg-white shadow-sm">
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

            <!-- Sleek Ballot Review & Action Bar (Bottom Floating Bar) -->
            <div id="ballotBottomBar" class="bg-white rounded-3xl p-5 border border-slate-200 shadow-xl flex flex-col sm:flex-row items-center justify-between gap-4 sticky bottom-6 z-30 transition-all">
                <div id="ballotBarContent" class="flex items-center space-x-3 w-full sm:w-auto">
                    <!-- Dynamic Ballot Status -->
                </div>

                <div id="ballotBarAction" class="flex items-center space-x-3 w-full sm:w-auto">
                    <!-- Dynamic Action Button -->
                </div>
            </div>

        </div>

        <!-- ================= PAGE 2: OFFICIAL PARTYLISTS ================= -->
        <div id="page-partylists" class="main-page-section hidden space-y-6">
            <div class="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-4">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b pb-4">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Accredited Student Council Partylists</h2>
                        <p class="text-xs text-slate-500">Official party accreditation and collective platforms for Academic Year 2026</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <label class="text-xs font-bold text-slate-500">Filter Department:</label>
                        <select id="partylistDeptFilter" onchange="filterPartylists(this.value)" class="text-xs font-semibold border rounded-xl px-3 py-2 bg-slate-50">
{dept_options_html}
                        </select>
                    </div>
                </div>

                <!-- Partylist Grid -->
                <div id="partylistsContainer" class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4">
                    <!-- Dynamic Partylists -->
                </div>
            </div>
        </div>

        <!-- ================= PAGE 3: LIVE RESULTS & TALLIES ================= -->
        <div id="page-results" class="main-page-section hidden space-y-6">
            <div class="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-4">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b pb-4">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Official Departmental Tallies &amp; Results</h2>
                        <p class="text-xs text-slate-500">Commission published live vote counts and winner designations</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <label class="text-xs font-bold text-slate-500">Department:</label>
                        <select id="resultsDeptFilter" onchange="switchResultsDept(this.value)" class="text-xs font-semibold border rounded-xl px-3 py-2 bg-slate-50">
{dept_options_html}
                        </select>
                    </div>
                </div>

                <!-- Dynamic Results / Sealed Notice -->
                <div id="resultsContentArea" class="pt-4 space-y-6">
                    <!-- Dynamic Content -->
                </div>
            </div>
        </div>

    </main>

    <!-- FOOTER -->
    <footer class="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-400 mt-auto">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-2">
            <div class="flex items-center space-x-2">
                <img src="/templates/ua-logo.png" alt="UA Seal" class="w-5 h-5 object-contain" onerror="this.onerror=null; this.src=\'/static/ua-logo.png\';">
                <span class="font-bold text-slate-700">University of the Assumption</span>
                <span>• UniVote Electronic Voting System</span>
            </div>
            <div>Institutional Commission on Elections &copy; 2026. All Rights Reserved.</div>
        </div>
    </footer>

    <!-- ================= MODALS ================= -->

    <!-- 1. SIGN IN MODAL -->
    <div id="signInModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-5 border border-blue-100 shadow-2xl relative">
            <div class="flex items-center justify-between border-b pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-ua-navy flex items-center justify-center text-white shadow-sm">
                        <i data-lucide="log-in" class="w-5 h-5 text-amber-300"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Student Sign In</h3>
                        <p class="text-[11px] text-slate-500">Sign in with your UA Student ID</p>
                    </div>
                </div>
                <button onclick="closeSignInModal()" type="button" class="text-slate-400 hover:text-slate-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <!-- Inline Alert Message Box -->
            <div id="signInAlertBox" class="hidden text-xs p-3 rounded-2xl border font-semibold"></div>

            <form id="formStudentAuth" onsubmit="handleAuthenticate(event)" class="space-y-4 text-xs">
                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Student ID Number *</label>
                    <input type="text" id="authStudentId" required placeholder="e.g., 2024000669" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none font-mono">
                    <p class="text-[10px] text-slate-400 mt-1">10-digit institutional identification number</p>
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">UA Institutional Email *</label>
                    <input type="email" id="authStudentEmail" required placeholder="student.name@ua.edu.ph" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Password *</label>
                    <div class="relative">
                        <input type="password" id="authPassword" required placeholder="Enter your password" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility(\'authPassword\', this)" class="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600">
                            <i data-lucide="eye" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                <div class="pt-2">
                    <button type="submit" class="w-full bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 rounded-xl transition shadow-md flex items-center justify-center space-x-1.5 text-xs">
                        <i data-lucide="lock" class="w-4 h-4 text-amber-300"></i>
                        <span>Authenticate &amp; Unlock Ballot</span>
                    </button>
                </div>
            </form>

            <div class="text-center pt-2 border-t border-slate-100">
                <p class="text-[11px] text-slate-500">
                    First time voting? 
                    <button type="button" onclick="switchToRegisterModal()" class="text-blue-700 font-bold hover:underline">
                        Register Account
                    </button>
                </p>
            </div>
        </div>
    </div>

    <!-- 2. REGISTRATION MODAL (With All 17 Departments in Alphabetical Order) -->
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
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Full Student Name *</label>
                    <input type="text" id="regFullName" oninput="updateDerivedEmailSuggestion()" required placeholder="e.g., Juan Dela T. Cruz" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none font-semibold">
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Student ID Number *</label>
                    <input type="text" id="regStudentId" required placeholder="e.g., 2024001244" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none font-mono">
                    <p class="text-[10px] text-slate-400 mt-0.5">Strictly 10 digits starting with admission year (2010–2026)</p>
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Academic Department *</label>
                    <select id="regDepartment" required class="w-full px-4 py-2.5 border border-slate-200 rounded-xl bg-white focus:ring-2 focus:ring-blue-600 focus:outline-none font-semibold text-slate-800">
{dept_options_html}
                    </select>
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">UA Institutional Email *</label>
                    <input type="email" id="regEmail" required placeholder="jdtcruz.student@ua.edu.ph" class="w-full px-4 py-2.5 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                    <p class="text-[10px] text-slate-400 mt-0.5">Must be an active @ua.edu.ph institutional email</p>
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Create Password *</label>
                    <div class="relative">
                        <input type="password" id="regPassword" required placeholder="Minimum 8 chars with 1 number" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility(\'regPassword\', this)" class="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600">
                            <i data-lucide="eye" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                <div>
                    <label class="block text-[11px] font-bold text-slate-700 mb-1">Confirm Password *</label>
                    <div class="relative">
                        <input type="password" id="regConfirmPassword" required placeholder="Re-enter password" class="w-full px-4 py-2.5 pr-10 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none">
                        <button type="button" onclick="togglePasswordVisibility(\'regConfirmPassword\', this)" class="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600">
                            <i data-lucide="eye" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

                <div class="pt-2">
                    <button type="submit" class="w-full bg-emerald-700 hover:bg-emerald-800 text-white font-bold py-3 rounded-xl transition shadow-md flex items-center justify-center space-x-1.5 text-xs">
                        <i data-lucide="user-check" class="w-4 h-4"></i>
                        <span>Register &amp; Verify Student Account</span>
                    </button>
                </div>
            </form>

            <div class="text-center pt-2 border-t border-slate-100">
                <p class="text-[11px] text-slate-500">
                    Already registered? 
                    <button type="button" onclick="switchToSignInModal()" class="text-blue-700 font-bold hover:underline">
                        Sign In here
                    </button>
                </p>
            </div>
        </div>
    </div>

    <!-- 3. REGISTRATION SUCCESS MODAL -->
    <div id="regSuccessModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-sm w-full p-6 text-center space-y-4 shadow-2xl border border-emerald-100">
            <div class="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-600 mx-auto flex items-center justify-center shadow-inner">
                <i data-lucide="check-circle" class="w-8 h-8"></i>
            </div>
            <div>
                <h3 class="text-lg font-black text-slate-900">Registration Successful!</h3>
                <p class="text-xs text-slate-500 mt-1">Your voter credentials have been registered in the database. Please sign in to cast your ballot.</p>
            </div>
            <button onclick="proceedFromRegSuccessToSignIn()" class="w-full bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 rounded-xl transition shadow-md flex items-center justify-center space-x-1.5 text-xs">
                <i data-lucide="log-in" class="w-4 h-4 text-amber-300"></i>
                <span>Proceed to Sign In</span>
            </button>
        </div>
    </div>

    <!-- 4. BALLOT REVIEW CONFIRMATION MODAL -->
    <div id="reviewModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 space-y-5 shadow-2xl border border-blue-100 max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between border-b pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-ua-navy text-white flex items-center justify-center shadow-sm">
                        <i data-lucide="check-square" class="w-5 h-5 text-amber-300"></i>
                    </div>
                    <div>
                        <h3 class="font-extrabold text-slate-900 text-base">Confirm Official Ballot</h3>
                        <p class="text-[11px] text-slate-500">Review your selected candidates before casting</p>
                    </div>
                </div>
                <button onclick="closeReviewModal()" class="text-slate-400 hover:text-slate-600">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3 text-xs text-amber-800 space-y-1">
                <p class="font-bold">Important Notice:</p>
                <p>Once you confirm and submit, your vote will be AES-256 encrypted and stored permanently. Ballots cannot be modified or re-cast.</p>
            </div>

            <div id="reviewCandidateList" class="space-y-2.5 text-xs">
                <!-- Dynamic Choices -->
            </div>

            <div class="flex items-center justify-end space-x-2 pt-3 border-t">
                <button type="button" onclick="closeReviewModal()" class="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-50 font-bold text-xs transition">
                    Modify Ballot
                </button>
                <button type="button" onclick="submitBallot()" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs transition shadow-md flex items-center space-x-1.5">
                    <i data-lucide="send" class="w-4 h-4"></i>
                    <span>Confirm &amp; Cast Ballot</span>
                </button>
            </div>
        </div>
    </div>

    <!-- 5. OFFICIAL DIGITAL VOTING RECEIPT & QR CODE MODAL -->
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
                
                <!-- Receipt Header with UA Seal -->
                <div class="flex justify-between items-center border-b border-slate-200 pb-3">
                    <div class="flex items-center space-x-3">
                        <img src="/templates/ua-logo.png" alt="University Seal" class="w-10 h-10 object-contain" onerror="this.onerror=null; this.src=\'/static/ua-logo.png\';">
                        <div>
                            <h4 class="font-bold text-slate-900 text-sm">UNIVERSITY OF THE ASSUMPTION</h4>
                            <p class="text-[10px] text-slate-500">Institutional Commission on Elections • UniVote</p>
                        </div>
                    </div>
                    <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2.5 py-1 rounded-full border border-emerald-200">VERIFIED</span>
                </div>

                <!-- Voter Information Grid -->
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-white p-3 rounded-2xl border border-slate-200">
                    <div>
                        <span class="text-slate-400 block text-[9px]">VOTER NAME</span>
                        <span id="receiptVoterName" class="font-bold text-slate-800 truncate block">---</span>
                    </div>
                    <div>
                        <span class="text-slate-400 block text-[9px]">STUDENT ID</span>
                        <span id="receiptStudentId" class="font-bold text-slate-800 block">---</span>
                    </div>
                    <div>
                        <span class="text-slate-400 block text-[9px]">ACADEMIC DEPARTMENT</span>
                        <span id="receiptVoterDept" class="font-bold text-slate-800 block truncate">---</span>
                    </div>
                    <div>
                        <span class="text-slate-400 block text-[9px]">DATE &amp; TIMESTAMP</span>
                        <span id="receiptTimestamp" class="font-bold text-slate-800 block">---</span>
                    </div>
                </div>

                <!-- Cast Ballot Choices -->
                <div class="space-y-1.5">
                    <span class="text-slate-500 font-bold text-[10px] uppercase tracking-wider block">Official Ballot Choices Cast:</span>
                    <div id="receiptChoicesList" class="space-y-1 bg-white p-3 rounded-2xl border border-slate-200 text-[11px]">
                        <!-- Dynamic Receipt Choices -->
                    </div>
                </div>

                <!-- QR Code & Audit Trail -->
                <div class="flex flex-col sm:flex-row items-center justify-between gap-4 bg-white p-3.5 rounded-2xl border border-slate-200">
                    <div class="space-y-1 text-left flex-grow">
                        <span class="text-slate-400 block text-[9px]">ENCRYPTED TRANSACTION TOKEN</span>
                        <span id="receiptToken" class="font-bold text-blue-900 text-[10px] break-all block">---</span>
                        <span class="text-slate-400 block text-[9px] pt-1">AUDIT CIPHER PAYLOAD (AES-256)</span>
                        <p id="receiptCipher" class="text-[9px] text-slate-500 break-all line-clamp-2">---</p>
                    </div>
                    <!-- Scannable QR Code -->
                    <div class="shrink-0 flex flex-col items-center">
                        <div id="receiptQrCode" class="w-24 h-24 bg-white p-1 rounded-xl border border-slate-200 flex items-center justify-center"></div>
                        <span class="text-[8px] text-slate-400 mt-1 uppercase">Scan to Verify</span>
                    </div>
                </div>

            </div>

            <!-- Receipt Actions -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-2 pt-2 border-t no-print">
                <button type="button" onclick="closeReceiptModal()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl border border-slate-200 text-slate-600 hover:bg-slate-50 font-bold text-xs transition">
                    Done
                </button>
                <div class="flex items-center space-x-2 w-full sm:w-auto">
                    <button type="button" onclick="window.print()" class="w-full sm:w-auto px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs transition shadow-sm flex items-center justify-center space-x-1.5">
                        <i data-lucide="printer" class="w-4 h-4"></i>
                        <span>Print Receipt</span>
                    </button>
                    <button type="button" onclick="downloadDigitalReceipt()" class="w-full sm:w-auto px-4 py-2.5 rounded-xl bg-ua-navy hover:bg-blue-800 text-white font-bold text-xs transition shadow-md flex items-center justify-center space-x-1.5">
                        <i data-lucide="download" class="w-4 h-4 text-amber-300"></i>
                        <span>Download Card</span>
                    </button>
                </div>
            </div>

        </div>
    </div>

    <!-- ================= CLIENT-SIDE DATA & SCRIPTS ================= -->
    <script>
        // Seed Master Data
        const DEFAULT_CANDIDATES = {candidates_json};
        const DEFAULT_POSITIONS = {positions_json};
        const DEFAULT_DEPARTMENTS = {depts_json};
        const DEFAULT_STUDENTS = {students_json};

        // State Variables
        let currentUser = null;
        let selectedChoices = {{}};
        let activePositionTab = \'all\';
        let activeBrowsingDept = \'College of Accountancy\';
        let activePartylistDept = \'College of Accountancy\';
        let activeResultsDept = \'College of Accountancy\';
        const AES_SECRET_KEY = \'UniVote-UA-2026\';

        // ================= HELPER FUNCTIONS =================
        function normalizeDept(name) {{
            if (!name) return \'\';
            let n = name.trim();
            if (n === \'Junior High School\') return \'Junior Highschool\';
            if (n === \'Senior High School\') return \'Senior Highschool\';
            if (n.toLowerCase() === \'college of hospitality managemet\') return \'College of Hospitality Management\';
            return n;
        }}

        function isStudentVoted(studentId) {{
            if (!studentId) return false;
            const votedMap = JSON.parse(localStorage.getItem(\'univote_voted_students\') || \'{{}}\');
            if (votedMap[studentId]) return true;
            const ballots = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\') || \'[]\');
            return ballots.some(b => b.studentId === studentId);
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

        function renderPartyBadge(c) {{
            const party = getCandidateParty(c);
            if (party === \'SIKLAB\') {{
                return `<span class="bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black text-[10px] px-2.5 py-0.5 rounded-full shadow-sm">SIKLAB</span>`;
            }} else {{
                return `<span class="bg-slate-100 text-slate-700 font-bold text-[10px] px-2.5 py-0.5 rounded-full border border-slate-200">Independent</span>`;
            }}
        }}

        // ================= INITIALIZATION =================
        document.addEventListener(\'DOMContentLoaded\', () => {{
            initializeDatabaseDefaults();
            checkElectionActiveState();
            checkSessionLock();
            renderPositionTabs();
            renderCandidateCards();
            updateBallotVisualizer();
            renderPartylists();
            renderResultsPage();
            lucide.createIcons();
        }});

        // REAL-TIME BROADCAST: Listen for Admin Wipe or Updates
        window.addEventListener(\'storage\', (e) => {{
            if (e.key === \'univote_voting_reset_trigger\' || e.key === \'univote_encrypted_ballots_db\' || e.key === \'univote_voted_students\') {{
                checkSessionLock();
                renderCandidateCards();
                updateBallotVisualizer();
                renderResultsPage();
            }}
        }});

        const UNIVOTE_DATA_VERSION = \'univote_v6_2026_11_08_browsing_17depts\';

        function initializeDatabaseDefaults() {{
            if (localStorage.getItem(\'univote_data_version\') !== UNIVOTE_DATA_VERSION) {{
                localStorage.setItem(\'univote_db_candidates\', JSON.stringify(DEFAULT_CANDIDATES));
                localStorage.setItem(\'univote_db_students\', JSON.stringify(DEFAULT_STUDENTS));
                localStorage.setItem(\'univote_data_version\', UNIVOTE_DATA_VERSION);
                // Wipe legacy global flags
                localStorage.removeItem(\'univote_has_voted\');
                localStorage.removeItem(\'univote_saved_choices\');
            }} else {{
                if (!localStorage.getItem(\'univote_db_candidates\')) {{
                    localStorage.setItem(\'univote_db_candidates\', JSON.stringify(DEFAULT_CANDIDATES));
                }}
                if (!localStorage.getItem(\'univote_db_students\')) {{
                    localStorage.setItem(\'univote_db_students\', JSON.stringify(DEFAULT_STUDENTS));
                }}
            }}

            if (!localStorage.getItem(\'univote_db_elections\')) {{
                const defaultElection = {{
                    title: \'UA University Student Council Elections 2026\',
                    startDate: \'2026-10-01\',
                    endDate: \'2026-11-30\',
                    active: true,
                    published: true
                }};
                localStorage.setItem(\'univote_db_elections\', JSON.stringify(defaultElection));
            }}
            if (!localStorage.getItem(\'univote_encrypted_ballots_db\')) {{
                localStorage.setItem(\'univote_encrypted_ballots_db\', JSON.stringify([]));
            }}
            if (!localStorage.getItem(\'univote_voted_students\')) {{
                localStorage.setItem(\'univote_voted_students\', JSON.stringify({{}}));
            }}
            if (!localStorage.getItem(\'univote_student_choices\')) {{
                localStorage.setItem(\'univote_student_choices\', JSON.stringify({{}}));
            }}
        }}

        function checkElectionActiveState() {{
            const elec = JSON.parse(localStorage.getItem(\'univote_db_elections\'));
            if (elec) {{
                const bannerTitle = document.getElementById(\'activeElectionBannerTitle\');
                if (bannerTitle) bannerTitle.innerText = elec.title;
                const scheduleEl = document.getElementById(\'electionScheduleDisplay\');
                if (scheduleEl) scheduleEl.innerText = `${{elec.startDate}} to ${{elec.endDate}}`;
                
                const inactiveBanner = document.getElementById(\'electionInactiveBanner\');
                if (inactiveBanner) {{
                    if (!elec.active) {{
                        inactiveBanner.classList.remove(\'hidden\');
                    }} else {{
                        inactiveBanner.classList.add(\'hidden\');
                    }}
                }}
            }}
        }}

        // ================= SESSION & BROWSING MODE =================
        function checkSessionLock() {{
            const savedSession = sessionStorage.getItem(\'univote_locked_session\');
            if (savedSession) {{
                try {{
                    currentUser = JSON.parse(savedSession);
                }} catch (e) {{
                    currentUser = null;
                }}
            }} else {{
                currentUser = null;
            }}

            if (currentUser) {{
                activeResultsDept = currentUser.dept;
                activePartylistDept = currentUser.dept;
                applySessionLockUI();

                if (isStudentVoted(currentUser.id)) {{
                    const studentChoicesMap = JSON.parse(localStorage.getItem(\'univote_student_choices\') || \'{{}}\');
                    selectedChoices = studentChoicesMap[currentUser.id] || {{}};
                }} else {{
                    selectedChoices = {{}};
                }}
            }} else {{
                selectedChoices = {{}};
                applyBrowsingModeUI();
            }}
        }}

        function applyBrowsingModeUI() {{
            const voterBadge = document.getElementById(\'voterBadge\');
            if (voterBadge) voterBadge.classList.add(\'hidden\');
            
            const unauthNavGroup = document.getElementById(\'unauthNavGroup\');
            if (unauthNavGroup) unauthNavGroup.classList.remove(\'hidden\');

            const browsingBanner = document.getElementById(\'browsingModeBanner\');
            if (browsingBanner) browsingBanner.classList.remove(\'hidden\');

            const votedBanner = document.getElementById(\'votedConfirmedBanner\');
            if (votedBanner) votedBanner.classList.add(\'hidden\');

            const browsingBadge = document.getElementById(\'browsingModeBadge\');
            if (browsingBadge) browsingBadge.classList.remove(\'hidden\');

            const deptSelector = document.getElementById(\'browsingDeptSelectorContainer\');
            if (deptSelector) deptSelector.classList.remove(\'hidden\');

            const candTitle = document.getElementById(\'candidateSectionTitle\');
            if (candTitle) candTitle.innerText = `${{activeBrowsingDept}} Candidates`;
            const candSub = document.getElementById(\'candidateSectionSub\');
            if (candSub) candSub.innerText = `Browsing official candidates and platforms for ${{activeBrowsingDept}}. Sign in with your UA account to vote.`;

            const selectEl = document.getElementById(\'browsingDeptSelect\');
            if (selectEl) selectEl.value = activeBrowsingDept;

            lucide.createIcons();
        }}

        function applySessionLockUI() {{
            const voterDisplay = document.getElementById(\'voterIdentityDisplay\');
            if (voterDisplay) voterDisplay.innerText = `${{currentUser.name}} (${{currentUser.dept}})`;
            
            const voterBadge = document.getElementById(\'voterBadge\');
            if (voterBadge) voterBadge.classList.remove(\'hidden\');
            
            const unauthNavGroup = document.getElementById(\'unauthNavGroup\');
            if (unauthNavGroup) unauthNavGroup.classList.add(\'hidden\');

            const browsingBanner = document.getElementById(\'browsingModeBanner\');
            if (browsingBanner) browsingBanner.classList.add(\'hidden\');

            const browsingBadge = document.getElementById(\'browsingModeBadge\');
            if (browsingBadge) browsingBadge.classList.add(\'hidden\');

            const deptSelector = document.getElementById(\'browsingDeptSelectorContainer\');
            if (deptSelector) deptSelector.classList.add(\'hidden\');

            const hasVoted = isStudentVoted(currentUser.id);
            const votedBanner = document.getElementById(\'votedConfirmedBanner\');
            if (votedBanner) {{
                if (hasVoted) {{
                    votedBanner.classList.remove(\'hidden\');
                }} else {{
                    votedBanner.classList.add(\'hidden\');
                }}
            }}

            const candTitle = document.getElementById(\'candidateSectionTitle\');
            if (candTitle) candTitle.innerText = `${{currentUser.dept}} Candidate Slate`;
            const candSub = document.getElementById(\'candidateSectionSub\');
            if (candSub) {{
                candSub.innerText = hasVoted
                    ? `Official council candidates for ${{currentUser.dept}} (Your ballot is cast)`
                    : `Official council candidates running strictly for ${{currentUser.dept}}. Select 1 candidate per position.`;
            }}

            lucide.createIcons();
        }}

        function switchBrowsingDept(dept) {{
            activeBrowsingDept = dept;
            const candTitle = document.getElementById(\'candidateSectionTitle\');
            if (candTitle) candTitle.innerText = `${{activeBrowsingDept}} Candidates`;
            const candSub = document.getElementById(\'candidateSectionSub\');
            if (candSub) candSub.innerText = `Browsing official candidates and platforms for ${{activeBrowsingDept}}. Sign in with your UA account to vote.`;
            renderCandidateCards();
        }}

        function handleStudentLogout() {{
            sessionStorage.removeItem(\'univote_locked_session\');
            currentUser = null;
            selectedChoices = {{}};
            checkSessionLock();
            renderCandidateCards();
            updateBallotVisualizer();
            renderResultsPage();
        }}

        // ================= AUTHENTICATION =================
        function handleAuthenticate(e) {{
            e.preventDefault();
            hideSignInAlert();

            const studentId = document.getElementById(\'authStudentId\').value.trim();
            const studentEmail = document.getElementById(\'authStudentEmail\').value.trim().toLowerCase();
            const password = document.getElementById(\'authPassword\').value;

            if (!isValidStudentId(studentId)) {{
                showSignInAlert("Invalid Student ID! Must be strictly 10 digits with admission year between 2010 and 2026 (e.g., 2024000669).");
                return;
            }}

            if (!isValidUaEmailGeneral(studentEmail)) {{
                showSignInAlert("Invalid Email! Institutional email must end with @ua.edu.ph (e.g., jdtcruz.student@ua.edu.ph).");
                return;
            }}

            const students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const foundStudent = students.find(s => s.id === studentId);

            if (!foundStudent) {{
                showSignInAlert("Student account not found in roster! Please click \'First-Time Registration\' to register.");
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

            sessionStorage.setItem(\'univote_locked_session\', JSON.stringify(userSession));
            currentUser = userSession;
            activeResultsDept = currentUser.dept;
            activePartylistDept = currentUser.dept;

            closeSignInModal();

            // Check if THIS specific student has voted
            if (isStudentVoted(currentUser.id)) {{
                const studentChoicesMap = JSON.parse(localStorage.getItem(\'univote_student_choices\') || \'{{}}\');
                selectedChoices = studentChoicesMap[currentUser.id] || {{}};
            }} else {{
                selectedChoices = {{}};
            }}

            applySessionLockUI();
            renderPositionTabs();
            renderCandidateCards();
            updateBallotVisualizer();
            renderResultsPage();
        }}

        // ================= REGISTRATION =================
        function handleStudentRegistration(e) {{
            e.preventDefault();
            hideRegisterAlert();

            const studentId = document.getElementById(\'regStudentId\').value.trim();
            const studentName = document.getElementById(\'regFullName\').value.trim();
            const studentEmail = document.getElementById(\'regEmail\').value.trim().toLowerCase();
            const department = document.getElementById(\'regDepartment\').value;
            const password = document.getElementById(\'regPassword\').value;
            const confirmPassword = document.getElementById(\'regConfirmPassword\').value;

            if (!studentName || studentName.length < 3) {{
                showRegisterAlert("Please enter your complete legal name.");
                return;
            }}

            if (!isValidStudentId(studentId)) {{
                showRegisterAlert("Invalid Student ID format. Must be strictly 10 digits with year between 2010 and 2026 (e.g., 2024001244).");
                return;
            }}

            if (!isValidUaEmailGeneral(studentEmail)) {{
                showRegisterAlert("Invalid email format. You must provide an active institutional email ending in @ua.edu.ph.");
                return;
            }}

            if (password !== confirmPassword) {{
                showRegisterAlert("Passwords do not match. Please re-enter identical passwords.");
                return;
            }}

            const passCheck = validatePasswordComplexity(password);
            if (!passCheck.valid) {{
                showRegisterAlert(passCheck.message);
                return;
            }}

            let students = JSON.parse(localStorage.getItem(\'univote_db_students\')) || [];
            const existingStudent = students.find(s => s.id === studentId);
            if (existingStudent) {{
                showRegisterAlert(`Student ID ${{studentId}} is already registered. Please sign in instead.`);
                return;
            }}

            const newStudent = {{
                id: studentId,
                name: studentName,
                email: studentEmail,
                dept: department,
                verified: true,
                passwordHash: CryptoJS.SHA256(password).toString()
            }};

            students.push(newStudent);
            localStorage.setItem(\'univote_db_students\', JSON.stringify(students));

            closeRegisterModal();
            document.getElementById(\'regSuccessModal\').classList.remove(\'hidden\');
        }}

        function proceedFromRegSuccessToSignIn() {{
            document.getElementById(\'regSuccessModal\').classList.add(\'hidden\');
            openSignInModal();
        }}

        // ================= VALIDATION UTILITIES =================
        function isValidStudentId(id) {{
            if (!/^\\d{{10}}$/.test(id)) return false;
            const year = parseInt(id.substring(0, 4), 10);
            return year >= 2010 && year <= 2026;
        }}

        function isValidUaEmailGeneral(email) {{
            const pattern = /^[a-zA-Z0-9._%+-]+@ua\\.edu\\.ph$/i;
            return pattern.test(email);
        }}

        function validatePasswordComplexity(pass) {{
            if (pass.length < 8) {{
                return {{ valid: false, message: "Password must be at least 8 characters in length." }};
            }}
            if (!/\\d/.test(pass)) {{
                return {{ valid: false, message: "Password must contain at least one numeric digit (0-9)." }};
            }}
            return {{ valid: true }};
        }}

        function deriveOfficialUaEmail(fullName) {{
            if (!fullName || typeof fullName !== \'string\') return \'\';
            const cleaned = fullName.trim().toLowerCase().replace(/[^a-z\\s]/g, \'\');
            const parts = cleaned.split(/\\s+/);
            if (parts.length === 0 || parts[0] === \'\') return \'\';
            if (parts.length === 1) return `${{parts[0]}}.student@ua.edu.ph`;
            
            const lastName = parts[parts.length - 1];
            let initials = \'\';
            for (let i = 0; i < parts.length - 1; i++) {{
                if (parts[i].length > 0) initials += parts[i][0];
            }}
            return `${{initials}}${{lastName}}.student@ua.edu.ph`;
        }}

        function updateDerivedEmailSuggestion() {{
            const name = document.getElementById(\'regFullName\').value;
            const emailInput = document.getElementById(\'regEmail\');
            if (emailInput && !emailInput.value) {{
                const derived = deriveOfficialUaEmail(name);
                if (derived) emailInput.placeholder = derived;
            }}
        }}

        function togglePasswordVisibility(fieldId, btn) {{
            const field = document.getElementById(fieldId);
            if (!field) return;
            if (field.type === \'password\') {{
                field.type = \'text\';
                btn.innerHTML = `<i data-lucide="eye-off" class="w-4 h-4"></i>`;
            }} else {{
                field.type = \'password\';
                btn.innerHTML = `<i data-lucide="eye" class="w-4 h-4"></i>`;
            }}
            lucide.createIcons();
        }}

        // ================= MODAL CONTROLLERS =================
        function openSignInModal() {{
            hideSignInAlert();
            document.getElementById(\'signInModal\').classList.remove(\'hidden\');
            lucide.createIcons();
        }}

        function closeSignInModal() {{
            document.getElementById(\'signInModal\').classList.add(\'hidden\');
        }}

        function openRegisterModal() {{
            hideRegisterAlert();
            document.getElementById(\'registerModal\').classList.remove(\'hidden\');
            lucide.createIcons();
        }}

        function closeRegisterModal() {{
            document.getElementById(\'registerModal\').classList.add(\'hidden\');
        }}

        function switchToRegisterModal() {{
            closeSignInModal();
            openRegisterModal();
        }}

        function switchToSignInModal() {{
            closeRegisterModal();
            openSignInModal();
        }}

        function showSignInAlert(msg) {{
            const box = document.getElementById(\'signInAlertBox\');
            box.className = "text-xs p-3 rounded-2xl border font-semibold bg-rose-50 border-rose-300 text-rose-800";
            box.innerText = msg;
            box.classList.remove(\'hidden\');
        }}

        function hideSignInAlert() {{
            const box = document.getElementById(\'signInAlertBox\');
            box.classList.add(\'hidden\');
            box.innerText = \'\';
        }}

        function showRegisterAlert(msg) {{
            const box = document.getElementById(\'registerAlertBox\');
            box.className = "text-xs p-3 rounded-2xl border font-semibold bg-rose-50 border-rose-300 text-rose-800";
            box.innerText = msg;
            box.classList.remove(\'hidden\');
        }}

        function hideRegisterAlert() {{
            const box = document.getElementById(\'registerAlertBox\');
            box.classList.add(\'hidden\');
            box.innerText = \'\';
        }}

        // ================= CANDIDATE RENDERING =================
        function renderPositionTabs() {{
            const container = document.getElementById(\'positionTabs\');
            const tabs = [
                {{ id: \'all\', name: \'All Positions\' }},
                ...DEFAULT_POSITIONS
            ];

            container.innerHTML = tabs.map(tab => {{
                const isActive = activePositionTab === tab.id;
                return `
                    <button 
                        type="button" 
                        onclick="filterPositionTab(\'${{tab.id}}\')" 
                        class="px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap transition shadow-sm ${{
                            isActive 
                                ? \'bg-ua-navy text-white shadow-blue-900/20 shadow-md\' 
                                : \'bg-white text-slate-600 hover:bg-slate-100 hover:text-slate-900 border border-slate-200\'
                        }}">
                        ${{tab.name}}
                    </button>
                `;
            }}).join(\'\');
        }}

        function filterPositionTab(posId) {{
            activePositionTab = posId;
            renderPositionTabs();
            renderCandidateCards();
        }}

        function renderCandidateCards() {{
            const container = document.getElementById(\'candidateCardsContainer\');
            const search = document.getElementById(\'candidateSearch\').value.toLowerCase();
            
            // Determine active target department:
            // If logged in: strictly locked to currentUser.dept
            // If in browsing mode: uses activeBrowsingDept
            const targetDept = currentUser ? normalizeDept(currentUser.dept) : normalizeDept(activeBrowsingDept);
            const hasVoted = currentUser ? isStudentVoted(currentUser.id) : false;

            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;

            // Filter candidates strictly for the target department
            const filtered = allCandidates.filter(c => {{
                const candDept = normalizeDept(c.targetDept);
                const matchesDept = (candDept === targetDept);
                const matchesPos = (activePositionTab === \'all\' || c.posId === activePositionTab);
                const matchesSearch = c.name.toLowerCase().includes(search) || 
                                      (c.party && c.party.toLowerCase().includes(search)) || 
                                      (c.dept && c.dept.toLowerCase().includes(search));
                return matchesDept && matchesPos && matchesSearch;
            }});

            if (filtered.length === 0) {{
                container.innerHTML = `
                    <div class="bg-white rounded-3xl p-8 text-center text-slate-400 border border-slate-200 space-y-2">
                        <i data-lucide="search-x" class="w-10 h-10 mx-auto text-slate-300"></i>
                        <p class="text-sm font-semibold text-slate-600">No Candidates Found</p>
                        <p class="text-xs text-slate-400">No candidates match the selected position or search criteria for ${{targetDept}}.</p>
                    </div>
                `;
                lucide.createIcons();
                return;
            }}

            // Group by position
            const grouped = {{}};
            DEFAULT_POSITIONS.forEach(pos => {{
                grouped[pos.id] = filtered.filter(c => c.posId === pos.id);
            }});

            let html = \'\';
            DEFAULT_POSITIONS.forEach(pos => {{
                const posCands = grouped[pos.id] || [];
                if (activePositionTab !== \'all\' && activePositionTab !== pos.id) return;
                if (posCands.length === 0) return;

                html += `
                    <div class="space-y-3 pt-2">
                        <div class="flex items-center space-x-2">
                            <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
                            <h3 class="font-black text-sm text-slate-900 uppercase tracking-wider">${{pos.name}}</h3>
                            <span class="text-[10px] font-bold text-slate-400">(${posCands.length} Candidate${posCands.length > 1 ? \'s\' : \'\'})</span>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                            ${posCands.map(c => renderSingleCandidateCard(c, pos, hasVoted)).join(\'\')}
                        </div>
                    </div>
                `;
            }});

            container.innerHTML = html;
            lucide.createIcons();
        }}

        function renderSingleCandidateCard(c, pos, hasVoted) {{
            const isSelected = selectedChoices[c.posId] === c.id;
            
            // Build action button based on mode:
            // 1. Browsing mode (not logged in): "Sign In to Vote" button
            // 2. Logged in and has voted: Disabled "Voted" button
            // 3. Logged in and voting active: "Select Candidate" / "Selected ✓" toggle button
            let actionBtnHtml = \'\';
            if (!currentUser) {{
                actionBtnHtml = `
                    <button type="button" onclick="openSignInModal()" class="w-full py-2.5 px-4 rounded-xl text-xs font-bold bg-ua-navy hover:bg-blue-800 text-white transition shadow-sm flex items-center justify-center space-x-1.5">
                        <i data-lucide="log-in" class="w-3.5 h-3.5 text-amber-300"></i>
                        <span>Sign In to Vote</span>
                    </button>
                `;
            }} else if (hasVoted) {{
                actionBtnHtml = `
                    <button type="button" disabled class="w-full py-2.5 px-4 rounded-xl text-xs font-bold bg-slate-100 text-slate-400 border border-slate-200 cursor-not-allowed flex items-center justify-center space-x-1">
                        <i data-lucide="check" class="w-3.5 h-3.5"></i>
                        <span>${{isSelected ? \'Selected in Cast Ballot\' : \'Ballot Cast\'}}</span>
                    </button>
                `;
            }} else {{
                actionBtnHtml = `
                    <button type="button" onclick="toggleSelectCandidate(\'${{c.posId}}\', \'${{c.id}}\')" class="w-full py-2.5 px-4 rounded-xl text-xs font-bold transition flex items-center justify-center space-x-1.5 ${{
                        isSelected 
                            ? \'bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-600/20\' 
                            : \'bg-white hover:bg-blue-50 text-blue-900 border-2 border-blue-200 hover:border-blue-400\'
                    }}">
                        <i data-lucide="${{isSelected ? \'check-circle-2\' : \'plus\'}}" class="w-4 h-4"></i>
                        <span>${{isSelected ? \'Selected Choice\' : \'Select Candidate\'}}</span>
                    </button>
                `;
            }}

            return `
                <div class="bg-white rounded-2xl border-2 transition-all p-4 space-y-3.5 flex flex-col justify-between ${{
                    isSelected 
                        ? \'border-emerald-500 shadow-md ring-2 ring-emerald-500/20 bg-emerald-50/20\' 
                        : \'border-slate-200 hover:border-blue-300 hover:shadow-md\'
                }}">
                    <div class="space-y-3">
                        <div class="flex items-start space-x-3">
                            <div class="relative shrink-0">
                                <img src="${{c.photo || \'/templates/ua-logo.png\'}}" 
                                     alt="${{c.name}}" 
                                     class="w-16 h-16 rounded-xl object-cover object-center border border-slate-200 shadow-sm"
                                     onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                ${{isSelected ? \'<span class="absolute -top-1.5 -right-1.5 bg-emerald-600 text-white rounded-full p-0.5 shadow"><i data-lucide="check" class="w-3.5 h-3.5"></i></span>\' : \'\'}}
                            </div>
                            <div class="min-w-0 flex-1">
                                <div class="flex items-center space-x-1.5 mb-1">
                                    ${{renderPartyBadge(c)}}
                                    <span class="text-[10px] font-bold text-slate-400 truncate">${{pos.name}}</span>
                                </div>
                                <h4 class="font-extrabold text-sm text-slate-900 truncate leading-tight">${{c.name}}</h4>
                                <p class="text-[11px] text-slate-500 truncate mt-0.5">${{c.dept || c.targetDept}}</p>
                            </div>
                        </div>

                        ${{c.platform ? `
                            <p class="text-[11px] text-slate-600 leading-relaxed line-clamp-2 italic bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                                "${{c.platform}}"
                            </p>
                        ` : \'\'}}

                        ${{c.advocacies && c.advocacies.length ? `
                            <div class="space-y-1">
                                <span class="text-[9px] font-black uppercase tracking-wider text-slate-400 block">Key Advocacies:</span>
                                <ul class="text-[10px] text-slate-600 space-y-0.5 list-disc list-inside">
                                    ${{c.advocacies.slice(0, 2).map(a => `<li class="truncate">${{a}}</li>`).join(\'\')}}
                                </ul>
                            </div>
                        ` : \'\'}}
                    </div>

                    <div class="pt-2 border-t border-slate-100">
                        ${{actionBtnHtml}}
                    </div>
                </div>
            `;
        }}

        // ================= BALLOT SELECTION & VOTING =================
        function toggleSelectCandidate(posId, candidateId) {{
            if (!currentUser) {{
                openSignInModal();
                return;
            }}

            if (isStudentVoted(currentUser.id)) {{
                alert("Your official ballot has already been cast and recorded. It cannot be altered.");
                return;
            }}

            if (selectedChoices[posId] === candidateId) {{
                delete selectedChoices[posId];
            }} else {{
                selectedChoices[posId] = candidateId;
            }}

            updateBallotVisualizer();
            renderCandidateCards();
        }}

        function updateBallotVisualizer() {{
            const barContent = document.getElementById(\'ballotBarContent\');
            const barAction = document.getElementById(\'ballotBarAction\');
            const hasVoted = currentUser ? isStudentVoted(currentUser.id) : false;

            const keys = Object.keys(selectedChoices);
            const totalRaces = DEFAULT_POSITIONS.length;

            if (!currentUser) {{
                // Browsing Mode View
                barContent.innerHTML = `
                    <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center shrink-0 shadow-inner">
                        <i data-lucide="eye" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h4 class="font-extrabold text-xs text-slate-900">Browsing Mode Active</h4>
                            <span class="bg-blue-100 text-blue-800 text-[10px] font-extrabold px-2 py-0.5 rounded-full">Preview</span>
                        </div>
                        <p class="text-[11px] text-slate-500">Previewing ${{activeBrowsingDept}} candidate slate. Sign in to vote.</p>
                    </div>
                `;
                barAction.innerHTML = `
                    <button type="button" onclick="openSignInModal()" class="w-full sm:w-auto bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 px-6 rounded-2xl transition shadow-lg flex items-center justify-center space-x-2 text-xs">
                        <i data-lucide="log-in" class="w-4 h-4 text-amber-300"></i>
                        <span>Sign In to Cast Vote</span>
                    </button>
                `;
            }} else if (hasVoted) {{
                // Already Voted View
                barContent.innerHTML = `
                    <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center shrink-0 shadow-inner">
                        <i data-lucide="check-circle" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h4 class="font-extrabold text-xs text-slate-900">Official Ballot Cast</h4>
                            <span class="bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2 py-0.5 rounded-full">Encrypted &amp; Sealed</span>
                        </div>
                        <p class="text-[11px] text-slate-500">Your vote for ${{currentUser.dept}} has been recorded in the audit registry.</p>
                    </div>
                `;
                barAction.innerHTML = `
                    <button type="button" onclick="openReceiptModal()" class="w-full sm:w-auto bg-emerald-700 hover:bg-emerald-800 text-white font-bold py-3 px-6 rounded-2xl transition shadow-lg flex items-center justify-center space-x-2 text-xs">
                        <i data-lucide="file-text" class="w-4 h-4 text-emerald-200"></i>
                        <span>View Official Receipt</span>
                    </button>
                `;
            }} else {{
                // Active Voting In-Progress View (Clean Slate)
                const isComplete = keys.length >= totalRaces;
                barContent.innerHTML = `
                    <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center shrink-0 shadow-inner">
                        <i data-lucide="vote" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h4 class="font-extrabold text-xs text-slate-900">Your Official Ballot (${{currentUser.dept}})</h4>
                            <span class="${{isComplete ? \'bg-emerald-100 text-emerald-800\' : \'bg-amber-100 text-amber-800\'}} text-[10px] font-black px-2 py-0.5 rounded-full">
                                ${{keys.length}} of ${{totalRaces}} Selected
                            </span>
                        </div>
                        <p class="text-[11px] text-slate-500">
                            ${{isComplete ? \'All council positions selected. Ready to review and cast ballot.\' : \'Please select your candidates for each council position.\'}}
                        </p>
                    </div>
                `;
                barAction.innerHTML = `
                    <button type="button" onclick="openReviewModal()" class="w-full sm:w-auto bg-ua-navy hover:bg-blue-800 text-white font-bold py-3 px-6 rounded-2xl transition shadow-lg flex items-center justify-center space-x-2 text-xs">
                        <i data-lucide="check-square" class="w-4 h-4 text-amber-300"></i>
                        <span>Review &amp; Cast Ballot</span>
                    </button>
                `;
            }}

            lucide.createIcons();
        }}

        // ================= BALLOT REVIEW & SUBMISSION =================
        function openReviewModal() {{
            if (!currentUser) {{
                openSignInModal();
                return;
            }}

            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            const container = document.getElementById(\'reviewCandidateList\');
            
            const keys = Object.keys(selectedChoices);
            if (keys.length === 0) {{
                container.innerHTML = `
                    <div class="p-4 bg-slate-50 rounded-2xl text-center text-slate-500">
                        No candidates selected yet. Please select candidates on your ballot slate.
                    </div>
                `;
            }} else {{
                container.innerHTML = DEFAULT_POSITIONS.map(pos => {{
                    const candId = selectedChoices[pos.id];
                    const cand = allCandidates.find(c => c.id === candId);

                    return `
                        <div class="flex items-center justify-between p-3 rounded-2xl border ${{cand ? \'border-blue-100 bg-blue-50/30\' : \'border-amber-200 bg-amber-50/40\'}}">
                            <div>
                                <span class="text-[10px] font-black uppercase text-slate-400 block">${{pos.name}}</span>
                                <span class="font-extrabold text-xs text-slate-900">${{cand ? cand.name : \'<span class="text-amber-700 italic">No Selection (Abstain)</span>\'}}</span>
                            </div>
                            <div>
                                ${{cand ? renderPartyBadge(cand) : \'\'}}
                            </div>
                        </div>
                    `;
                }}).join(\'\');
            }}

            document.getElementById(\'reviewModal\').classList.remove(\'hidden\');
            lucide.createIcons();
        }}

        function closeReviewModal() {{
            document.getElementById(\'reviewModal\').classList.add(\'hidden\');
        }}

        function submitBallot() {{
            if (!currentUser) return;

            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            const deptCandidates = allCandidates.filter(c => normalizeDept(c.targetDept) === normalizeDept(currentUser.dept));
            const availablePositions = DEFAULT_POSITIONS.filter(pos => deptCandidates.some(c => c.posId === pos.id));

            const keys = Object.keys(selectedChoices);
            if (keys.length < availablePositions.length) {{
                alert(`Cannot submit incomplete ballot. You must complete your candidate choices for all available positions (${{availablePositions.length}}) before submitting.`);
                return;
            }}

            closeReviewModal();

            const timestamp = new Date().toLocaleString();
            const payload = {{
                studentId: currentUser.id,
                voterToken: currentUser.token,
                department: currentUser.dept,
                votes: selectedChoices,
                timestamp: timestamp
            }};

            const cipher = CryptoJS.AES.encrypt(JSON.stringify(payload), AES_SECRET_KEY).toString();

            // Save encrypted payload into Database with studentId
            let ballotsDb = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\')) || [];
            ballotsDb.push({{
                studentId: currentUser.id,
                voterToken: currentUser.token,
                department: currentUser.dept,
                cipherPayload: cipher,
                timestamp: timestamp
            }});
            localStorage.setItem(\'univote_encrypted_ballots_db\', JSON.stringify(ballotsDb));

            // Record vote per-student
            let votedMap = JSON.parse(localStorage.getItem(\'univote_voted_students\') || \'{{}}\');
            votedMap[currentUser.id] = true;
            localStorage.setItem(\'univote_voted_students\', JSON.stringify(votedMap));

            let choicesMap = JSON.parse(localStorage.getItem(\'univote_student_choices\') || \'{{}}\');
            choicesMap[currentUser.id] = selectedChoices;
            localStorage.setItem(\'univote_student_choices\', JSON.stringify(choicesMap));

            // Cleanse legacy global flags
            localStorage.removeItem(\'univote_has_voted\');
            localStorage.removeItem(\'univote_saved_choices\');

            applySessionLockUI();
            updateBallotVisualizer();
            renderCandidateCards();

            // Display Digital Receipt Immediately
            openReceiptModal(cipher, timestamp);
        }}

        // ================= DIGITAL RECEIPT & QR CODE =================
        function openReceiptModal(cipherPayload, timestampStr) {{
            if (!currentUser) return;

            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            const time = timestampStr || new Date().toLocaleString();

            document.getElementById(\'receiptVoterName\').innerText = currentUser.name;
            document.getElementById(\'receiptStudentId\').innerText = currentUser.id;
            document.getElementById(\'receiptVoterDept\').innerText = currentUser.dept;
            document.getElementById(\'receiptTimestamp\').innerText = time;
            document.getElementById(\'receiptToken\').innerText = currentUser.token;

            // Retrieve cipher if not passed
            let cipher = cipherPayload;
            if (!cipher) {{
                const ballots = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\')) || [];
                const b = ballots.find(x => x.studentId === currentUser.id || x.voterToken === currentUser.token);
                cipher = b ? b.cipherPayload : \'AES256-ENCRYPTED-AUDIT-TRAIL\';
            }}
            document.getElementById(\'receiptCipher\').innerText = cipher;

            // Render Choices List
            const choicesContainer = document.getElementById(\'receiptChoicesList\');
            choicesContainer.innerHTML = DEFAULT_POSITIONS.map(pos => {{
                const candId = selectedChoices[pos.id];
                const cand = allCandidates.find(c => c.id === candId);
                return `
                    <div class="flex justify-between items-center py-0.5 border-b border-slate-100 last:border-0">
                        <span class="text-slate-500 font-semibold">${{pos.name}}:</span>
                        <span class="font-bold text-slate-800">${{cand ? cand.name : \'Abstain\'}} (${{cand ? getCandidateParty(cand) : \'--\'}})</span>
                    </div>
                `;
            }}).join(\'\');

            // Generate Scannable QR Code
            const qrContainer = document.getElementById(\'receiptQrCode\');
            qrContainer.innerHTML = \'\';
            const qrContent = `UniVote-UA-Audit|Student:${{currentUser.id}}|Dept:${{currentUser.dept}}|Token:${{currentUser.token}}|Time:${{time}}`;
            
            try {{
                new QRCode(qrContainer, {{
                    text: qrContent,
                    width: 88,
                    height: 88,
                    colorDark: "#020381",
                    colorLight: "#ffffff",
                    correctLevel: QRCode.CorrectLevel.M
                }});
            }} catch (e) {{
                qrContainer.innerHTML = `<img src="https://api.qrserver.com/v1/create-qr-code/?size=88x88&data=${{encodeURIComponent(qrContent)}}" class="w-20 h-20">`;
            }}

            document.getElementById(\'receiptModal\').classList.remove(\'hidden\');
            lucide.createIcons();
        }}

        function closeReceiptModal() {{
            document.getElementById(\'receiptModal\').classList.add(\'hidden\');
        }}

        function downloadDigitalReceipt() {{
            if (!currentUser) return;
            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            let text = "==========================================================\\n";
            text += "         UNIVERSITY OF THE ASSUMPTION - UNIVOTE          \\n";
            text += "             OFFICIAL DIGITAL VOTING RECEIPT             \\n";
            text += "==========================================================\\n\\n";
            text += `STATUS             : OFFICIAL BALLOT CAST & AUDITED [VERIFIED]\\n`;
            text += `TIMESTAMP          : ${{document.getElementById(\'receiptTimestamp\').innerText}}\\n`;
            text += `STUDENT ID         : ${{currentUser.id}}\\n`;
            text += `VOTER NAME         : ${{currentUser.name}}\\n`;
            text += `INSTITUTIONAL EMAIL: ${{currentUser.email || \'N/A\'}}\\n`;
            text += `ACADEMIC DEPARTMENT: ${{currentUser.dept}}\\n`;
            text += `TRANSACTION TOKEN  : ${{currentUser.token}}\\n\\n`;
            text += "OFFICIAL BALLOT CHOICES:\\n";
            text += "----------------------------------------------------------\\n";
            
            DEFAULT_POSITIONS.forEach(pos => {{
                const candId = selectedChoices[pos.id];
                const cand = allCandidates.find(c => c.id === candId);
                const name = cand ? cand.name : \'Abstain\';
                const party = cand ? getCandidateParty(cand) : \'--\';
                text += `${{pos.name.padEnd(30)}} : ${{name}} (${{party}})\\n`;
            }});

            text += "----------------------------------------------------------\\n";
            text += `AES-256 CIPHER AUDIT:\\n${{document.getElementById(\'receiptCipher\').innerText}}\\n\\n`;
            text += "==========================================================\\n";
            text += " Institutional Commission on Elections - UA Pampanga 2026 \\n";
            text += "==========================================================\\n";

            const blob = new Blob([text], {{ type: \'text/plain;charset=utf-8\' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement(\'a\');
            a.href = url;
            a.download = `UniVote_Receipt_${{currentUser.id}}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}

        // ================= NAVIGATION TAB SWITCHER =================
        function switchMainTab(tabKey) {{
            document.querySelectorAll(\'.main-page-section\').forEach(e => e.classList.add(\'hidden\'));
            document.querySelectorAll(\'.main-nav-btn\').forEach(e => {{
                e.classList.remove(\'bg-blue-50\', \'text-ua-navy\');
                e.classList.add(\'text-slate-600\');
            }});

            const page = document.getElementById(`page-${{tabKey}}`);
            const btn = document.getElementById(`nav-btn-${{tabKey}}`);
            if (page) page.classList.remove(\'hidden\');
            if (btn) {{
                btn.classList.add(\'bg-blue-50\', \'text-ua-navy\');
                btn.classList.remove(\'text-slate-600\');
            }}

            if (tabKey === \'partylists\') renderPartylists();
            if (tabKey === \'results\') renderResultsPage();
            lucide.createIcons();
        }}

        // ================= PARTYLISTS VIEW =================
        function filterPartylists(dept) {{
            activePartylistDept = dept;
            renderPartylists();
        }}

        function renderPartylists() {{
            const container = document.getElementById(\'partylistsContainer\');
            const dept = normalizeDept(activePartylistDept);
            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            const deptCandidates = allCandidates.filter(c => normalizeDept(c.targetDept) === dept);

            const siklabCandidates = deptCandidates.filter(c => getCandidateParty(c) === \'SIKLAB\');
            const indepCandidates = deptCandidates.filter(c => getCandidateParty(c) === \'Independent\');

            let cardsHtml = \'\';

            if (siklabCandidates.length > 0) {{
                cardsHtml += `
                    <div class="bg-white rounded-3xl p-6 border-2 border-amber-200 shadow-sm space-y-4">
                        <div class="flex items-center justify-between border-b border-amber-100 pb-3">
                            <div class="flex items-center space-x-2">
                                <span class="bg-gradient-to-r from-amber-500 to-orange-500 text-white font-black text-xs px-3 py-1 rounded-full shadow-sm">SIKLAB</span>
                                <h3 class="font-extrabold text-slate-900 text-sm">Alyansang Siklab</h3>
                            </div>
                            <span class="text-[10px] font-bold text-amber-800 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200">${{siklabCandidates.length}} Slated Candidates</span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed italic">
                            "Empowering Assumptionists through transformative student leadership, dynamic campus advocacy, and transparent student representation."
                        </p>
                        <div class="space-y-2 pt-2">
                            <span class="text-[10px] font-black uppercase text-slate-400 block tracking-wider">Candidate Lineup (${{dept}}):</span>
                            <div class="space-y-1.5">
                                ${{siklabCandidates.map(c => `
                                    <div class="flex items-center space-x-2 text-xs">
                                        <img src="${{c.photo || \'/templates/ua-logo.png\'}}" class="w-6 h-6 rounded-md object-cover border" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                        <span class="font-bold text-slate-800">${{c.name}}</span>
                                        <span class="text-slate-400 text-[10px]">(${DEFAULT_POSITIONS.find(p => p.id === c.posId)?.name || c.posId})</span>
                                    </div>
                                `).join(\'\')}}
                            </div>
                        </div>
                    </div>
                `;
            }}

            if (indepCandidates.length > 0) {{
                cardsHtml += `
                    <div class="bg-white rounded-3xl p-6 border-2 border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                            <div class="flex items-center space-x-2">
                                <span class="bg-slate-100 text-slate-700 font-bold text-xs px-3 py-1 rounded-full border border-slate-200">Independent</span>
                                <h3 class="font-extrabold text-slate-900 text-sm">Independent Slate</h3>
                            </div>
                            <span class="text-[10px] font-bold text-slate-600 bg-slate-50 px-2.5 py-0.5 rounded-full border border-slate-200">${{indepCandidates.length}} Candidates</span>
                        </div>
                        <p class="text-xs text-slate-600 leading-relaxed italic">
                            Dedicated individual leadership driven by student-first values, collegiate service, and uncompromised governance.
                        </p>
                        <div class="space-y-2 pt-2">
                            <span class="text-[10px] font-black uppercase text-slate-400 block tracking-wider">Candidate Lineup (${{dept}}):</span>
                            <div class="space-y-1.5">
                                ${{indepCandidates.map(c => `
                                    <div class="flex items-center space-x-2 text-xs">
                                        <img src="${{c.photo || \'/templates/ua-logo.png\'}}" class="w-6 h-6 rounded-md object-cover border" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                        <span class="font-bold text-slate-800">${{c.name}}</span>
                                        <span class="text-slate-400 text-[10px]">(${DEFAULT_POSITIONS.find(p => p.id === c.posId)?.name || c.posId})</span>
                                    </div>
                                `).join(\'\')}}
                            </div>
                        </div>
                    </div>
                `;
            }}

            if (!cardsHtml) {{
                cardsHtml = `<div class="col-span-2 text-center text-slate-400 py-8 text-xs">No candidate partylists recorded for ${{dept}}.</div>`;
            }}

            container.innerHTML = cardsHtml;
        }}

        // ================= RESULTS VIEW =================
        function switchResultsDept(dept) {{
            activeResultsDept = dept;
            renderResultsPage();
        }}

        function renderResultsPage() {{
            const container = document.getElementById(\'resultsContentArea\');
            if (!container) return;

            const elec = JSON.parse(localStorage.getItem(\'univote_db_elections\'));
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

            const targetDept = normalizeDept(activeResultsDept);
            const allCandidates = JSON.parse(localStorage.getItem(\'univote_db_candidates\')) || DEFAULT_CANDIDATES;
            const deptCandidates = allCandidates.filter(c => normalizeDept(c.targetDept) === targetDept);
            const ballots = JSON.parse(localStorage.getItem(\'univote_encrypted_ballots_db\')) || [];
            const deptBallots = ballots.filter(b => normalizeDept(b.department) === targetDept);

            // Compute tallies
            const tallies = {{}};
            deptBallots.forEach(b => {{
                try {{
                    const bytes = CryptoJS.AES.decrypt(b.cipherPayload, AES_SECRET_KEY);
                    const p = JSON.parse(bytes.toString(CryptoJS.enc.Utf8));
                    const votes = p.votes || {{}};
                    Object.keys(votes).forEach(posId => {{
                        const candId = votes[posId];
                        if (!tallies[posId]) tallies[posId] = {{}};
                        tallies[posId][candId] = (tallies[posId][candId] || 0) + 1;
                    }});
                }} catch (e) {{}}
            }});

            const totalVotes = deptBallots.length;

            let html = `
                <div class="bg-blue-50/70 border border-blue-200 rounded-3xl p-6 flex flex-col md:flex-row items-center justify-between gap-4">
                    <div>
                        <h3 class="font-black text-lg text-blue-950">${{targetDept}}</h3>
                        <p class="text-xs text-blue-700">Total Encrypted Ballots Cast: <span class="font-black text-sm">${{totalVotes}}</span></p>
                    </div>
                    <span class="bg-emerald-100 text-emerald-800 text-xs font-black px-3.5 py-1.5 rounded-full border border-emerald-200 flex items-center space-x-1.5">
                        <i data-lucide="check-circle" class="w-4 h-4"></i>
                        <span>Published by UA COMELEC</span>
                    </span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            `;

            DEFAULT_POSITIONS.forEach(pos => {{
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
                    <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-sm">
                        <div class="border-b pb-2 flex items-center justify-between">
                            <h4 class="font-extrabold text-xs text-slate-900 uppercase tracking-wider">${{pos.name}}</h4>
                            <span class="text-[10px] font-bold text-slate-400">${{posCands.length}} Candidates</span>
                        </div>
                        <div class="space-y-2.5">
                            ${{posCands.map(c => {{
                                const count = (tallies[pos.id] && tallies[pos.id][c.id]) || 0;
                                const pct = totalVotes > 0 ? ((count / totalVotes) * 100).toFixed(1) : \'0.0\';
                                const isLead = c.id === leaderId && count > 0;
                                return `
                                    <div class="rounded-xl border ${{isLead ? \'border-amber-300 bg-amber-50/50\' : \'border-slate-100 bg-slate-50\'}} p-2.5 space-y-1">
                                        <div class="flex items-center justify-between text-xs">
                                            <div class="flex items-center space-x-1.5 truncate">
                                                <img src="${{c.photo || \'/templates/ua-logo.png\'}}" class="w-6 h-6 rounded-md object-cover border shrink-0" onerror="this.onerror=null; this.src=\'/templates/ua-logo.png\';">
                                                <span class="font-bold text-slate-900 truncate">${{c.name}}</span>
                                                ${{isLead ? \'<span class="bg-amber-500 text-white font-black text-[8px] px-1.5 py-0.2 rounded-full uppercase">LEAD</span>\' : \'\'}}
                                            </div>
                                            <span class="font-black text-slate-900 shrink-0 ml-2">${{count}}</span>
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

            html += `</div>`;
            container.innerHTML = html;
            lucide.createIcons();
        }}
    </script>
</body>
</html>\'\'\'
'''

# Lab 5: AI Agents - Terminal-Based AI Operations
## CISC 395 - Applied Generative AI and LLM Applications

**Due:** [Date specified on Blackboard]

**Submission:** Upload to Blackboard — `Lab05_YourName.md` + generated files (see checklist)

---

## Prerequisites

**Complete before the lab begins.**

### Set Up Your Workspace and Download Lab Files

Open VS Code, then open the `CISC395/` folder (`File > Open Folder`). Open the integrated terminal (`` Ctrl+Shift+` `` on Windows, `` Cmd+Shift+` `` on Mac). Run:

```bash
mkdir Lab05
cd Lab05

# Download (curl is built-in on Mac and Windows 10/11)
curl -o Lab05.zip "https://raw.githubusercontent.com/tisage/CISC395/refs/heads/main/Lab05/Lab05.zip"

# Unzip (Mac / Linux)
unzip Lab05.zip

# Unzip (Windows)
tar -xf Lab05.zip

cd ..
```

Verify structure from the workspace root:

```bash
tree Lab05        # Mac/Linux
tree /F Lab05     # Windows
```

Expected:
```
Lab05/
├── data/
│   └── student_grades.csv
├── code/
│   ├── calculator.py
│   └── buggy_sort.py
├── messy/
│   └── [10 poorly-named files]
└── papers/
    └── [research paper PDF]
```

---

## Overview

| Exercise | Topic | Deliverable |
|----------|-------|-------------|
| 1 | Workspace Setup and Context File | `GEMINI.md` + answers in this file |
| 2 | AI-Powered Paper Reading | `papers/paper_summary.md` + answers in this file |
| 3 | Grade Data Analysis | `data/grade_report.md` + answers in this file |
| 4 | Digital Organization Challenge | reorganized `messy/` + answers in this file |
| Reflection | | answers in this file |

**No coding required.** All exercises use terminal AI sessions.

**How to enter a session:**
```bash
gemini       # Gemini CLI
copilot      # GitHub Copilot CLI
```

---

## Exercise 1: Workspace Setup and Context File (20 points)

### Part A: Enter Your First Session

Navigate into `Lab05/` and start a session:

```bash
cd Lab05
gemini
```

Approve the folder trust prompt when it appears.

**Screenshot:** Take a screenshot of the session start (`screenshot_01.png`).

---

### Part B: Create Your GEMINI.md

Inside the session, ask AI to draft a `GEMINI.md` context file for this project and save it:

**The prompt you used:**
```
[Paste your exact prompt here]
```

After saving, verify it loaded:
```
> /memory show
```

**`/memory show` output (first 3–5 lines is enough):**
```
[Paste just enough to confirm the context file was loaded]
```

> `GEMINI.md` will be submitted as a separate file — do not paste its full content here.

---

### Part C: Test Your Context

With `GEMINI.md` loaded, ask AI about `code/buggy_sort.py` — without describing it yourself:

```
> Look at code/buggy_sort.py and explain what it does. Is there a bug?
```

**AI's response:**
```
[Paste the full response here]
```

**Reflection:** Did AI correctly identify the bug without any hints? Did having `GEMINI.md` make a difference compared to asking cold? (2–3 sentences)

```
[Your answer]
```

---

## Exercise 2: AI-Powered Paper Reading (30 points)

### Required Sections

Your `paper_summary.md` must contain all five sections:

| # | Section | What it should cover |
|---|---------|----------------------|
| 1 | **Introduction** | What the paper proposes and its key contribution |
| 2 | **Core Principles** | The key technical idea or methodology |
| 3 | **Impact and Influence** | Why this paper matters and how widely adopted |
| 4 | **Influence on Modern AI** | How the paper's ideas appear in today's systems |
| 5 | **Relevance to Your Major** | How this connects to your major/career — your own words |

### Write and Run Your Prompt

Write a prompt that reads the PDF, applies at least two techniques from Units 2–3, requires all five sections, and saves the result as `papers/paper_summary.md`.

**Your prompt:**
```
[Write your complete prompt here]

Techniques used: [e.g., "Role Prompting + Structured Output"]
```

> `papers/paper_summary.md` will be submitted as a separate file — do not paste its content here.

**Reflection:**

1. Which section did AI handle best? Which was weakest? Why? (2–3 sentences)

```
[Your answer]
```

2. Did you need to refine your prompt or ask follow-up questions? What worked and what did not? (2–3 sentences)

```
[Your answer]
```

---

## Exercise 3: Grade Data Analysis (25 points)

### Part A: Explore the Data

Ask at least three different questions about `data/student_grades.csv`. For each, paste your prompt and the AI's response.

**Suggested questions (choose 3 or write your own):**
- What is the grade distribution (A/B/C/D/F)?
- Who are the top 3 students by total score?
- Which students are at risk (below 70%)?
- What is the class average, highest, and lowest score?

---

**Question 1 — Your prompt:**
```
[Paste your prompt]
```
**AI's response:**
```
[Paste response]
```

---

**Question 2 — Your prompt:**
```
[Paste your prompt]
```
**AI's response:**
```
[Paste response]
```

---

**Question 3 — Your prompt:**
```
[Paste your prompt]
```
**AI's response:**
```
[Paste response]
```

---

### Part B: Generate a Grade Report

Ask AI to synthesize findings into `data/grade_report.md` (class stats, top performers, students needing support, one recommendation).

**Your prompt:**
```
[Paste your prompt here]
```

**Verify the file was created** (paste one line of terminal output):
```
[e.g.,   dir data   →   student_grades.csv   grade_report.md]
```

> `data/grade_report.md` will be submitted as a separate file — do not paste its content here.

---

## Exercise 4: Digital Organization Challenge (15 points)

### Part A: Show the Current State

Run `dir messy` (Windows) or `ls messy` (Mac/Linux) and paste the output:

```
[Paste terminal output showing all 10 files]
```

---

### Part B: Ask AI to Propose an Organization Plan

Ask AI to analyze `messy/`, propose a folder structure as a tree diagram, assign each file to a subfolder with a reason, and suggest better names — **without moving anything yet**.

**Your prompt:**
```
[Paste your prompt here]
```

**AI's proposed plan:**
```
[Paste the tree structure, file assignments, and naming suggestions]
```

---

### Part C: Evaluate and Implement

**Your evaluation:** Do you agree with the plan? What would you change? (2–3 sentences)

```
[Your answer]
```

Ask AI to execute the plan. Show the result:

```bash
tree messy        # Mac/Linux
tree /F messy     # Windows
```

**`tree messy` output after reorganization:**
```
[Paste here]
```

---

## Reflection (10 points)

**1. Session vs. Single Command**

This lab used session-based interaction where AI built up context across multiple messages. How did that change the quality of results compared to asking one-off questions? Give a specific example from your session. (3–4 sentences)

```
[Your answer]
```

**2. Permissions**

Describe one moment where AI asked your permission before taking an action. What did it want to do, and did you review the content before approving? (2–3 sentences)

```
[Your answer]
```

**3. One Real Use Case**

Name one task from your actual student or professional life that you will use terminal AI for after this lab. Be specific: what folder, what prompt, what output. (2–3 sentences)

```
[Your answer]
```

---

## Submission Checklist

**Upload all of the following to Blackboard:**

- [ ] `Lab05_YourName.md` — this file, fully filled in
- [ ] `GEMINI.md` — your context file (from Exercise 1B)
- [ ] `papers/paper_summary.md` — AI-generated paper summary (from Exercise 2)
- [ ] `data/grade_report.md` — AI-generated grade report (from Exercise 3B)
- [ ] `screenshot_01.png` — session start screenshot (from Exercise 1A)

> The reorganized `messy/` folder is verified by the `tree` output pasted in Exercise 4C — no separate upload needed.

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Exercise 1** | **20** | |
| Screenshot (session start) | 5 | Screenshot shows successful session with folder authorization |
| Prompt + `/memory show` | 8 | Prompt is complete; `/memory show` confirms context loaded |
| Code context test | 7 | AI response pasted; reflection shows understanding of why context helps |
| **Exercise 2** | **30** | |
| Prompt design (2+ techniques) | 10 | Techniques named and correctly applied |
| `paper_summary.md` (submitted file) | 15 | All 5 sections present and substantive; Section 5 in student's own words |
| Reflection | 5 | Honest evaluation of AI output quality |
| **Exercise 3** | **25** | |
| 3 prompts + AI responses | 15 | Questions are specific; responses are accurate and informative |
| `grade_report.md` (submitted file) | 10 | Report includes stats, insights, and a recommendation |
| **Exercise 4** | **15** | |
| Before state shown | 3 | All 10 files visible in terminal output |
| Organization prompt + AI plan | 8 | Plan is logical; student evaluates it critically |
| Tree output after reorganization | 4 | Files moved and renamed; folder structure visible |
| **Reflection** | **10** | |
| Session context reflection | 4 | Specific example cited |
| Permissions moment | 3 | Concrete example from the session |
| Future use case | 3 | Realistic and specific |
| **Total** | **100** | |

---

## Common Commands Reference

**Navigation**

| Task | Windows | Mac / Linux |
|------|---------|-------------|
| Show current path | `cd` | `pwd` |
| Go into a folder | `cd Lab05` | `cd Lab05` |
| Go up one level | `cd ..` | `cd ..` |
| List files | `dir` | `ls` |
| List a subfolder | `dir data` | `ls data` |
| Show folder tree | `tree /F` | `tree` |

**Gemini CLI**

| Command | What it does |
|---------|--------------|
| `gemini` | Enter an interactive session |
| `/memory show` | Display loaded GEMINI.md context |
| `/memory refresh` | Reload GEMINI.md after editing |
| `/compress` | Compress long conversation |
| `/quit` | Exit the session |

**GitHub Copilot CLI**

| Command | What it does |
|---------|--------------|
| `copilot` | Enter an interactive session |
| `/compact` | Compress long conversation |
| `/quit` | Exit the session |

---

**Estimated time:** 90 minutes in class, with optional finishing at home

**End of Lab 5**

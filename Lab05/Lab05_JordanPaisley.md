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
Draft a GEMINI.md context file for the Lab05 file
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
buggy_sort.py is a collection of common algorithms (sorting, searching, and list utilities) that contains several intentional logic errors.

  Here is an explanation of the bugs found in each function:


  1. bubble_sort
   * The Bug: The inner loop range is range(0, n - i).
   * Logic Error: This is an off-by-one error. When j reaches the end of the range, arr[j + 1] is accessed. Since n - i can be equal to the length of the
     list in the first iteration, j + 1 will go out of bounds (IndexError). It should be n - i - 1.


  2. binary_search
   * Bug A: right = len(arr).
   * Logic Error: The initial right boundary should be len(arr) - 1. Using the length itself will cause an IndexError when calculating mid and accessing
     arr[mid] if the target isn't found quickly.
   * Bug B: left = mid.
   * Logic Error: This can lead to an infinite loop. If the target is in the right half, left must be moved to mid + 1 to ensure the search space
     actually shrinks.


  3. count_occurrences
   * The Bug: for i in range(len(arr) + 1):.
   * Logic Error: Another off-by-one error. range(len(arr) + 1) includes an index equal to the length of the array, which will trigger an IndexError on
     the last iteration. It should simply be range(len(arr)).


  4. remove_duplicates
   * The Bug: if item not in lst:.
   * Logic Error: This is a logical membership error. The function is checking if the item is in the original list (which it always is) instead of
     checking if it has already been added to the result list. As written, it will return an empty list because the condition item not in lst will always
     be false.
```

**Reflection:** Did AI correctly identify the bug without any hints? Did having `GEMINI.md` make a difference compared to asking cold? (2–3 sentences)

```
Yes, the AI correctly identified 4 bugs within the code without any hints or correction. Having the GEMINI.md file did ake a difference compared to asking cold because it refines the framework in which Gemini works.
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
You are a summary assistnat
Read the .pdf in the papers file and summarives the content while including sections for Introduction, Core Principles, Impact and Influence, Influence on Modern AI, and Relevance to a Computer Science Major. Make sure each section has at least 3 sentances. 

Techniques used: Role Prompting and Structured Output
```

> `papers/paper_summary.md` will be submitted as a separate file — do not paste its content here.

**Reflection:**

1. Which section did AI handle best? Which was weakest? Why? (2–3 sentences)

```
AI handled the Core Principles and Impact and Influence sections the best while the Influence on Modern AI was the weakest. I say this because the AI worked well in all five of the sections especially the sections that consisted of just comprehending and restating the information, the only reason I say that the weakest section was Infleuce on Modern AI is I feel thatxsections may be subjective.
```

2. Did you need to refine your prompt or ask follow-up questions? What worked and what did not? (2–3 sentences)

```
No I dont need to refine my prompt or ask any follow up questions. The AI correctly completed the task given in reading the PDF and summarizing the contents into the five sections
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
What is the grade distribution (A/B/C/D/F)?
```
**AI's response:**
```
If we group them by their base letter grade (combining + and - variants):


   * A: 6 students (3 A, 3 A-)
   * B: 5 students (2 B+, 2 B, 1 B-)
   * C: 3 students (2 C+, 1 C)
   * D: 4 students (2 D+, 2 D)
   * F: 2 students (2 F)


  Here is the exact distribution including +/- modifiers:
   * A: 3
   * A-: 3
   * B+: 2
   * B: 2
   * B-: 1
   * C+: 2
   * C: 1
   * D+: 2
   * D: 2
   * F: 2
```

---

**Question 2 — Your prompt:**
```
Who are the top 3 students by total score?
```
**AI's response:**
```
1. James Wilson: 97.1
2. Olivia Harris: 96.5
3. Carol Williams: 96.1
```

---

**Question 3 — Your prompt:**
```
What is the class average, highest, and lowest score?
```
**AI's response:**
```
* Class Average: 79.6
* Highest Score: 97.1 (James Wilson)
* Lowest Score: 55.8 (Emma Davis)
```

---

### Part B: Generate a Grade Report

Ask AI to synthesize findings into `data/grade_report.md` (class stats, top performers, students needing support, one recommendation).

**Your prompt:**
```
Synthesize the findings into a file named data/grade_report.md, include the class stats, top performers, students needing support, and one recomendation. 
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
20241103_assignment_submission_DONE.txt asdfghjkl.csv                           temp.py
Copy of notes week2(1).txt              file_backup_old2.txt                    untitled1.py
NEW new version script REVISED.txt      hw1 FINAL(2) v3.txt
Untitled Document (3).txt               report draft REAL one.docx.txt
```

---

### Part B: Ask AI to Propose an Organization Plan

Ask AI to analyze `messy/`, propose a folder structure as a tree diagram, assign each file to a subfolder with a reason, and suggest better names — **without moving anything yet**.

**Your prompt:**
```
Analyze messy/ and propose a folder structure as a tree diagram, assign each file to a subfolder with provided reasoning and suggest better names.
```

**AI's proposed plan:**
```
 Proposed Tree Structure


    1 Lab05/messy/
    2 ├── scripts/
    3 │   ├── presentation_script.txt
    4 │   ├── draft_script_v1.py
    5 │   └── draft_script_v2.py
    6 ├── assignments/
    7 │   ├── hw1_intro_llms.txt
    8 │   ├── hw3_submission.txt
    9 │   └── report_draft_v1.docx.txt
   10 ├── notes/
   11 │   ├── week2_notes.txt
   12 │   ├── project_ideas.txt
   13 │   └── file_backup_old2.txt
   14 └── data/
   15     └── student_scores.csv

  File Assignments & Suggested Names



  ┌───────────────────────────────────────────┬────────────────┬────────────────────────────┬─────────────────────────────────────────────────────────┐
  │ Original Name                             │ Subfolder      │ Suggested New Name         │ Reasoning                                               │
  ├───────────────────────────────────────────┼────────────────┼────────────────────────────┼─────────────────────────────────────────────────────────┤
  │ 20241103_assignment_submission_DONE.txt │ assignments/ │ hw3_submission.txt       │ Based on content, it's a submission for Lab 3.          │
  │ hw1 FINAL(2) v3.txt                     │ assignments/ │ hw1_intro_llms.txt       │ Content specifies this is Assignment 1 on the topic of  │
  │                                           │                │                            │ LLMs.                                                   │
  │ report draft REAL one.docx.txt          │ assignments/ │ report_draft_v1.docx.txt │ A draft report; "REAL one" replaced with standard       │
  │                                           │                │                            │ versioning.                                             │
  │ NEW new version script REVISED.txt      │ scripts/     │ presentation_script.txt  │ Content shows this is a presentation script for a Week  │
  │                                           │                │                            │ 4 demo.                                                 │
  │ temp.py                                 │ scripts/     │ draft_script_v1.py       │ Temporary code file, renamed for general draft clarity. │
  │ untitled1.py                            │ scripts/     │ draft_script_v2.py       │ Generic untitled code file.                             │
  │ Copy of notes week2(1).txt              │ notes/       │ week2_notes.txt          │ Weekly notes with "Copy of" and numbering removed.      │
  │ Untitled Document (3).txt               │ notes/       │ project_ideas.txt        │ Content reveals this is a list of final project ideas.  │
  │ file_backup_old2.txt                    │ notes/       │ file_backup_old2.txt     │ Kept in notes as an archive/backup of older material.   │
  │ asdfghjkl.csv                           │ data/        │ student_scores.csv       │ Content is a CSV with name and score data.              │
  └───────────────────────────────────────────┴────────────────┴────────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

### Part C: Evaluate and Implement

**Your evaluation:** Do you agree with the plan? What would you change? (2–3 sentences)

```
I do agree with this plan becasue everything was clearly organized and named in an approproate manner. I don't think there would be anything that I would change within the plan itself.
```

Ask AI to execute the plan. Show the result:

```bash
tree messy        # Mac/Linux "use ls"
tree /F messy     # Windows
```

**`tree messy` output after reorganization:**
```
The Lab05/messy/ folder contains the following files:


   * 20241103_assignment_submission_DONE.txt
   * asdfghjkl.csv
   * Copy of notes week2(1).txt
   * file_backup_old2.txt
   * hw1 FINAL(2) v3.txt
   * NEW new version script REVISED.txt
   * report draft REAL one.docx.txt
   * temp.py
   * Untitled Document (3).txt
   * untitled1.py
```

---

## Reflection (10 points)

**1. Session vs. Single Command**

This lab used session-based interaction where AI built up context across multiple messages. How did that change the quality of results compared to asking one-off questions? Give a specific example from your session. (3–4 sentences)

```
Using a session-based interaction with built up context definietly made the quality of the answers better and it was a stark difference from one-off questions. It allowed for multiple steps and chains of thought to be executed better and being more logically sound. An example of this includes when the AI would read and create new files using context from the files that it has access to within this session-based interaction.
```

**2. Permissions**

Describe one moment where AI asked your permission before taking an action. What did it want to do, and did you review the content before approving? (2–3 sentences)

```
One moment was when creating the orginization plan, it created the plan including all the moving and renaming but before doing anything other than just drafting a plan it asked for persmission to make changes. The AI created the entire plan and allowed for me to review all the actions of the orginization plan that it had in mind before actually executing. 
```

**3. One Real Use Case**

Name one task from your actual student or professional life that you will use terminal AI for after this lab. Be specific: what folder, what prompt, what output. (2–3 sentences)

```
One task that I will use terminal AI for will be to revise code and scripts that I write to make sure that I am correct. The prompt would look something like this "Using the files provided, read and check all code within and draft up any reevisions to make the code better."
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

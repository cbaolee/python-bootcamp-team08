# Study Planner - Usage Demo

A short demo of the team study planner (T-W3). For the full description of modules and options, see [`shared/study_planner/README.md`](../shared/study_planner/README.md).

## 1. Setup

```bash
git clone https://github.com/cbaolee/python-bootcamp-team08.git
cd python-bootcamp-team08
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install pytest ruff
```

## 2. Input

`samples/tasks.csv`:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## 3. Make a plan

We have 2 hours tonight, and today is 2026-10-26:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

Output:

```
Tonight (2.0 h):
1. Assignment - 1.5 h
2. DS exam - 0.5 h
```

Why this order?

| Task       | Days left | Score = importance / days left |
| ---------- | --------- | ------------------------------ |
| Assignment | 1         | 4 / 1 = 4.0                    |
| DS exam    | 4         | 5 / 4 = 1.25                   |

The Assignment has the higher score, so it goes first and gets all 1.5 h it needs. The remaining 0.5 h goes to the DS exam.

Without `--today` the tool uses the real date of today, so the result changes from day to day.

## 4. Export the plan to JSON

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26 --export-json plan.json
```

The plan is printed as before, and `plan.json` is created:

```json
[
  {
    "task": {
      "title": "Assignment",
      "importance": 4,
      "effort_h": 1.5,
      "deadline": "2026-10-27"
    },
    "hours": 1.5
  },
  {
    "task": {
      "title": "DS exam",
      "importance": 5,
      "effort_h": 6.0,
      "deadline": "2026-10-30"
    },
    "hours": 0.5
  }
]
```

## 5. See what the tool is doing

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26 --verbose
```

Extra DEBUG lines are printed (the time will be different on your machine):

```
2026-10-26 20:00:00 - DEBUG - Reading file...
2026-10-26 20:00:00 - DEBUG - Prioritising tasks...
2026-10-26 20:00:00 - DEBUG - Allocating time for plan...
Tonight (2.0 h):
1. Assignment - 1.5 h
2. DS exam - 0.5 h
```

## 6. Errors

All errors go to stderr and the exit code is 1.

**File does not exist**

```bash
python -m shared.study_planner nofile.csv --hours 2
```

```
Error: file not found: nofile.csv
```

**Bad data in the CSV** (`samples/tasks_bad.csv` has `high` as an importance value on line 3):

```bash
python -m shared.study_planner samples/tasks_bad.csv --hours 2
```

```
Error: Invalid data format at 3
```

**Empty CSV** (only the header line, or an empty file):

```
Error: CSV file is empty or has no data rows
```

Check the exit code:

```bash
python -m shared.study_planner nofile.csv --hours 2
echo $?        # prints 1  (on Windows PowerShell: echo $LASTEXITCODE)
```

## 7. Run the tests

```bash
pytest -q
ruff check
```

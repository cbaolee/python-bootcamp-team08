# Study Planner

A small command-line tool that turns a CSV list of tasks into a study plan for tonight. It ranks the tasks by priority and then fills the available hours.

## Pipeline

```
CSV file -> parse_csv -> prioritise -> allocate -> render -> text plan
                                          |
                                          +-> export_json -> JSON file (optional)
```

## Quick start

Run from the repository root:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
```

Output:

```
Tonight (2.0 h):
1. Assignment - 1.5 h
2. DS exam - 0.5 h
```

## Input format

A CSV file with a header row and exactly four columns:

| Column       | Type              | Meaning                                             |
| ------------ | ----------------- | --------------------------------------------------- |
| `title`      | text              | name of the task                                    |
| `importance` | integer           | how important the task is (higher = more important) |
| `effort_h`   | number            | hours the task needs                                |
| `deadline`   | date `YYYY-MM-DD` | due date                                            |

Example (`samples/tasks.csv`):

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## Command-line arguments

```
python -m shared.study_planner <file_path> --hours HOURS [--today YYYY-MM-DD] [--verbose] [--export-json PATH]
```

| Argument             | Required | Description                                                                                                       |
| -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `file_path`          | yes      | path to the CSV file with tasks                                                                                   |
| `--hours`            | yes      | hours available for studying (a number, for example `2` or `1.5`)                                                 |
| `--today`            | no       | the date to use as "today", format `YYYY-MM-DD`. Default: the real date today. Use it to get reproducible results |
| `--verbose`          | no       | print DEBUG log messages for each step                                                                            |
| `--export-json PATH` | no       | also write the allocated blocks to a JSON file                                                                    |

## Modules

| Module                        | Main function                      | Input                  | Output                  | What it does                                             |
| ----------------------------- | ---------------------------------- | ---------------------- | ----------------------- | -------------------------------------------------------- |
| `shared/contract.py`          | `Task`, `Block`                    | -                      | dataclasses             | shared data types used by every module                   |
| `shared/errors.py`            | `InfeasiblePlan`, `check_feasible` | tasks, available hours | raises `InfeasiblePlan` | error type for plans that need more hours than available |
| `study_planner/parse.py`      | `parse_csv(path)`                  | CSV path               | `list[Task]`            | reads the CSV and validates every row                    |
| `study_planner/prioritise.py` | `prioritise(tasks, today)`         | tasks, date            | sorted `list[Task]`     | sorts tasks by priority score                            |
| `study_planner/allocate.py`   | `allocate(tasks, hours)`           | sorted tasks, hours    | `list[Block]`           | gives hours to tasks one by one                          |
| `study_planner/render.py`     | `render(blocks)`                   | blocks                 | `str`                   | builds the text plan                                     |
| `study_planner/export.py`     | `export_json(blocks, path)`        | blocks, path           | JSON file               | saves the plan as JSON                                   |
| `study_planner/summary.py`    | `summarize(blocks)`                | blocks                 | `dict`                  | counts blocks and tasks and sums hours per task          |
| `study_planner/__main__.py`   | `main()`                           | command-line arguments | printed plan            | connects all steps above (the CLI)                       |

### Data types

```python
@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date


@dataclass
class Block:
    task: Task
    hours: float
```

### Priority rule

```
score = importance / days_left      (days_left = deadline - today)
```

- A higher score is planned first.
- A task that is due today or already late (`days_left <= 0`) gets an infinite score, so it is always first.
- If two scores are equal, the task with the higher importance goes first.

Example with `--today 2026-10-26`: Assignment = 4 / 1 = 4.0, DS exam = 5 / 4 = 1.25. So Assignment comes first.

### Allocation rule

`allocate` goes through the sorted tasks. Each task gets `min(effort_h, remaining_hours)`. It stops when no hours are left. A task can get less time than it needs when the hours run out.

## Output

`render` prints the total planned hours and one numbered line per block. If there is nothing to schedule it prints `No tasks scheduled.`

With `--export-json plan.json`, the file contains a list of blocks, and dates are written as `YYYY-MM-DD`:

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
  }
]
```

## Error handling

All errors go to stderr and the program exits with code 1.

| Situation                                                        | Message                                                             |
| ---------------------------------------------------------------- | ------------------------------------------------------------------- |
| CSV file does not exist                                          | `Error: file not found: <path>`                                     |
| CSV has a header but no data rows (or is empty)                  | `Error: CSV file is empty or has no data rows`                      |
| A row does not have 4 columns                                    | `Error: Invalid number of columns at line <n>`                      |
| A value cannot be converted (for example `importance` is `high`) | `Error: Invalid data format at <n>`                                 |
| `--today` is not a valid date                                    | `<time> - ERROR - Error: --today must have correct form YYYY-MM-DD` |

Note: `InfeasiblePlan` and `check_feasible` exist in `shared/errors.py` and the CLI handles the error, but the CLI does not call `check_feasible` now. If `--hours` is smaller than the total effort, the CLI still runs and plans only part of the work. If you call check_feasible yourself, it raises InfeasiblePlan: need 7.5 h but only 2.0 h available.

## Logging

By default the tool logs at INFO level. With `--verbose` it also prints DEBUG messages (reading the file, prioritising, allocating):

```
2026-10-26 20:00:00 - DEBUG - Reading file...
2026-10-26 20:00:00 - DEBUG - Prioritising tasks...
2026-10-26 20:00:00 - DEBUG - Allocating time for plan...
```

## Tests

```bash
pytest -q       # all tests, including the end-to-end test
ruff check      # code style
```

The end-to-end test is in `tests/test_end_to_end.py`.

## See also

A short step-by-step demo: [`docs/study_planner.md`](../../docs/study_planner.md)

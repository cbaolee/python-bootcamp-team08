# Team conventions

## 1. Branch names

| Use                    | Name                           | Example                       |
| ---------------------- | ------------------------------ | ----------------------------- |
| New capability         | `feat/<issue>-<short-name>`    | `feat/12-fee-calculator`      |
| Bug fix                | `fix/<issue>-<short-name>`     | `fix/15-router-empty-message` |
| Documentation          | `docs/<issue>-<short-name>`    | `docs/8-conventions`          |
| Tests                  | `test/<issue>-<short-name>`    | `test/20-eval-cases`          |
| Tooling, CI, config    | `chore/<issue>-<short-name>`   | `chore/3-issue-templates`     |
| Weekly Python homework | `py/w<week>-<github-username>` | `py/w1-tuongvii2327`          |

Rules:

- Add the issue number when there is one.
- Use lowercase letters, digits and hyphens only. No spaces, no Vietnamese diacritics.
- Create every branch from an up-to-date `main`: `git switch main`, `git pull`, then `git switch -c <name>`.
- Never commit or push directly to `main`.
- After the PR is merged, delete the branch locally and on GitHub.

## 2. Commit messages

Format (Conventional Commits):

```
<type>(<scope>): <short summary in imperative mood>

<optional body: why the change was needed>

<optional footer: Closes #12, Co-authored-by: ...>
```

| Type       | Meaning                               |
| ---------- | ------------------------------------- |
| `feat`     | a new capability                      |
| `fix`      | a bug fix                             |
| `docs`     | documentation only                    |
| `test`     | adding or fixing tests                |
| `refactor` | restructure code, no behaviour change |
| `perf`     | faster or cheaper, same behaviour     |
| `style`    | formatting only                       |
| `chore`    | tooling, dependencies, CI             |

Rules:

- One commit, one idea.
- Messages like "update", "fix stuff", "WIP" or "lab1" are not accepted.
- Homework: commit after each exercise, at least 5 commits per week, for example `feat(py-w1): W1-2 word counter`.
- Use the same email in Git as in your GitHub account, so commits are linked to you.

## 3. Issues, pull requests and merging

- Every piece of work starts as an issue made from a template in `.github/ISSUE_TEMPLATE/`. Labels and milestones are set on the issue.
- Homework PR title: `py-w1: <github-username>`. Put `Closes #<issue>` in the description and request your rotation reviewer.
- Other PR titles follow the commit format, for example `chore: add issue and pull request templates`.
- Fill in the PR template: What, Why, How tested, AI use, Checklist.
- Keep a PR small and focused (about 300 lines or fewer). No secrets, no files larger than 5 MB.
- A homework PR counts as submitted only when it is merged, CI is green and the assigned reviewer approved it.
- Merge with "Squash and merge", then delete the branch.

## 4. Folder structure

```
python-bootcamp-team08/
├── README.md
├── PROGRESS.md              # one row per member per week, with PR links
├── .github/                 # templates, CI workflow
├── docs/                    # team documents
├── members/
│   └── <member_folder>/
│       ├── w1/
│       ├── w2/
│       └── w3/
├── shared/
│   └── study_planner/       # team code (T-W2, T-W3)
└── tests/                   # tests provided by the instructor
```

Each member writes code only inside their own folder for individual exercises.

## 5. File names

- Normal files: `snake_case`, with no spaces and no Vietnamese diacritics. Example: `text_tools.py`, `team_notes.md`.
- Special files: `UPPERCASE`. Example: `README.md`, `PROGRESS.md`, `CONTRIBUTING.md`.
- Exercise files: use exactly the names the exercise gives, because the instructor's tests import them.

## 6. Python code convention

### 6.1 Tools

- Format with `ruff format`, check with `ruff check`. Do not format by hand.
- Run `pytest -q` before every commit. Tests must pass. Never delete, skip or weaken a test to make it pass.
- CI runs `ruff check` and `pytest -q` on every PR.

### 6.2 Layout and naming

| Item                          | Style              |
| ----------------------------- | ------------------ |
| Indentation                   | 4 spaces, no tabs  |
| Variables, functions, methods | `snake_case`       |
| Modules (files)               | `snake_case`       |
| Classes                       | `PascalCase`       |
| Constants                     | `UPPER_SNAKE_CASE` |
| Private helpers               | leading underscore |

Function names and signatures that an exercise gives must be copied exactly, because the instructor's tests import them.
Use clear, descriptive names. Avoid one-letter names except short loop counters.

### 6.3 Language rules

- Add type hints to every function.
- Add a docstring to every public function and class.
- Never use a mutable default argument. Use `None` and create the value inside the function.
- Assigning a list to another name does not copy it. Copy it explicitly.
- Prefer idioms: `enumerate`, `zip`, comprehensions, `dict.get`.
- Open files with `with open(...)` and `encoding="utf-8"`.
- `input()` always returns a string. Convert it yourself.
- Put imports at the top of the file, one per line, in this order: standard library, third-party, our own code.
- Runnable files use the `if __name__ == "__main__":` guard.
- Test functions are named `test_<what_it_checks>`.
- Line length and quote style follow the `ruff format` defaults.

### 6.4 Comments

- Explain why, not the obvious what.
- Write comments and docstrings in English, with simple words.
- Do not leave dead code or debug prints in a PR.

## 7. Before you open a PR

- [ ] Branch name follows section 1.
- [ ] Commit messages follow section 2.
- [ ] PR title and description follow section 3, and the reviewer is the one in the rotation.
- [ ] Folders and files follow sections 4 and 5.
- [ ] Code follows section 6: `ruff check`, `ruff format` and `pytest -q` pass.
- [ ] No secrets, no personal data, no machine-specific files.

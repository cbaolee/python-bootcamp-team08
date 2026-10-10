# Python Bootcamp - Team 08 (25C11)

This is the Python Bootcamp homework repository of Team 08, class 25C11, for CSC10014 - Computational Thinking. We use it to learn the fundamentals of Python and to practice Git and GitHub team workflows.

## Team members

| No. | Name | Student ID | GitHub username |
|-----|------|------------|-----------------|
| 1 | Lê Chí Bảo | 25127017 | cbaolee |
| 2 | Huỳnh Gia Đạt | 25127032 | hgdat2534 |
| 3 | Trịnh Trần Hương Mai | 25127212 | hmai |
| 4 | Cao Thanh Kim Hoa | 25127333 | paikabluu |
| 5 | Nguyễn Quốc Tuấn | 25127248 | SilvQT |
| 6 | Thái Mạc Tường Vi | 25127559 | tuongvii2327 |

## Prerequisites

- Python: 3.12.0+
- Git: 2.54.0+

## Setup

To set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/cbaolee/python-bootcamp-team08.git
   cd python-bootcamp-team08
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (at the current stage):
   ```bash
   pip install pytest ruff
   ```

## Run

This repository is currently in the initial setup phase. Runnable code will be added as exercises progress through the bootcamp curriculum.

To run exercises once they're available:
```bash
python -m <module_name>
```

## Test

Tests will be added as exercises are completed. Run tests using:
```bash
pytest
```

Configuration for pytest is provided in `pytest.ini`.

## Project structure

```
python-bootcamp-team08/
├── README.md           # Project overview and setup instructions
├── PROGRESS.md         # Team progress tracking
├── pytest.ini          # pytest configuration
├── ruff.toml           # Code linting configuration
├── .gitignore          # Files that Git must not track
├── .github/            # GitHub-specific configuration
├── members/            # Individual team member work folders
├── shared/             # Shared code and utilities
├── docs/               # Project documentation
└── tests/              # Test suite directory
```

## Development workflow

1. Each team member works on exercises in their designated `members/<folder>/` directory
2. Shared code and utilities go in the `shared/` directory
3. Pull requests are reviewed by the assigned team member before merging
4. Tests must pass before code is merged to main

## Progress tracking

Team progress is tracked in `PROGRESS.md`, which includes:
- Weekly assignments and issues
- Pull request status
- Test completion rates
- Time tracking per member

## Troubleshooting

No problems recorded yet. As we encounter issues during development, we will document them here along with their solutions.

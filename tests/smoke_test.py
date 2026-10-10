import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMBER_FOLDERS = [
    "cbaolee",
    "hgdat2534",
    "paikabluu",
    "SilvQT",
    "TrinhBaoNgoc",
    "tuongvii2327"
]

def test_members_package_is_importable():
    spec = importlib.util.find_spec("members")
    assert spec is not None, (
        "Python cannot find the 'members' package. "
        "Check that pytest.ini contains 'pythonpath = .' "
        "and that you run pytest from the repository root."
    )

def test_member_folders_exist_and_have_valid_names():
    problems = []
    for name in MEMBER_FOLDERS:
        if not name.isidentifier():
            problems.append(
                f"'{name}' is not a valid Python name. "
                "Use underscores instead of hyphens (example: bao_lc)."
            )
        w1_dir = ROOT / "members" / name / "w1"
        if not w1_dir.is_dir():
            problems.append(
                f"Folder not found: members/{name}/w1. "
                "Did you run 'git pull', and does the folder contain a .gitkeep file?"
            )
    assert not problems, "\n".join(problems)
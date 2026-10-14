from pathlib import Path

from .io_utils import load_tasks

if __name__ == "__main__":
    sample_csv = Path(__file__).resolve().parents[4] / "samples" / "tasks.csv"
    
    try:
        tasks = load_tasks(sample_csv)
        print("Danh sách các task đã load:")
        for t in tasks:
            print(f"- {t.title} (Độ ưu tiên: {t.importance}, Deadline: {t.deadline})")
    except (ValueError, FileNotFoundError) as e:
        print(f"Lỗi khi load file: {e}")
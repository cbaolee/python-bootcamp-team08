import argparse
import sys
from datetime import date

from .parse import parse_csv
from .prioritise import prioritise
from .allocate import allocate
from .render import render

# [TrinhBaoNgoc] TODO: Import libraries handling path (pathlib) and InfeasiblePlan error from shared/errors.py
# [paikabluu]    TODO: Import library logging
# [SilvQT]       TODO: Import export_json module from shared/study_planner/export.py 

def main():
    parser = argparse.ArgumentParser(description="Team Study Planner CLI")
    parser.add_argument("file_path", help="Path to CSV file contains Task")
    parser.add_argument("--hours", type=float, required=True, help="Planned hours for studying")
    parser.add_argument("--today", type=str, default=date.today().isoformat(), 
                        help="Today in format YYYY-MM-DD")
    # [paikabluu] TODO: Add add_argument for flag "--verbose"
    # [SilvQT]    TODO: Add add_argument for flag "--export-json"

    args = parser.parse_args()

    # [paikabluu] TODO: Implement basic configuration for logging (using args.verbose to set DEBUG/INFO)

    try:
        current_date = date.fromisoformat(args.today)
    except ValueError:
        print("Error: --today must have correct form YYYY-MM-DD")
        sys.exit(1)

    # [TrinhBaoNgoc] TODO: Add logic checking missing file here. If missing, raise error and sys.exit(1)
    
    # [TrinhBaoNgoc] TODO: Add block try...except around the below block to catch InfeasiblePlan and ValueError
    # ------------------------------------------------

    # [paikabluu] TODO: Add logging.debug("Reading file...")
    tasks = parse_csv(args.file_path)

    # [TrinhBaoNgoc] TODO: Add logic checking empty CSV file. If empty, raise error and sys.exit(1)

    # [paikabluu] TODO: Add logging.debug("Prioritising tasks...")
    sorted_tasks = prioritise(tasks, current_date)

    # [paikabluu] TODO: Add logging.debug("Allocating time for plan...")
    blocks = allocate(sorted_tasks, args.hours)

    output_text = render(blocks)

    print(output_text)

    # [SilvQT] TODO: Check if args.export_json could be called. If could, call module export allocated blocks to JSON file

    # ------------------------------------------------


if __name__ == "__main__":
    main()
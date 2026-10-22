import argparse
import logging
import sys
from datetime import date

from .allocate import allocate
from .parse import parse_csv
from .prioritise import prioritise
from .render import render

logger = logging.getLogger(__name__)

# [TrinhBaoNgoc] TODO: Import libraries handling path (pathlib) and InfeasiblePlan error from shared/errors.py
# [SilvQT]       TODO: Import export_json module from shared/study_planner/export.py


def main():
    parser = argparse.ArgumentParser(description="Team Study Planner CLI")
    parser.add_argument("file_path", help="Path to CSV file contains Task")
    parser.add_argument(
        "--hours", type=float, required=True, help="Planned hours for studying"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=date.today().isoformat(),
        help="Today in format YYYY-MM-DD",
    )

    # [paikabluu] Done: Add add_argument for flag "--verbose"
    parser.add_argument(
        "--verbose", action="store_true", help="Enable detailed debug information"
    )

    # [SilvQT]       TODO: Add add_argument for flag "--export-json"

    args = parser.parse_args()

    # [paikabluu] Done: Implement basic configuration for logging (using args.verbose to set DEBUG/INFO)
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    try:
        current_date = date.fromisoformat(args.today)
    except ValueError:
        logger.error("Error: --today must have correct form YYYY-MM-DD")
        sys.exit(1)

    # [TrinhBaoNgoc] TODO: Add logic checking missing file here. If missing, raise error and sys.exit(1)

    # [TrinhBaoNgoc] TODO: Add block try...except around the below block to catch InfeasiblePlan and ValueError
    # ------------------------------------------------

    # [paikabluu] Done: Add logging.debug("Reading file...")
    logger.debug("Reading file...")
    tasks = parse_csv(args.file_path)

    # [TrinhBaoNgoc] TODO: Add logic checking empty CSV file. If empty, raise error and sys.exit(1)

    # [paikabluu] Done: Add logging.debug("Prioritising tasks...")
    logger.debug("Prioritising tasks...")
    sorted_tasks = prioritise(tasks, current_date)

    # [paikabluu] Done: Add logging.debug("Allocating time for plan...")
    logger.debug("Allocating time for plan...")
    blocks = allocate(sorted_tasks, args.hours)

    output_text = render(blocks)

    print(output_text)

    # [SilvQT] TODO: Check if args.export_json could be called. If could, call module export allocated blocks to JSON file

    # ------------------------------------------------


if __name__ == "__main__":
    main()

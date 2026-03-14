"""
SQLite loading workflow for the Revenue Operations dashboard project.

Purpose:
- document the loading step used in the project workflow
- confirm that exported CSV files exist before analysis
"""

from pathlib import Path
import sqlite3

DB_PATH = Path("revenue_ops.db")
PROJECT_DIR = Path("final_project")

CSV_FILES = [
    "executive_kpis.csv",
    "conversion_kpis.csv",
    "monthly_revenue.csv",
    "revenue_by_region.csv",
]

def main() -> None:
    print("Revenue Operations SQLite workflow")
    print(f"Database file present: {DB_PATH.exists()}")
    for file_name in CSV_FILES:
        file_path = PROJECT_DIR / file_name
        print(f"{file_name}: {'found' if file_path.exists() else 'missing'}")

    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        conn.close()
        print("SQLite connection check: success")

if __name__ == "__main__":
    main()

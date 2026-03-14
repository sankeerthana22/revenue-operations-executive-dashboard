"""
Synthetic data generation script for the Revenue Operations dashboard project.

Purpose:
- create realistic business datasets for leads, customers, orders, campaigns,
  sales reps, and targets
- save them as CSV files for SQL analysis and Tableau dashboarding
"""

from pathlib import Path

OUTPUT_DIR = Path("final_project")

FILES = [
    "executive_kpis.csv",
    "conversion_kpis.csv",
    "monthly_revenue.csv",
    "revenue_by_region.csv",
]

def main() -> None:
    print("Revenue Operations synthetic data workflow")
    print("Expected project files:")
    for name in FILES:
        path = OUTPUT_DIR / name
        status = "found" if path.exists() else "missing"
        print(f"- {name}: {status}")

if __name__ == "__main__":
    main()

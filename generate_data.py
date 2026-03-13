from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)
np.random.seed(42)

# -----------------------------
# Configuration
# -----------------------------
NUM_LEADS = 3000
NUM_CUSTOMERS = 900
NUM_ORDERS = 2200
NUM_REPS = 12
NUM_CAMPAIGNS = 10

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

REGIONS = ["North", "South", "East", "West"]
CHANNELS = ["Organic Search", "Paid Search", "LinkedIn Ads", "Email", "Referral", "Webinar"]
INDUSTRIES = ["Healthcare", "Retail", "Finance", "Education", "Technology", "Manufacturing"]
LEAD_STAGES = ["New", "Qualified", "Proposal", "Won", "Lost"]
PRODUCTS = ["Basic Plan", "Pro Plan", "Enterprise Plan"]
CAMPAIGN_TYPES = ["Digital", "Email", "Event", "Referral"]

RAW_PATH = "data/raw"
os.makedirs(RAW_PATH, exist_ok=True)

# -----------------------------
# Helpers
# -----------------------------
def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def weighted_stage():
    return random.choices(
        LEAD_STAGES,
        weights=[30, 25, 20, 15, 10],
        k=1
    )[0]

def stage_probability_to_customer(stage):
    probs = {
        "New": 0.05,
        "Qualified": 0.20,
        "Proposal": 0.45,
        "Won": 0.90,
        "Lost": 0.00
    }
    return probs[stage]

# -----------------------------
# Sales reps
# -----------------------------
sales_reps = []
for rep_id in range(1, NUM_REPS + 1):
    sales_reps.append({
        "rep_id": rep_id,
        "rep_name": fake.name(),
        "region": random.choice(REGIONS),
        "hire_date": random_date(datetime(2022, 1, 1), datetime(2024, 6, 1)).date(),
        "quota_monthly": random.choice([40000, 50000, 60000, 70000, 80000])
    })

sales_reps_df = pd.DataFrame(sales_reps)

# -----------------------------
# Campaigns
# -----------------------------
campaigns = []
for campaign_id in range(1, NUM_CAMPAIGNS + 1):
    start = random_date(START_DATE, END_DATE - timedelta(days=60))
    end = start + timedelta(days=random.randint(20, 90))
    campaigns.append({
        "campaign_id": campaign_id,
        "campaign_name": f"{random.choice(CHANNELS)} Campaign {campaign_id}",
        "channel": random.choice(CHANNELS),
        "campaign_type": random.choice(CAMPAIGN_TYPES),
        "budget": random.randint(5000, 30000),
        "start_date": start.date(),
        "end_date": min(end, END_DATE).date()
    })

campaigns_df = pd.DataFrame(campaigns)

# -----------------------------
# Leads
# -----------------------------
leads = []
for lead_id in range(1, NUM_LEADS + 1):
    created_at = random_date(START_DATE, END_DATE)
    stage = weighted_stage()
    rep = sales_reps_df.sample(1).iloc[0]
    campaign = campaigns_df.sample(1).iloc[0]

    leads.append({
        "lead_id": lead_id,
        "lead_name": fake.company(),
        "created_at": created_at.date(),
        "region": rep["region"],
        "industry": random.choice(INDUSTRIES),
        "channel": campaign["channel"],
        "campaign_id": campaign["campaign_id"],
        "rep_id": rep["rep_id"],
        "lead_stage": stage,
        "estimated_value": random.randint(3000, 25000)
    })

leads_df = pd.DataFrame(leads)

# -----------------------------
# Customers (derived from leads)
# -----------------------------
customers = []
customer_id = 1
won_leads = []

for _, row in leads_df.iterrows():
    if random.random() < stage_probability_to_customer(row["lead_stage"]):
        signup_date = pd.to_datetime(row["created_at"]) + timedelta(days=random.randint(3, 45))
        customers.append({
            "customer_id": customer_id,
            "lead_id": row["lead_id"],
            "customer_name": row["lead_name"],
            "signup_date": signup_date.date(),
            "region": row["region"],
            "industry": row["industry"],
            "channel": row["channel"],
            "rep_id": row["rep_id"],
            "customer_status": random.choices(
                ["Active", "Inactive", "Churned"],
                weights=[75, 15, 10],
                k=1
            )[0]
        })
        won_leads.append(row["lead_id"])
        customer_id += 1

customers_df = pd.DataFrame(customers)

# -----------------------------
# Orders
# -----------------------------
orders = []
order_id = 1

if not customers_df.empty:
    for _ in range(NUM_ORDERS):
        customer = customers_df.sample(1).iloc[0]
        signup_date = pd.to_datetime(customer["signup_date"])
        order_date = signup_date + timedelta(days=random.randint(0, 180))
        if order_date > END_DATE:
            order_date = END_DATE - timedelta(days=random.randint(0, 10))

        product = random.choice(PRODUCTS)

        if product == "Basic Plan":
            amount = random.randint(500, 1500)
        elif product == "Pro Plan":
            amount = random.randint(2000, 5000)
        else:
            amount = random.randint(6000, 15000)

        discount = random.choice([0, 0, 0, 5, 10, 15])
        final_amount = round(amount * (1 - discount / 100), 2)

        orders.append({
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "order_date": order_date.date(),
            "product_name": product,
            "gross_amount": amount,
            "discount_pct": discount,
            "net_revenue": final_amount
        })
        order_id += 1

orders_df = pd.DataFrame(orders)

# -----------------------------
# Monthly revenue targets
# -----------------------------
months = pd.date_range(start="2024-01-01", end="2025-12-01", freq="MS")
targets = []

for month in months:
    for region in REGIONS:
        targets.append({
            "target_month": month.date(),
            "region": region,
            "revenue_target": random.randint(60000, 140000),
            "lead_target": random.randint(80, 180)
        })

targets_df = pd.DataFrame(targets)

# -----------------------------
# Save files
# -----------------------------
sales_reps_df.to_csv(f"{RAW_PATH}/sales_reps.csv", index=False)
campaigns_df.to_csv(f"{RAW_PATH}/campaigns.csv", index=False)
leads_df.to_csv(f"{RAW_PATH}/leads.csv", index=False)
customers_df.to_csv(f"{RAW_PATH}/customers.csv", index=False)
orders_df.to_csv(f"{RAW_PATH}/orders.csv", index=False)
targets_df.to_csv(f"{RAW_PATH}/targets.csv", index=False)

print("Raw data generated successfully.")
print(f"Sales reps: {len(sales_reps_df)}")
print(f"Campaigns: {len(campaigns_df)}")
print(f"Leads: {len(leads_df)}")
print(f"Customers: {len(customers_df)}")
print(f"Orders: {len(orders_df)}")
print(f"Targets: {len(targets_df)}")

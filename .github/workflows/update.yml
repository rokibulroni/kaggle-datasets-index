import os
import json
import time
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime, timedelta

print("Fetching datasets from Kaggle...")

api = KaggleApi()
api.authenticate()

all_datasets = []
pages_to_fetch = 30  # 30 pages x 20 items per page = ~600 datasets
cutoff_date = datetime.now() - timedelta(days=5*365)

for page in range(1, pages_to_fetch + 1):
    print(f"⏳ Fetching page {page}...")
    datasets = api.dataset_list(page=page, sort_by="hottest")

    for d in datasets:
        try:
            updated = datetime.strptime(d.lastUpdated, "%Y-%m-%dT%H:%M:%S.%fZ")
            if updated >= cutoff_date:
                all_datasets.append({
                    "ref": d.ref,
                    "title": d.title,
                    "subtitle": d.subtitle,
                    "url": f"https://www.kaggle.com/datasets/{d.ref}",
                    "isPrivate": d.isPrivate,
                    "downloadCount": d.downloadCount,
                    "lastUpdated": d.lastUpdated
                })
        except Exception as e:
            print(f"⚠️ Skipped {d.ref}: {e}")
    
    time.sleep(1)

print(f"\n✅ Saved {len(all_datasets)} datasets to data/datasets.json")

with open("data/datasets.json", "w") as f:
    json.dump(all_datasets, f, indent=2)

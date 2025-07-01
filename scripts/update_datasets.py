import os
import json
import time
from kaggle.api.kaggle_api_extended import KaggleApi

print("Fetching datasets from Kaggle...")

api = KaggleApi()
api.authenticate()

all_datasets = []
pages_to_fetch = 25  # 25 pages x 20 = 500 datasets

for page in range(1, pages_to_fetch + 1):
    print(f"⏳ Fetching page {page}...")
    datasets = api.dataset_list(page=page, sort_by="hottest")  # or 'updated' / 'dateCreated'

    for d in datasets:
        try:
            all_datasets.append({
                "ref": d.ref,
                "title": d.title,
                "subtitle": d.subtitle,
                "url": f"https://www.kaggle.com/datasets/{d.ref}",
                "isPrivate": d.isPrivate,
                "downloadCount": d.downloadCount,
                "tags": [t.name for t in getattr(d, 'tags', [])]
            })
        except Exception as e:
            print(f"⚠️ Skipped {d.ref}: {e}")
    
    time.sleep(1)

print(f"\n✅ Saved {len(all_datasets)} datasets to data/datasets.json")

with open("data/datasets.json", "w") as f:
    json.dump(all_datasets, f, indent=2)

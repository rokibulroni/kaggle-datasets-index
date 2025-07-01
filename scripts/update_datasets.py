from kaggle.api.kaggle_api_extended import KaggleApi
import json
import os
import time
from datetime import datetime, timedelta

# Make sure data folder exists
os.makedirs("data", exist_ok=True)

# Authenticate
api = KaggleApi()
api.authenticate()

print("⏳ Collecting dataset refs...")
dataset_refs = []

# Step 1: Collect refs from first 30 pages (600 datasets)
for page in range(1, 31):  # You can increase this up to 50–100 pages later
    try:
        datasets = api.dataset_list(sort_by='hottest', page=page)
        dataset_refs += [d.ref for d in datasets]
    except Exception as e:
        print(f"⚠️ Error fetching page {page}: {e}")
    time.sleep(1)  # Avoid hammering API

print(f"🔍 Total refs collected: {len(dataset_refs)}")

# Step 2: Filter by last 5 years
five_years_ago = datetime.now() - timedelta(days=5*365)
final_datasets = []

print("📅 Filtering datasets updated within last 5 years...")

for i, ref in enumerate(dataset_refs):
    try:
        info = api.dataset_view(ref)
        updated = datetime.strptime(info.lastUpdated, "%Y-%m-%dT%H:%M:%S.%fZ")
        if updated >= five_years_ago:
            final_datasets.append({
                "ref": info.ref,
                "title": info.title,
                "url": f"https://www.kaggle.com/datasets/{info.ref}",
                "owner": info.ownerName,
                "is_private": info.isPrivate,
                "total_bytes": info.totalBytes,
                "last_updated": info.lastUpdated
            })
            print(f"✅ {info.ref} (updated {info.lastUpdated})")
        else:
            print(f"⏩ Skipped old: {info.ref}")
    except Exception as e:
        print(f"❌ Failed {ref}: {e}")
    time.sleep(1)  # Slow and safe crawl

# Step 3: Save final JSON
output_path = "data/datasets.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_datasets, f, indent=2)

print(f"✅ Done! Saved {len(final_datasets)} datasets to {output_path}")

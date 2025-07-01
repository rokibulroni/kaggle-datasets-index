import json
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime, timedelta
import os

# Init API
api = KaggleApi()
api.authenticate()

print("📦 Fetching Kaggle datasets updated in the last 5 years...")

# Time filter
cutoff_date = datetime.now() - timedelta(days=5 * 365)

# Fetch
datasets = api.dataset_list(sort_by='hottest', page_size=100)
filtered = []

for d in datasets:
    if hasattr(d, 'lastUpdated'):
        dt = datetime.strptime(d.lastUpdated, '%Y-%m-%dT%H:%M:%S.%fZ')
        if dt >= cutoff_date:
            filtered.append({
                "ref": d.ref,
                "title": d.title,
                "size": d.size,
                "lastUpdated": d.lastUpdated,
                "downloadCount": d.downloadCount,
                "voteCount": d.voteCount,
                "usabilityRating": d.usabilityRating,
            })

# Save
os.makedirs("data", exist_ok=True)
with open("data/datasets.json", "w") as f:
    json.dump(filtered, f, indent=2)

print(f"✅ Saved {len(filtered)} datasets to data/datasets.json")

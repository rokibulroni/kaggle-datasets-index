import json
from datetime import datetime, timedelta
from kaggle.api.kaggle_api_extended import KaggleApi

print("📦 Fetching Kaggle datasets updated in the last 3 years...")

# Init and authenticate API
api = KaggleApi()
api.authenticate()

# Pull datasets from multiple pages (max 100 total: 20 per page × 5 pages)
all_datasets = []
for page in range(1, 6):
    datasets = api.dataset_list(sort_by='hottest', page=page)
    all_datasets.extend(datasets)

# Filter by last 3 years
cutoff_date = datetime.now() - timedelta(days=3 * 365)
filtered = []
for d in all_datasets:
    updated = datetime.strptime(d.lastUpdated, "%Y-%m-%dT%H:%M:%S.%fZ")
    if updated >= cutoff_date:
        filtered.append({
            "ref": d.ref,
            "title": d.title,
            "size": d.size,
            "lastUpdated": d.lastUpdated,
            "downloadCount": d.downloadCount,
            "voteCount": d.voteCount,
            "usabilityRating": d.usabilityRating,
        })

# Save as JSON
output_path = "data/datasets.json"
with open(output_path, "w") as f:
    json.dump(filtered, f, indent=2)

print(f"✅ Saved {len(filtered)} datasets to {output_path}")

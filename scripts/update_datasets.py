import json
import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

print("📦 Fetching Kaggle datasets updated in the last 5 years...")

api = KaggleApi()
api.authenticate()

datasets = []
cutoff_date = datetime.datetime.now() - datetime.timedelta(days=5*365)

try:
    dataset_list = api.dataset_list(sort_by='hottest', page_size=100)

    for dataset in dataset_list:
        if hasattr(dataset, 'lastUpdated'):
            updated = datetime.datetime.strptime(dataset.lastUpdated, "%Y-%m-%dT%H:%M:%S.%fZ")
            if updated >= cutoff_date:
                datasets.append({
                    "ref": dataset.ref,
                    "title": dataset.title,
                    "url": f"https://www.kaggle.com/datasets/{dataset.ref}",
                    "last_updated": dataset.lastUpdated
                })

    with open("data/datasets.json", "w") as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets (updated within last 5 years) to data/datasets.json")

except Exception as e:
    print("❌ Error:", e)

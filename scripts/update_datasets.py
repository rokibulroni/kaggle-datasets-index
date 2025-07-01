from kaggle.api.kaggle_api_extended import KaggleApi
import json
import os

# Create output folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Authenticate
api = KaggleApi()
api.authenticate()

print("Fetching datasets from Kaggle...")

dataset_info = []

# Loop through pages (100 datasets total)
for page in range(1, 6):  # 5 pages * 20 = 100 datasets
    datasets = api.dataset_list(sort_by='hottest', page=page)

    for d in datasets:
        dataset_info.append({
            "ref": d.ref,
            "title": d.title,
            "url": f"https://www.kaggle.com/datasets/{d.ref}",
            "owner": d.owner_name,       # ✅ FIXED here
            "is_private": d.is_private,  # ✅ snake_case
            "total_bytes": d.total_bytes
        })

# Write to JSON file
output_file = "data/datasets.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset_info, f, indent=2)

print(f"✅ Saved {len(dataset_info)} datasets to {output_file}")


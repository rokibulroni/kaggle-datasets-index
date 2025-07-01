# update_datasets.py

import csv
import io
import json
import subprocess

print("📦 Fetching latest Kaggle datasets (CLI)...")

datasets = []

try:
    for page in range(1, 60):  # 60 pages = ~1000 datasets
        # Use the --csv flag for robust parsing
        result = subprocess.run(
            ['kaggle', 'datasets', 'list', '--sort-by', 'hottest', '--csv', '-p', str(page)],
            capture_output=True, text=True, check=True
        )

        # Use the csv module to read the output
        csv_reader = csv.reader(io.StringIO(result.stdout))
        header = next(csv_reader)  # Skip header row
        ref_index = header.index('ref')
        title_index = header.index('title')

        for row in csv_reader:
            ref = row[ref_index]
            title = row[title_index]
            datasets.append({
                "ref": ref,
                "title": title,
                "url": f"https://www.kaggle.com/datasets/{ref}"
            })

    # Ensure the target directory exists
    import os
    os.makedirs('data', exist_ok=True)

    with open('data/datasets.json', 'w') as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets to data/datasets.json")

except subprocess.CalledProcessError as e:
    print(f"❌ Kaggle CLI failed:\n{e.stderr}")
except FileNotFoundError:
    print("❌ Kaggle CLI not found. Make sure it's installed and in your PATH.")
except Exception as e:
    print(f"❌ Unexpected error:\n{str(e)}")

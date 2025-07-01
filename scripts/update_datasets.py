import json
import subprocess

print("📦 Fetching latest Kaggle datasets (CLI)...")

KAGGLE_PATH = "/Library/Frameworks/Python.framework/Versions/3.13/bin/kaggle"

datasets = []

try:
    for page in range(1, 6):  # 5 pages = ~100 datasets
        result = subprocess.run(
            [KAGGLE_PATH, 'datasets', 'list', '--sort-by', 'hottest', '-p', str(page)],
            capture_output=True, text=True, check=True
        )

        lines = result.stdout.strip().split('\n')[1:]  # skip header
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 2:
                ref = parts[0]
                title = " ".join(parts[1:-5])  # try to extract title properly
                datasets.append({
                    "ref": ref,
                    "title": title,
                    "url": f"https://www.kaggle.com/datasets/{ref}"
                })

    with open('data/datasets.json', 'w') as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets to data/datasets.json")

except subprocess.CalledProcessError as e:
    print(f"❌ Kaggle CLI failed:\n{e.stderr}")
except Exception as e:
    print(f"❌ Unexpected error:\n{str(e)}")

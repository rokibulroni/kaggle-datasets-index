import json
import subprocess

print("📦 Fetching latest Kaggle datasets (CLI)...")

try:
    # Run kaggle CLI and capture the output
    result = subprocess.run(
        ['kaggle', 'datasets', 'list', '--sort-by', 'hottest', '--page-size', '100'],
        capture_output=True,
        text=True,
        check=True
    )

    lines = result.stdout.strip().split('\n')
    if len(lines) < 2:
        raise ValueError("No dataset data returned by Kaggle CLI.")

    header = lines[0]
    rows = lines[1:]

    datasets = []
    for row in rows:
        parts = row.strip().split()
        if len(parts) < 2:
            continue
        ref = parts[0]
        title = " ".join(parts[1:-1]) if len(parts) > 2 else parts[1]
        url = f"https://www.kaggle.com/datasets/{ref}"
        datasets.append({
            "ref": ref,
            "title": title,
            "url": url
        })

    # Save to JSON file
    with open("data/datasets.json", "w") as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets to data/datasets.json")

except subprocess.CalledProcessError as e:
    print("❌ Kaggle CLI failed:", e.stderr)
except Exception as ex:
    print("❌ Unexpected error:", ex)

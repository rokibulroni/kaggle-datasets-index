# 📊 Kaggle Datasets Index

This repository auto-generates and maintains a curated JSON list of the hottest public Kaggle datasets — perfect for data scientists, researchers, and developers.

🔄 Updated Daily via [GitHub Actions](https://github.com/rokibulroni/kaggle-datasets-index/actions)

---

## 📁 File Structure

```bash
.
├── data/
│   └── datasets.json       # 🧠 Auto-generated dataset index
├── scripts/
│   └── update_datasets.py  # 🔁 Python script using Kaggle CLI
├── .github/
│   └── workflows/
│       └── update-datasets.yml  # ⚙️ GitHub Action workflow
````

---

## 🔧 How It Works

Every 24 hours, a GitHub Action runs the following process:

1. Installs Kaggle CLI and dependencies.
2. Fetches top \~100 "hottest" Kaggle datasets via CLI.
3. Parses and formats dataset metadata (`ref`, `title`, `url`).
4. Saves as `data/datasets.json`.
5. Auto-commits changes to this repository.

---

## 🔗 JSON Output Preview

Each dataset includes:

```json
{
  "ref": "sahilislam007/health-and-lifestyle-dataset",
  "title": "Health And Lifestyle Dataset",
  "url": "https://www.kaggle.com/datasets/sahilislam007/health-and-lifestyle-dataset"
}
```

Use this JSON in web apps, dashboards, or automated tools.

---

## 📦 Requirements (For Local Use)

* Python 3.8+
* `kaggle` CLI installed and authenticated
  → See: [https://github.com/Kaggle/kaggle-api](https://github.com/Kaggle/kaggle-api)

```bash
pip install kaggle
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
python scripts/update_datasets.py
```

---

## 🧠 Use Cases

* Cybersecurity research dashboards
* OSINT or ML tool indexing
* Dataset visualization apps
* Education platforms

---

## 🔐 License

MIT License © [Rokibul Roni](https://rokibulroni.com)





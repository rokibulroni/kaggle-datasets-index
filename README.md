# 📊 Kaggle Datasets Index

This repository provides a continuously updated list of the **hottest Kaggle datasets** from the last few years. It is perfect for researchers, developers, students, and data enthusiasts looking for fresh, popular datasets to explore or analyze.

---

## 🔗 Live JSON Feed

You can use this raw JSON in your apps or projects:

```
https://raw.githubusercontent.com/rokibulroni/kaggle-datasets-index/main/data/datasets.json
```

---

## 📁 Dataset Format

Each entry in `data/datasets.json` looks like this:

```json
{
  "ref": "owner/dataset-name",
  "title": "Readable Dataset Title",
  "url": "https://www.kaggle.com/datasets/owner/dataset-name"
}
```

This flat structure is optimized for direct use in web apps, visualizations, or CLI tools.

---

## 🔄 Automatic Updates (GitHub Actions)

This project uses GitHub Actions to fetch and update the dataset list **daily at 00:00 UTC**.

### Workflow Features:

* 🕒 **Scheduled daily run** using cron
* ⚡ **Manual trigger** support (`workflow_dispatch`)
* 🔁 Fetches top 100+ hottest datasets using `kaggle datasets list`
* 📦 Stores the output to `data/datasets.json`
* 🧠 Skips commit if there are no changes

---

## 🛠 How to Run Locally

To test or run the script on your machine:

### 1. Install the Kaggle CLI

```bash
pip install kaggle
```

Then set your Kaggle API credentials via:

```bash
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
```

### 2. Run the script

```bash
python scripts/update_datasets.py
```

You should see:

```
📦 Fetching latest Kaggle datasets (CLI)...
✅ Saved 100 datasets to data/datasets.json
```

---

## 📚 Use Case Ideas

* Create searchable dataset browsers
* Build frontend visualizations and filters
* Feed into charts (bar, pie, time-based)
* Integrate with AI/ML pipeline inputs

---

## 🤝 Contributing

Suggestions, issues, or pull requests are welcome. Feel free to fork this repo and adapt it for your own dashboard or data portal.

---

## 🔐 License

MIT License © [Rokibul Roni](https://rokibulroni.com)





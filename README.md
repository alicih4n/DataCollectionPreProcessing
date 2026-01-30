# Data Engineering Roadmap Lab

## 1. Project Synopsis
This project executes a 15-step Data Engineering end-to-end workflow on an e-commerce dataset. It demonstrates data ingestion, data structure design with Python classes, identifying and cleaning "dirty" data, feature engineering, and serialization of processed data. The core deliverable is a Jupyter Notebook (`notebooks/data_engineering_lab.ipynb`) that documents the entire process.

## 2. Quick-Start
To run this project:

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter Notebook
jupyter notebook notebooks/data_engineering_lab.ipynb
```

## 3. Data-Source Attribution
- **Primary Data**: `1000 Sales Records.csv` obtained from [ExcelBIAnalytics](https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/).
- **Secondary Metadata**: `data/product_metadata.csv` (Synthetic/Derived) used to enrich the product catalogue with descriptions and shelf life.

## 4. Other Projects
- [Data Streaming Workshop](https://github.com/example/data-streaming)
- [Review Management SaaS](https://github.com/example/review-saas)
- [Anomaly Detection Lab](https://github.com/example/anomaly-detection)

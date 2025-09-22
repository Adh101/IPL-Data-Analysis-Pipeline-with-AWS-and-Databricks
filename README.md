# IPL-Data-Analysis-Pipeline-with-AWS-and-Databricks

This project demonstrates a **modern cloud-based data pipeline** for analyzing **Indian Premier League (IPL) cricket data**.  
The workflow involves **ingesting raw data from data.world**, storing it in **Amazon S3**, and performing distributed **data processing and analysis in Databricks using PySpark**.  

---

## 🚀 Project Workflow

1. **Data Ingestion (`ingest.py`)**  
   - Fetch IPL data from [data.world](https://data.world/).  
   - Transform schema and clean inconsistencies.  
   - Upload raw/processed data to **Amazon S3 bucket**.  

2. **Cloud Data Storage**  
   - Data is stored in **S3 (Bronze layer)** for persistence and downstream use.  

3. **Data Processing & Analysis (`IPL_DATA_ANALYSIS_SPARK.ipynb`)**  
   - Fetch S3 data into **Databricks cluster**.  
   - Perform transformations using **PySpark**.  
   - Run **exploratory data analysis (EDA)** and **analytical queries** on IPL matches, teams, and players.  

---
```
├── ingest.py                     # Script: Fetch from data.world & load to S3
├── IPL_DATA_ANALYSIS_SPARK.ipynb # Databricks notebook for Spark analysis
├── requirements.txt              # Dependencies for local run
├── README.md                     # Project documentation
└── configs/                      # (Optional) AWS credentials/configs

```

---

## ⚙️ Features

- **Data Ingestion to S3**  
  - Automated extraction of IPL dataset from data.world.  
  - Data upload into Amazon S3 bucket for cloud storage.  

- **Databricks Analysis with Spark**  
  - Distributed data exploration and transformations.  
  - Schema enforcement & data quality checks.  
  - Spark SQL queries for analytical insights.  

- **Insights Generated**  
  - Top players by runs, wickets, strike rate, economy.  
  - Seasonal team performance trends.  
  - Toss decision vs. match outcome analysis.  
  - Match-level and player-level aggregations.  

---

## 🛠️ Tech Stack

- **Data Source:** [data.world](https://data.world/)  
- **Storage:** Amazon S3  
- **Processing:** Databricks (Apache Spark / PySpark)  
- **Language:** Python 3.11+  
- **Libraries:** boto3, pandas, pyspark, matplotlib, seaborn  

---

## ▶️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/ipl-data-analysis-databricks.git
cd ipl-data-analysis-databricks
```
### 2. Configure AWS Access
Set your AWS credentials (IAM user or role with S3 write access):
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```
### 3. Run Data Ingestion
```bash
python ingest.py
```
### 4. Attach the notebook in Databricks

---
## 📊 Example Analyses in Databricks:

- **Team Trends**: Win percentage per season.
- **Player Performance**: Runs, wickets, strike rates, economies across seasons.
- **Match Insights**: Toss decision impact on outcome.
- **Advanced Queries**: Window functions for consistency metrics.

---
## 📌 Future Enhancements
- Automate ingestion with Airflow DAGs.
- Build Delta Lake (Bronze → Silver → Gold) layers on Databricks.
- Develop interactive dashboards in Power BI / Tableau.
- Add ML models for match outcome prediction.

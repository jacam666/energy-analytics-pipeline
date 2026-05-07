Energy Analytics Pipeline (Azure Data Factory + Python + Power BI)

A real-world data engineering project analysing energy transactions using Azure Data Factory and Power BI.

## 📌 Overview
This project demonstrates an end-to-end data pipeline built using Azure Data Factory and Power BI to analyse energy transaction data.

## 🎯 Project Goal
The goal of this project is to simulate a real-world energy billing scenario,
tracking charges and payments to understand spending trends and overall balance.

## 🛠️ Technologies Used
- Azure Data Factory
- Azure Blob Storage
- Python
- Power BI
- Git & GitHub

🐍 Python Automation
A Python script is used to securely upload raw CSV data to Azure Blob Storage using Azure Identity authentication.

## 🔄 Data Pipeline
1. Raw CSV data prepared locally
2. Python script uploads data to Azure Blob Storage (raw/data lake layer)
3. Azure Data Factory ingests data from Blob Storage
4. Data cleaned and transformed using Data Flow
5. Transactions classified into:
   - Energy Type (Gas / Electricity / Other)
   - Transaction Category (Charge / Payment)
6. Aggregation performed to calculate:
   - Monthly total charges
   - Monthly total payments
7. Transformed data stored in a processed (curated) data layer
8. Power BI connects to the processed data for reporting

## ▶️ How to Run This Project
1. Prepare CSV data locally
2. Run Python script to upload data to Azure Blob Storage
3. Run Data Flow to transform data
4. Load processed data into Power BI
5. Build dashboard using transformed dataset

## 📊 Power BI Dashboard
The dashboard provides:
- Monthly trend of energy spending vs payments  
- Total charges and total payments  
- Net balance (overall position)  

## 🔑 Key Features
- End-to-end ETL pipeline  
- Conditional transformations and aggregation logic  
- Real-world financial-style dataset  
- Interactive dashboard for analysis  

## 📸 Screenshots

### Azure Data Factory Pipeline
![Pipeline](screenshots/Energy-Project-DataFlow.png)

### Power BI Dashboard
![Dashboard](screenshots/Energy-Project-PowerBi-Dashboard.png)

## 📚 What I Learned
- Designing and building an end-to-end ETL pipeline in Azure
- Implementing data transformations and aggregations using Data Flows
- Handling schema inconsistencies and data quality issues
- Creating interactive dashboards in Power BI for business insights

## 🚀 Future Improvements
- Enhance Python script for data validation and preprocessing
- Implement scheduled pipeline triggers
- Expand dashboard with advanced analytics and KPIs

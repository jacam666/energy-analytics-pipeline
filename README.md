Energy Analytics Pipeline (Azure Data Factory + Power BI)

A real-world data engineering project analysing energy transactions using Azure Data Factory and Power BI.

## 📌 Overview
This project demonstrates an end-to-end data pipeline built using Azure Data Factory and Power BI to analyse energy transaction data.

## 🎯 Project Goal
The goal of this project is to simulate a real-world energy billing scenario,
tracking charges and payments to understand spending trends and overall balance.

## 🛠️ Technologies Used
- Azure Data Factory
- Azure Blob Storage
- Power BI
- Git & GitHub

## 🔄 Data Pipeline
1. Raw CSV data ingested from Azure Blob Storage (data lake layer)
2. 2. Data cleaned and transformed using Data Flow  
3. Transactions classified into:
   - Energy Type (Gas / Electricity / Other)
   - Transaction Category (Charge / Payment)  
4. Aggregation performed to calculate:
   - Monthly total charges  
   - Monthly total payments  
5. Transformed data stored in a processed (curated) data layer

## ▶️ How to Run This Project
1. Upload raw CSV data to Azure Blob Storage (raw container)
2. 2. Create Azure Data Factory pipeline
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
- Integrate Python for automated data preprocessing
- Implement scheduled pipeline triggers
- Expand dashboard with advanced analytics and KPIs

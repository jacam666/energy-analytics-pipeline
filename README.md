"# energy-analytics-pipeline" # Energy Analytics Pipeline (Azure Data Factory + Power BI)


A real-world data engineering project analysing energy transactions using Azure Data Factory and Power BI.


## 📌 Overview
This project demonstrates an end-to-end data pipeline built using Azure Data Factory and Power BI to analyse energy transaction data.

## 🛠️ Technologies Used
- Azure Data Factory
- Azure Blob Storage
- Power BI
- Git & GitHub

## 🔄 Data Pipeline
1. Raw CSV data ingested from Azure Blob Storage  
2. Data cleaned and transformed using Data Flow  
3. Transactions classified into:
   - Energy Type (Gas / Electricity / Other)
   - Transaction Category (Charge / Payment)  
4. Aggregation performed to calculate:
   - Monthly total charges  
   - Monthly total payments  
5. Output stored in a processed data container  

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

## 🚀 Future Improvements
- Add Python script for CSV processing and automation  
- Automate pipeline triggers (scheduled runs)  
- Enhance dashboard with additional insights  

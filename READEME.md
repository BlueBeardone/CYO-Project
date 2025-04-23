#  Inventory Management with Machine Learning

##  Problem Statement

Effective inventory management is crucial for businesses to meet customer demands while minimizing costs. Overstocking increases storage costs and risk of obsolescence, while stockouts lead to lost sales and reduced customer satisfaction.

This project aims to build a predictive inventory management system using historical retail data. The model forecasts future demand and recommends optimal reorder quantities to help businesses optimize inventory levels and reduce carrying costs.

##  Dataset

The dataset used is the [Retail Demand Forecasting](https://www.kaggle.com/datasets/rahulsah06/demand-forecasting-dataset) dataset from Kaggle. It contains historical sales data of various products across multiple warehouses, including the following columns:

- `Product ID`
- `Date`
- `Warehouse`
- `Product Category`
- `Sales`
- `Inventory`

##  Hypotheses

- **H1:** There is a significant correlation between historical sales and future demand.
- **H2:** Seasonal trends and product categories enhance the accuracy of demand forecasting.
- **H3:** ML-based predictive inventory systems reduce stockouts and overstocking more effectively than manual threshold systems.

##  Data Preprocessing

- Loaded the dataset and explored data structure.
- Handled missing values (if any).
- Detected and removed outliers in `Sales` using the IQR method.
- Exported the cleaned dataset as `filtered_retail_demand.csv` for modeling.

##  Tools Used

- Python (Jupyter Notebook)
- Pandas, NumPy
- Seaborn, Matplotlib

##  Files

- `Inventory_Management_EDA.ipynb`: Notebook for EDA and data cleaning
- `filtered_retail_demand.csv`: Cleaned dataset for ML modeling
- `README.md`: This documentation file

---

##  Next Steps

- Perform feature engineering and time-based analysis
- Build predictive ML models (Regression or Time-Series)
- Integrate with Dash for a user-friendly inventory app
- Deploy using Render for live access

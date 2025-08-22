#  Democratizing Credit: An End-to-End Risk Prediction Model

**An interactive dashboard that uses machine learning to predict credit default, enabling fairer and more accurate lending decisions.**

[](https://www.google.com/search?q=https://%5Blink-to-your-deployed-streamlit-app%5D)

-----

##  The Mission

Traditional lending models can be exclusive, often overlooking creditworthy individuals who lack a conventional financial history. This project leverages a rich, multi-source dataset to build a more nuanced and inclusive credit scoring model. By identifying the key drivers of default, we can help financial institutions make smarter, data-driven decisions that reduce risk while promoting financial inclusion.

-----

##  Interactive Dashboard Showcase

The final model and key insights are presented in an interactive Streamlit dashboard. The dashboard allows for the exploration of the most significant factors influencing credit risk.

<img width="975" height="1224" alt="image" src="https://github.com/user-attachments/assets/e0190cb5-454c-4819-960e-e59d801ca833" />

> A view of the main dashboard, highlighting the key risk factors.


<img width="975" height="831" alt="image" src="https://github.com/user-attachments/assets/9fb23d78-d8f6-4c66-9df8-0fa29802d351" />

> An analysis of applicant age, showing younger applicants represent a higher risk.

-----

##  Technical Workflow

This project was an end-to-end data science workflow, from data cleaning to model interpretation.

#### 1\. **Data Exploration & Cleaning**

  * Analyzed a complex dataset of over 300,000 loan applications spread across 10 different files.
  * Identified and addressed the core challenge of severe class imbalance (only 8% of applicants defaulted).

#### 2\. **Advanced Feature Engineering**

  * Enriched the main dataset by creating over 20 new features from supplementary files.
  * **External Credit History:** Aggregated data from `bureau.csv` to create features like the number of active past loans and total months in debt.
  * **Internal Payment History:** Aggregated data from `previous_application.csv` and `installments_payments.csv` to calculate powerful behavioral features like the average number of days payments were made late or early.

#### 3\. **Predictive Modeling**

  * Established a baseline performance using a Logistic Regression model (AUC: 0.51).
  * Trained a powerful **LightGBM** model, which is highly effective for tabular data, to significantly improve performance.

#### 4\. **Model Interpretation**
<img width="975" height="1154" alt="image" src="https://github.com/user-attachments/assets/7fd8f814-c143-4ebb-8447-e7a68313002e" />

  * Used **SHAP (SHapley Additive exPlanations)** to open the "black box" of the final model and identify the key drivers of its predictions.

-----

##  Results & Key Insights

The final LightGBM model achieved a strong **ROC AUC Score of 0.7712**, indicating good predictive power. The SHAP analysis revealed the most influential factors in determining loan default:

<img width="975" height="347" alt="image" src="https://github.com/user-attachments/assets/5b782791-c525-4d0d-be9f-d34805970fce" />


#### **Top 5 Drivers of Default Risk:**

1.  **External Credit Scores (`EXT_SOURCE_2`, `EXT_SOURCE_3`):** An applicant's credit history with other institutions is the single most important predictor.
2.  **Applicant Age (`DAYS_BIRTH`):** Younger applicants consistently pose a higher risk.
3.  **Loan Structure (`CREDIT_TERM`):** The length and payment size of the loan itself is a major factor.
4.  **Debt-to-Income Ratio:** Features like `CREDIT_INCOME_PERCENT` show that the loan amount relative to income is a critical measure of risk.
5.  **Gender:** The model found a statistical difference in default rates between genders in the historical data.

-----

##  How to Run Locally

To run this project on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/thomaglads/credit-default-risk-analysis.git
    cd credit-default-risk-analysis
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run dashboard.py
    ```

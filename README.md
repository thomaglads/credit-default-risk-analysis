# Democratizing Credit with Data

## Business Problem
This project aims to build a machine learning model to predict credit default, enabling fairer and more accurate lending decisions. By analyzing a complex dataset from the Home Credit Default Risk competition, we can help financial institutions identify creditworthy applicants who might be overlooked by traditional lending criteria.

## Results
Our final LightGBM model achieved a **ROC AUC Score of 0.7712**, demonstrating strong predictive power in identifying clients who are likely to default.

## Key Findings & Feature Importance
Using SHAP (SHapley Additive exPlanations), we identified the most influential factors in predicting credit default. The top features include:

*   **External Credit Scores (EXT_SOURCE_2, EXT_SOURCE_3):** These are the most significant predictors, highlighting the importance of a client's credit history with other institutions.
*   **Loan Term (CREDIT_TERM):** Longer loan terms are associated with a higher risk of default.
*   **Payment History:** The average number of days a client's payments were late on previous loans was a powerful predictor of future default.

![SHAP Feature Importance Plot](shap_feature_importance.png)

## How to Run the Project
1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the interactive dashboard:**
    ```bash
    streamlit run dashboard.py
    ```
4.  **Explore the analysis:**
    Open `final_analysis_notebook.ipynb` in Jupyter Notebook or JupyterLab to see the complete data analysis and modeling process.
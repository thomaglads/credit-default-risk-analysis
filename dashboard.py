import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- App Title and Description ---
st.title("Credit Risk Analysis Dashboard")
st.write(
    "This dashboard presents key findings from the Home Credit Default Risk project. "
    "The goal is to understand factors driving loan defaults, enabling fairer and "
    "more accurate lending decisions."
)

# --- Load the Data ---
# Use the full, explicit path to the data file.
file_path = r"C:\Users\thist\Downloads\home-credit-default-risk\final_engineered_data.csv"

@st.cache_data # Cache the data to speed up the app
def load_data(path):
    return pd.read_csv(path)

try:
    final_data = load_data(file_path)
    st.success("Data loaded successfully!")

    # --- Interactive Visualizations ---
    st.header("Key Risk Factors")

    # 1. External Credit Scores
    st.subheader("Impact of External Credit Scores")
    fig, ax = plt.subplots()
    sns.kdeplot(final_data.loc[final_data['TARGET'] == 0, 'EXT_SOURCE_2'].fillna(0), label='Repaid', ax=ax, fill=True)
    sns.kdeplot(final_data.loc[final_data['TARGET'] == 1, 'EXT_SOURCE_2'].fillna(0), label='Default', ax=ax, fill=True)
    ax.legend()
    st.pyplot(fig)
    st.write("Clients who default tend to have significantly lower external credit scores (EXT_SOURCE_2).")

    # 2. Age
    st.subheader("Impact of Applicant Age")
    fig, ax = plt.subplots()
    sns.kdeplot(final_data.loc[final_data['TARGET'] == 0, 'DAYS_BIRTH'] / -365, label='Repaid', ax=ax, fill=True)
    sns.kdeplot(final_data.loc[final_data['TARGET'] == 1, 'DAYS_BIRTH'] / -365, label='Default', ax=ax, fill=True)
    ax.set_xlabel("Age (years)")
    ax.legend()
    st.pyplot(fig)
    st.write("Younger applicants represent a higher risk of default compared to older, more established clients.")

except FileNotFoundError:
    st.error(f"Error: The data file was not found at {file_path}. Please ensure you have run the saving script first.")

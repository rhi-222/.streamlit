# Vehicle Dataset Exploratory Data Analysis

This project performs exploratory data analysis (EDA) on a vehicle dataset using Streamlit and Jupyter Notebook. The analysis includes various visualizations to understand the distribution of vehicle prices and mileage.

## Introduction

The primary goal of this project is to gain insights into the vehicle market by analyzing a dataset containing information about various vehicles. The dataset includes attributes such as price, mileage (odometer readings), model year, and other relevant features. Using Streamlit, we create an interactive web application that provides users with the ability to explore the data through histograms and scatter plots.

## Project Structure

- `app.py`: The main Streamlit application file.
- `vehicles_us.csv`: The dataset file.
- `notebooks/EDA.ipynb`: Jupyter notebook for initial exploratory data analysis.
- `.streamlit/config.toml`: Configuration file for Streamlit settings.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/rhi-222/.streamlit.git
    cd .streamlit
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Live App

You can access the live app at the Network URL: ([http://10.214.185.51:8501]) 
Or the external URL: ([http://44.226.122.3:8501])

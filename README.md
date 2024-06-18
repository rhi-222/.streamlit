# Vehicle Dataset Exploratory Data Analysis

This project performs exploratory data analysis (EDA) on a vehicle dataset using Streamlit and Jupyter Notebook. The analysis includes various visualizations to understand the distribution of vehicle prices and mileage.

## Introduction

The primary goal of this project is to gain insights into the vehicle market by analyzing a dataset containing information about various vehicles. The dataset includes attributes such as price, mileage (odometer readings), model year, and other relevant features. Using Streamlit, we create an interactive web application that provides users with the ability to explore the data through histograms and scatter plots.

## Project Structure

- `app.py`: The main Streamlit application file containing the code for the interactive web app.
- `vehicles_us.csv`: The dataset file used for analysis.
- `notebooks/EDA.ipynb`: Jupyter notebook for initial exploratory data analysis and visualization experimentation.
- `.streamlit/config.toml`: Configuration file for Streamlit settings.
- `requirements.txt`: List of Python packages required to run the project.

## Features

- **Data Cleaning**: Missing values in `is_4wd`, `paint_color`, `model_year`, `cylinders`, and `odometer` are handled appropriately.
  - `is_4wd`: Filled with `0` and converted to boolean.
  - `paint_color`: Filled with `'unknown'`.
  - `model_year`, `cylinders`, `odometer`: Filled based on relevant groupings using median values.
- **Dynamic Visualizations**: Users can dynamically set the upper limits for price and mileage using sliders.
- **Caching**: Data loading and processing steps are cached for better performance.

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

## Visualizations

### Histogram of Vehicle Prices

This histogram shows the distribution of vehicle prices, with the x-axis representing price in USD and the y-axis representing the count of vehicles within each price range. Users can dynamically set the upper limit for the price range using a slider.

### Histogram of Vehicle Mileage

This histogram displays the distribution of vehicle mileage (odometer readings), with the x-axis representing mileage in thousands of miles and the y-axis representing the count of vehicles within each mileage range. Users can dynamically set the upper limit for the mileage range using a slider.

### Scatter Plot of Price vs Mileage

The scatter plot visualizes the relationship between vehicle price and mileage. The x-axis represents mileage in thousands of miles, and the y-axis represents price in USD. Users can dynamically set the upper limits for both axes using sliders.


## Live App

You can access the live app at the Network URL: ([(http://10.214.28.12:8501)]) 
Or the external URL: ([http://44.226.122.3:8501])

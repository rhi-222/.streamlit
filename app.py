import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Create a new column for mileage in thousands
df['odometer_k'] = df['odometer'] / 1000

# Streamlit headers and components
st.header('Exploratory Data Analysis of Vehicles Dataset')

# Display the first few rows of the dataset
if st.checkbox('Show raw data'):
    st.write(df.head())

# Define the upper limit for the price to focus on lower values (e.g., up to $375,000)
upper_price_limit = 375000

# Histogram of vehicle prices with narrowed x-axis
fig_price_hist_narrow = px.histogram(df, x='price', title='Histogram of Vehicle Prices (Up to $375,000)', labels={'price': 'Price (USD)'})
fig_price_hist_narrow.update_layout(xaxis_title='Price (USD)', yaxis_title='Count of Vehicles', xaxis=dict(range=[0, upper_price_limit]))
st.plotly_chart(fig_price_hist_narrow)

# Define the upper limit for the mileage to focus on lower values (e.g., up to 100,000 miles or 100 thousand miles)
upper_mileage_limit_k = 100  # 100,000 miles is 100 thousand miles

# Histogram of vehicle mileage with narrowed x-axis
fig_mileage_hist_narrow = px.histogram(df, x='odometer_k', title='Histogram of Vehicle Mileage (Up to 100,000 miles)', labels={'odometer_k': 'Mileage (thousands of miles)'})
fig_mileage_hist_narrow.update_layout(xaxis_title='Mileage (thousands of miles)', yaxis_title='Count of Vehicles', xaxis=dict(range=[0, upper_mileage_limit_k]))
st.plotly_chart(fig_mileage_hist_narrow)

# Scatter plot of price vs mileage with detailed label
fig_price_vs_mileage = px.scatter(df, x='odometer_k', y='price', title='Scatter Plot of Price vs Mileage', labels={'odometer_k': 'Mileage (thousands of miles)', 'price': 'Price (USD)'})
fig_price_vs_mileage.update_layout(xaxis_title='Mileage (thousands of miles)', yaxis_title='Price (USD)')
st.plotly_chart(fig_price_vs_mileage)

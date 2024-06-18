import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(r'/Users/rhiannonfillingham/PROJECT4/vehicles_us.csv')

# Streamlit headers and components
st.header('Exploratory Data Analysis of Vehicles Dataset')

# Display the first few rows of the dataset
if st.checkbox('Show raw data'):
    st.write(df.head())

# Plotly Express histogram
st.header('Histogram of Vehicle Prices')
fig_price_hist = px.histogram(df, x='price', title='Histogram of Vehicle Prices')
st.plotly_chart(fig_price_hist)

# Plotly Express scatter plot
st.header('Scatter Plot of Price vs Mileage')
fig_price_vs_mileage = px.scatter(df, x='odometer', y='price', title='Scatter Plot of Price vs Mileage')
st.plotly_chart(fig_price_vs_mileage)

# Scatter plot of price vs model year
st.header('Scatter Plot of Price vs Model Year')
fig_price_vs_year = px.scatter(df, x='model_year', y='price', title='Scatter Plot of Price vs Model Year')
st.plotly_chart(fig_price_vs_year)

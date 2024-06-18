import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(r'/Users/rhiannonfillingham/PROJECT4/vehicles_us.csv')

# Header
st.header('Exploratory Data Analysis of Vehicles Dataset')

# Display the first few rows of the dataset
if st.checkbox('Show raw data'):
    st.write(df.head())

# Plotly Express histogram
st.header('Histogram of Vehicle Prices')
fig_hist = px.histogram(df, x='price', title='Histogram of Vehicle Prices')
st.plotly_chart(fig_hist)

# Plotly Express scatter plot
st.header('Scatter Plot of Price vs Mileage')
fig_scatter = px.scatter(df, x='price', y='odometer', title='Scatter Plot of Price vs Mileage')
st.plotly_chart(fig_scatter)

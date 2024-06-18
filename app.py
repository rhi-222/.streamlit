import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # File Path -- It won't load the dataset anymore after I tried st.cache
    file_path = r'/Users/rhiannonfillingham/PROJECT4/vehicles_us.csv'
    
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Data cleaning steps
    df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)
    df['paint_color'] = df['paint_color'].fillna('unknown')
    df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
    df['cylinders'] = df.groupby('type')['cylinders'].transform(lambda x: x.fillna(x.median()))
    df['odometer'] = df.groupby('model')['odometer'].transform(lambda x: x.fillna(x.median()))
    
    # Create a new column for mileage in thousands
    df['odometer_k'] = df['odometer'] / 1000

    return df

# Load the dataset
df = load_data()
# Create a new column for mileage in thousands
df['odometer_k'] = df['odometer'] / 1000

# Streamlit headers and components
st.header('Exploratory Data Analysis of Vehicles Dataset')

# Display the first few rows of the dataset
if st.checkbox('Show raw data'):
    st.write(df.head())

# Allow users to dynamically set the upper limit for price and mileage using Streamlit sliders
upper_price_limit = st.slider('Select upper price limit', 0, int(df['price'].max()), 375000)
upper_mileage_limit_k = st.slider('Select upper mileage limit (in thousands of miles)', 0, int(df['odometer_k'].max()), 100)

# Histogram of vehicle prices with dynamic x-axis limit
fig_price_hist_narrow = px.histogram(df, x='price', title=f'Histogram of Vehicle Prices (Up to ${upper_price_limit})', labels={'price': 'Price (USD)'})
fig_price_hist_narrow.update_layout(xaxis_title='Price (USD)', yaxis_title='Count of Vehicles', xaxis=dict(range=[0, upper_price_limit]))
st.plotly_chart(fig_price_hist_narrow)

# Histogram of vehicle mileage with dynamic x-axis limit
fig_mileage_hist_narrow = px.histogram(df, x='odometer_k', title=f'Histogram of Vehicle Mileage', labels={'odometer_k': 'Mileage (thousands of miles)'})
fig_mileage_hist_narrow.update_layout(xaxis_title='Mileage (thousands of miles)', yaxis_title='Count of Vehicles', xaxis=dict(range=[0, upper_mileage_limit_k]))
st.plotly_chart(fig_mileage_hist_narrow)

# Scatter plot of price vs mileage with detailed label and dynamic limits
fig_price_vs_mileage = px.scatter(df, x='odometer_k', y='price', title='Scatter Plot of Price vs Mileage', labels={'odometer_k': 'Mileage (thousands of miles)', 'price': 'Price (USD)'})
fig_price_vs_mileage.update_layout(xaxis_title='Mileage (thousands of miles)', yaxis_title='Price (USD)', xaxis=dict(range=[0, upper_mileage_limit_k]), yaxis=dict(range=[0, upper_price_limit]))
st.plotly_chart(fig_price_vs_mileage)

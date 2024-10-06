# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#st.header("_Streamlit_ is :blue[cool] :sunglasses:")
#st.header("Vehículos disponibles: 🚗🚙🚐")

# Title of the app centered
st.title('US Vehicle Advertisement Listings')

# Read file
df = pd.read_csv('./vehicles_us_ok.csv')

#table in the app
st.write(df)

# histogram  vehicles vs manufacturer
st.subheader('Histogram of the types of vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
# plot the histogram
st.plotly_chart(fig)

# histogram of price distribution between manufacturers
st.subheader('Histogram of price distribution between manufacturers')
# drop down menu for selecting the manufacturer 1 and 2 
# index 1 and 2 are used to set default values for the drop down menu
manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].unique(), index=2)
# create a normalized histogram checkbox
normalized = st.checkbox('Normalized')





fig = px.histogram(df, x="manufacturer", color="type", title="Number of cars for each manufacturer")


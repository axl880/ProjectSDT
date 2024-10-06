# load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# main title of the app
st.title('US Dynamic Vehicle Listings for Sale!')

#header with text and emoticons 
st.header("_List of Vehicle Brands Available for 1994-2019 Models in the U.S._ 🛻 🚗 🚙 🚐")

# Read file
df = pd.read_csv('./vehicles_us_ok.csv')

#table in the app
st.write(df)

# histogram  vehicles vs manufacturer
st.subheader('Histogram of Vehicle Types Across Manufacturers')
fig = px.histogram(df, x='manufacturer', color='type')
st.plotly_chart(fig)

# Histogram Showing Price Distribution Across Manufacturers
st.subheader('Histogram Showing Price Distribution Across Manufacturers').

# Select Manufacturer 1 and Manufacturer 2 from the dropdown menu
# Default values for the dropdown menu are set using indexes 1 and 2.
manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].unique(), index=2)

# Create a checkbox to normalize the histogram
normalized = st.checkbox('Normalized')



# Generate a histogram using inputs from Manufacturer 1 and Manufacturer 2
fig = go.Figure()

#color
colors = ['#2ca02c', '#bcbd22']
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer1]['price'], name=manufacturer1, opacity=0.75, histnorm='percent',marker_color=colors[0]))
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer2]['price'], name=manufacturer2, opacity=0.75, histnorm='percent',marker_color=colors[1]))

#Adjust the histogram to be normalized if the checkbox is checked
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

# x-axis title
fig.update_xaxes(title_text='Price')

# y-axis title
fig.update_yaxes(title_text='Percentage')

# plot the histogram
st.plotly_chart(fig)




# scatter plot matrix 
st.subheader('Scatter plot matrix')

# Dropdowns for selecting each dimension 
# Indexes 1, 2, and 3 define the default selections for the dropdown menu
x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)

# drop down for the color
color = st.selectbox('Color', df.columns, index=3)

# Dynamic subheader for the scatter plot matrix
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')

# create the scatter plot matrix
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)

# plot the scatter plot matrix
st.plotly_chart(fig)
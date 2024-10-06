# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# Title of the app centered
st.title('US Dynamic Vehicle Listings for Sale!')


st.header("_List of Vehicle Brands Available for 1994-2019 Models in the U.S._ 🛻 🚗 🚙 🚐")
           

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



#fig = px.histogram(df, x="manufacturer", color="type", title="Number of cars for each manufacturer")


# error
# create a histogram with manufacturer1 and manufacturer2 input
fig = go.Figure()
#color
colors = ['#636EFA', '#EF553B']
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer1]['price'], name=manufacturer1, opacity=0.75, histnorm='percent',marker_color=colors[0]))
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer2]['price'], name=manufacturer2, opacity=0.75, histnorm='percent',marker_color=colors[1]))
# normalize the histogram if the checkbox is checked
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
# drop down for each dimension 
# index 1, 2, and 3 are used to set default values for the drop down menu
x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)
# drop down for the color
color = st.selectbox('Color', df.columns, index=3)
# subheader for the scatter plot matrix that automatically updates
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')
# create the scatter plot matrix
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
# plot the scatter plot matrix
st.plotly_chart(fig)
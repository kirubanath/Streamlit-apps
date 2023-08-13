import streamlit as sl
import pandas as pd
import time as ts
import datetime
import matplotlib.pyplot as plt
import numpy as np

# #codes to remove the hamburger icon the watermark
# sl.markdown('''
# <style>  
# .css-6q9sum.ef3psqc3{
#             visibility:hidden;
# }
# .css-cio0dv.ea3mdgi1{
#             visibility:hidden;
# }         
# </style>
# ''', unsafe_allow_html=True)

sl.markdown(
    """
    <h1 style = 'text-align:center;'>
    Visualize Different Graphs
    </h1>
    """,
    unsafe_allow_html=True
)

#create a sidebar for taking user inputs:
sidebar = sl.sidebar
sidebar.title("Select a type of graph:")
option = sidebar.radio("radio",options=("Line","Bar","H-bar"), label_visibility="hidden")

#create graphs using matplotlib and display them:
style = "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"

if option == "Line":
    #Line graph:
    sl.markdown("<h2 style ='text-align:center'>Line Graph</h2>", unsafe_allow_html=True)
    x = np.linspace(0,10,100)
    fig = plt.figure()
    plt.style.use(style=style)
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),"--")
    sl.write(fig)
elif option == "Bar":
    #Bar graph:
    sl.markdown("<h2 style ='text-align:center'>Bar Graph</h2>", unsafe_allow_html=True)
    x = np.array([1,2,3,4,5])
    fig = plt.figure()
    plt.style.use(style=style)
    plt.bar(x,x*10)
    sl.write(fig)
else:
    #Horizontal bar graph:
    sl.markdown("<h2 style ='text-align:center'>Horizontal Bar Graph</h2>", unsafe_allow_html=True)
    x = np.array([1,2,3,4,5])
    fig = plt.figure()
    plt.style.use(style=style)
    plt.barh(x,x*10)
    sl.write(fig)
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json


# Read CSV file into a pandas DataFrame
import ast
row = 4
df = pd.read_csv("./my_data.csv")
url = ast.literal_eval(df['images'][row])
for u in url:
    st.image(u)
    


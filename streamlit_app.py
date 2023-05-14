from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json


# Read CSV file into a pandas DataFrame
df = pd.read_csv("./my_data.csv")
imgs = df['images']
for image_file in imgs:
    st.image(image_file, caption=image_file, use_column_width=True)
    


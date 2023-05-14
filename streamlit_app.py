from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json


# Read CSV file into a pandas DataFrame
df = pd.read_csv("./my_data.csv")
df['images_data']
IMAGES = [
    'https://restb-hackathon.s3.amazonaws.com/real_estate_dataset/images/303464__013.jpg',
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
]
for image_file in IMAGES:
    st.image(image_file, caption=image_file, use_column_width=True)
    


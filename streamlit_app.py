from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import pandas as pd


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

with open('./hackupc2023_restbai__dataset_sample.json') as f:
    data = json.load(f)

df = pd.DataFrame(data).T
st.image('https://restb-hackathon.s3.amazonaws.com/real_estate_dataset/images/303464__013.jpg')
st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920")
IMAGES = [
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
]
import streamlit as st
from PIL import Image

def show_photos(photos_list):
    """
    A function that takes a list of photos and displays them in a grid.
    
    Parameters:
        photos_list (list): A list of photo file paths or URLs.
    """
    
    # Check if photos_list is empty
    if not photos_list:
        st.warning("No photos to display.")
        return
    
    # Loop through the list of photos and display each photo in a grid
    for photo in photos_list:
        try:
            image = Image.open(photo)
            st.image(image, caption=photo)
        except Exception as e:
            st.warning(f"Could not display {photo}. {str(e)}")



show_photos(IMAGES)

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
IMAGES = [
    'https://restb-hackathon.s3.amazonaws.com/real_estate_dataset/images/303464__013.jpg',
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
    'https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920',
]
for image_file in IMAGES:
    st.image(image_file, caption=image_file, use_column_width=True)
    
df = pd.DataFrame(data).T
st.image('https://restb-hackathon.s3.amazonaws.com/real_estate_dataset/images/303464__013.jpg')
st.image("https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920")



show_photos(IMAGES)

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
IMAGES = [
    "https://unsplash.com/photos/GJ8ZQV7eGmU/download?force=true&w=1920",
    "https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920",
    "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
    "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
    "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
]

import streamlit as st
import streamlit.components.v1 as components
st.map(df, use_container_width=True)
def show_carousel_of_photos(photos_list):
    """
    A function that takes a list of photos and displays them in a carousel.
    
    Parameters:
        photos_list (list): A list of photo file paths or URLs.
    """
    
    # Check if photos_list is empty
    if not photos_list:
        st.warning("No photos to display.")
        return
    
    # Generate HTML code for the carousel using the streamlit-components library
    carousel_code = """
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
            {}
        </ol>
        <div class="carousel-inner">
            {}
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    """
    
    # Generate HTML code for the carousel indicators and items
    indicators_code = ""
    items_code = ""
    for i, photo in enumerate(photos_list):
        indicators_code += f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}" class=""></li>'
        active = "active" if i == 0 else ""
        items_code += f'<div class="carousel-item {active}"><img src="{photo}" class="d-block w-100" alt="Photo {i+1}"></div>'
    
    st.map(df, use_container_width=True)
    # Combine the HTML code for the carousel
    carousel_html = carousel_code.format(indicators_code, items_code)
    st.map(df, use_container_width=True)
    # Display the carousel using the components.html function from streamlit-components
    components.html(carousel_html, height=500)

    
    import pandas as pd
    import requests

    st.map(df, use_container_width=True)
    st.map(df, use_container_width=False)
    
    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

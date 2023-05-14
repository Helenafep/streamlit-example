from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import pandas as pd
from streamlit_elements import elements, mui, html, sync

def slideshow_swipeable(images):
    # Generate a session state key based on images.
    key = f"slideshow_swipeable_{str(images).encode().hex()}"

    # Initialize the default slideshow index.
    if key not in st.session_state:
        st.session_state[key] = 0

    # Get the current slideshow index.
    index = st.session_state[key]

    # Create a new elements frame.
    with elements(f"frame_{key}"):

        # Use mui.Stack to vertically display the slideshow and the pagination centered.
        # https://mui.com/material-ui/react-stack/#usage
        with mui.Stack(spacing=2, alignItems="center"):

            # Create a swipeable view that updates st.session_state[key] thanks to sync().
            # It also sets the index so that changing the pagination (see below) will also
            # update the swipeable view.
            # https://mui.com/material-ui/react-tabs/#full-width
            # https://react-swipeable-views.com/demos/demos/
            with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                for image in images:
                    html.img(src=image, css={"width": "100%"})

            # Create a handler for mui.Pagination.
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            def handle_change(event, value):
                # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                st.session_state[key] = value-1

            # Display the pagination.
            # As the index value can also be updated by the swipeable view, we explicitely
            # set the page value to index+1 (page value starts at 1).
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


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
st.title("Streamlit Elements Slideshow")

st.subheader("Swipeable slideshow")
slideshow_swipeable(IMAGES)
st.image('https://restb-hackathon.s3.amazonaws.com/real_estate_dataset/images/303464__013.jpg')

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Esto es una puta basura", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns
    
    import streamlit as st
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        [np.array([41.3887900,2.1589900])],
        columns=['lat', 'lon'])
    print(df)
    
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

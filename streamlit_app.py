import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import gzip

# Load data
# Define file paths
IMDb_path = 'IMDb_data.csv.gz'

# Load the gzipped CSV file into a pandas DataFrame
try:
    with gzip.open(IMDb_path, 'rt', encoding='utf-8') as file:
        IMDb_df = pd.read_csv(file)
except FileNotFoundError:
    pass
except Exception as e:
    pass

# Initialize
if "rerun" not in st.session_state:
    st.session_state.rerun = True

# Home page
st.title("Thursday Filmday :clapper::film_projector:")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Film Chooser
st.header("Film Chooser", divider="rainbow")

# Process
st.subheader('Search Filters', divider='grey')

    # Title
#titles = sorted(IMDb_df['primaryTitle'].unique().tolist())
#selected_title = st.multiselect(
##    "Title:",
#    (titles),
#)

    # Year
min_year = IMDb_df['startYear'].min()
max_year = datetime.now().year
selected_years = st.slider("Select a range of years:", 
                   min_year, max_year,
                   (min_year, max_year),
                   step=1)

    # Time
min_time = 30
max_time = 300
selected_time = st.slider("Select a film length in minutes:", 
                   min_time, max_time,
                   (min_time, max_time),
                   step=1)

    # Genres
genres = sorted(IMDb_df.columns[7:33 + 1].tolist())
genres.insert(0, 'No preference')
selected_genre = st.multiselect(
    "Genre(s):",
    (genres),
)

    # Ratings
min_rating = 1
max_rating = 10 
selected_rating = st.slider("Select a range of film IMDb ratings:", 
               min_rating, max_rating,
               (1, 10))

    # Votes
min_votes = round(IMDb_df['numVotes'].min(), -3)
max_votes = round(IMDb_df['numVotes'].max()+1000, -3)
selected_votes = st.slider("Select a range of how many have voted for the film rating:", 
               min_votes, max_votes,
               (min_votes, max_votes),
               step=1000)

    # Director
#director = IMDb_df['nmDirector_1', 'nmDirector_2'].unique().tolist()
#director.insert(0, 'No preference')
#selected_director = st.selectbox(
#    "Director:",
#    (director),
#)

# UI and buttons
st.subheader('Filter Values', divider='grey')

left_column, right_column = st.columns(2)

with left_column:
        st.write('**Selected values:**')

                # Title
        #st.write(print(selected_title))

            # Year
        st.write(f"Year range: **{selected_years[0]}** and **{selected_years[1]}**")

                    # Time
        st.write(f"Film duration range: **{selected_time[0]}** and **{selected_time[1]}**")

            # Ratings
        st.write(f"IMDb rating range: **{selected_rating[0]}** and **{selected_rating[1]}**")

            # Votes
        st.write(f"IMDb voting range: **{selected_votes[0]}** and **{selected_votes[1]}**")

            # Director
        #st.write(print(selected_director))

with right_column:
        st.write('**Selected genres:**')

                # Genres
        # Initialize the string variable
        s = ''

        # Genres
        if len(selected_genre) > 3:
            st.error("You can select a maximum of 3 genres!")
        else:
            for i in selected_genre:
                s += "- " + i + "\n"
            
            if s:
                st.markdown(s)

# Movie Stats
st.header("Movie Stats", divider="rainbow")

st.write(
    'This page is still under construction'
)

# Film Archive
st.header("Film Archive", divider="rainbow")

st.write(
    'This page is still under construction'
)
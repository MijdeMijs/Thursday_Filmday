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
    
    # Title
#titles = sorted(IMDb_df['primaryTitle'].unique().tolist())

#selected_title = st.multiselect(
##    "Title:",
#    (titles),
#)

#st.write(print(selected_title))

    # Year
min_year = IMDb_df['startYear'].min()
max_year = datetime.now().year

selected_years = st.slider("Select a range of years:", 
                   min_year, max_year,
                   (min_year, max_year),
                   step=1)

st.write("Values:", selected_years)

    # Time
min_time = 30
max_time = 300

selected_time = st.slider("Select a film length in minutes:", 
                   min_time, max_time,
                   (min_time, max_time),
                   step=1)

st.write("Values:", selected_time)

    # Genres
genres = sorted(IMDb_df.columns[7:33 + 1].tolist())
genres.insert(0, 'No preference')

# UI and buttons
selected_genre = st.multiselect(
    "Genre(s):",
    (genres),
)

if len(selected_genre) > 3:
    st.error("You can select a maximum of 3 genres!")
else:
    s = ''
    for i in selected_genre:
        s += "- " + i + "\n"
        
    if s:
        st.markdown(s)

    # Ratings
min_rating = 1
max_rating = 10 

selected_rating = st.slider("Select a range of film IMDb ratings:", 
               min_rating, max_rating,
               (1, 10))

    # Votes
min_votes = IMDb_df['numVotes'].min()
max_votes = IMDb_df['numVotes'].max()

selected_votes = st.slider("Select a range of how many have voted for the film rating:", 
               min_votes, max_votes,
               (min_votes, max_votes))

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
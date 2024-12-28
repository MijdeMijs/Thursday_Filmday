import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import gzip

if "modal_shown" not in st.session_state:
   st.session_state.modal_shown = False

# Cookies!!!
@st.dialog('Cookies!?')
def show_modal():
   st.write('**NEVER ALLOW COOKIES!** We don\'t need :cookie: or :cupcake:!!! We want MUFFINS!')
   
   gift = 'https://www.youtube.com/watch?v=kwgYSfqO0fg'
   pop_up = ''

   col1, col2, col3 = st.columns([5, 5, 10])

   with col1:
       if st.button("Bake a :cookie:"):
           pop_up = "WHY!? Don\'t give your data!"

   with col2:
       if st.button("Bake a :cupcake:"):
           pop_up = 'DISSAPOINTMENT ACHIEVED!'

   with col3:
       st.link_button(':gift:', gift)

   st.write(f'**:red[{pop_up}]**')

if not st.session_state.modal_shown:
   show_modal()
   st.session_state.modal_shown = True
      
# Load data
# Define file paths
IMDb_path = 'IMDb_data.csv.gz'

@st.cache_data
def load_data():
    # Load the gzipped CSV file into a pandas DataFrame
    with gzip.open(IMDb_path, 'rt', encoding='utf-8') as file:
        data = pd.read_csv(file)
    return data

IMDb_df = load_data()  # This is only executed once

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
st.write('Welcome to the Film Chooser! This is a tool that might help you select choose a movie for the movie night. It is very simple to use. You just provide your preferences in the filter options below (see Search Filters). After you\'re done, quickly check your choices (Applied Filters). A table with options that are within your requirements will automatically update (see Possible Movies). Good luck chosing your movie!!!')

# Process
st.subheader('Search Filters', divider='grey')

    # Genres
# Initialize genre list
@st.cache_data
def genre_list():
    genre_list = sorted(IMDb_df.columns[8:34 + 1].tolist())
    genre_list.insert(0, 'No preference...')
    return genre_list

genres = genre_list()

main_genre = st.selectbox('Select a main genre:', genres)
genre_selection = [main_genre]

# Disable additional genres if "No preference..." is selected
if main_genre == "No preference...":
    st.write("Note! Select a main genre to select additional genres.")
    additional_genre_options = []

    operator = 0
else:
    # Filter out the main genre from the additional genres list
    additional_genre_options = [genre for genre in genres if genre != main_genre and genre != "No preference..."]

    additional_genres = st.multiselect(
        "Additional genre(s):",
        options = additional_genre_options    
    )

    genre_selection.extend(additional_genres)

            # AND/OR operator
    if st.checkbox('AND/OR operator'):
        operator = 1
        st.write('**OR** operator is selected to pass your genres. Notice that this could give :red[**less precise**], but :red[**more movie options**]!')
    else:
        operator = 0
        st.write('**AND** operator is selected to pass your genres. Notice that this could give :red[**more precise**], but :red[**fewer movie options**]!')

    # Year
min_year = IMDb_df['startYear'].min()
max_year = datetime.now().year
selected_years = st.slider("Range of premiere years:", 
                   min_year, max_year,
                   (1970, max_year),
                   step=1)

    # Time
min_time = 30
max_time = 240
selected_time = st.slider("Range of film duration in minutes:", 
                   min_time, max_time,
                   (60, 120),
                   step=5)

    # Ratings
min_rating = 1
max_rating = 10 
selected_rating = st.slider("Range of film IMDb ratings:", 
               min_rating, max_rating,
               (6, 10))

    # Votes
min_votes = 0
max_votes = 500000
selected_votes = st.slider("Minimum number of votes for the IMDb film rating (the blockbusters have at least 200,000 votes):", 
               min_votes, max_votes, 100000,
               step=1000)

# UI and buttons
st.subheader('Applied Filters', divider='grey')

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
        st.write(f"Minimum number of IMDb votes: **{selected_votes}**")

            # Director
        #st.write(print(selected_director))

with right_column:
        st.write('**Selected genres:**')

                # Genres
        # Initialize the string variable
        s = ''

        # Genres
        if len(genre_selection) > 3:
            st.error("You can select a maximum of 2 additional genres!")
        else:
            for i in genre_selection:
                s += "- " + i + "\n"
            
            if s:
                st.markdown(s)

# Possible Movies List
st.subheader('Possible Movies', divider='grey')

filters = (
    IMDb_df['startYear'].between(selected_years[0], selected_years[1]) &
    IMDb_df['runtimeMinutes'].between(selected_time[0], selected_time[1]) &
    IMDb_df['averageRating'].between(selected_rating[0], selected_rating[1]) &
    (IMDb_df['numVotes'] >= selected_votes)
)

# Apply genre-based filtering if necessary
if genre_selection and 'No preference...' not in genre_selection:
    if operator == 0:  # AND condition
        genre_filter = (IMDb_df[genre_selection] == 1).all(axis=1)
    elif operator == 1:  # OR condition
        genre_filter = (IMDb_df[genre_selection].sum(axis=1) > 0)
    filters &= genre_filter

# Apply the combined filter to the DataFrame
filtered_df = IMDb_df[filters]

    # Make new df with possible film options
filtered_data = {'ID': filtered_df['tconst'],
                 'Film': filtered_df['primaryTitle'],
                 'Year': filtered_df['startYear'],
                 'Duration': filtered_df['runtimeMinutes'],
                 'Genres': filtered_df['genres'],
                 'IMDb Rating': filtered_df['averageRating'],
                 'Number of votes': filtered_df['numVotes'],
                 '1st director': filtered_df['nmDirector_1'],
                 '2nd director': filtered_df['nmDirector_2']}
new_df = pd.DataFrame(filtered_data)

st.write(new_df.iloc[:, 1:].reset_index(drop=True))

if 'No preference...' in genre_selection:
    warning = f':red[**Warning!** Genre is not filtered because \'No preference...\' is selected!]'
else:
    warning = ''

st.write(warning)

st.subheader('Visit IMDb Page', divider='grey')

left_column, right_column = st.columns(2)

with left_column:
    # Allow the user to select the sorting column
    sort_column = st.selectbox("Select a column to sort by:", new_df.columns[[1, 2, 4, 5]])

        # Ascending or descending
    if st.checkbox('Ascending or descending'):
        ascent = False
        st.write(f'Currently, **{sort_column}** in descending order.')
    else:
        ascent = True
        st.write(f'Currently, **{sort_column}** in ascending order.')

    # Sort the DataFrame dynamically
    sorted_new_df = new_df.sort_values(by=sort_column, ascending=ascent).iloc[:, :-2].reset_index(drop=True)

    # Select the first 10 rows of the sorted DataFrame
    top_10 = sorted_new_df.head(10)

with right_column:
    IMDb_link = st.selectbox("Select IMDb film page:", top_10['Film'].unique())
    ID = top_10[top_10['Film'] == IMDb_link].iloc[0, 0]

    # Define the URL you want to link to
    url = f'https://www.imdb.com/title/{ID}/'

    # Create the button
    st.link_button("Visit the IMDb film page!", url)
    
st.write(top_10.iloc[:, 1:])

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

# Footer at the bottom
st.markdown(
    """
    <style>
        .footer {
            width: 100%;
            background-color: #f9f9f9;
            text-align: center;
            padding: 10px 0;
            margin-top: 20px;
            font-size: 14px;
            color: #6c757d;
        }
    </style>
    <div class="footer">
        <p>The Tursday Filmday web page was made possible by <a href="https://eelslap.com/" target="_blank">ADHD hyperfocus</a>, <a href="https://streamlit.io/" target="_blank">Streamlit</a> and <a href="https://developer.imdb.com/" target="_blank">IMDb Developer</a>
    </div>
    """,
    unsafe_allow_html=True
)
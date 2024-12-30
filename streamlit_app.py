# ===============================
# region Imports
# ===============================
import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import gzip

# endregion

# ===============================
# region Cookie pop-up
# ===============================

# Check if pop-up has been shown
if "modal_shown" not in st.session_state:
   st.session_state.modal_shown = False

# Show pop-up with buttons
@st.dialog('Cookies!?')
def show_modal():
   st.write('**NEVER ALLOW COOKIES!** We don\'t need :cookie: or :cupcake:!!! We want MUFFINS!')
   
   gift = 'https://www.youtube.com/watch?v=kwgYSfqO0fg'
   pop_up = ''

   pop_up_col1, pop_up_col2, pop_up_col3 = st.columns([5, 5, 10])

   with pop_up_col1:
       if st.button("Bake a :cookie:"):
           pop_up = "WHY!? Don\'t give your data!"

   with pop_up_col2:
       if st.button("Bake a :cupcake:"):
           pop_up = 'DISSAPOINTMENT ACHIEVED!'

   with pop_up_col3:
       st.link_button(':gift:', gift)

   st.write(f'**:red[{pop_up}]**')

# Run pop-up and update session state
if not st.session_state.modal_shown:
   show_modal()
   st.session_state.modal_shown = True

# endregion

# ===============================
# region Load data
# ===============================

# Define load and cache IMDb data
@st.cache_data
def load_data():
    # Load the gzipped CSV file into a pandas DataFrame
    with gzip.open('IMDb_data.csv.gz', 'rt', encoding='utf-8') as file:
        data = pd.read_csv(file)
    return data

# Load IMDb data
IMDb_df = load_data()

# endregion

# ===============================
# region Initialize
# ===============================
if "rerun" not in st.session_state:
    st.session_state.rerun = True

# endregion

# ===============================
# region Home page
# ===============================

# Title
st.title("Thursday Filmday :clapper::film_projector:")

# Web page introduction
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# endregion

# ===============================
# region 1. Film Chooser
# ===============================

# Title
st.header("Film Chooser", divider="rainbow")

# Introduction
st.write('Welcome to the Film Chooser! This is a tool that might help you select choose a movie for the movie night. It is very simple to use. You just provide your preferences in the filter options below (see Search Filters). After you\'re done, quickly check your choices (Applied Filters). A table with options that are within your requirements will automatically update (see Possible Movies). Good luck chosing your movie!!!')

# ===============================
# region 1.1 Search Filters
# ===============================

st.subheader('Search Filters', divider='violet')

# ===============================
# region Genre selection
# ===============================

st.write('**Genre:**')

st.write('Select the genres that you would like to watch. First select a main genre and then select additional genres if you like. If you don\'t care about the genre of a movie, you can select the option **\'No preference for any genre...\'** (default) in the \'Main genre\' selection field. This option won\'t filter films by genre. If you do want to select a genre, but you don\'t care what the main genre of a movie is, choose **\'No preference for a main genre...\'** in the \'Main genre\' selection field. This will allow you to filter genres without considering the main genre of a film.')

# ===============================
# region AND/OR jack in the box
# ===============================

def AND_OR():
    if st.checkbox('AND/OR operator'):
        operator = 1
        st.write('**OR** operator is selected to pass your genres. Notice that this could give :red[**less precise**], but :red[**more movie options**]!')
    else:
        operator = 0
        st.write('**AND** operator is selected to pass your genres. Notice that this could give :red[**more precise**], but :red[**fewer movie options**]!')
    return operator

# endregion

# ===============================
# region Genre list
# ===============================

# Define initialize and cache genre list
@st.cache_data
def genre_list():
    genre_list = sorted(IMDb_df.columns[8:34 + 1].tolist())
    genre_list.insert(0, 'No preference for a main genre...')
    genre_list.insert(0, 'No preference for any genre...')
    return genre_list

# Run genre list
genres = genre_list()

# endregion

# select main genre 
main_genre = st.selectbox('Main genre:', genres)

# ===============================
# region Genre if-statement
# ===============================

def process_genre_selection(main_genre, genres):
    if main_genre == "No preference for any genre...":
        genre_options = []
        other_genres = []
        genre_selection = []
        operator = 0
        genre_tag = 0
    elif main_genre == "No preference for a main genre...":
        genre_options = [
            genre for genre in genres if genre not in ["No preference for any genre...", 
                                                       "No preference for a main genre..."]
        ]
        other_genres = st.multiselect(
            "Select a maximum of **three** genre(s):",
            options=genre_options
        )
        genre_selection = other_genres.copy()
        operator = AND_OR()
        genre_tag = 1
    else:
        genre_options = [
            genre for genre in genres if genre != main_genre and genre not in ["No preference for any genre...", 
                                                                               "No preference for a main genre..."]
        ]
        other_genres = st.multiselect(
            "Select a maximum of **two** additional genre(s):",
            options = genre_options    
        )
        genre_selection = other_genres.copy()
        operator = AND_OR()
        genre_tag = 2

    return genre_options, other_genres, genre_selection, operator, genre_tag

genre_options, other_genres, genre_selection, operator, genre_tag = process_genre_selection(main_genre, genres)

# endregion

# ===============================
# region Check length
# ===============================

if genre_tag == 1 and len(genre_selection) > 3:
            st.error("You can select a maximum of 3 genres!")
elif genre_tag == 2 and len(genre_selection) > 2:
            st.error("You can select a maximum of 2 additional genres!")

# endregion

st.divider()

# endregion

# ===============================
# region Simple filter parameters
# ===============================

# year
min_year = IMDb_df['startYear'].min()
max_year = datetime.now().year
default_min_year = 1970
default_max_year = max_year

# time 
min_time = 30
max_time = 240
default_min_time = 60
default_max_time = 120

# ratings
min_rating = 1
max_rating = 10
default_min_rating = 6
default_max_rating = max_rating

# votes
min_votes = 0
max_votes = 500000
default_min_votes = 100000
step_size = 1000

# endregion

# ===============================
# region Simple filters
# ===============================    

# year slider
st.write('**Year:**')
selected_years = st.slider("Range of premiere years:", 
                   min_year, max_year,
                   (default_min_year, default_max_year),
                   step=1)
st.divider()

# time slider
st.write('**Duration:**')
selected_time = st.slider("Range of film duration in minutes:", 
                   min_time, max_time,
                   (default_min_time, default_max_time),
                   step=5)
st.divider()

# ratings slider
st.write('**Rating:**')
selected_rating = st.slider("Range of film IMDb ratings:", 
               min_rating, max_rating,
               (default_min_rating, default_max_rating))
st.divider()

# votes slider
st.write('**Votes:**')
selected_votes = st.slider("Minimum number of votes for the IMDb film rating (the blockbusters have at least 200,000 votes):", 
               min_votes, max_votes, 
               default_min_votes,
               step=step_size)

# endregion

# endregion

# ===============================
# region 1.2 Applied Filters
# ===============================

st.subheader('Applied Filters', divider='violet')

# ===============================
# region Left & right layout column
# ===============================

left_column, right_column = st.columns(2)

# ===============================
# region Left layout column
# ===============================

with left_column:
        st.write('**Selected values:**')

        # year
        st.write(f"Year range: **{selected_years[0]}** and **{selected_years[1]}**")

        # time
        st.write(f"Film duration range: **{selected_time[0]}** and **{selected_time[1]}**")

        # ratings
        st.write(f"IMDb rating range: **{selected_rating[0]}** and **{selected_rating[1]}**")

        # votes
        st.write(f"Minimum number of IMDb votes: **{selected_votes}**")

# endregion

# ===============================
# region Right layout column
# ===============================

with right_column:
        st.write('**Selected genres:**')

        # Genres
        # Initialize the string variable
        s = ''

        # Genres
        if (genre_tag == 1 and len(genre_selection) > 3) or (genre_tag == 2 and len(genre_selection) > 2):
            st.error("More that 3 genres are selected!")
        elif genre_tag == 1:
            for i in genre_selection:
               s += "- " + i + "\n"            
            if s:
                st.markdown(s)
            else:
                st.write('No genres selected...')
        elif genre_tag == 2:
            st.write(f'Main genre: **{main_genre}**')
            filtered_genre_selection = [
                 genre for genre in genre_selection if genre != main_genre
            ]
            st.write('Additional genre(s):')
            for i in filtered_genre_selection:
                s += "- " + i + "\n"            
            if s:
                st.markdown(s)
            else:
                st.write('No additional genres selected...')
        else:
            st.write('No genres selected...')

# endregion

# endregion

# endregion

# ===============================
# region 1.3 Possible Movies
# ===============================

st.subheader('Possible Movies', divider='violet')

# ===============================
# region Define & apply filters
# ===============================

@st.cache_data
def IMDb_filter(IMDb_df, 
                selected_years, 
                selected_time, 
                selected_rating, 
                selected_votes,
                genre_tag, 
                main_genre, 
                operator, 
                genre_selection):
    
    # Define static filters
    filters = (
        IMDb_df['startYear'].between(selected_years[0], selected_years[1]) &
        IMDb_df['runtimeMinutes'].between(selected_time[0], selected_time[1]) &
        IMDb_df['averageRating'].between(selected_rating[0], selected_rating[1]) &
        (IMDb_df['numVotes'] >= selected_votes)
    )

    # Add main genre filter if genre_tag = 2
    if genre_tag == 2:
        filters = filters & (IMDb_df['main_genre'] == main_genre)

    # Apply genre-based filtering if necessary including AND/OR operator
    if genre_tag != 0 :
        if operator == 0:  # AND condition
            genre_filter = (IMDb_df[genre_selection] == 1).all(axis=1)
        elif operator == 1:  # OR condition
            genre_filter = (IMDb_df[genre_selection].sum(axis=1) > 0)
        filters &= genre_filter

    # Apply filters to IMDb_df
    return IMDb_df[filters]

# Run IMDb_filter() over IMDb_df based on filter settings by user
filtered_df = IMDb_filter(IMDb_df, 
                          selected_years, 
                          selected_time, 
                          selected_rating, 
                          selected_votes,
                          genre_tag, 
                          main_genre, 
                          operator, 
                          genre_selection)

# endregion

# ===============================
# region Display filtered movies
# ===============================

@st.cache_data
def display_filtered_df(filtered_df):

    # Feature selection for new df
    filtered_data = {'ID': filtered_df['tconst'],
                    'Film': filtered_df['primaryTitle'],
                    'Year': filtered_df['startYear'],
                    'Duration': filtered_df['runtimeMinutes'],
                    'Main genre': filtered_df['main_genre'],
                    'Additional genres': filtered_df['other_genres'],
                    'IMDb Rating': filtered_df['averageRating'],
                    'Number of votes': filtered_df['numVotes']}
    
    # Selected features to Pandas df
    display_df = pd.DataFrame(filtered_data)

    # Hide ID feature for user and re-index
    return display_df

# Run display_filtered_df()
display_df = display_filtered_df(filtered_df)

# Show display_df or error message to user
if display_df.empty:
    display_df = st.error('No movies found with the chosen filters!')
else:
    st.write(f'Found **{len(display_df)}** films within your chosen filters:')
    st.write(display_df.iloc[:, 1:].reset_index(drop=True))

# endregion

# ===============================
# region No genre warning
# ===============================

if not genre_selection:
    warning = f':red[**Warning!** No filter applied on genre!]'
    st.write(warning)

# endregion

# endregion

# ===============================
# region 1.4 Visit IMDb Page
# ===============================

st.subheader('Visit IMDb Page', divider='grey')

# ===============================
# region Top selection
# ===============================

top_n_choice = st.selectbox('Select a top (10 - 1000):', ['Top 10', 
                                                          'Top 50', 
                                                          'Top 100', 
                                                          'Top 500',
                                                          'Top 1000'])

top_n_mapping = {
    'Top 10': 10,
    'Top 50': 50,
    'Top 100': 100,
    'Top 500': 500,
    'Top 1000': 1000
}

top_n = top_n_mapping[top_n_choice]

# endregion

# ===============================
# region Top sort function
# ===============================

@st.cache_data
def sort_top(display_df, sort_column, ascent, top_n):

    # Sort display_df dynamically and select the first n-rows (top_n) of sorted display_df
    top_n_list = display_df.sort_values(by=sort_column, 
                                        ascending=ascent).reset_index(drop=True).head(top_n)
    
    return top_n_list

# endregion

# ===============================
# region Left & right layout column
# ===============================

left_column, right_column = st.columns(2)

# ===============================
# region Left layout column
# ===============================

with left_column:

    # Select on column display_df is sorted
    sort_column = st.selectbox("Select a column to sort by:", display_df.columns[[6, 2, 3, 7]])

    # Descending or ascending
    if st.checkbox('Descending or ascending'):
        ascent = True
        st.write(f'Currently, **{sort_column}** is ordered in ascending order.')
    else:
        ascent = False
        st.write(f'Currently, **{sort_column}** is ordered in descending order.')
    
    # Run sorting fuction with user inputs
    top_list = sort_top(display_df, sort_column, ascent, top_n)

# endregion

# ===============================
# region Right layout column
# ===============================

with right_column:

    # Select a movie
    IMDb_link = st.selectbox("Select IMDb film page:", top_list['Film'].unique())
    
    # Get film ID
    ID = top_list[top_list['Film'] == IMDb_link].iloc[0, 0]

    # Define IMDb URL
    url = f'https://www.imdb.com/title/{ID}/'

    # Create button with IMDb link 
    st.link_button("Visit the IMDb film page!", url)
    
# endregion

# endregion

st.divider()

st.write(top_list.iloc[:, 1:])

# endregion

# endregion

# ===============================
# region Movie Stats
# ===============================
st.header("Movie Stats", divider="rainbow")

st.write(
    'This page is still under construction'
)

# endregion

# ===============================
# region Film Archive
# ===============================
st.header("Film Archive", divider="rainbow")

st.write(
    'This page is still under construction'
)

# endregion

# ===============================
# region Footer
# ===============================

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

# endregion
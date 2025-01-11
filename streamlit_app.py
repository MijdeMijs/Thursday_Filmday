# ===============================
# region Imports
# ===============================
import streamlit as st
from streamlit_theme import st_theme
import numpy as np
import pandas as pd
import time
from datetime import datetime
import gzip
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# endregion

# ===============================
# region Get theme
# ===============================

theme = st_theme()

theme_col = theme.get('base', 'light')

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

   pop_up_col1, pop_up_col2, pop_up_col3 = st.columns([6, 6, 11])

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
# region Sessionstate guards
# ===============================

if 'first_run' not in st.session_state:
    st.session_state.first_run = True

if 'show_popup_Friends' not in st.session_state:
    st.session_state.show_popup_Friends = False

# endregion

# ===============================
# region Bug the Caterpillar
# ===============================

# ===============================
# region Bug random path
# ===============================

# Generate random positions within the specified range
@st.cache_data
def Bug_random_positions(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
        # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

# Generate random keyframe positions
random_positions_Bug = Bug_random_positions()

# endregion

# ===============================
# region Bug keyframes
# ===============================

@st.cache_data
def keyframes_CSS_Bug(random_positions_Bug):
    keyframes = "@keyframes move_Bug {"
    step = 0
    for top, left in random_positions_Bug:
        keyframes += f"{step}% {{ top: {top}%; left: {left}%; }}"
        step += int(100 / (len(random_positions_Bug) - 1))  # Evenly distribute steps
    keyframes += "}"
    return keyframes

keyframes_Bug = keyframes_CSS_Bug(random_positions_Bug)

# endregion

# ===============================
# region Bug CSS
# ===============================

st.markdown(
    f"""
    <style>
    body {{
        overflow: hidden; /* Prevent scrollbars if the bug moves beyond visible areas */
    }}

    .bug {{
        font-size: 25px; /* Perfect bug size */
        position: fixed; /* Fixed positioning allows movement across the entire screen */
        z-index: 1000; /* Ensure it floats above all Streamlit components */
        animation: move_Bug 400s linear infinite; /* Smooth and infinite roaming */
        pointer-events: none; /* Allow interaction with elements underneath */
    }}

    {keyframes_Bug}
    </style>
    """,
    unsafe_allow_html=True,
)

# endregion

# ===============================
# region Bug initialize
# ===============================

if "show_bug" not in st.session_state:
    st.session_state.show_bug = False

if 'bug_first_run' not in st.session_state:
    st.session_state.bug_first_run = False

# endregion

# ===============================
# region Bug pop-up initialize
# ===============================

# Initialize session state for Bug the Caterpillar visibility
if 'show_popup_Bug' not in st.session_state:
    st.session_state.show_popup_Bug = False

# Function to display the Bug the Caterpillar pop-up
@st.dialog("Bug the Caterpillar")
def show_popup_Bug():
    st.write("Oh no! Bug the Caterpillar spawned! :bug:")

# endregion

# ===============================
# region Bug random spawn
# ===============================

# Function to randomly set show_popup to True
def random_bug():
    if not st.session_state.show_bug and random.random() < 0.005:  # 0.5% chance to spawn Bug the Caterpillar
        st.session_state.show_bug = True

# Call the function to potentially show the popup
random_bug()
    
# endregion

# endregion

# ===============================
# region Escargot the Snail
# ===============================

# ===============================
# region Escargot random path
# ===============================

@st.cache_data
def Escargot_random_positions(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
    # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

random_positions_Escargot = Escargot_random_positions()

# endregion

# ===============================
# region Escargot keyframes
# ===============================

@st.cache_data
def keyframes_CSS_Escargot(random_positions_Escargot):
    keyframes = "@keyframes move_Escargot {"
    step = 0
    for top, left in random_positions_Escargot:
        keyframes += f"{step}% {{ top: {top}%; left: {left}%; }}"
        step += int(100 / (len(random_positions_Escargot) - 1))  # Evenly distribute steps
    keyframes += "}"
    return keyframes

keyframes_Escargot = keyframes_CSS_Escargot(random_positions_Escargot)

# endregion

# ===============================
# region Escargot CSS
# ===============================

st.markdown(
    f"""
    <style>
    body {{
        overflow: hidden; /* Prevent scrollbars if the bug moves beyond visible areas */
    }}

    .escargot {{
        font-size: 25px; /* Perfect bug size */
        position: fixed; /* Fixed positioning allows movement across the entire screen */
        z-index: 1000; /* Ensure it floats above all Streamlit components */
        animation: move_Escargot 4000s linear infinite; /* Smooth and infinite roaming */
        pointer-events: none; /* Allow interaction with elements underneath */
    }}

    {keyframes_Escargot}
    </style>
    """,
    unsafe_allow_html=True,
)

# endregion

# ===============================
# region Escargot initialize
# ===============================

if "show_escargot" not in st.session_state:
    st.session_state.show_escargot = False

if 'escargot_first_run' not in st.session_state:
    st.session_state.escargot_first_run = False

# endregion

# ===============================
# region Escargot pop-up initialize
# ===============================

# Initialize session state for Escargot the Snail visibility
if 'show_popup_Escargot' not in st.session_state:
    st.session_state.show_popup_Escargot = False

# Function to display the Escargot the Snail pop-up
@st.dialog("Monsieur Escargot the Snail")
def show_popup_Escargot():
    st.write("Escargot the Snail is is keeping you company! :snail:")

# endregion

# ===============================
# region Random Escargot
# ===============================

# Function to randomly set show_popup to True
def random_escargot():
    if not st.session_state.show_escargot and random.random() < 0.05: # 5% chance to spawn Escargot the Snail
        st.session_state.show_escargot = True

# Call the function to potentially show the popup
random_escargot()

# Display the bug if the button is clicked
if st.session_state.show_escargot:
    st.markdown(
        """
        <div class="escargot">🐌</div>
        """,
        unsafe_allow_html=True,
    )

# endregion

# endregion

# ===============================
# region Both friends pop-up
# ===============================

# Function to display the both friends pop-up
@st.dialog("Two buddies")
def show_popup_Friends():
    st.write('''Now you have two friends! Bug the Caterpillar :bug: 
             and Escargot the Snail :snail:''')

# endregion

# ===============================
# region Load data
# ===============================

# ===============================
# region IMDb data
# ===============================

# Define load and cache IMDb data
@st.cache_data
def load_data():
    # Load the gzipped CSV file into a pandas DataFrame
    with gzip.open('IMDb_data.csv.gz', 'rt', encoding='utf-8') as file:
        data = pd.read_csv(file)
    
    IMDb_df_version = pd.to_datetime(data.iloc[0, 0])

    data = data.iloc[1:].reset_index(drop=True)

    return data, IMDb_df_version

# Load IMDb data
IMDb_df, IMDb_df_version = load_data()

# endregion

# ===============================
# region Archieve data
# ===============================

# Define load and cache archieve data
@st.cache_data
def load_data():
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv('archieve.csv', delimiter=',')
    
    archieve_df_version = pd.to_datetime(data.iloc[0, 0])

    data = data.iloc[1:].reset_index(drop=True)

    data['date'] = pd.to_datetime(data['date'], 
                                  format='%Y-%m-%d %H:%M:%S')

    data['cumulative_votes'] = data.groupby('room')['votes'].cumsum()
    data['cumulative_win'] = data.groupby('room')['watched'].cumsum()

    return data, archieve_df_version

# Load archieve data
archieve_df, archieve_df_version = load_data()

# endregion

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

# ===============================
# region Intro
# ===============================

# Title
st.title("Thursday Filmday :clapper::film_projector:")

# Web page introduction
st.write("""
    Welcome to **Thursday Filmday**! :clapper:

    This app is designed to enhance your movie night experience with three exciting sections:

    1. **Movie Chooser**: This section helps you select the perfect film for your movie night. Whether you're in the mood for a comedy, drama, or action-packed thriller, the Movie Chooser will guide you to the best options.

    2. **Movie Stats**: Dive into some fun statistics about all the movies we've watched together. Discover interesting trends, favorite genres, and more. It's a great way to see our collective movie-watching habits!

    3. **Film Archive**: Here, you can browse through a comprehensive list of all the films we've watched and suggested. It's a handy reference to revisit past favorites or find new recommendations.

    I've also hidden some fun easter eggs throughout the app for you to discover. I put a lot of effort into creating this page, so I hope you enjoy it. Please be gentle, as the app might not be the most efficient in the world.

    Enjoy your movie night and happy watching! :popcorn:
    """)

# endregion

# ===============================
# region Spawn friends
# ===============================

# ===============================
# region Spawn Bug
# ===============================

# Button to toggle the bug visibility
if st.button(':no_entry_sign: DON\'T PRESS!!!'):
    st.session_state.show_bug = True

# Display the bug if the button is clicked
if st.session_state.show_bug:
    st.markdown(
        """
        <div class="bug">🐛</div>
        """,
        unsafe_allow_html=True,
    )

# endregion

# ===============================
# region Control messages
# ===============================

if not st.session_state.first_run:
    if st.session_state.show_bug and st.session_state.show_escargot and not st.session_state.show_popup_Friends:
        show_popup_Friends()
        st.write("Friends condition met")
        st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Bug = True
        st.session_state.show_popup_Escargot = True
    elif (st.session_state.show_bug 
          and not st.session_state.show_popup_Bug
          and not st.session_state.bug_first_run):
        show_popup_Bug()
        st.write("Bug condition met")
        # st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Bug = True
    elif (st.session_state.show_escargot 
          and not st.session_state.show_popup_Escargot 
          and not st.session_state.escargot_first_run):
        show_popup_Escargot()
        st.write("Escargot condition met")
        # st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Escargot = True
else:
    st.session_state.first_run = False
    st.session_state.bug_first_run = st.session_state.show_bug 
    st.session_state.escargot_first_run = st.session_state.show_escargot

# endregion

# endregion

# endregion

# ===============================
# region 1. Film Chooser
# ===============================

# Title
st.header("Film Chooser", divider="rainbow")

# Introduction
st.write('''Welcome to the Film Chooser! This is a tool that might help you to choose a 
         movie for the movie night. It is very simple to use, but here are some tips:''')

st.write("""[Search Filters](#search-filters) - When starting the Thursday Filmday app, 
         default filter settings are applied. You can select a main genre and additional 
         genres, or choose **'No preference for any genre...'** to avoid filtering by 
         genre. If you want to filter genres but don't care about the main genre, select 
         **'No preference for a main genre...'**. Be cautious with the votes setting; low 
         settings might exclude good movies. For blockbusters, set a high filter on votes 
         (minimum 200,000).""")

st.write('''[Applied Filters](#applied-filters) - Get a short overview of the filter 
         settings.''')

st.write('''[Possible Movies](#possible-movies) - In this list, you'll find all films 
         that match the filter settings you choose. This list will automatically update if 
         you decide to change the filter settings. You'll also see how many films were 
         found and get notified with a warning if you didn't select a genre.''')

st.write('''[Visit IMDb Page](#visit-imdb-page) - With this function, you can easily visit 
         the IMDb film pages of movies that are in the Possible Movies list. Here, you 
         select a subset of films based on a movie's feature that you choose.''')

st.markdown("""
    <style>
    @keyframes rainbow {
        0% {color: red;}
        14% {color: orange;}
        28% {color: yellow;}
        42% {color: green;}
        57% {color: blue;}
        71% {color: indigo;}
        85% {color: violet;}
        100% {color: red;}
    }
    .rainbow-text {
        animation: rainbow 5s infinite;
        font-weight: bold;
    }
    </style>
    <p class="rainbow-text">Good luck chosing your movie!!!</p>
    """, unsafe_allow_html=True)

# Check data set version
if IMDb_df_version.month == datetime.now().month:
    IMDb_df_version = IMDb_df_version.strftime('%B %d, %Y')
    st.markdown(f'''<span style="font-size: 13px;">*IMDb data version: 
                **{IMDb_df_version}***</span>''', 
                unsafe_allow_html=True)
else:
    IMDb_df_version = IMDb_df_version.strftime('%B %d, %Y')
    st.markdown(f'''<span style="font-size: 13px;">:red[***Notice!** Still using IMDb 
                data version **{IMDb_df_version}**!*]</span>''', 
                unsafe_allow_html=True)

# ===============================
# region 1.1 Search Filters
# ===============================

st.subheader('Search Filters', divider='violet')

# ===============================
# region Genre selection
# ===============================

st.write('**Genre:**')

# ===============================
# region AND/OR jack in the box
# ===============================

def AND_OR():
    if st.toggle('AND/OR operator'):
        operator = 1
        st.write('''**OR** operator is selected to pass your genres. Notice that this 
                 could give :red[**less precise**], but :red[**more movie options**]!''')
    else:
        operator = 0
        st.write('''**AND** operator is selected to pass your genres. Notice that this 
                 could give :red[**more precise**], but :red[**fewer movie options**]!''')
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
    genre_options = []
    other_genres = []
    genre_selection = []
    operator = 0
    genre_tag = 0

    if main_genre == "No preference for any genre...":
        pass
    else:
        genre_options = [
            genre for genre in genres if genre not in ["No preference for any genre...", "No preference for a main genre..."]
        ]
        if main_genre != "No preference for a main genre...":
            genre_options = [genre for genre in genre_options if genre != main_genre]
            max_genres = 2
            genre_tag = 2
        else:
            max_genres = 3
            genre_tag = 1

        other_genres = st.multiselect(
            f"Select a maximum of **{max_genres}** genre(s):",
            options=genre_options
        )
        genre_selection = other_genres.copy()
        operator = AND_OR()

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

# Function to calculate the required values and cache the result
@st.cache_data
def calculate_values(df):
    # year
    min_year = int(df['startYear'].min())
    max_year = datetime.now().year
    default_min_year = 1970
    default_max_year = max_year

    # time 
    min_time = 30
    max_time = 240
    default_min_time = 60
    default_max_time = 120

    # ratings
    min_rating = float(1)
    max_rating = float(10)
    default_min_rating = float(6)
    default_max_rating = max_rating
    ratings_step_size = 0.5

    # votes
    min_votes = 0
    max_votes = 500000
    default_min_votes = 100000
    votes_step_size = 1000

    return (min_year, max_year, default_min_year, default_max_year,
            min_time, max_time, default_min_time, default_max_time,
            min_rating, max_rating, default_min_rating, default_max_rating,
            ratings_step_size, min_votes, max_votes, default_min_votes, votes_step_size)

# Call the function and cache the result
(min_year, max_year, default_min_year, default_max_year,
 min_time, max_time, default_min_time, default_max_time,
 min_rating, max_rating, default_min_rating, default_max_rating,
 ratings_step_size, min_votes, max_votes, default_min_votes, votes_step_size) = calculate_values(IMDb_df)

# endregion

# ===============================
# region Simple filters
# ===============================    

# year slider
st.write('**Year:**')
selected_years = st.slider("Range of years in which a film went into premiere:", 
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
               min_value=min_rating,
               max_value=max_rating,
               value=(default_min_rating, default_max_rating),
               step=ratings_step_size,
               format="%.1f")
st.divider()

# votes slider
st.write('**Votes:**')
selected_votes = st.slider("Minimum number of votes for the IMDb film rating:", 
               min_votes, max_votes, 
               default_min_votes,
               step=votes_step_size)

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

        # Check for genre selection errors
        if (genre_tag == 1 and len(genre_selection) > 3) or (genre_tag == 2 and len(genre_selection) > 2):
            st.error("More than 3 genres are selected!")
        else:
            if genre_tag == 1:
                s = "\n".join([f"- {genre}" for genre in genre_selection])
                st.markdown(s if s else 'No genres selected...')
            elif genre_tag == 2:
                st.write(f'Main genre: **{main_genre}**')
                filtered_genre_selection = [genre for genre in genre_selection if genre != main_genre]
                s = "\n".join([f"- {genre}" for genre in filtered_genre_selection])
                st.write('Additional genre(s):')
                st.markdown(s if s else 'No additional genres selected...')
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
        filters &= (IMDb_df['main_genre'] == main_genre)

    # Apply genre-based filtering if necessary including AND/OR operator
    if genre_tag != 0:
        if operator == 0:  # AND condition
            genre_filter = IMDb_df[genre_selection].all(axis=1)
        elif operator == 1:  # OR condition
            genre_filter = IMDb_df[genre_selection].any(axis=1)
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
    # Create the DataFrame with selected features and reset the index
    display_df = filtered_df[['tconst', 'primaryTitle', 'startYear', 'runtimeMinutes', 
                              'main_genre', 'other_genres', 'averageRating', 
                              'numVotes']].copy()
    display_df.columns = ['ID', 'Film', 'Year', 'Duration', 'Main genre', 
                          'Additional genres', 'IMDb Rating', 'Number of votes']
    
    # Reset the index and add 1 to start from 1
    display_df.reset_index(drop=True, inplace=True)
    display_df.index = display_df.index + 1
    display_df.index.name = 'Index'

    return display_df

# Run display_filtered_df()
display_df = display_filtered_df(filtered_df)

# Show display_df or error message to user
if (genre_tag == 1 and len(genre_selection) > 3) or (genre_tag == 2 and len(genre_selection) > 2):
    st.error('More than 3 genres are selected!')
elif display_df.empty:
    st.error('No movies found within the boundaries of the chosen filters!')
else:
    st.write(f'Found **{len(display_df)}** films within your chosen filters:')
    st.dataframe(display_df.iloc[:, 1:])

# endregion

# ===============================
# region No genre warning
# ===============================

if main_genre in ['No preference for any genre...', 
                  'No preference for a main genre...']:
    if not genre_selection:
        warning = ':red[**Warning!** No filter applied on genre!]'
        st.write(warning)

# endregion

# endregion

# ===============================
# region 1.4 Visit IMDb Page
# ===============================

st.subheader('Visit IMDb Page', divider='violet')

st.write('''Select a Top Tier List of films and visit their IMDb pages! Start by choosing 
         the list size (**Top Tier List**). Then, select a movie feature (**Select a movie 
         feature**). By default, movies with the best IMDb ratings are at the top. You 
         can reverse the order by ticking the **Descending or ascending** checkbox. Select 
         a film from the Top Tier List (**Select film**) and click **Visit IMDb film 
         page!** to go to the IMDb page for more information and trailers.''')

# ===============================
# region If-statement show Visit IMDb Page
# ===============================

if (genre_tag == 1 and len(genre_selection) > 3) or (genre_tag == 2 and len(genre_selection) > 2):
    # Error message too many genres
    st.error('More than 3 genres are selected!')
elif display_df.empty:
    # Error message empty df
    st.error('No movies found within the boundaries of the chosen filters!')
else:
    # ===============================
    # region Top selection
    # ===============================

    top_n_choice = st.selectbox('Top Tier List:', ['Top 10', 
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
        
        top_n_list = top_n_list.reset_index(drop=True)
        top_n_list.index = top_n_list.index + 1
        top_n_list.index.name = 'Top'

        return top_n_list

    # endregion

    # ===============================
    # region Left & right layout column
    # ===============================

    left_column, right_column = st.columns(2)

    # ===============================
    # region Left layout column
    # ===============================

    # st.write(display_df)

    with left_column:

        # Select on column display_df is sorted
        sort_column = st.selectbox("Select a movie feature:", display_df.columns[[6, 2, 3, 7]])
        
        # Descending or ascending
        if st.toggle('Descending or ascending'):
            ascent = True
            st.write(f'Currently, **{sort_column}** is ordered in **ascending** order.')
        else:
            ascent = False
            st.write(f'Currently, **{sort_column}** is ordered in **descending** order.')
        
        # Run sorting fuction with user inputs
        top_list = sort_top(display_df, sort_column, ascent, top_n)

    # endregion

    # ===============================
    # region Right layout column
    # ===============================

    with right_column:

        # Select a movie
        IMDb_link = st.selectbox("Select film:", top_list['Film'].unique())
        
        # Get film ID
        ID = top_list[top_list['Film'] == IMDb_link].iloc[0, 0]

        # Define IMDb URL
        url = f'https://www.imdb.com/title/{ID}/'

        # Link button with spinner
        spin_col1, spin_col2 = st.columns([2, 2])

        # Link button in first column
        with spin_col1:
            st.link_button("Visit IMDb page!", url)

        # Spinner in second column
        with spin_col2:
            with st.spinner('Loading link...'):
                
                # Load 1 second                
                time.sleep(1)

            # CSS to align spinner
            st.markdown(
            """
            <style>
            .stButton button {
                margin-right: 10px;
            }
            .stSpinner {
                display: inline-block;
                vertical-align: middle;
                margin-top: 7px;                
            }
            </style>
            """,
            unsafe_allow_html=True
            )
        
    # endregion

    # endregion

    # endregion

    st.divider()

    # ===============================
    # region Display top
    # ===============================

    if ascent == True:
        ascent_descent = 'ascending'
    else:
        ascent_descent = 'descending'    

    st.write(f'Top **{top_n} / {len(display_df)}** based on **{ascent_descent} {sort_column}**:')

    st.dataframe(top_list.iloc[:, 1:])

    # endregion

# endregion

# endregion

# ===============================
# region Movie Stats
# ===============================
st.header("Movie Stats", divider="rainbow")

# ===============================
# region Matplotlib settings
# ===============================

if theme_col == 'light':
    facecolor = 'white'
    axcolor = 'white'
    textcolor = 'black'
    bordercolor = 'black'
elif theme_col == 'dark':
    facecolor = '#0e1117'
    axcolor = '#333333'
    textcolor = 'white'
    bordercolor = 'white'

# Apply the facecolor to all future plots
plt.rcParams['figure.facecolor'] = facecolor
plt.rcParams['axes.facecolor'] = axcolor
plt.rcParams['text.color'] = textcolor
plt.rcParams['axes.labelcolor'] = textcolor
plt.rcParams['xtick.color'] = textcolor
plt.rcParams['ytick.color'] = textcolor
plt.rcParams['axes.edgecolor'] = bordercolor

# endregion

# ===============================
# region General
# ===============================

@st.cache_data
def watched(archieve_df):
    # Filter the DataFrame to include only rows where 'watched' is equal to 1
    watched_df = archieve_df[archieve_df['watched'] == 1]
    return watched_df

watched_df = watched(archieve_df)    

n_unique_genres = watched_df['main_genre'].nunique()     

n_nights = int(archieve_df['watched'].sum())
n_suggest = archieve_df['primaryTitle'].dropna().count()
n_suggest_unique = archieve_df['primaryTitle'].nunique()
n_votes = int(archieve_df['votes'].dropna().sum())
n_canceled = int(archieve_df.groupby('date')['canceled'].max().sum())

st.write(f"""
🎥✨ **Welcome to the Ultimate Movie Night Recap!** ✨🎥  

Ladies and gentlemen, movie enthusiasts, and armchair critics, it’s time to dive into the drama, competition, and cinematic revelations of our movie night showdown. This page is your guide to everything that went down—from the nail-biting voting battles to the genre trends shaping our evenings. Let’s break it down:  

---

🏆 **[Winners](#winners)**: Who’s got the golden touch?  
The rooms battled valiantly, vying for the ultimate prize: having their movie pick reign supreme. Some rooms emerged victorious with bold selections, while others struggled to get their voices heard. Whether you’re celebrating triumph or planning your next comeback strategy, this section reveals who’s on top!  

🗳️ **[Votes](#number-of-votes)**: The popularity contest you didn’t know you were part of.  
How many votes did each room rack up? Who’s the crowd favorite, and who might need to brush up on their campaign tactics? We explore the total and cumulative votes, offering a look at how the showdown unfolded over time.  

⭐ **[IMDb Ratings](#imdb-ratings)**: Quality over quantity?  
Here, we explore the ratings of the films we’ve watched and the suggestions that didn’t make the cut. Are your picks cinematic masterpieces or guilty pleasures? Plus, we throw in a fun ratio for each room—are you contributing above-average quality films or coasting on questionable taste?  

⏱️ **[Film Duration](#film-duration)**: Short and snappy or long and epic?  
Do the chosen movies reflect an affinity for breezy watch-times or a love for sprawling sagas? This section unpacks the runtimes of both selected films and those that were merely suggestions.  

🎭 **[Genres](#genres)**: A colorful glimpse into our preferences.  
Finally, we analyze the genres that made it to movie night. From high-octane action to introspective drama, we’ve dabbled in it all—but which genres dominate, and which are waiting for their turn?  

---

In total, we've had **{n_nights} movie nights**! We suggested **{n_suggest} films** of 
which **{n_suggest_unique} films** where unique suggestions. Unfortunately, we had to 
cancel **{n_canceled} movie nights**...
""")


st.write(f'''''')

# endregion

# ===============================
# region Winners
# ===============================

n_winner = watched_df.groupby('room')['watched'].sum()

# Sort the result from max to min
sorted_n_winner = n_winner.sort_values(ascending=False)

# Get the names of the rooms from max to min
rooms_sorted = sorted_n_winner.index.tolist()

# Assign them to their own objects
room_1 = rooms_sorted[0]
room_2 = rooms_sorted[1]
room_3 = rooms_sorted[2]
room_4 = rooms_sorted[3]
room_5 = rooms_sorted[4]
room_6 = rooms_sorted[5]

st.subheader('Winners', divider='violet')

st.write(f"""
         🎥✨ **Ladies and gentlemen, welcome to the Great Movie Night Suggestion 
         Showdown!** ✨🎥

         In this heated competition, the rooms battled it out to see who could win the 
         most movie choices for film night. Let’s break it down:

         - 🏆 **{room_1}** took the crown with a whopping **{int(sorted_n_winner[0])} wins**! Clearly, this room 
         has the golden taste in movies, or maybe they’ve mastered the art of sneaky 
         lobbying. Either way, they're the reigning champs—*bow down to their cinematic
         wisdom!*

         - 🍿 **{room_2}** came in hot with **{int(sorted_n_winner[1])} wins**, just 
         {int(sorted_n_winner[0]-sorted_n_winner[1])} shy of Room 2. Close, but 
         no popcorn. Maybe next time they’ll add a little extra butter to their choices 
         to push them to the top.

         - 🎭 **{room_3}** was solidly middle-of-the-pack with **{int(sorted_n_winner[2])} wins**. Not too shabby, 
         but it seems they might need to up their game to catch the big players. 
         *More rom-coms? Maybe fewer “artsy” films?*

         - 🎬 **{room_4}** clocked in with **{int(sorted_n_winner[3])} wins**, which is… respectable. But hey, 
         {room_4}, maybe try something bold next time—*like picking a movie that wasn’t 
         released 20 years ago.*

         - 💯 **{room_5}**, with just **{int(sorted_n_winner[4])} wins**. Ouch. Did your movie picks even make it 
         out of the suggestion phase? Did you try recommending **:red["Spy"]** every week? Don’t worry—*underdogs make for the best comeback stories!*

         - ❓ As for the mysterious **“Alternative”** category with its lonely 
         **{int(sorted_n_winner[5])} win**—it’s basically the referee stepping in with a “let’s just watch 
         something else entirely!” Or was it a team effort?

         So there you have it—**{room_1}** is the ultimate movie-picking mastermind!
        """)    

# Function to sum the votes per room and plot the bar chart
@st.cache_data
def plot_n_winner(df, n_winner, theme):

    force_recache = theme

    # Plot a bar chart with rainbow bars, black borders, and medium grey background within the axis
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    bars = ax.bar(n_winner.index, n_winner.values, color=plt.cm.rainbow(np.linspace(0, 1, len(n_winner))), edgecolor='black')  # Set the bar colors to rainbow with black borders
    ax.set_ylabel('Times won', fontsize=14)
    ax.set_xticklabels(n_winner.index, rotation=0, fontsize=14)

    # Set y-axis to show no decimals
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.yticks(fontsize=14)

    # Remove x-axis label
    ax.set_xlabel('')

    # Add the count on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=14)

    # Set the y-axis limit to be 5 higher than the highest bar
    ax.set_ylim(0, n_winner.max() + 5)

    return fig

# Call the function and cache the result
fig_1 = plot_n_winner(archieve_df, n_winner, theme)

# Display the plot in Streamlit
st.pyplot(fig_1)        

st.divider()

@st.cache_data
def plot_winners_over_time(df, theme):

    force_recache = theme

    # Plotting
    fig, ax = plt.subplots()

    # Get the unique groups
    groups = df['room'].unique()

    # Generate rainbow colors for the groups
    colors = plt.cm.rainbow(np.linspace(0, 1, len(groups)))

    # Scatter plot with connecting lines per group using rainbow colors
    for color, (key, grp) in zip(colors, df.groupby(['room'])):
        ax.plot(grp['date'], grp['cumulative_win'], marker='o', linestyle='-',
                markersize=4, label=key, color=color)

    # Set labels and title
    ax.set_ylabel('Cumulative wins')

    # Set y-axis to show no decimals
    ax.yaxis.get_major_locator().set_params(integer=True)
    
    # Rotate x-axis labels to format dates
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %d, %Y'))

    # Show one tick on the first of the month
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[2, 5, 8, 11]))
    ax.xaxis.set_minor_locator(plt.matplotlib.dates.DayLocator(bymonthday=1))

    # Align the dates on x-axis to make the year line up with the tick
    fig.autofmt_xdate()

    # Show legend
    plt.legend(title='Room', fontsize=9)

    return fig

# Call the function and cache the result
fig_2 = plot_winners_over_time(archieve_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_2)

# endregion

# ===============================
# region Votes
# ===============================

votes_per_room = archieve_df.groupby('room')['votes'].sum()

# Sort the result from max to min
sorted_votes_per_room = votes_per_room.sort_values(ascending=False)

# Get the names of the rooms from max to min
rooms_sorted_votes_per_room = sorted_votes_per_room.index.tolist()

# Assign them to their own objects
room_1_vote = rooms_sorted_votes_per_room[0]
room_2_vote = rooms_sorted_votes_per_room[1]
room_3_vote = rooms_sorted_votes_per_room[2]
room_4_vote = rooms_sorted_votes_per_room[3]
room_5_vote = rooms_sorted_votes_per_room[4]
room_6_vote = rooms_sorted_votes_per_room[5]

st.subheader('Number of votes', divider='violet')

st.write(f"""
🗳️✨ **Let’s talk about votes, babygirl!** ✨🗳️

A total of **{n_votes} votes** where given! In the first figure, we see **{room_1_vote}** 
flexing its popularity muscles with 
**{int(sorted_votes_per_room[0])} total votes**—an undeniable fan favorite! 
**{room_2_vote}** and **{room_3_vote}** also put up a decent fight with 
**{int(sorted_votes_per_room[1])}** and **{int(sorted_votes_per_room[2])} votes**, 
respectively. Meanwhile, **{room_4_vote}** brought a modest 
**{int(sorted_votes_per_room[3])} votes** to the table. (*Do we need to send out 
a motivational speech, {room_5_vote}?*)
""")

# Function to sum the votes per room and plot the bar chart
@st.cache_data
def plot_votes_per_room(df, theme):

    force_recache = theme

    # Sum the votes per room
    votes_per_room = df.groupby('room')['votes'].sum()

    # Plot a bar chart with rainbow bars, black borders, and medium grey background within the axis
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    bars = ax.bar(votes_per_room.index, votes_per_room.values, color=plt.cm.rainbow(np.linspace(0, 1, len(votes_per_room))), edgecolor='black')  # Set the bar colors to rainbow with black borders
    ax.set_ylabel('Total votes', fontsize=14)
    ax.set_xticklabels(votes_per_room.index, rotation=0, fontsize=14)

    # Set y-axis to show no decimals
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.yticks(fontsize=14)

    # Remove x-axis label
    ax.set_xlabel('')

    # Add the count on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=14)

    # Set the y-axis limit to be 5 higher than the highest bar
    ax.set_ylim(0, votes_per_room.max() + 5)

    return fig

# Call the function and cache the result
fig_3 = plot_votes_per_room(archieve_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_3)

st.divider()

st.write(f'''The second figure takes us on a journey through time as the cumulative votes 
         pile up. **{room_1_vote}’s** rise to the top was steady and strong—like a 
         blockbuster climbing the box office charts. **{room_2_vote}** made a valiant 
         effort to keep up, but ultimately fell behind. And **{room_5_vote}**… well, 
         let’s just say their graph looks more like a gentle slope than a steep climb. 
         *Baby steps, right?*
        ''')

@st.cache_data
def plot_votes_over_time(df, theme):

    force_recache = theme

    # Plotting
    fig, ax = plt.subplots()

    # Get the unique groups
    groups = df['room'].unique()

    # Generate rainbow colors for the groups
    colors = plt.cm.rainbow(np.linspace(0, 1, len(groups)))

    # Scatter plot with connecting lines per group using rainbow colors
    for color, (key, grp) in zip(colors, df.groupby(['room'])):
        ax.plot(grp['date'], grp['cumulative_votes'], marker='o', linestyle='-',
                markersize=4, label=key, color=color)

    # Set labels and title
    ax.set_ylabel('Cumulative votes')

    # Set y-axis to show no decimals
    ax.yaxis.get_major_locator().set_params(integer=True)
    
    # Rotate x-axis labels to format dates
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %d, %Y'))

    # Show one tick on the first of the month
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[2, 5, 8, 11]))
    ax.xaxis.set_minor_locator(plt.matplotlib.dates.DayLocator(bymonthday=1))

    # Align the dates on x-axis to make the year line up with the tick
    fig.autofmt_xdate()

    # Show legend
    plt.legend(title='Room', fontsize=9)

    return fig

# Call the function and cache the result
fig_4 = plot_votes_over_time(archieve_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_4)

st.write(f'''**Moral of the story:** {room_1_vote}’s the crowd-pleaser, and 
         {room_5_vote}’s got some catching up to do! 🚀
        ''')

# endregion

# ===============================
# region IMDb ratings
# ===============================

st.subheader('IMDb ratings', divider='violet')

st.write(f'''
         **IMDb Ratings Overview** 🎥✨ 
         
         The first plot shows the IMDb ratings of the films that were ultimately chosen 
         for movie night. Each room's choices are represented, along with how their 
         selections stack up in terms of quality (according to IMDb, of course!). The 
         spread, average, and range of ratings provide a glimpse into the kind of films 
         each room tends to champion—whether they're blockbusters, cult classics, or 
         hidden gems.

         On average, the films that we watched together had an **IMDb rating of 
         {watched_df['averageRating'].mean().round(2)} 
         (sd={watched_df['averageRating'].std().round(2)})**. The IMDb rating average of all
         suggested films was **{archieve_df['averageRating'].mean().round(2)}
         (sd={archieve_df['averageRating'].std().round(2)})**.
        ''')

@st.cache_data
def plot_IMDb_rating_suggested_room(df, theme):

    force_recache = theme

    # Group by room and get average ratings
    grouped_data = [df[df['room'] == room]['averageRating'].dropna().values for room in sorted(df['room'].unique())]

    # Plot a boxplot with the specified style
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    box = ax.boxplot(grouped_data, patch_artist=True)

    # Set the box colors to rainbow with black borders
    colors = plt.cm.rainbow(np.linspace(0, 1, len(grouped_data)))
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')

    # Set the whisker and cap colors to black
    for whisker in box['whiskers']:
        whisker.set_color('black')
    for cap in box['caps']:
        cap.set_color('black')

    # Set the median line color to black
    for median in box['medians']:
        median.set_color('black')

    # Add mean as a small x
    means = [np.mean(group) for group in grouped_data]
    ax.scatter(range(1, len(means) + 1), means, color='black', marker='x', s=100, zorder=3)

    # Add sample size per group on y=9.75
    sample_sizes = [len(group) for group in grouped_data]
    for i, size in enumerate(sample_sizes):
        ax.text(i + 1, 9.75, f'n={size}', ha='center', va='center', fontsize=12)

    ax.set_ylabel('IMDb rating', fontsize=14)
    ax.set_xticklabels(sorted(df['room'].unique()), rotation=0, fontsize=14)

    ax.set_ylim((df['averageRating'].min()-(10-df['averageRating'].max())), 10)

    # Remove x-axis label
    ax.set_xlabel('')

    return fig, grouped_data

# Call the function and cache the result
fig_5, grouped_data = plot_IMDb_rating_suggested_room(watched_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_5)

# Define the names
names = ["Alternative", "Room 1", "Room 2", "Room 3", "Room 4", "Room 5"]

# Create a dictionary with names as keys and arrays as values
named_arrays = {name: arr for name, arr in zip(names, grouped_data)}

# Calculate the mean/size ratio for each group
ratios = {name: np.mean(arr) / watched_df['averageRating'].mean() for name, arr in named_arrays.items()}

# Assign the ratios to individual variables
Alternative = ratios["Alternative"]
ratio_1 = ratios["Room 1"].round(3)
ratio_2 = ratios["Room 2"].round(3)
ratio_3 = ratios["Room 3"].round(3)
ratio_4 = ratios["Room 4"].round(3)
ratio_5 = ratios["Room 5"].round(3)

st.write(f'''
         Let's check the **average room IMDb rating/average watched film IMDb rating 
         ratio**! If you're ratio is high, this means that you generally have high 
         quality contributions. If you're ratio is low, you've got to train you're taste!
         Rooms below 1.0 contrubute below average quality films, while rooms above 1.0 
         contrubute above average quality films. Maybe consider voting on someone else 
         next time?

         - Room 1: **{ratio_1}**
         - Room 2: **{ratio_2}**
         - Room 3: **{ratio_3}**
         - Room 4: **{ratio_4}**
         - Room 5: **{ratio_5}**

         <p><span style='font-size:13px;'>Notice! Beware of selection bias! Rooms with a 
         low number of wins might have an unusually high or low ratio due to limited 
         data.</span>
         
         The second plot shifts focus to the suggested films—many of which didn’t quite 
         make the cut. It’s a behind-the-scenes look at what each room brought to the 
         table. From here, we can see the range of ideas: some rooms stick to high-rated, 
         critically acclaimed movies, while others might be a bit more adventurous 
         (or chaotic) in their picks.
        ''', unsafe_allow_html=True)

@st.cache_data
def plot_IMDb_rating_room(df, theme):

    force_recache = theme

    # Group by room and get average ratings
    grouped_data = [df[df['room'] == room]['averageRating'].dropna().values for room in sorted(df['room'].unique())]

    # Plot a boxplot with the specified style
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    box = ax.boxplot(grouped_data, patch_artist=True)

    # Set the box colors to rainbow with black borders
    colors = plt.cm.rainbow(np.linspace(0, 1, len(grouped_data)))
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')

    # Set the whisker and cap colors to black
    for whisker in box['whiskers']:
        whisker.set_color('black')
    for cap in box['caps']:
        cap.set_color('black')

    # Set the median line color to black
    for median in box['medians']:
        median.set_color('black')

    # Add mean as a small x
    means = [np.mean(group) for group in grouped_data]
    ax.scatter(range(1, len(means) + 1), means, color='black', marker='x', s=100, zorder=3)

    # Add sample size per group on y=9.75
    sample_sizes = [len(group) for group in grouped_data]
    for i, size in enumerate(sample_sizes):
        ax.text(i + 1, 9.75, f'n={size}', ha='center', va='center', fontsize=12)

    ax.set_ylabel('IMDb rating', fontsize=14)
    ax.set_xticklabels(sorted(df['room'].unique()), rotation=0, fontsize=14)

    ax.set_ylim((df['averageRating'].min()-(10-df['averageRating'].max())), 10)

    # Remove x-axis label
    ax.set_xlabel('')

    return fig, grouped_data

# Call the function and cache the result
fig_6, grouped_data = plot_IMDb_rating_room(archieve_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_6)

st.write(f'''Together, these plots show how the chosen films compare to the broader 
         pool of suggestions. It’s an ongoing story—dynamic and ever-changing as more 
         movie nights unfold! Whether the IMDb ratings go up, down, or stay steady, 
         every movie pick adds a new twist to the tale.
        ''')

# endregion 

# ===============================
# region Film duration
# ===============================

st.subheader('Film duration', divider='violet')

st.write(f'''
         **Movie Duration Analysis** ⏱️✨

         The first plot highlights the runtime (in minutes) of the movies that made it 
         to movie night. Each room’s chosen films are represented, showing whether they 
         prefer snappy, fast-paced stories or long, immersive epics. The average 
         runtimes and spreads hint at each room's movie-night vibe. The average film we
         watched had a duration of **{archieve_df['runtimeMinutes'].mean().round(2)} 
         minutes**.
         ''')

@st.cache_data
def plot_IMDb_duration_room(df, theme):

    force_recache = theme

    # Group by room and get average ratings
    grouped_data = [df[df['room'] == room]['runtimeMinutes'].dropna().values for room in sorted(df['room'].unique())]

    # Plot a boxplot with the specified style
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    box = ax.boxplot(grouped_data, patch_artist=True)

    # Set the box colors to rainbow with black borders
    colors = plt.cm.rainbow(np.linspace(0, 1, len(grouped_data)))
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')

    # Set the whisker and cap colors to black
    for whisker in box['whiskers']:
        whisker.set_color('black')
    for cap in box['caps']:
        cap.set_color('black')

    # Set the median line color to black
    for median in box['medians']:
        median.set_color('black')

    # Add mean as a small x
    means = [np.mean(group) for group in grouped_data]
    ax.scatter(range(1, len(means) + 1), means, color='black', marker='x', s=100, zorder=3)

    # Add sample size per group on y=182
    sample_sizes = [len(group) for group in grouped_data]
    for i, size in enumerate(sample_sizes):
        ax.text(i + 1, (df['runtimeMinutes'].max()+4), f'n={size}', ha='center', va='center', fontsize=12)

    ax.set_ylabel('Duration (minutes)', fontsize=14)
    ax.set_xticklabels(sorted(df['room'].unique()), rotation=0, fontsize=14)

    ax.set_ylim((df['runtimeMinutes'].min()-10), (df['runtimeMinutes'].max()+10))

    # Remove x-axis label
    ax.set_xlabel('')

    return fig, grouped_data

# Call the function and cache the result
fig_7, grouped_data = plot_IMDb_duration_room(watched_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_7)

st.write(f'''The second plot digs into the runtimes of all the suggested films—whether 
         they were chosen or not. Here, we get a broader sense of what each room 
         brought forward. Some rooms might aim for epic sagas with towering runtimes, 
         while others pitch films that fit neatly into a busy evening schedule.
        ''')

@st.cache_data
def plot_IMDb_duration_suggested_room(df, theme):

    force_recache = theme

    # Group by room and get average ratings
    grouped_data = [df[df['room'] == room]['runtimeMinutes'].dropna().values for room in sorted(df['room'].unique())]

    # Plot a boxplot with the specified style
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    box = ax.boxplot(grouped_data, patch_artist=True)

    # Set the box colors to rainbow with black borders
    colors = plt.cm.rainbow(np.linspace(0, 1, len(grouped_data)))
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')

    # Set the whisker and cap colors to black
    for whisker in box['whiskers']:
        whisker.set_color('black')
    for cap in box['caps']:
        cap.set_color('black')

    # Set the median line color to black
    for median in box['medians']:
        median.set_color('black')

    # Add mean as a small x
    means = [np.mean(group) for group in grouped_data]
    ax.scatter(range(1, len(means) + 1), means, color='black', marker='x', s=100, zorder=3)

    # Add sample size per group on y=9.75
    sample_sizes = [len(group) for group in grouped_data]
    for i, size in enumerate(sample_sizes):
        ax.text(i + 1, (df['runtimeMinutes'].max()+4), f'n={size}', ha='center', va='center', fontsize=12)

    ax.set_ylabel('Duration (minutes)', fontsize=14)
    ax.set_xticklabels(sorted(df['room'].unique()), rotation=0, fontsize=14)

    ax.set_ylim((df['runtimeMinutes'].min()-10), (df['runtimeMinutes'].max()+10))

    # Remove x-axis label
    ax.set_xlabel('')

    return fig, grouped_data

# Call the function and cache the result
fig_8, grouped_data = plot_IMDb_duration_suggested_room(archieve_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_8)

st.write(f'''Together, these visuals reveal a lot about each room’s cinematic style. 
         Whether your picks skew longer or shorter, every suggestion adds to the 
         tapestry of movie night fun—and who knows what the next selection will bring?
         ''')

# endregion 

# ===============================
# region Genres
# ===============================

st.subheader('Genres', divider='violet')

st.write(f'''
         **Genres Galore** 🎥🎭

         Take a look at this colorful breakdown of the genres we’ve tackled on movie nights. 
         We’ve dipped our toes into all kinds of cinematic waters, from high-energy thrillers 
         to heartfelt tearjerkers—and everything in between.

         It’s clear we’ve got a soft spot for certain genres, while others have been left 
         standing awkwardly in the corner, waiting for their moment to shine. Maybe they’re 
         just “acquired tastes”?

         Whatever the case, our genre selection shows we’re a diverse bunch—sometimes 
         action-packed, sometimes introspective, and occasionally downright silly. The real 
         question is: what’s next? Are we diving into high drama, or will we surprise everyone 
         with something completely offbeat? Stay tuned!
         ''') 

@st.cache_data
def plot_n_genres(df, theme):

    force_recache = theme

    # Sum the votes per room
    n_genre = df['main_genre'].value_counts().sort_values(ascending=True)

    # Plot a horizontal bar chart with rainbow bars, black borders, and medium grey background within the axis
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    bars = ax.barh(n_genre.index, n_genre.values, color=plt.cm.rainbow(np.linspace(0, 1, len(n_genre))), edgecolor='black')  # Set the bar colors to rainbow with black borders
    ax.set_xlabel('Times watched', fontsize=16)
    ax.set_yticklabels(n_genre.index, rotation=0, fontsize=14)

    # Set x-axis to show no decimals
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.xticks(fontsize=14)

    # Remove y-axis label
    ax.set_ylabel('')

    # Add the count on top of the bars
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 1, bar.get_y() + bar.get_height()/2, int(xval), ha='left', va='center', fontsize=14)

    # Set the x-axis limit to be 5 higher than the highest bar
    ax.set_xlim(0, n_genre.max() + 5)

    return fig

# Call the function and cache the result
fig_7 = plot_n_genres(watched_df, theme)

# Display the plot in Streamlit
st.pyplot(fig_7)

# endregion

st.divider()

st.write(f'''✨ **In Conclusion**:  
        Every movie night is a blend of strategy, taste, and a sprinkle of luck. 
         Whether you’re basking in victory or plotting your next move, the stats and 
         visuals here give you all the tools to stay in the game. So, are you ready for 
         the next showdown? Let the movie magic continue! 🍿
        ''')

# endregion

# ===============================
# region Film Archive
# ===============================
st.header("Film Archive", divider="rainbow")

st.write('''The Film Archive is a comprehensive hub where you can revisit all the films 
         we’ve enjoyed together. It lets you see which room suggested each film, track 
         how many votes each room received, and even check out the movie snack of the 
         night. You can explore the archive by individual movie nights or view the entire 
         collection in one go. Each film entry is enriched with additional IMDb 
         information, providing a quick overview of key details. For added convenience, 
         there’s a dedicated IMDb film page button, so you can instantly visit the 
         official page for any movie. It’s the perfect way to relive past movie nights 
         and discover new favorites!''')

# Check data set version
if archieve_df_version.month == datetime.now().month:    
    archieve_df_version = archieve_df_version.strftime('%B %d, %Y')
    text = f'*IMDb data version: **{archieve_df_version}***'
    st.markdown(f'''<span style="font-size: 13px;">*Archieve version: 
                **{archieve_df_version}***</span>''', 
                unsafe_allow_html=True)
else:
    archieve_df_version = archieve_df_version.strftime('%B %d, %Y')
    st.markdown(f'''<span style="font-size: 13px;">:red[***Notice!** Still using archieve 
                version **{archieve_df_version}**!*]</span>''', 
                unsafe_allow_html=True)

st.divider()

# ===============================
# region Archieve subset
# ===============================

@st.cache_data
def movie_night_info_sub(archieve_df):

    # Feature selection for new df
    info_subset = {'ID': archieve_df['tconst'],
                   'watched': archieve_df['watched'],
                   'canceled': archieve_df['canceled'],
                   'Date': archieve_df['date'],
                   'Room': archieve_df['room'],
                   'Film': archieve_df['primaryTitle'],
                   'Votes': archieve_df['votes'],
                   'Movie snack': archieve_df['snack'],
                   'Year': archieve_df['startYear'],
                   'Duration': archieve_df['runtimeMinutes'],
                   'Main genre': archieve_df['main_genre'],
                   'Additional genres': archieve_df['other_genres'],
                   'IMDb Rating': archieve_df['averageRating'],
                   'Number of IMDb votes': archieve_df['numVotes']}
    
    # Selected features to Pandas df
    movie_night_info_df = pd.DataFrame(info_subset)

    # Hide ID feature for user and re-index
    return movie_night_info_df, info_subset

movie_night_info, info_subset = movie_night_info_sub(archieve_df)

# !!! VERY WEIRD BUG HERE: If 'filtered_info' is not in return and
# defined, the 'Votes' feature will get the 'Movie snack' string
# but only if the data is '09 Martch 2023'... !!! 

# endregion

# ===============================
# region Unique formatted dates
# ===============================

@st.cache_data
def get_unique_dates(movie_night_info):
    unique_dates = movie_night_info['Date'].dt.strftime('%d %B %Y').unique()
    return unique_dates

dates = get_unique_dates(movie_night_info)

# endregion

# ===============================
# region Random emoji
# ===============================

positive_emojis = [
    ':smile:', ':grinning:', ':grin:', ':laughing:', ':blush:', ':innocent:',
    ':slightly_smiling_face:', ':hugs:', ':partying_face:', ':heart_eyes:',
    ':star-struck:', ':kissing_heart:', ':yum:', ':sunglasses:',
    ':smiling_face_with_3_hearts:', ':smile_cat:', ':smiley_cat:',
    ':joy_cat:', ':heart_eyes_cat:'
]

# Select a positive random emoji
positive_random_emoji = random.choice(positive_emojis)

negative_emojis = [
    ':white_frowning_face:', ':worried:', ':cry:', ':sob:', ':angry:', ':rage:',
    ':disappointed:', ':pensive:', ':confused:', ':persevere:',
    ':disappointed_relieved:', ':weary:', ':tired_face:', ':fearful:',
    ':cold_sweat:', ':scream:', ':astonished:', ':flushed:', ':dizzy_face:',
    ':face_with_symbols_on_mouth:'
]

# Select a negative random emoji
negative_random_emoji = random.choice(negative_emojis)

# endregion

# ===============================
# region Complete archieve cache
# ===============================

# ===============================
# region Format date
# ===============================

# Function to convert the 'Date' column to datetime
@st.cache_data
def convert_to_datetime(df):
    df['Date'] = pd.to_datetime(df['Date'])
    return df

complete_movie_night_info = movie_night_info.copy()

# Apply the function and cache the result
complete_movie_night_info = convert_to_datetime(complete_movie_night_info)

# Function to format the date
@st.cache_data
def format_date(date):
    return date.strftime('%d %b %Y')

# Apply the function to the 'Date' column and replace the original column
complete_movie_night_info['Date'] = complete_movie_night_info['Date'].apply(format_date)

# endregion

# ===============================
# region Format grey color
# ===============================

@st.cache_data
def color_alternate_weeks(df):
    colors = ['background-color: rgba(255, 255, 255, 0.25)', 
              'background-color: rgba(128, 128, 128, 0.2)']
    color_map = []
    current_color = 0
    
    for i in range(len(df)):
        # Determine alternating week color
        if i == 0 or (pd.to_datetime(df['Date'].iloc[i]).isocalendar()[1] != pd.to_datetime(df['Date'].iloc[i - 1]).isocalendar()[1]):
            current_color = 1 - current_color
        row_color = [colors[current_color]] * len(df.columns)

        # Check if 'watched' == 1 and override color for the row
        if df['watched'].iloc[i] == 1:
            row_color = ['background-color: rgba(152, 251, 152, 0.3)'] * len(df.columns)
          
        color_map.append(row_color)
      
    return pd.DataFrame(color_map, index=df.index, columns=df.columns)

styled_df_complete = complete_movie_night_info.style.apply(color_alternate_weeks, axis=None)

# endregion

# endregion

# ===============================
# region Archieve checkbox
# ===============================

if st.toggle('View entire archieve'):
    complete_archieve = 1
else:
    complete_archieve = 0

# endregion

# ===============================
# region Complete or single
# ===============================
if complete_archieve == 0:

    # ===============================
    # region Single
    # ===============================

    # ===============================
    # region Define & apply filters
    # ===============================

    st.write('Choose a movie night date. The elected film is highlited in green.')

    movie_night_date = st.selectbox('Movie night date:', dates)

    @st.cache_data
    def movie_night_date_filter(movie_night_info, movie_night_date):

        movie_night_date_filter = (
            movie_night_info['Date'] == movie_night_date
        )

        return movie_night_info[movie_night_date_filter]

    single_movie_night_info = movie_night_date_filter(movie_night_info, movie_night_date)

    # endregion

    # ===============================
    # region Film data layout
    # ===============================

    # Function to highlight rows where watched is 1
    def highlight_rows(row):
        return ['background-color: rgba(152, 251, 152, 0.3)' if row.watched == 1 
                else '' for _ in row]

    # Apply highlight_rows(row) to dataframe
    styled_df = single_movie_night_info.style.apply(highlight_rows, axis=1)

    # Preserve integer formatting 
    styled_df = styled_df.format({
        'watched': '{:.0f}',
        'canceled': '{:.0f}',
        'Votes': '{:.0f}',
        'Year': '{:.0f}',
        'Duration': '{:.0f}',
        'IMDb Rating': '{:.1f}',
        'Number of IMDb votes': '{:,.0f}'
    })

    info_to_display = (list(single_movie_night_info.columns[4:7]) + 
                       list(single_movie_night_info.columns[8:]))

    # endregion

    # ===============================
    # region Movie snack
    # ===============================

    if single_movie_night_info['Movie snack'].isnull().all():
        st.write(f'''During this movie night, there was **no movie snack** 
                 {negative_random_emoji}''')
    else:
        movie_snack = single_movie_night_info['Movie snack'].dropna().iloc[0]
        if (single_movie_night_info['Date'] == datetime(2024, 5, 30)).any():
            st.write(f'''The movie snack of this movie night was: 
                     **{movie_snack}** :couplekiss:''')
        else:
            st.write(f'''The movie snack of this movie night was: 
                     **{movie_snack}** {positive_random_emoji}''')

    # endregion

    # ===============================
    # region Display selected archieve
    # ===============================

    # Display the styled dataframe in Streamlit
    if sum(single_movie_night_info['canceled']) >= 1:
        st.error("This movie night was canceled...")
        st.dataframe(styled_df, 
                    column_order=info_to_display, 
                    hide_index=True)
    else:
        st.dataframe(styled_df, 
                    column_order=info_to_display, 
                    hide_index=True)
    
    # endregion

    # endregion
else:

    # ===============================
    # region Complete
    # ===============================

    # ===============================
    # region Format values
    # ===============================

    # Preserve integer formatting 
    styled_df_complete = styled_df_complete.format({
        'watched': '{:.0f}',
        'canceled': '{:.0f}',
        'Votes': '{:.0f}',
        'Year': '{:.0f}',
        'Duration': '{:.0f}',
        'IMDb Rating': '{:.1f}',
        'Number of IMDb votes': '{:,.0f}'
    })

    # endregion

    # ===============================
    # region Select display
    # ===============================

    info_to_display = list(styled_df_complete.columns[3:])

    st.write(f'''This is the archieve complete film archieve! It includes a stunning
             **{n_nights} movie nights**! Elected films are highlighted in green.''')

    st.dataframe(styled_df_complete, 
                 column_order=info_to_display, 
                 hide_index=True)

    # endregion

    # endregion

# endregion

# ===============================
# region Left & right layout column
# ===============================

left_column, right_column = st.columns(2)

# ===============================
# region Left column
# ===============================

with left_column:

    # Select a movie
    if complete_archieve == 0:
        archieve_selection = single_movie_night_info['Film'].dropna().unique()
    else:
        archieve_selection = movie_night_info['Film'].dropna().unique()

    selected_archieve_film = st.selectbox("Select film:", archieve_selection)

    # Get film ID from archieve
    if complete_archieve == 0:
        archieve_ID = single_movie_night_info[single_movie_night_info['Film'] == selected_archieve_film].iloc[0, 0]
    else:
        archieve_ID = movie_night_info[movie_night_info['Film'] == selected_archieve_film].iloc[0, 0]

    # Define IMDb URL
    url_from_archieve = f'https://www.imdb.com/title/{archieve_ID}/'

    # Link button with spinner
    archieve_col1, archieve_col2 = st.columns([2, 2])

    # Link button in first column
    with archieve_col1:
        st.link_button("Visit IMDb page!", url_from_archieve)

        # Spinner in second column
    with archieve_col2:
        with st.spinner('Loading link...'):
                
            # Load 1 second                
            time.sleep(1)

        # CSS to align spinner
        st.markdown(
        """
        <style>
        .stButton button {
            margin-right: 10px;
        }
        .stSpinner {
            display: inline-block;
            vertical-align: middle;
            margin-top: 7px;                
        }
        </style>
        """,
        unsafe_allow_html=True
        )
    
# endregion

# endregion    

st.divider()

# endregion

# ===============================
# region Footer
# ===============================

# Custom CSS to adapt the footer to the browser's theme settings
st.markdown("""
    <style>
    @media (prefers-color-scheme: dark) {
        .footer {
            background-color: #333333;
            color: #FFFFFF;
        }
    }
    @media (prefers-color-scheme: light) {
        .footer {
            background-color: #f9f9f9;
            color: #6c757d;
        }
    }
    .footer {
             width: 100%;
             text-align: center;
             align-items: center;
             padding: 5px 10px 5px 10px;
             margin-top: 20px;
             margin-bottom: 0px;
             font-size: 14px;
         }
    </style>
     <div class="footer">
         <p>The Thursday Filmday app was made possible by Midas, the man who hesitated 
            for so long about which movie to watch that he developed a movie app in the 
            meantime - <a href="https://eelslap.com/" target="_blank">ADHD hyperfocus</a> - 
            <a href="https://streamlit.io/" target="_blank">Streamlit</a> - 
            <a href="https://developer.imdb.com/" target="_blank">IMDb Developer</a> and
            a lot of <a href="https://chatgpt.com/" target="_blank">ChatGPT-4</a>
         <p>&#128027; If you find any bugs, please report! &#128027;<p> 
     </div>
    """, unsafe_allow_html=True)

# endregion

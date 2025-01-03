# ===============================
# region Imports
# ===============================
import streamlit as st
import numpy as np
import pandas as pd
import time
from datetime import datetime
import gzip
import toml

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
    #st.write()
    text = f'*IMDb data version: **{IMDb_df_version}***'
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
    if st.checkbox('AND/OR operator'):
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
min_year = int(IMDb_df['startYear'].min())
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
if (genre_tag == 1 and len(genre_selection) > 3) or (genre_tag == 2 and len(genre_selection) > 2):
    # Error message too many genres
    st.error('More than 3 genres are selected!')
elif display_df.empty:
    display_df = st.error('No movies found within the boundaries of the chosen filters!')
else:
    st.write(f'Found **{len(display_df)}** films within your chosen filters:')
    st.write(display_df.iloc[:, 1:].reset_index(drop=True))

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
        sort_column = st.selectbox("Select a movie feature:", display_df.columns[[6, 2, 3, 7]])
        # Descending or ascending
        if st.checkbox('Descending or ascending'):
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
            st.link_button("Visit IMDb film page!", url)

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

    if ascent == True:
        ascent_descent = 'ascending'
    else:
        ascent_descent = 'descending'    

    st.write(f'Top **{top_n} / {len(display_df)}** based on **{ascent_descent} {sort_column}**:')

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
            <a href="https://streamlit.io/" target="_blank">Streamlit</a> and 
            <a href="https://developer.imdb.com/" target="_blank">IMDb Developer</a>
     </div>
    """, unsafe_allow_html=True)

# endregion

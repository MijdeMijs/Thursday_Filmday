# ===============================
# region Imports
# ===============================
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import gzip
import random

# endregion

# ===============================
# region Sidebar
# ===============================

# Sidebar: Random Film Button
st.sidebar.title("Random Film Generator")

st.sidebar.write("Can't decide what to watch? Let our Random Film Generator choose for you! Click the button and get a film title, IMDb rating, and duration. Enjoy your movie night! 🍿🎥")

if st.sidebar.button("Generate random film!"):
    # Check if the data is ready
    if "filtered_data" in st.session_state:
        # Sample one row
        random_row = st.session_state["filtered_data"].sample(1)

        # Extract the required data
        random_film = random_row["Film"].iloc[0]
        random_rating = random_row["IMDb Rating"].iloc[0]
        random_duration = random_row["Duration"].iloc[0]
        random_year = random_row["Year"].iloc[0]
        random_ID = random_row["ID"].iloc[0]

        # List of funny texts
        funny_texts = [
            "Reading your aura...",
            "Taming a monkey...",
            "Brewing some coffee...",
            "Counting stars...",
            "Feeding the unicorns...",
            "Polishing the pixels...",
            "Summoning good vibes...",
            "Tickling the code...",
            "Charging the flux capacitor...",
            "Aligning the planets...",
            "Petting the cat...",
            "Warming up the servers...",
            "Finding Waldo...",
            "Herding cats...",
            "Sharpening pencils...",
            "Calibrating the matrix...",
            "Baking cookies...",
            "Inflating balloons...",
            "Painting rainbows...",
            "Hacking the mainframe...",
            "Teleporting data...",
            "Tickling the electrons...",
            "Spinning up the hamster wheel...",
            "Inflating the internet...",
            "Waking up the servers...",
            "Unleashing the magic...",
            "Mixing the potions...",
            "Charging the crystals...",
            "Consulting the oracle...",
            "Tuning the algorithms...",
            "Rebooting the matrix...",
            "Casting spells...",
            "Brewing the potion...",
            "Hunting for Easter eggs...",
            "Rewiring the circuits...",
            "Synchronizing the clocks...",
            "Lubricating the gears...",
            "Recalibrating the sensors...",
            "Recharging the batteries...",
            "Assembling the pixels..."
        ]

        # Randomly choose a funny text
        progress_text = random.choice(funny_texts)

        # Create a progress bar
        my_bar = st.sidebar.progress(0)
        
        # Randomly choose a duration between 0.5 and 3 seconds
        duration = random.uniform(0.1, 2)

        # Calculate the sleep time per iteration
        sleep_time = duration / 100

        for percent_complete in range(100):
            time.sleep(sleep_time)
            my_bar.progress(percent_complete + 1, text=progress_text)

        time.sleep(1)
        my_bar.empty()
        
        st.sidebar.write(f'''
                         Maybe you'd like to watch **{random_film}**?
                         
                         **Rating: {random_rating.round(1)} | 
                         Duration: {int(random_duration)}** |
                         **Year: {int(random_year)}**
                         ''')
        
        # Define IMDb URL
        random_url = f'https://www.imdb.com/title/{random_ID}/'

        st.sidebar.link_button('Visit IMDb page!', random_url)

    else:
        # Centered warning text using Markdown and CSS
        st.sidebar.markdown(
            """
            <div style="text-align: center; background-color: #FFA726; padding: 10px; border: 1px solid #ffa500; border-radius: 5px; color: black;">
                <strong>⚠️ First select filters! ⚠️</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.sidebar.write('')
        st.sidebar.page_link("pages/1_🎬_Film_Chooser.py", label="Go to Film Chooser", icon="🎬")

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
# region Little friends
# ===============================

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
def Bug_random_positions_2(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
        # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

# Generate random keyframe positions
random_positions_Bug_2 = Bug_random_positions_2()

# endregion

# ===============================
# region Bug keyframes
# ===============================

def keyframes_CSS_Bug(random_positions_Bug):
    keyframes = "@keyframes move_Bug {"
    step = 0
    for top, left in random_positions_Bug:
        keyframes += f"{step}% {{ top: {top}%; left: {left}%; }}"
        step += int(100 / (len(random_positions_Bug) - 1))  # Evenly distribute steps
    keyframes += "}"
    return keyframes

keyframes_Bug = keyframes_CSS_Bug(random_positions_Bug_2)

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

# Display the bug if the button is clicked
if st.session_state.show_bug:
    st.markdown(
        """
        <div class="bug">🐛</div>
        """,
        unsafe_allow_html=True,
    )
    
# endregion

# endregion

# ===============================
# region Escargot the Snail
# ===============================

# ===============================
# region Escargot random path
# ===============================

@st.cache_data
def Escargot_random_positions_2(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
    # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

random_positions_Escargot_2 = Escargot_random_positions_2()

# endregion

# ===============================
# region Escargot keyframes
# ===============================

def keyframes_CSS_Escargot(random_positions_Escargot):
    keyframes = "@keyframes move_Escargot {"
    step = 0
    for top, left in random_positions_Escargot:
        keyframes += f"{step}% {{ top: {top}%; left: {left}%; }}"
        step += int(100 / (len(random_positions_Escargot) - 1))  # Evenly distribute steps
    keyframes += "}"
    return keyframes

keyframes_Escargot = keyframes_CSS_Escargot(random_positions_Escargot_2)

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
    if not st.session_state.show_escargot and random.random() < 0.01: # 2.5% chance to spawn Escargot the Snail
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
# region Control messages
# ===============================

if not st.session_state.first_run:
    if st.session_state.show_bug and st.session_state.show_escargot and not st.session_state.show_popup_Friends:
        show_popup_Friends()
        st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Bug = True
        st.session_state.show_popup_Escargot = True
    elif (st.session_state.show_bug 
          and not st.session_state.show_popup_Bug
          and not st.session_state.bug_first_run):
        show_popup_Bug()
        # st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Bug = True
    elif (st.session_state.show_escargot 
          and not st.session_state.show_popup_Escargot 
          and not st.session_state.escargot_first_run):
        show_popup_Escargot()
        # st.session_state.show_popup_Friends = True
        st.session_state.show_popup_Escargot = True
else:
    st.session_state.first_run = False
    st.session_state.bug_first_run = st.session_state.show_bug 
    st.session_state.escargot_first_run = st.session_state.show_escargot

# endregion

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

# endregion

# ===============================
# region Film Chooser intro
# ===============================

st.header(":clapper: Film Chooser", divider="rainbow")

st.write('''Welcome to the Film Chooser! This is a tool that might help you to choose a 
         movie for the movie night. It is very simple to use, but here are some tips:''')

st.write("""
         **[Search Filters](#search-filters):** When starting the Thursday Filmday app, 
         default filter settings are applied. You can select a main genre and additional 
         genres, or choose **'No preference for any genre...'** to avoid filtering by 
         genre. If you want to filter genres but don't care about the main genre, select 
         **'No preference for a main genre...'**. Be cautious with the votes setting; low 
         settings might exclude good movies. For blockbusters, set a high filter on votes 
         (minimum 200,000).""")

st.write("""
         **[Applied Filters](#applied-filters):** Get a short overview of the filter 
         settings.""")

st.write("""
         **[Possible Movies](#possible-movies):** In this list, you'll find all films that
         match the filter settings you choose. This list will automatically update if you 
         decide to change the filter settings. You'll also see how many films were found 
         and get notified with a warning if you didn't select a genre.""")

st.write("""
         **[Visit IMDb Page](#visit-imdb-page):** With this function, you can easily visit 
         the IMDb film pages of movies that are in the Possible Movies list. Here, you 
         select a subset of films based on a movie's feature that you choose.""")

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

# endregion

# ===============================
# region Version control
# ===============================

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
    
# endregion

# ===============================
# region 1.1 Search Filters
# ===============================

st.subheader('Search Filters', divider='violet')

st.write('''
        Because some behavior of the Thursday Filmday app drives me up the wall,
        I'll give you two whimsical options for your filters: **(1) forget** your filters
        when you navigate between pages. This will make the filters behave like a well-trained puppy 🐶
        **(2) save** your filters when you navigate between pages. The filters won't reset if you return to the Film Chooser,
        but beware! The filters will act like a mischievous gremlin 😈
	 ''')

# Initialize session state if not already done
if 'genre_save' not in st.session_state:
    st.session_state.genre_save = 0

# Toggle button with session state
if st.toggle('Forget/Save', key='toggle', value=st.session_state.genre_save):
    st.session_state.genre_save = 1
else:
    st.session_state.genre_save = 0

save = st.session_state.genre_save

# ===============================
# region Genre selection
# ===============================

st.write('**Genre:**')

# ===============================
# region AND/OR jack in the box
# ===============================

# Define AND_OR operator
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

# ===============================
# region Main genre
# ===============================

if save == 1:
    if 'selected_main_genre' not in st.session_state:
        st.session_state['selected_main_genre'] = genres[0]

    def save_main_genre():
         st.session_state['selected_main_genre'] = st.session_state['key_main_genre']

    main_genre = st.selectbox('Main genre:', genres,
                              key='key_main_genre',
                              index=genres.index(st.session_state['selected_main_genre']),
                              on_change=save_main_genre)
else:
    main_genre = st.selectbox('Main genre:', genres)

# endregion

# ===============================
# region Genre if-statement
# ===============================

# Initialize session state
if 'selected_other_genres' not in st.session_state:
    st.session_state['selected_other_genres'] = []

# Define a callback function to update session state
def save_other_genres():
    st.session_state['selected_other_genres'] = st.session_state['key_other_genres']

def process_genre_selection(main_genre, genres, save):
    genre_options = []
    other_genres = []
    genre_selection = []
    operator = 0
    genre_tag = 0

    if main_genre == "No preference for any genre...":
        pass
    else:
        genre_options = [
            genre for genre in genres if genre not in ["No preference for any genre...", 
                                                       "No preference for a main genre..."]
        ]
        if main_genre != "No preference for a main genre...":
            genre_options = [genre for genre in genre_options if genre != main_genre]
            max_genres = 2
            genre_tag = 2
        else:
            max_genres = 3
            genre_tag = 1

        if save == 1:
            other_genres = st.multiselect(
            f"Select a maximum of **{max_genres}** genre(s):",
            options=genre_options,
            default=st.session_state['selected_other_genres'],
            key='key_other_genres',
            on_change=save_other_genres)

            genre_selection = other_genres.copy()
            operator = AND_OR()
        else:
            other_genres = st.multiselect(
            f"Select a maximum of **{max_genres}** genre(s):",
            options=genre_options)

            genre_selection = other_genres.copy()
            operator = AND_OR()

    return genre_options, other_genres, genre_selection, operator, genre_tag

(genre_options, other_genres, 
 genre_selection, operator, 
 genre_tag) = process_genre_selection(main_genre, genres, save)

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
    default_min_year = 1985
    default_max_year = max_year

    # time 
    min_time = 30
    max_time = 240
    default_min_time = 60
    default_max_time = 120

    # ratings
    min_rating = float(1)
    max_rating = float(10)
    default_min_rating = float(7)
    default_max_rating = max_rating
    ratings_step_size = 0.5

    # votes
    min_votes = 0
    max_votes = 500000
    default_min_votes = 100000
    votes_step_size = 500

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

if save == 1:
    # year slider

    st.write('**Year:**')
    if 'slider_year' not in st.session_state:
        st.session_state.slider_year = (1985, datetime.now().year) 
    selected_years = st.slider("Range of years in which a film went into premiere:", 
                       min_year, max_year,
                       (st.session_state.slider_year[0], 
                        st.session_state.slider_year[1]),
                       step=1)
    if selected_years is not None:
        st.session_state.slider_year = selected_years
    st.divider()

    # time slider
    st.write('**Duration:**')
    if 'slider_duration' not in st.session_state:
        st.session_state.slider_duration = (60, 120) 
    selected_time = st.slider("Range of film duration in minutes:", 
                      min_time, max_time,
                      (st.session_state.slider_duration[0], 
                       st.session_state.slider_duration[1]),
                      step=5)
    if selected_time is not None:
        st.session_state.slider_duration = selected_time
    st.divider()

    # ratings slider
    st.write('**Rating:**')
    if 'slider_rating' not in st.session_state:
        st.session_state.slider_rating = (7.0, 10.0) 
    selected_rating = st.slider("Range of film IMDb ratings:", 
                        min_value=min_rating,
                        max_value=max_rating,
                        value=(st.session_state.slider_rating[0],
                               st.session_state.slider_rating[1]),
                        step=ratings_step_size,
                        format="%.1f")
    if selected_rating is not None:
        st.session_state.slider_rating = selected_rating
    st.divider()

    # votes slider
    st.write('**Votes:**')
    if 'slider_votes' not in st.session_state:
        st.session_state.slider_votes = 100000
    selected_votes = st.slider("Minimum number of votes for the IMDb film rating:", 
                       min_votes, max_votes, 
                       st.session_state.slider_votes,
                       step=votes_step_size)
    if selected_votes is not None:
        st.session_state.slider_votes = selected_votes
else:
    # year slider
    st.write('**Year:**')
 
    selected_years = st.slider("Range of years in which a film went into premiere:", 
                       min_year, max_year,
                       (default_min_year, default_max_year),
                       step=1)
    st.divider()

    # time slider 
    selected_time = st.slider("Range of film duration in minutes:", 
                      min_time, max_time,
                      (default_min_time, default_max_time),
                      step=5)
    st.divider()

    # ratings slider 
    selected_rating = st.slider("Range of film IMDb ratings:", 
                        min_value=min_rating,
                        max_value=max_rating,
                        value=(default_min_rating, default_max_rating),
                        step=ratings_step_size,
                        format="%.1f")
    st.divider()

    # votes slider
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
# region Session state for random film button
# ===============================

# Save the filtered data to session state
st.session_state["filtered_data"] = display_df

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
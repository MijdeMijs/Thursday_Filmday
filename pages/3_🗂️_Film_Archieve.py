# ===============================
# region Imports
# ===============================
import streamlit as st
import pandas as pd
import time
from datetime import datetime
import random
import random

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
    if not st.session_state.show_escargot and random.random() < 0.025: # 2.5% chance to spawn Escargot the Snail
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

# ===============================
# region Load data
# ===============================

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
# region Film Archive
# ===============================

# ===============================
# region Archive intoduction
# ===============================

st.header(" :card_index_dividers: Film Archive", divider="rainbow")

st.write('''The Film Archive is a comprehensive hub where you can revisit all the films 
         we’ve enjoyed together. It lets you see which room suggested each film, track 
         how many votes each room received, and even check out the movie snack of the 
         night. You can explore the archive by individual movie nights or view the entire 
         collection in one go. Each film entry is enriched with additional IMDb 
         information, providing a quick overview of key details. For added convenience, 
         there’s a dedicated IMDb film page button, so you can instantly visit the 
         official page for any movie. It’s the perfect way to relive past movie nights 
         and discover new favorites!''')

# endregion

# ===============================
# region Archive version control
# ===============================

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

# endregion

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
                   'duel': archieve_df['duel'],
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
# region Random emoji
# ===============================

positive_emojis = [
    ':smile:', ':grinning:', ':grin:', ':laughing:', ':blush:', ':innocent:',
    ':slightly_smiling_face:', ':hugging_face:', ':partying_face:', ':heart_eyes:',
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
    # region Single night text
    # ===============================

    st.write(f'''
             🎉 Ready for a cinematic adventure? First, pick a year to travel back 
             in time! Then, choose your movie night date. The elected film, highlighted 
             in green, awaits your discovery. 🌟🍿

             Let the movie magic begin! 🎬✨
             ''')

    # endregion

    # ===============================
    # region Define & apply filters
    # ===============================

    # Get the current year
    current_year = datetime.now().year

    # Create a list of years from 2023 to the current year
    years = list(range(2023, current_year+1))

    movie_night_year = st.selectbox('Select year:', years)

    # Function to get unique dates for the selected year
    def get_unique_dates(movie_night_info, movie_night_year):
        # Filter the DataFrame for the specified year
        filtered_info = movie_night_info[movie_night_info['Date'].dt.year == movie_night_year]
        
        # Get unique dates in the desired format
        unique_dates = filtered_info['Date'].dt.strftime('%d %B %Y').unique()
        return unique_dates

    # Get unique dates for the selected year
    dates = get_unique_dates(movie_night_info, movie_night_year)

    movie_night_date = st.selectbox(f'Select movie night date ({movie_night_year}):', 
                                    dates)

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

    info_to_display = (list(single_movie_night_info.columns[5:8]) + 
                       list(single_movie_night_info.columns[9:]))

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

    # ===============================
    # region Duel
    # ===============================

    if single_movie_night_info['duel'].sum() == 1:
        film_row = single_movie_night_info[single_movie_night_info['watched'] == 1]
        roma_victor = str(film_row.iloc[0,5])
        st.write(f''':crossed_swords: On this fateful day, a valiant duel unfolded! 
                 A noble warrior fell, defending their honor and cherished movie. 
                 **{roma_victor}** emerged triumphant! All hail the new champion!''')

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

    info_to_display = list(styled_df_complete.columns[4:])

    n_nights = int(archieve_df['watched'].sum())

    st.write(f"""
             **Welcome to the ultimate film archive!** 🎬✨ 
             
             Dive into the treasure trove of **{n_nights} unforgettable movie nights**! 
             The chosen films, highlighted in green, shine like stars in our cinematic 
             galaxy. 🌟🍿
             
             Ready to explore the legends of movie nights past? 🎥📚
             """)

    st.dataframe(styled_df_complete, 
                 column_order=info_to_display, 
                 hide_index=True)

    # endregion

    # ===============================
    # region Duel list
    # ===============================

    # Filter rows where duel is 1
    duel_df = movie_night_info[movie_night_info['duel'] == 1]

    # Write the information using streamlit
    for index, row in duel_df.iterrows():
        # Convert date to desired format
        date_obj = pd.to_datetime(row['Date'])
        formatted_date = date_obj.strftime("%d %b %Y")
        
        st.write(f"""⚔️ On **{formatted_date}**, **{row['Room']}** successfully defended 
                 the title **{row['Film']}**.""")
    
    # endregion

    # endregion

# endregion

st.divider()

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

    selected_archieve_film = st.selectbox("Select a film to visit its IMDb page:", archieve_selection)

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
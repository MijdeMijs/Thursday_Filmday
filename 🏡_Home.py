# ===============================
# region Imports
# ===============================
import streamlit as st
import time
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
   st.write('''**NEVER ALLOW COOKIES!** We don\'t need :cookie: or :cupcake:!!! We want 
            MUFFINS!''')
   
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
def Bug_random_positions_1(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
        # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

# Generate random keyframe positions
random_positions_Bug_1 = Bug_random_positions_1()

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

keyframes_Bug = keyframes_CSS_Bug(random_positions_Bug_1)

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
def Escargot_random_positions_1(num_points=100):
    positions = []
    for _ in range(num_points):
        top = random.randint(12, 95)  # Random top position (12% to 95%)
        left = random.randint(5, 95)  # Random left position (5% to 95%)
        positions.append((top, left))
    # Ensure the last position matches the first
    positions.append(positions[0])
    return positions

random_positions_Escargot_1 = Escargot_random_positions_1()

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

keyframes_Escargot = keyframes_CSS_Escargot(random_positions_Escargot_1)

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

    This app is designed to enhance your movie night experience with three 
         exciting sections:

    1. **Film Chooser**: This section helps you select the perfect film 
         for your movie night. Whether you're in the mood for a comedy, 
         drama, or action-packed thriller, the Film Chooser will guide 
         you to the best options.
    """)

st.page_link("pages/1_🎬_Film_Chooser.py", label="Go to Film Chooser", icon="🎬")

st.write("""
    2. **Movie Stats**: Dive into some fun statistics about all the movies 
         we've watched together. Discover interesting trends, favorite 
         genres, and more. It's a great way to see our collective 
         movie-watching habits!
    """)

st.page_link("pages/2_📊_Movie_Stats.py", label="Go to Movie Stats", icon="📊")

st.write("""
    3. **Film Archive**: Here, you can browse through a comprehensive list 
         of all the films we've watched and suggested. It's a handy 
         reference to revisit past favorites or find new recommendations.
    """)

st.page_link("pages/3_🗂️_Film_Archieve.py", label="Go to Film Archieve", icon="🗂️")

st.write("""
    I've also hidden some fun easter eggs throughout the app for you to 
         discover. I put a lot of effort into creating this page, so I 
         hope you enjoy it. Please be gentle, as the app might not be the 
         most efficient in the world.

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

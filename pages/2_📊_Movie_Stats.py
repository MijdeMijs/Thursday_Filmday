# ===============================
# region Imports
# ===============================
import streamlit as st
from streamlit_theme import st_theme
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
# region Get theme
# ===============================

theme = st_theme()

theme_col = theme.get('base', 'light')

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
# region Matplotlib settings
# ===============================

if theme_col == 'light':
    facecolor = 'white'
    axcolor = 'white'
    textcolor = 'black'
    bordercolor = 'black'
elif theme_col == 'dark':
    facecolor = '#0e1117'
    axcolor = '#666666'
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
# region Movie Stats
# ===============================
st.header(":bar_chart: Movie Stats", divider="rainbow")

# ===============================
# region General values
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

# endregion

# ===============================
# region Introduction
# ===============================

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

# endregion

# ===============================
# region Winners
# ===============================

# ===============================
# region Specific values
# ===============================

# Number of times won
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

# endregion

# ===============================
# region Text winners
# ===============================

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

# endregion

# ===============================
# region Rooms times won plot
# ===============================

# Plot function
# @st.cache_data
def plot_n_winner(n_winner):

    # Plot a bar
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(n_winner.index, n_winner.values, 
                  color=plt.cm.rainbow(np.linspace(0, 1, len(n_winner))), 
                  edgecolor='black')
    
    # Axis
    ax.set_xlabel('')
    ax.set_xticklabels(n_winner.index, rotation=0, fontsize=14)
    ax.set_ylabel('Times won', fontsize=14)
    
    # Set y-axis to show no decimals
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.yticks(fontsize=14)

    # Add count on top of bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=14)

    # Set y-axis limit
    ax.set_ylim(0, n_winner.max() + 5)

    return fig

# Call plot function
fig_1 = plot_n_winner(n_winner)

# Display the plot in Streamlit
st.pyplot(fig_1)        

# endregion

st.divider()

# ===============================
# region Rooms times won trend
# ===============================

# @st.cache_data
def plot_winners_over_time(df):

    # Plot
    fig, ax = plt.subplots()

    # Get unique groups
    groups = df['room'].unique()

    # Rainbow colors for groups
    colors = plt.cm.rainbow(np.linspace(0, 1, len(groups)))

    # Scatter plot with connecting lines per group using rainbow colors
    for color, (key, grp) in zip(colors, df.groupby(['room'])):
        ax.plot(grp['date'], grp['cumulative_win'], marker='', linestyle='-',
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
fig_2 = plot_winners_over_time(archieve_df)

# Display the plot in Streamlit
st.pyplot(fig_2)

# endregion

# endregion

# ===============================
# region Votes
# ===============================

# ===============================
# region Specific values
# ===============================

# Number of votes
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

# endregion

# ===============================
# region Text votes
# ===============================

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

# endregion

# ===============================
# region Votes plot
# ===============================

# Plot function
# @st.cache_data
def plot_votes_per_room(df):

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
    ax.set_ylim(0, votes_per_room.max() + 10)

    return fig

# Call plot function
fig_3 = plot_votes_per_room(archieve_df)

# Display the plot in Streamlit
st.pyplot(fig_3)

# endregion

st.divider()

st.write(f'''The second figure takes us on a journey through time as the cumulative votes 
         pile up. **{room_1_vote}’s** rise to the top was steady and strong—like a 
         blockbuster climbing the box office charts. **{room_2_vote}** made a valiant 
         effort to keep up, but ultimately fell behind. And **{room_5_vote}**… well, 
         let’s just say their graph looks more like a gentle slope than a steep climb. 
         *Baby steps, right?*
        ''')

# ===============================
# region Votes trend
# ===============================

# Plot function
# @st.cache_data
def plot_votes_over_time(df):

    # Plotting
    fig, ax = plt.subplots()

    # Get the unique groups
    groups = df['room'].unique()

    # Generate rainbow colors for the groups
    colors = plt.cm.rainbow(np.linspace(0, 1, len(groups)))

    # Scatter plot with connecting lines per group using rainbow colors
    for color, (key, grp) in zip(colors, df.groupby(['room'])):
        ax.plot(grp['date'], grp['cumulative_votes'], marker='', linestyle='-',
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

# Call plot function
fig_4 = plot_votes_over_time(archieve_df)

# Display the plot in Streamlit
st.pyplot(fig_4)

# endregion

st.write(f'''**Moral of the story:** {room_1_vote}’s the crowd-pleaser, and 
         {room_5_vote}’s got some catching up to do! 🚀
        ''')

# endregion

# ===============================
# region IMDb ratings
# ===============================

# ===============================
# region Text IMDb ratings
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

# endregion

# ===============================
# region Plot ratings chosen
# ===============================

# Plot function
# @st.cache_data
def plot_IMDb_rating_chosen_room(df):

    # Group by room and get average ratings
    grouped_data = [df[df['room'] == room]['averageRating'].dropna().values for room in sorted(df['room'].unique())]

    # Flier properties to set outlier color
    flierprops = dict(marker='o', color='red')

    # Plot a boxplot with the specified style
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure background color to white
    box = ax.boxplot(grouped_data, patch_artist=True, flierprops=flierprops)

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

    # Set the outlier (flier) color
    # for flier in box['fliers']:
    #     flier.set(marker='o', color='black')

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

# Call plot function
fig_5, grouped_data_rating = plot_IMDb_rating_chosen_room(watched_df)

# Display the plot in Streamlit
st.pyplot(fig_5)

# endregion

# ===============================
# region Room quality
# ===============================

# @st.cache_data
def IMDb_rating_ratio(grouped_data_rating, watched_df):
    
    grouped_data_rating = grouped_data_rating[1:6]

    # Define the names
    names = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5"]

    # Create a dictionary with names as keys and arrays as values
    named_arrays = {name: arr for name, arr in zip(names, grouped_data_rating)}

    # Your original ratios dictionary
    ratios = {name: np.mean(arr) / watched_df['averageRating'].mean() for name, arr in named_arrays.items()}

    # Calculate min and max values
    min_val = min(ratios.values())
    max_val = max(ratios.values())

    # Apply min-max normalization
    scaled_ratios = {name: (value - min_val) / (max_val - min_val) for name, value in ratios.items()}

    return scaled_ratios

scaled_ratios = IMDb_rating_ratio(grouped_data_rating, watched_df)    

# Assign the ratios to individual variables
ratio_1 = scaled_ratios["Room 1"].round(3)
ratio_2 = scaled_ratios["Room 2"].round(3)
ratio_3 = scaled_ratios["Room 3"].round(3)
ratio_4 = scaled_ratios["Room 4"].round(3)
ratio_5 = scaled_ratios["Room 5"].round(3)

st.write(f'''
         Let's check the **normalized average room IMDb rating/average watched film IMDb 
         rating ratio**! If your ratio is high, it means you generally contribute 
         high-quality films. If your ratio is low, you might need to refine your taste!
         With a value of 0.5, you're just an average bloke. Unworthy of a special 
         mentioning. Rooms with ratios below 0.5 contribute below-average quality films, 
         while rooms with ratios above 0.5 contribute above-average quality films. Maybe 
         consider voting on someone else next time?

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

# endregion

# ===============================
# region Plot ratings suggested
# ===============================

# Plot function
# @st.cache_data
def plot_IMDb_rating_room(df):

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

# Call plot function
fig_6, grouped_data = plot_IMDb_rating_room(archieve_df)

# Display the plot in Streamlit
st.pyplot(fig_6)

# endregion

st.write(f'''Together, these plots show how the chosen films compare to the broader 
         pool of suggestions. It’s an ongoing story—dynamic and ever-changing as more 
         movie nights unfold! Whether the IMDb ratings go up, down, or stay steady, 
         every movie pick adds a new twist to the tale.
        ''')

# endregion

# ===============================
# region Film duration
# ===============================

# ===============================
# region Text film duration
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

# endregion

# ===============================
# region Plot film duration chosen
# ===============================

# Plot function
# @st.cache_data
def plot_IMDb_duration_room(df):

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

# Call plot function
fig_7, grouped_data = plot_IMDb_duration_room(watched_df)

# Display the plot in Streamlit
st.pyplot(fig_7)

# endregion

st.write(f'''The second plot digs into the runtimes of all the suggested films—whether 
         they were chosen or not. Here, we get a broader sense of what each room 
         brought forward. Some rooms might aim for epic sagas with towering runtimes, 
         while others pitch films that fit neatly into a busy evening schedule.
        ''')

# ===============================
# region Plot film duration suggested
# ===============================

# Plot functions
# @st.cache_data
def plot_IMDb_duration_suggested_room(df):

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

# Call plot function
fig_8, grouped_data = plot_IMDb_duration_suggested_room(archieve_df)

# Display the plot in Streamlit
st.pyplot(fig_8)

# endregion

st.write(f'''Together, these visuals reveal a lot about each room’s cinematic style. 
         Whether your picks skew longer or shorter, every suggestion adds to the 
         tapestry of movie night fun—and who knows what the next selection will bring?
         ''')

# endregion

# ===============================
# region Genres
# ===============================

# ===============================
# region Text genres
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

# endregion

# ===============================
# region Plot genres
# ===============================

# Plot function
# @st.cache_data
def plot_n_genres(df):

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

# Call plot function
fig_7 = plot_n_genres(watched_df)

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
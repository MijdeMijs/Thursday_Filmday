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
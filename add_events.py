# core package
import streamlit as st
from datetime import datetime

# EDA package
import pandas as pd

# DB fanctions packages
from db_fxns import *



# this def run_add_events() will be used in the app.py
def run_add_events():
    
    # Define the categories and subcategories
    event_categories = {
                "Corporate Events": ["Conference", "Seminar", "Workshop", "Trade show", "Product launch", "Company retreat", "Team-building event", "Board meeting", "Networking event", "Staff Parties", "Summer Fun Events", "Sales Kick Offs", "Brand activation", "Influencer Event"],
                "Exhibitions and Expo": ["Trade exhibition", "Art expo", "Science fair", "Technology showcase", "Car show"],
                "Travel and Tourism Event": ["Travel expos", "Tourism showcases", "Adventure sports events", "Cultural tours"],
                "Art and Craft Event": ["Art gallery openings", "Craft fairs", "Art workshops", "Sculpture exhibitions"],
                "Fashion Event": ["Fashion shows", "Clothing launches", "Fashion weeks", "Designer exhibitions"],
                "Community Event": ["Farmers markets", "Charity runs", "Neighborhood cleanups", "Food drives", "Community workshops", "Town Events", "Christmas Events", "Family Fun Day Events"],
                "Sports Event": ["Football matches", "Basketball games", "Tennis tournaments", "Olympic events", "Marathons"],
                "Cultural and Religious Event": ["Religious festivals", "Cultural parades", "Carnivals"],
                "Entertainment Event": ["Concerts", "Music festivals", "Movie premieres", "Theater performances", "Comedy shows", "Sporting events"],
                "Private Event": ["Wedding", "Birthday party", "Anniversary celebration", "Graduation party", "Baby shower", "Retirement party", "Reunion"]
    }
    
    # set the sub header
    st.subheader("Add New Event")
    
    # provide data input areas
    name = st.text_input("Event Name")
    address = st.text_input("Event Address")
    start_day = st.date_input("Event Start Date", datetime.today())
    end_day = st.date_input("Event End Date", datetime.today())
    main_category = st.selectbox("Main Category", options=list(event_categories.keys()), index=0)
    sub_category = st.selectbox("Sub Category", options=event_categories[main_category])
    indoor = st.checkbox("Indoor Event")
    outdoor = st.checkbox("Outdoor Event")
    online = st.checkbox("Online Event")

    # if you push this button, the data will be in the database 
    submit_button = st.button(label='Submit')
    if submit_button:
        # Call the function to process the form data
        # Ensure this function is defined and handles the data correctly
        add_data(name, address, start_day, end_day, indoor, outdoor, online, main_category, sub_category)
        st.success(f"Event '{name}' added successfully!")
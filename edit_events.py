# core package
import streamlit as st
from datetime import datetime

# EDA package
import pandas as pd

# DB fanctions packages
from db_fxns import *
  
  
  
# this def run_edit_events() will be used in the app.py
def run_edit_events():
    
    # set the sub header
    st.subheader("View All Events")
    
    # all data will be shown in dataframe format
    result = view_all_data()
    df = pd.DataFrame(result, columns=["name",
                                        "address",
                                        "start_day",
                                        "end_day",
                                        "indoor",
                                        "outdoor",
                                        "online",
                                        "main_category",
                                        "sub_category"])
    st.dataframe(df)
    
    
    # set the sub header
    st.subheader("Edit Events")
    
    # all data in the database will be shown and we can select one in this select box
    list_of_events = [i[0] for i in view_all_data()]    
    selected_event = st.selectbox("Event to be deleted", list_of_events)
    
    # we can get the detail data selected above
    event_result = get_data_by_event_name(selected_event)
    df_event_result = pd.DataFrame(event_result, columns=["name",
                                        "address",
                                        "start_day",
                                        "end_day",
                                        "indoor",
                                        "outdoor",
                                        "online",
                                        "main_category",
                                        "sub_category"])
    df_event_result = df_event_result.T
    df_event_result.columns = ['event data']
    st.dataframe(df_event_result)
    
    
    # this sentense jsut asks the question
    st.write("How do you edit?")
    
    # get the old information
    if not df_event_result.empty:
        name = df_event_result.loc['name', 'event data']
        address = df_event_result.loc['address', 'event data']
        start_day = df_event_result.loc['start_day', 'event data']
        end_day = df_event_result.loc['end_day', 'event data']
        indoor = df_event_result.loc['indoor', 'event data']
        outdoor = df_event_result.loc['outdoor', 'event data']
        online = df_event_result.loc['online', 'event data']
        main_category = df_event_result.loc['main_category', 'event data']
        sub_category = df_event_result.loc['sub_category', 'event data']


                    
    # set the layout
    col1,col2 = st.columns(2)
    
    # input area for new_name, new_address, new_start_day and new_end_day will be left with old data as defaluts
    with col1:
        new_name = st.text_input("Event Name",name)
        new_address = st.text_input("Address",address)
        new_start_day = st.date_input("Start Date", datetime.strptime(start_day, '%Y-%m-%d'))
        new_end_day = st.date_input("End Date", datetime.strptime(end_day, '%Y-%m-%d'))
    
    # input area for new_indoor, new_outdoor, new_online, new_main_category and new_sub_category will be left with old data as defaluts
    with col2:    
        st.write("Event Type")
        new_indoor = st.checkbox("Indoor", indoor == 1)
        new_outdoor = st.checkbox("Outdoor", outdoor == 1)
        new_online = st.checkbox("Online", online == 1)
        new_main_category = st.text_input("Main Category",main_category)
        new_sub_category = st.text_input("Sub Category",sub_category)

    # if you push the button, the data in the database will be updated
    if st.button("Update Task"):
        edit_data(new_name, new_address, new_start_day, new_end_day, new_indoor, new_outdoor, new_online, new_main_category, new_sub_category,
              name, address, start_day, end_day, indoor, outdoor, online, main_category, sub_category)
        st.success(f"Edited {name}")




        



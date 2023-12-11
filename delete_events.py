# core package
import streamlit as st
from datetime import datetime

# EDA package
import pandas as pd

# DB fanctions packages
from db_fxns import *



# make a creating a new table function 
def run_delete_events():
    # set the sub header
    st.subheader("All Events")

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
    st.subheader("Delete Events")
    
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
    
    name = df_event_result.loc['name', 'event data']



    # this is just warning before deleting items
    st.warning(f"Do you delete {name}?")
    
    # if you push this button, the data will be deleted in the dataframe
    if st.button("Delete"):
        delete_data(name)
        st.info(f"Deleted{name}")
        
        
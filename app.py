# core package
import streamlit as st

# DB functions package
from db_fxns import *

# other pages other than this top page
from add_events import run_add_events
from edit_events import run_edit_events
from delete_events import run_delete_events





def main():
    # if there are no tanles this code makes a new table automatically
    create_event_table()
    
    # set the title
    st.title("Questionnaire for Event Management Professionals")
    
    # set the side bar
    menu = ["Home", "Add events", "Edit Events", "Delete Events"]
    choice = st.sidebar.selectbox("Menu", menu)



    # if you choose "Home" in the side bar, you see here
    if choice == "Home":
        # jsut this introduction will be shown
        st.subheader("This page allows you to add, edit, and delete events.")



    # if you choose "Add events" in the side bar, you see here
    if choice == "Add events":
        run_add_events()
        
    
    
    # if you choose "Edit Events" in the side bar, you see here
    if choice == "Edit Events":
        run_edit_events()
        


    # if you choose "Delete Events" in the side bar, you see here
    if choice == "Delete Events":
        run_delete_events()
        


if __name__ == '__main__':
    main()

import streamlit as st  
from streamlit_option_menu import option_menu

def sidebar():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
def setting_page():
    t.set_page_config(
        page_title="KMP",
        page_icon=":u5272:",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
def main():
    setting_page()
    st.title("Welcome")
    sidebar()
    
if __name__=='__main__' :
    main()



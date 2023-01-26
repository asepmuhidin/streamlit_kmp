import streamlit as st  
from pathlib import Path

from streamlit_option_menu import option_menu

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"


def sidebar():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        
def setting_page():
    st.set_page_config(
        page_title="KMP",
        layout="centered"
    )
    
def main():
    setting_page()
    st.title("Welcome")
    sidebar()
    
if __name__=='__main__' :
    main()



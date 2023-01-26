from pathlib import Path

import streamlit as st  # pip install streamlit
from PIL import Image  # pip install pillow

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ---
PRODUCT_NAME = "kmp"
PRODUCT_TAGLINE = "kirata media perkasa"



def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":u5272:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(CSS_FILE)


# --- SIDEBAR SECTION ---
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
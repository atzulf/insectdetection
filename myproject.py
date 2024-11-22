import os
import streamlit as st
from utils import add_background
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

# Gunakan path absolut untuk file background
image_path = r"D:\KULIAH UNY\SEMESTER 5 TI\Aplikasi Web\PraktikumStreamlit\finalproject\src\image\bg.png"

# Tambahkan background
add_background(image_path)

pages = ["Home", "Classification", "About"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
# logo_path = os.path.join(parent_dir, "cubes.svg")

styles = {
    "nav": {
        "background-color": "#1B4842",
        "justify-content": "center",
        "font-family": "Poppins",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "15px",
    },
    "active": {
        # "background-color": "#1D93B3",
        "color": "#1D93B3",
        "font-weight": "normal",
    }
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    # logo_path=logo_path,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.show_home,
    "Classification": pg.show_classification,
    "About": pg.show_about,
}
go_to = functions.get(page)
if go_to:
    go_to()
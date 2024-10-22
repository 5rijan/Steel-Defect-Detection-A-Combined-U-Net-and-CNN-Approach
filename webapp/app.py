import streamlit as st
from st_pages import add_page_title

st.set_page_config(layout="wide")

# TOML content as a Python string
toml_content = """
[[pages]]
path = "pages/introduction.py"
name = "Introduction"
icon = "📖"

[[pages]]
path = "webapp/cnn.py"
name = "CNN "
icon = "📊"

[[pages]]
path = "webapp/unet.py"
name = "U-Net"
icon = "📄"
"""

# Parse the TOML content
import toml
from io import StringIO

parsed_toml = toml.load(StringIO(toml_content))

# Create navigation
st.sidebar.title("Navigation")
for page in parsed_toml["pages"]:
    st.sidebar.page_link(page["path"], label=f"{page['icon']} {page['name']}")

# Determine current page
current_page_name = st.experimental_get_query_params().get("page", ["Introduction"])[0]

import json

import streamlit as st
from anytree import RenderTree

from mwis.core.animal import get_animals_tree
from mwis.core.mwis import mwis

# region streamlithide
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.set_page_config(
    page_title="Maximum Weight Independent Set",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# endregion
st.markdown(""" # Maximum Weight Independent Set """)

st.markdown(""" ## Start by Uploading a JSON file """)

# region json upload
uploaded_file = st.file_uploader("Choose a JSON file", type="json")
if uploaded_file:
    # Read the file as a string data
    file_details = {
        "FileName": uploaded_file.name,
        "FileType": uploaded_file.type,
        "FileSize": uploaded_file.size,
    }
    json_bytes = uploaded_file.read()
    data = json.loads(json_bytes.decode("utf-8"))
    king, animals = get_animals_tree(data)
# endregion

# region tree display
st.markdown(""" ## The Tree """)
if uploaded_file:
    st.code(RenderTree(king))
# endregion


# region mwis
st.markdown(
    """
## Invitation List
"""
)
# Options of force king inclusion
force_king_inclusion = st.checkbox("Force King Inclusion", value=True)

if uploaded_file:
    party_score, invited_list = mwis(king, force_king_inclusion)
    invited_list = sorted(
        invited_list, key=lambda x: list(animals.keys()).index(x.name)
    )
    st.markdown(f"**Total Party Score:** {party_score}")
    st.markdown(
        f"**Animals Invited:** {', '.join([animal.name for animal in invited_list])}"
    )
# endregion

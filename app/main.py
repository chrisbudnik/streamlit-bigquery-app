import hmac
import time
import streamlit as st
import pandas as pd

from exceptions import AppError
from elements import (
    ui_element_main_selectors, 
    ui_element_advanced_selectors, 
    ui_element_top_selectors, 
    ui_element_upload_data_process, 
    ui_element_campaign_details_form,
    ui_element_file_download_process,
    ui_element_abgroups_process
)
from query import QueryConstructor


# Page config
st.set_page_config(
    page_title='marketing automation', 
    page_icon='🔥'
    )
# Transform into get environment variable SITE_PASSWORD
password = "password123"

# Check password func with state management
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], password):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

# Do not continue if check_password is not True.
if not check_password():
    st.stop()  


# Main Streamlit app starts here
st.title("Automation Tool")
st.write('Description... ')

# introduce sidebar
with st.sidebar.title("Navigation"):
# Authentication Token Input
    input_token = st.text_input('Input token (auth)', type="password")


# Select Boxes for Country and Last Number Metric in Columns
top_values = ui_element_top_selectors()

# RPM Params with Select Boxes in a Grid
main_parameter_toggle = st.checkbox('Main params')
if main_parameter_toggle:
    main_values = ui_element_main_selectors()

# Advanced Params with Select Boxes in a Grid
advanced_parameter_toggle = st.checkbox('Advanced params')
if advanced_parameter_toggle:
    advanced_values = ui_element_advanced_selectors()


# initialize query constructor
constructor = QueryConstructor()
all_params = top_values | main_values | advanced_values

# Summarize query requirements
requirements = {k: v for k, v in all_params.items() if v != 'not included' and v is not False}


data = pd.DataFrame({
        'country': [],
        'customers': [],
        'share_customers': [],
        'cost': []
    })

@st.cache_data
def get_data():
    data = pd.DataFrame({
        'Cost': [100, 200, 300],
        'Result': ['Success', 'Partial', 'Failed']
    })
    return data

# Estimate Costs Table
if st.button('Estimate group size & costs.'):
    data = get_data()

st.table(data)

# Prepare lists toggle and content display
prepare_lists_toggle = st.toggle('Move to the next steps: Prepare and export lists')
if prepare_lists_toggle:
    st.write('Content related to preparing lists would be here.')

    # Fill in campaign details form
    ui_element_campaign_details_form(requirements)

    # Data Upload Process
    st.header("Data upload to Storage")
    st.write('In this part data is uploaded to BigQuery and Cloud Storage. \
             First step is to choose the ab groups splits. Usually the best option \
             is to stick to defaults: classic split and 10% test size.')

    # Define ab groups splits
    ui_element_abgroups_process()

    # Button to upload data to BigQuery and Cloud Storage with status updates
    ui_element_upload_data_process()
    
    # Option to download data into files
    ui_element_file_download_process()


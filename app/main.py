import hmac
import time
import streamlit as st
import pandas as pd

from exceptions import AppError
from elements import ui_element_main_selectors, ui_element_advanced_selectors

# Page config
st.set_page_config(
    page_title='micropromo automation', 
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

# Authentication Token Input
input_token = st.text_input('Input token (auth)', type="password")

# Select Boxes for Country and Last Number Metric in Columns
col1, col2 = st.columns(2)
with col1:
    country = st.selectbox('Country', ['Country 1', 'Country 2', 'Country 3'])
with col2:
    last_number_metric = st.selectbox('Region', ['Metric 1', 'Metric 2', 'Metric 3'])

# RPM Params with Select Boxes in a Grid
main_parameter_toggle = st.checkbox('Main params - if toggle is on show other selectors')
if main_parameter_toggle:
    main_values = ui_element_main_selectors()
    st.write(main_values)

# Advanced Params with Select Boxes in a Grid
advanced_parameter_toggle = st.checkbox('Advanced params - if toggle is on show other selectors')
if advanced_parameter_toggle:
    advanced_values = ui_element_advanced_selectors()
    st.write(advanced_values) 

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
prepare_lists_toggle = st.checkbox('Prepare lists - if true (toggle button) show content below')
if prepare_lists_toggle:
    st.write('Content related to preparing lists would be here.')


# Button to upload data to BigQuery and Cloud Storage
if st.button('Upload data to BigQuery and Cloud Storage'):
    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)

    status.update(label="Download complete!", state="complete", expanded=False)
    st.success('Data uploaded successfuly to BQ and Storage')
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Check files in google storage", url="https://console.cloud.google.com/storage/browser/cloud-run-demo-csv")
    with col2:
        st.link_button("Check files in BigQuery", url="https://console.cloud.google.com/bigquery?hl=en&project=business-reserved")



# Show message on button click
if st.button('Show message'):
    st.success('Message displayed!')


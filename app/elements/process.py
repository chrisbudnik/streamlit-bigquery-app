import streamlit as st
import time


def ui_element_abgroups_process():
    """AB Groups Process."""    

    st.write('In this part you can check the AB groups splits and select type')

    split_type = st.selectbox("Select the Type of Split", ['Classic', 'Equal', "Custom"])
    split_value = 0

    if split_type == 'Classic':
        st.write('Define the test size (\%)')
        split_value = st.slider('Test size', 0., 15., value=10., step=2.5)

    if split_type == 'Equal':
        st.write('Define the number of equal groups')
        split_value = st.slider('Test size', 1, 5, 2, step=1)

    if split_type == 'Custom':
        st.write('Define the groups')
        st.warning('Warning: The groups should be equal to 100% \
                   Currently not supported')
        
    return split_type, split_value


def ui_element_upload_data_process():
    """Upload Data Process."""
    st.write("One click and data is uploaded to both destinations.")

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

        st.session_state["allow_file_download"] = True

    if st.toggle('Optional: Check resources'):
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Check files in google storage", url="https://console.cloud.google.com/storage/browser/")
        with col2:
            st.link_button("Check files in BigQuery", url="https://console.cloud.google.com/bigquery")


def ui_element_file_download_process(data):
    """File Download Process."""

    try:
        download_condition = st.session_state["allow_file_download"]
    except KeyError:
        download_condition = False
    
    if download_condition:

        if st.toggle('Optional: Download data to files'):
            st.header("Download data to files")
            st.write('You have an option to download the data to files - csv or excel.')

            # Toggle for showing advanced features
            
            
            # Use the columns feature to display advanced features in two columns
            col1, col2 = st.columns(2)

            with col1:
                # Advanced features field for selecting columns to export in the second column
                export_columns = st.multiselect(
                    "Select Columns to Export",
                    ['col1', 'col2', 'col3'],
                    default=['col1', 'col2']
                )

            with col2:
                # Advanced features field for export to CSV in the first column
                export_csv = st.radio("Export format", ['.CSV', '.XLSX'])
            
            st.download_button("Download data", data="data", file_name="data.csv", mime="text/csv")


import streamlit as st
import time


def ui_element_upload_data_process():
    """Upload Data Process."""

    st.header("Data upload to Storage")
    st.write('In this part data is uploaded to BigQuery and Cloud Storage.')

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

    st.write('In this part you can check the files in BigQuery and Cloud Storage.')

    if st.toggle('Optional: Check resources'):
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Check files in google storage", url="https://console.cloud.google.com/storage/browser/")
        with col2:
            st.link_button("Check files in BigQuery", url="https://console.cloud.google.com/bigquery")

    
def ui_element_check_resource_process():
    """Check Resource Process."""
    pass

def ui_element_file_download_process():
    """File Download Process."""

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


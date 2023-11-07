import streamlit as st

def ui_element_campaign_details_form(requirements):
    """Campaign Details Form."""

    st.header("Create a Promotion Form")
    st.write("Use this form to create a promotion and define details. \
             Once you submit the form, the promotion will be sent to the marketing team for review. \
             you also have the option to check selected requirements.")
    
    name = st.text_input("Enter the promotion name: e.g. Retention-003")

    # Promotion type selection
    promotion_type = st.selectbox("Select the Type of Promotion", ['Email', 'Campaign', 'SMS'])

    # Field for inputting description
    description = st.text_area("Enter the Description of the Promotion")

    # Requirements are generated automatically based on promotion type

    st.write(f"Requirements (auto-generated):")
    st.write(requirements)


    # Submit button
    if st.button("Submit Promotion"):
        # Process form data here (placeholder)
        st.success("Promotion Submitted Successfully!")

    return name, promotion_type, description
import streamlit as st

def ui_element_campaign_details_form():
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
    requirements = {
        'Email': "Must follow email content guidelines.",
        'Campaign': "Must adhere to campaign creation policies.",
        'SMS': "Should comply with SMS regulations and character limits."
    }
    st.code(f"'Requirements for {promotion_type}: {requirements[promotion_type]}'")


    # Submit button
    if st.button("Submit Promotion"):
        # Process form data here (placeholder)
        st.success("Promotion Submitted Successfully!")

    return name, promotion_type, description
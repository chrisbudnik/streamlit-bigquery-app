import streamlit as st


def ui_element_top_selectors():
    col1, col2 = st.columns(2)
    with col1:
        country = st.multiselect('Country', ['Country 1', 'Country 2', 'Country 3'])
        date = st.date_input('Date', value=None, min_value=None, max_value=None, key=None)
    with col2:
        region = st.multiselect('Region', ['Metric 1', 'Metric 2', 'Metric 3'])

    return {"country": country, "region": region, "date": date}

def ui_element_main_selectors():
    """Main parameters for the app layout."""

    col1, col2, col3 = st.columns(3)  
    with col1:
        select1 = st.selectbox('segment', ['not included', 'newcomers', 'promising', 'champions'])
        select4 = st.selectbox('product', ['not included', 'Option 1', 'Option 2', 'Option 3'])
    with col2:
        select2 = st.selectbox('top_category', ['not included', 'Option 1', 'Option 2', 'Option 3'])
        select5 = st.selectbox('only_promo', ['not included', 'Option 1', 'Option 2', 'Option 3'])
    with col3:
        select3 = st.selectbox('top_subcategory', ['not included', 'Option 1', 'Option 2', 'Option 3'])
        select6 = st.selectbox('regular_buyer', ['not included', 'Option 1', 'Option 2', 'Option 3'])

    return {"segment": select1, "product": select4, "top_category": select2, 
            "only_promo": select5, "top_subcategory": select3, "regular_buyer": select6}


def ui_element_advanced_selectors():
    col1, col2, col3 = st.columns(3)
    with col1:
        toggle1 = st.toggle('Extended group')
    with col2:
        toggle2 = st.toggle('Exclude high risk customers')
    with col3:
        toggle3 = st.toggle('Exclude low risk customers')
    
    return {"extended_group": toggle1, "exclude_high_risk_customers": toggle2, 
            "exclude_low_risk_customers": toggle3}
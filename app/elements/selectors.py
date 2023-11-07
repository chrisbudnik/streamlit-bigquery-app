import streamlit as st


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

    return select1, select2, select3, select4, select5, select6


def ui_element_advanced_selectors():
    col1, col2, col3 = st.columns(3)
    with col1:
        toggle1 = st.toggle('Extended group')
    with col2:
        toggle2 = st.toggle('Exclude high risk customers')
    with col3:
        toggle3 = st.toggle('Exclude low risk customers')
    
    return toggle1, toggle2, toggle3
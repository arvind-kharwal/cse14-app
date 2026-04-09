import streamlit as st
about_page = st.Page(
    page = 'views/about.py',
    title='About us',
    default=True
)

contact_page= st.Page(
    page = 'views/contact.py',
    title='Contact us',
)

profile_page= st.Page(
    page = 'views/profile.py',
    title='My Profile',
)

nb = st.navigation(pages=[about_page,profile_page,contact_page])
st.logo('assets/moon.png')
nb.run()
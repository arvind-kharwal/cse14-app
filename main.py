import streamlit as st
about_page = st.Page(
    page = 'views/about.py',
    title='About us',
    icon=':material/home:',
    default=True
)

contact_page= st.Page(
    page = 'views/contact.py',
    title='Contact us',
    icon=":material/thumb_up:"
)

profile_page= st.Page(
    page = 'views/profile.py',
    title='My Profile',
    icon=":material/person:",
)
#nb = st.navigation(pages=[about_page,profile_page,contact_page])
nb = st.navigation(
    {
        'info': [about_page,profile_page],
        'Useful Links': [contact_page],
    }
)
st.logo('assets/moon.png')
nb.run()
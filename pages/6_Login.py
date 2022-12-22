import streamlit as st

st.title('Log in')

st.markdown('<a href="https://travelwithme.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=2rbsk90sb8shq7oh8t1mh6r50n&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2F44.195.168.80" target="_self" style="background-color: #ffffff; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 0.25rem; color: black; padding: 0.25rem 0.75rem; text-align: center; text-decoration: none;display: inline-block; font-weight: 400; font-size: 0.9rem;">Login through cognito</a>', unsafe_allow_html=True)

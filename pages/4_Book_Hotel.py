import streamlit as st

st.title("Your Information")
print(st.session_state)
st.write("Confirm your booking: " + st.session_state["hotel"]["name"])
name = st.text_input("Name")
options = ['Male', 'Female', 'Other']
gender = st.selectbox('Gender:', options)
stream = st.text_input("Write me a sentence")
book_button = st.button("Book")

st.subheader("Recommendations")
count = 1
for hotel in st.session_state.rec:
    st.write(str(count) + ". " + hotel)
    count += 1

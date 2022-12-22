import streamlit as st
import requests

def Book():
    API_ENDPOINT = "https://a91201uwt9.execute-api.us-east-1.amazonaws.com/dev/book"
    info = st.session_state
    response = requests.post(API_ENDPOINT, params={"hotel_name": info["hotel"]["name"], "hotel_city": info["location"], "user_name": username, "mbti_str": stream, "duration": str(info["checkin_date"]) + "," + str(info["checkout_date"])})
    st.session_state.partners = response.json()
    print(st.session_state.partners)

st.title("Your Information")
print(st.session_state)
st.write("Confirm your booking: " + st.session_state["hotel"]["name"])
username = st.text_input("Username")
stream = st.text_input("Write me a sentence")
if st.button("Book"):
    Book()

st.subheader("Recommendations")
count = 1
for hotel in st.session_state.rec:
    st.write(str(count) + ". " + hotel)
    count += 1

import streamlit as st
import requests
from streamlit import beta_container
from streamlit_custom_notification_box import custom_notification_box

st.title('Search hotels')

# st.session_state['hotel'] = None
# st.session_state['location'] = None

API_ENDPOINT = "https://a91201uwt9.execute-api.us-east-1.amazonaws.com/dev/search"

# Get the search query from the user
location = st.text_input("Location")
checkin_date = st.date_input('Check-in date')
checkout_date = st.date_input('Check-out date')
num_of_adults = st.text_input("Number of adults")
num_of_children = st.text_input("Number of children")
children_age = st.text_input("Children age")
room_number = st.text_input("Number of rooms")
free_cancellation = st.selectbox("Need free cancellation", ["No", "Yes"])
if free_cancellation == "Yes":
  free_cancellation = 1
else:
  free_cancellation = 0


def set_state(hotel):
  #print(hotel_name)
  #st.text("Please go to Book Hotel page to finish your booking")
  styles = {'material-icons':{'color': 'blue'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}

  custom_notification_box(icon='info', textDisplay='Please go to Book Hotel page to finish your booking', externalLink='', url='#', styles=styles, key="foo")
  st.session_state.hotel = hotel
  st.session_state.checkin_date = checkin_date
  st.session_state.checkout_date = checkout_date
  print(st.session_state)
  API_ENDPOINT = "https://a91201uwt9.execute-api.us-east-1.amazonaws.com/dev/rec"
  response = requests.post(API_ENDPOINT, params={"hotel_name": hotel["name"]})
  st.session_state.rec = response.json()
  print("debug")

# Define the search function
def search():
  # Send the GET request to the API endpoint
  response = requests.get(API_ENDPOINT, params={"location": location, "adults_number": num_of_adults, "checkin_date": checkin_date, "checkout_date": checkout_date, "children_age": children_age, "children_number": num_of_children, "room_number": room_number, "free_cancellation": free_cancellation})
  st.session_state["location"] = location
  # Process the response and display the results
  results = response.json()
  # print("results:", results)
  # print("hotel:")
  #for result in results:
  #
  count = 0
  for hotel in results:
    # print(hotel)
    with st.form(key=str(count)):
    # Add some elements to the container
      st.text("Name: " + hotel["name"])
      st.text("Address: " + hotel["address"])
      st.text("Rating: " + hotel["score"])
      st.image(hotel["pic_url"], width=300)
      st.text("Price: $" + str(hotel["price"]))
      #st.checkbox("Choose this hotel", on_change=set_state, args=(hotel['name'],), key=str(count))
      #st.markdown('<a href="/View_Hotel" target="_self" style="background-color: #ffffff; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 0.25rem; color: black; padding: 0.25rem 0.75rem; text-align: center; text-decoration: none;display: inline-block; font-weight: 400; font-size: 0.9rem;">Book</a>', unsafe_allow_html=True)
      st.form_submit_button(label="Choose", on_click=set_state, args=(hotel,))
    count += 1
  #st.write(results)


# Add a button to perform the search
if st.button("Search"):
  search()

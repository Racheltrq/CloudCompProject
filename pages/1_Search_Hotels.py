import streamlit as st
import requests
from streamlit import beta_container

st.title('Search your hotels')

API_ENDPOINT = "https://a91201uwt9.execute-api.us-east-1.amazonaws.com/dev/search"

# Get the search query from the user
location = st.text_input("Location")
checkin_date = st.date_input('Check-in date')
checkout_date = st.date_input('Check-out date')
num_of_adults = st.text_input("Number of adults")
num_of_children = st.text_input("Number of children")
children_age = st.text_input("Children age")
free_cancellation = st.selectbox("Need free cancellation", ["No", "Yes"])


# Define the search function
def search():
  # Send the GET request to the API endpoint
  response = requests.get(API_ENDPOINT, params={"location": location, "adults_number": num_of_adults, "checkin_date": checkin_date, "checkout_date": checkout_date, "children_age": children_age, "children_number": num_of_children})

  # Process the response and display the results
  results = response.json()
  #for result in results:
  #
  count = 0
  for hotel in results:
    with st.expander(hotel["name"], False):
    # Add some elements to the container
      st.text(hotel["address"])
      st.text(hotel["score"])
      st.image(hotel["pic_url"], width=300)
      st.text("$" + str(hotel["price"]))
      if st.button("Book", key=count, args=(hotel)):
        pass
    count += 1
  #st.write(results)

# Add a button to perform the search
if st.button("Search"):
  search()
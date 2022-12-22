import streamlit as st

hotel = st.session_state.hotel
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
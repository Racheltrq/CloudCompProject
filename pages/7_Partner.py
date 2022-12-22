import streamlit as st
import requests
from streamlit import beta_container
from streamlit_custom_notification_box import custom_notification_box

st.title("Find your partner")

email = st.text_input("Email Address")
subject = st.text_input("Subject")
body = st.text_input("Message")

 

def send():
    API_ENDPOINT = "https://a91201uwt9.execute-api.us-east-1.amazonaws.com/dev/partner"
    response = requests.post(API_ENDPOINT, params={"body": body, "email_addr": email, "subject": subject})
    styles = {'material-icons':{'color': 'blue'},
            'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
            'notification-text': {'':''},
            'close-button':{'':''},
            'link':{'':''}}

    custom_notification_box(icon='info', textDisplay='Email has been sent!', externalLink='', url='#', styles=styles, key="foo")


st.subheader("Your recommended travel partners")
for i in st.session_state.partners["match"]:
    st.write(i)

if st.button("Send"):
    send()
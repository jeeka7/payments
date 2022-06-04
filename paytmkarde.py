import streamlit as st

st.write("This is to check payments gateway APIs")

import requests

url = "https://mercury-uat.phonepe.com/v4/debit/"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-CALLBACK-URL": "https://www.demoMerchant.com/callback"
}

response = requests.post(url, headers=headers)

print(response.text)

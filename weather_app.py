#show with streamlit 

import requests , json
import streamlit as st

st.title(" Weather APP")

city_name = st.text_input("enter city name :")

API_key  = "35165323d81e243608acaac53c9d96bb"

# your API key here
api_key = "35165323d81e243608acaac53c9d96bb"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

if st.button("show weather"):
    if city_name:

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name +"&&units=metric"#{get celsius}

        result = requests.get(complete_url)

        json_result = result.json()

        if json_result["cod"] == 200:
            st.success(f"info for = {city_name.upper()} is OK")
            st.write(json_result)

        else:
            st.error("city is not found !")

    else:
        st.warning("please enter city name !")
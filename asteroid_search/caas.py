#!/usr/bin/env python3
"""Clint's Asteroid Approach Search
   Created By: Clint Robertson
   Technologies: Python, Streamlit, Pandas and NASA's Asteroid-NEO API """

import streamlit as st
import requests
import pandas as pd
import math
import config


def main():
    st.title(" Clint's - Asteroid Approach Search")
    st.write("")
    st.write("Have you ever wondered how close we've actually come to being hit by an asteroid?")
    st.write("Well, now you can find these near earth asteroids yourself!")
    st.write("View its name, size, time of closest approach and speed the asteroid is/was traveling.")
    st.write("Also, you can see how many miles it missed the Earth by and if it is potentially hazardous.")
    st.write("---Created using Python, Streamlit, Pandas and NASA's Asteroid-NEO API--")
    final_dictionary = {
        "Name": [],
        "Date and Time": [],
        "Avg Size(mi)": [],
        "Speed(mph)": [],
        "Miss Distance(mi)": [],
        "Pot. HAZ": []
    }

    st.write("")
    st.write("**DATES YOU ENTER MUST BE WITHIN 7 DAYS OF EACH OTHER**")
    START_DATE = st.text_input("Enter Start Date below as YYYY-MM-DD", "")
    END_DATE = st.text_input("Enter End Date below as YYYY-MM-DD", "")
    API_KEY = config.secret_key
    neo_data = requests.get(
        f"https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}").json()

    NEO = neo_data["near_earth_objects"]
    for date, dict_list in NEO.items():
        for asteroid in dict_list:
            name = asteroid["name"]
            size_min = round(float(asteroid["estimated_diameter"]["miles"]["estimated_diameter_min"]), 2)
            size_max = round(float(asteroid["estimated_diameter"]["miles"]["estimated_diameter_max"]), 2)
            avg_size = (size_min + size_max) / 2
            date_and_time = asteroid["close_approach_data"][0]["close_approach_date_full"]
            speed = math.trunc(float(asteroid["close_approach_data"][0]["relative_velocity"]["miles_per_hour"]))
            potentially_hazardous = asteroid["is_potentially_hazardous_asteroid"]
            miss_distance = math.trunc(float(asteroid["close_approach_data"][0]["miss_distance"]["miles"]))

            final_dictionary["Name"].append(name)
            final_dictionary["Date and Time"].append(date_and_time)
            final_dictionary["Avg Size(mi)"].append(avg_size)
            final_dictionary["Speed(mph)"].append(speed)
            final_dictionary["Miss Distance(mi)"].append(miss_distance)

            if potentially_hazardous:
                final_dictionary["Pot. HAZ"].append("Yes")
            else:
                final_dictionary["Pot. HAZ"].append("No")

    st.write(pd.DataFrame(final_dictionary))
    st.write("")
    st.write("**CUSTOM PYTHON DICTIONARY BELOW**")
    st.write("Copy the data for yourself already in a dictionary below...")
    st.write(final_dictionary)
    st.write("")

    if st.button('Click here to say goodbye!'):
        st.write('Hope you enjoyed the app...Come back soon')


if __name__ == '__main__':
    main()


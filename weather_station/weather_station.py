import streamlit as st
import requests
import json
from datetime import datetime

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1&lang=en&m"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            current = data['current_condition'][0]

            temp_c = current['temp_C']
            weather_desc = current['weatherDesc'][0]['value']
            humidity = current['humidity']
            wind_speed = current['windspeedKmph']
            area = data['nearest_area'][0]['areaName'][0]['value']

            return {
                'city': area,
                'temperature': temp_c,
                'condition': weather_desc,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'last_updated': current['observation_time']
            }
        else:
            return None

    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

st.set_page_config(
    page_title="🌤️ Weather Station",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Weather Station")
st.markdown("### Your Personal Weather Dashboard")
st.write("Enter a city name to get the current weather conditions.")

city = st.text_input("📍 City Name:", value="London")

if st.button("🔍 Get Weather"):
    with st.spinner(f"⏳ Fetching weather for {city}..."):
        weather_data = get_weather(city)

    if weather_data is None:
        st.error("❌ Could not fetch weather data. Please check the city name or your internet connection.")
    else:
        st.success(f"✅ Weather data for {weather_data['city']}")

        with st.container():
            col1, col2 = st.columns(2)

            col1.metric("🌡️ Temperature", f"{weather_data['temperature']}°C")
            col1.metric("☁️ Condition", weather_data['condition'])

            col2.metric("💧 Humidity", f"{weather_data['humidity']}%")
            col2.metric("💨 Wind Speed", f"{weather_data['wind_speed']} km/h")

            st.caption(f"🕐 Last updated: {weather_data['last_updated']} UTC")

        temp = float(weather_data['temperature'])

        if temp < 0:
            st.info("🥶 It's freezing! Bundle up!")
        elif temp < 10:
            st.info("🧥 It's chilly. Wear a jacket.")
        elif temp < 20:
            st.info("🌤️ Pleasant weather. Enjoy!")
        elif temp < 30:
            st.info("☀️ Warm and sunny. Stay hydrated!")
        else:
            st.info("🔥 It's hot! Stay cool and drink water.")

st.divider()
st.caption("📊 Data provided by wttr.in (free weather service)")
st.caption("💻 Built with Streamlit")

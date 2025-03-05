import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np



st.title("Taxi Fare Prediction")

# Pickup Date and Time
pickup_date = st.date_input("Pick up Date", value='today')
pickup_time = st.time_input("Pick up Time", value=datetime.now().time())

# Pickup Location
pickup_lat = st.number_input("Pickup Latitude", min_value=-90.0, max_value=90.0, value=40.7128)
pickup_lon = st.number_input("Pickup Longitude", min_value=-180.0, max_value=180.0, value=-74.0060)

# Dropoff Location
dropoff_lat = st.number_input("Dropoff Latitude", min_value=-90.0, max_value=90.0, value=40.7328)
dropoff_lon = st.number_input("Dropoff Longitude", min_value=-180.0, max_value=180.0, value=-73.9970)

# Passenger Count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=2)

# Combine Date and Time
pickup_datetime = datetime.combine(pickup_date, pickup_time)

# Display Inputs for Verification
st.write(f"Pickup Date and Time: {pickup_datetime}")
st.write(f"Pickup Location: Latitude {pickup_lat}, Longitude {pickup_lon}")
st.write(f"Dropoff Location: Latitude {dropoff_lat}, Longitude {dropoff_lon}")
st.write(f"Passenger Count: {passenger_count}")


def predict_fare(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, passenger_count, pickup_datetime):
    url = 'https://taxifare-825878548711.europe-west1.run.app/predict'
    params = {
        "pickup_latitude": pickup_lat,
        "pickup_longitude": pickup_lon,
        "dropoff_latitude": dropoff_lat,
        "dropoff_longitude": dropoff_lon,
        "passenger_count": passenger_count,
        "pickup_datetime": pickup_datetime.strftime('%Y-%m-%d %H:%M:%S')
    }

 # Send GET request to the API
    response = requests.get(url = url, params=params)

    # Handle the API response
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON response
        return data.get('fare', 0)  # Extract fare from response
    else:
        st.write(f"Error: {response.status_code}")
        return None


# Button to submit data
if st.button("Predict Fare"):
    # Call your prediction API here or add the logic to predict the fare
    fare = predict_fare(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, passenger_count, pickup_datetime)

    if fare is not None:
        st.write(f"The predicted fare is: ${fare:.2f}")
    else:
        st.write("Error in fetching the prediction.")




def get_map_data():

    return pd.DataFrame(
            np.random.randn(10, 2) / [50, 50] + [40.7128, -74.0060],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)

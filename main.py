import requests # To make API requests
from datetime import datetime # To work with date and time
import smtplib # To send emails
import time # To add delays in the loop

# Define your latitude and longitude
MY_LAT = 48.135124
MY_LONG = 11.581981

# Define your email credentials
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password" # Use an App Password instead of your real password

def is_iss_overhead():
    """
    Check if the ISS is within a 5-degree range of the user's location.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json") # Get ISS location data
    response.raise_for_status() # Raise an error if the request fails
    data = response.json() # Convert response to JSON format

    # Extract ISS latitude ang longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within a 5-degree range of the user's location
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    """
    Check if it is currently nighttime at the user's location
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # Use UTC time format
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) # Get sunrise/sunset data
    response.raise_for_status() # Raise an error if the request fails
    data = response.json() # Convert response to JSON format

    # Extract sunrise and sunset hours in UTC
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current time in UTC
    time_now = datetime.now().hour

    # Check if the current time is after sunset or before sunrise
    if time_now >= sunset or time_now <= sunrise:
        return True

# Run an infinite loop to check ISS position every 60 seconds
while True:
    time.sleep(60) # Wait for 60 seconds before checking again.
    if is_iss_overhead() and is_night(): # If ISS is overhead and it's nighttime
        connection = smtplib.SMTP("smtp.gmail.com")  # Connect to Gmail's SMTP server
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD) # Log in to the email account
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky." # Send email alert
        )
        connection.close() # Close the connection





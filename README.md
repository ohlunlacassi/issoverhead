# ISS Tracker

## Description
This Python script tracks the International Space Station (ISS) and sends an email notification when the ISS is overhead at your location during nighttime.

## Features
- Fetches real-time ISS location using the Open Notify API.
- Checks local sunrise and sunset times via the Sunrise-Sunset API.
- Sends an email alert when the ISS is overhead and it is nighttime.
- Runs in an infinite loop, checking every 60 seconds.

## Requirements
- Python 3
- Required Python packages:
  - requests
  - smtplib
  - datetime
  - time

## Configuration
- Modify MY_LAT and MY_LONG to set your location.
- Modify my_email and password
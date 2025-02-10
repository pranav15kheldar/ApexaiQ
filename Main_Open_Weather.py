"""Open Weather Api"""

#Import Libries and Module 
import requests
import json


API_KEY = "e7d09741869880f91c2891e5ce03a5f0"
file_name = "Open_Weather.json"
location_file_name = "Location.json"
zip_code = int(input("Enter Zip Code:"))

def location():
    """Fectues Coordinate of Enter Zip code using Open Weather Geocoding API Saves its latitude and Longitude Coordinate in json file"""

     # Decelar Golbal to be access by other functions also
    global lat
    global lon
    
    location_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},IN&appid={API_KEY}"
    location_response = requests.get(location_url)
    print(location_response.json())

    # Save json response 
    location_data = location_response.json()
    # Store json response in json file
    with open(location_file_name , "w") as file:
        json.dump(location_data , file , indent=4)
    
    # Fetch lat and longitude from json file and store in respective variable 
    lat = location_response.json()["lat"]
    lon = location_response.json()["lon"]
    print(lat,lon)
  

def current_weather() :
    """Fetches Current temperature for given coordinates using open weather api """

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.get(url)
    print(response.status_code)
    print(response.json())

    data = response.json()
    # Store Fetch data in json file
    with open(file_name , "w") as file:
        json.dump(data , file , indent=4)


if __name__ == "__main__" :
    location()
    current_weather()
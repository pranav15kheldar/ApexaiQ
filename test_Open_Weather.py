"""Test open weather"""

#Import Libries and Module
import json
import pytest

class TestOpenWeather:
    #open Json file and store data of json file
    with open("Location.json","r") as file:
        location_data = json.load(file)
    
    with open("Open_Weather.json" , "r") as weather_file :
        weather_data = json.load(weather_file)

    def test_key_checks(self):
        assert "lat" in self.location_data is not None
        assert "lon" in self.location_data is not None
        assert "name" in self.location_data is not None
        assert "temp" in self.weather_data["main"] is not None
        assert "lat" in self.weather_data["coord"] is not None
        assert "lon" in self.weather_data["coord"] is not None
    
    def test_key_type(self):
        lat = self.location_data["lat"]
        assert isinstance(lat , (int , float))
        lon = self.location_data["lon"]
        assert isinstance(lon , (int,float))
        temp = self.weather_data["main"]["temp"]
        assert isinstance(temp,(int,float))
        city_name = self.location_data["name"]
        assert isinstance(city_name,(str))
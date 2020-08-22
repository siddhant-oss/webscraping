import requests
import pandas as pd
from bs4 import BeautifulSoup
#Get requests in
page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.Xz6lyGzivIU'
)
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [
    item.find(class_='short-desc').get_text() for item in items
]

weather_stuff = pd.DataFrame({
    'period': period_name,
    'short_description': short_description
})

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
  
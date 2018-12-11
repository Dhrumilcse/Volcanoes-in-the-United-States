#1.0 Import Library
import json
import folium
import pandas as pd

#Load Data
geo_data = json.load(open("us-states.json"))
emp_data = pd.read_csv("us-unemployment.csv")

#Create base map
map = folium.Map(location=[37.0902,-100.7129], zoom_start = 4)

#Method to create Choropleth map, All parameters are mandatory
folium.Choropleth(
    geo_data=geo_data, data=emp_data,
    name = 'Unemployment Rate',
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(map)

#Save the map
map.save("map1.html")

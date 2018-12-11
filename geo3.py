#Import Library
import folium

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8, tiles = "Mapbox bright")

#Add Multiple Marker
for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map1.html")

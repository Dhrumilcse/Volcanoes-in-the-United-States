#Import Library
import folium

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8)

#Save the map
map.save("map1.html")

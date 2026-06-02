import streamlit as st
import folium
import requests
from streamlit_folium import st_folium

st.title("🚑 Emergency Help Locator")

# Default location (you can change)
default_lat = 17.4401
default_lon = 78.3489

lat = st.number_input("Latitude", value=default_lat)
lon = st.number_input("Longitude", value=default_lon)

# Emergency type selection
place_type = st.selectbox(
    "Select Emergency Service",
    ["hospital", "police", "fire_station", "shelter"]
)

# Overpass API query function
def get_places(lat, lon, place):
    query = f"""
    [out:json];
    node
      ["amenity"="{place}"]
      (around:3000,{lat},{lon});
    out;
    """

    url = "https://overpass-api.de/api/interpreter"
    response = requests.get(url, params={'data': query})
    data = response.json()

    places = []
    for element in data["elements"]:
        name = element.get("tags", {}).get("name", "Unknown")
        plat = element["lat"]
        plon = element["lon"]
        places.append((name, plat, plon))

    return places

# Get places
places = get_places(lat, lon, place_type)

# Create map
m = folium.Map(location=[lat, lon], zoom_start=14)

# User marker
folium.Marker(
    [lat, lon],
    tooltip="You are here",
    icon=folium.Icon(color="blue")
).add_to(m)

# Add emergency places
for name, plat, plon in places:
    folium.Marker(
        [plat, plon],
        tooltip=name,
        icon=folium.Icon(color="red")
    ).add_to(m)

st.write(f"Found {len(places)} nearby {place_type}s")

st_folium(m, width=700, height=500)

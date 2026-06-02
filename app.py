```python
import streamlit as st
import pandas as pd

from utils.geocoder import get_coordinates
from utils.emergency_services import get_nearby_services
from utils.routing import get_route
from utils.map_utils import create_map, display_map

st.set_page_config(
    page_title="QuickAid",
    page_icon="🚑",
    layout="wide"
)

st.title("🚑 QuickAid")
st.subheader("Emergency Help Locator")

location = st.text_input(
    "Enter Location",
    placeholder="e.g. Gachibowli, Hyderabad"
)

service_type = st.selectbox(
    "Select Emergency Service",
    ["Hospital", "Police Station", "Fire Station", "Pharmacy"]
)

service_map = {
    "Hospital": "hospital",
    "Police Station": "police",
    "Fire Station": "fire station",
    "Pharmacy": "pharmacy"
}

if st.button("Find Nearby Services"):

    lat, lon = get_coordinates(location)

    if lat is None or lon is None:
        st.error("Location not found.")
        st.stop()

    services = get_nearby_services(
        lat,
        lon,
        service_map[service_type]
    )

    if not services:
        st.warning("No nearby services found.")
        st.stop()

    services = sorted(
        services,
        key=lambda x: x["distance"]
    )

    st.session_state["lat"] = lat
    st.session_state["lon"] = lon
    st.session_state["services"] = services

if "services" in st.session_state:

    st.success(
        f"📍 Your Location: "
        f"{st.session_state['lat']:.5f}, "
        f"{st.session_state['lon']:.5f}"
    )

    st.markdown("## 🏥 Select Service")

    service_names = [
        service["name"]
        for service in st.session_state["services"]
    ]

    selected_name = st.selectbox(
        "Choose Service",
        service_names
    )

    selected_service = next(
        service
        for service in st.session_state["services"]
        if service["name"] == selected_name
    )

    route = get_route(
        st.session_state["lat"],
        st.session_state["lon"],
        selected_service["lat"],
        selected_service["lon"]
    )

    google_maps_url = (
        f"https://www.google.com/maps/dir/"
        f"{st.session_state['lat']},"
        f"{st.session_state['lon']}/"
        f"{selected_service['lat']},"
        f"{selected_service['lon']}"
    )

    st.markdown("## 🏆 Selected Service")

    st.success(
        f"""
🏥 {selected_service['name']}

📍 Distance: {selected_service['distance']} km

⏱ Estimated Time: {route['duration_min']} min
"""
    )

    st.link_button(
        "🗺 Open Directions in Google Maps",
        google_maps_url
    )

    if route:
        st.info(
            f"🚗 Travel Distance: {route['distance_km']} km | "
            f"⏱ Estimated Time: {route['duration_min']} min"
        )

    st.markdown("## 📋 Nearby Services")

    table_data = []

    for service in st.session_state["services"]:

        service_route = get_route(
            st.session_state["lat"],
            st.session_state["lon"],
            service["lat"],
            service["lon"]
        )

        table_data.append({
            "Name": service["name"],
            "Distance (km)": service["distance"],
            "Estimated Time (min)": (
                service_route["duration_min"]
                if service_route else "N/A"
            ),
            "Latitude": round(service["lat"], 5),
            "Longitude": round(service["lon"], 5)
        })

    df = pd.DataFrame(table_data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("## 🗺 Route Map")

    m = create_map(
        st.session_state["lat"],
        st.session_state["lon"],
        services=st.session_state["services"],
        route=route
    )

    display_map(m)
```

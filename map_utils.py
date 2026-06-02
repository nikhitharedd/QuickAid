import folium
from streamlit_folium import st_folium

def create_map(user_lat, user_lon, services=None, route=None):
    """
    Create OpenStreetMap with user location,
    emergency service markers, and route.
    """

    m = folium.Map(
        location=[user_lat, user_lon],
        zoom_start=14
    )

    # User location marker
    folium.Marker(
        [user_lat, user_lon],
        popup="Your Location",
        tooltip="You",
        icon=folium.Icon(color="blue", icon="user")
    ).add_to(m)

    # Emergency service markers
    if services:
        for place in services:
            lat = place.get("lat")
            lon = place.get("lon")
            name = place.get("tags", {}).get("name", "Unknown")

            folium.Marker(
                [lat, lon],
                popup=name,
                tooltip=name,
                icon=folium.Icon(color="red", icon="plus-sign")
            ).add_to(m)

    # Route line
    if route and route.get("coordinates"):
        route_points = [
            [coord[1], coord[0]]
            for coord in route["coordinates"]
        ]

        folium.PolyLine(
            route_points,
            weight=6,
            color="green",
            opacity=0.8
        ).add_to(m)

    return m


def display_map(map_object):
    """
    Display map in Streamlit.
    """
    st_folium(
        map_object,
        width=1000,
        height=600
    )

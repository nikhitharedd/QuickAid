import requests

def get_route(start_lat, start_lon, end_lat, end_lon):
    """
    Get route coordinates between two points using OSRM.
    """

    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};{end_lon},{end_lat}"
        f"?overview=full&geometries=geojson"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["code"] == "Ok":
            route = data["routes"][0]

            return {
                "distance_km": round(route["distance"] / 1000, 2),
                "duration_min": round(route["duration"] / 60, 2),
                "coordinates": route["geometry"]["coordinates"]
            }

    except Exception as e:
        print("Routing Error:", e)

    return None

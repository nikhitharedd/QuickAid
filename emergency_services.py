import requests
from geopy.distance import geodesic

def get_nearby_services(user_lat, user_lon, service):

    url = "https://nominatim.openstreetmap.org/search"

    response = requests.get(
        url,
        params={
            "q": f"{service} near {user_lat},{user_lon}",
            "format": "json",
            "limit": 10
        },
        headers={
            "User-Agent": "QuickAid"
        }
    )

    data = response.json()

    services = []

    for item in data:

        lat = float(item["lat"])
        lon = float(item["lon"])

        distance = round(
            geodesic(
                (user_lat, user_lon),
                (lat, lon)
            ).km,
            2
        )

        services.append({
            "name": item.get("display_name", "Unknown"),
            "lat": lat,
            "lon": lon,
            "distance": distance,
            "phone": item.get("phone", "Not Available")
        })

    services.sort(key=lambda x: x["distance"])

    return services

# 🚑 QuickAid

QuickAid is an Emergency Help Locator built using Streamlit and OpenStreetMap services. It helps users quickly find nearby hospitals, police stations, fire stations, and pharmacies along with route information, distance, and estimated travel time.

---

## Features

* 📍 Location-based emergency service search
* 🏥 Nearby hospitals
* 🚓 Nearby police stations
* 🚒 Nearby fire stations
* 💊 Nearby pharmacies
* 🗺 Interactive route map
* 🚗 Travel distance calculation
* ⏱ Estimated travel time
* 🌍 Google Maps directions
* 📊 Service information displayed in a table

---

## Project Structure

```text
QuickAid/
│
├── app.py
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
├── AGENTS.md
│
├── assets/
│
├── utils/
│   ├── geocoder.py
│   ├── emergency_services.py
│   ├── routing.py
│   ├── map_utils.py
│
├── data/
│
└── docs/
```

---

## Technologies Used

* Python
* Streamlit
* OpenStreetMap (Nominatim)
* OSRM Routing API
* Folium
* Pandas
* Geopy

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/QuickAid.git
cd QuickAid
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Usage

1. Enter a location.
2. Select an emergency service.
3. Click **Find Nearby Services**.
4. Choose a service from the list.
5. View:

   * Distance
   * Travel Time
   * Route Map
   * Google Maps Directions

---

## Configuration

No API keys are currently required.

QuickAid uses:

* OpenStreetMap Nominatim
* OSRM Routing Service

Both services are publicly available.

---

## Future Enhancements

* Live GPS Location
* Emergency Contact Integration
* Ambulance Tracking
* AI Emergency Assistant
* Multi-language Support
* Real-time Traffic Analysis

---

## Documentation

Additional documentation:

* CONTRIBUTING.md
* USER_MANUAL.md
* AGENTS.md

---

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

---

## Author

Nikhitha Reddy

B.Tech Student | Python Developer | Open Source Contributor

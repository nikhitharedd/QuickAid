# AGENTS.md

## Project Name

QuickAid – Emergency Help Locator

## Purpose

QuickAid helps users quickly locate nearby emergency services and obtain route guidance.

## Main Components

### app.py

Main Streamlit application.

### utils/geocoder.py

Converts location names into coordinates.

### utils/emergency_services.py

Fetches nearby emergency services.

### utils/routing.py

Calculates route distance and estimated travel time.

### utils/map_utils.py

Generates and displays interactive maps.

## Technology Stack

* Python
* Streamlit
* Folium
* Geopy
* OpenStreetMap
* OSRM Routing API

## Development Guidelines

* Keep modules independent.
* Follow Python coding standards.
* Document important functions.
* Test changes before deployment.

## Future Enhancements

* Live location tracking
* AI-powered emergency assistant
* Ambulance tracking
* Real-time traffic analysis
* Multi-language support

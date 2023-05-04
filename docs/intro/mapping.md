(intro/mapping)=
# Mapping

Get to know how geospatial data is captured and used in Fieldmark

## Data Capture

Fieldmark can capture geospatial data in two ways:

1. A single point
2. A bounding box drawn on a map

Data are stored in [geojson](https://geojson.org/) format, and can be expressed as longitude and latitude.

### Device limitations

Fieldmark collects the geospatial data captured by the device and will be as accurate as that device allows. While most tablets offer sufficient accuracy in online settings, many have error ranges of 20m or more which may not be satisfactory for many projects.

We recommend using an external Bluetooth device.
     
## Basemaps

By default, Fieldmark will display a base map sourced from [OpenStreetMap](https://www.openstreetmap.org/) for any map field. (You must connect to the internet before going offline to see the map.)

Functionality to display custom geotiffs is currently in beta testing.  

## Export

Geospatial data will be exported in .kml and .geojson formats.

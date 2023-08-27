# GeoJSON to IMDF Converter

This repository contains a script to convert standard GeoJSON files into Apple's Indoor Mapping Data Format (IMDF) compatible ones with some automation.

## Overview

The Indoor Mapping Data Format (IMDF) is an open standard developed by Apple for indoor location services. It provides a way to describe indoor maps, including geometry, topology, and metadata. This script converts standard GeoJSON files into Apple's IMDF compatible ones. It initializes dictionaries with predefined values for different structures like address, amenity, anchor, building, etc., and then iterates through the GeoJSON features to convert them into the IMDF compatible format. It also generates a UUID for each feature.

## How to Use

1. Clone this repository.
2. Run the `geojson_2_imdf_structs.ipynb` Jupyter Notebook.
3. Modify the script to include your GeoJSON file and run the notebook.

## Requirements

- Python 3
- Jupyter Notebook
- UUID library

## License

This project is licensed under the MIT License.

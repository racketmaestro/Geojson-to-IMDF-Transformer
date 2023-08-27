# GeoJSON to IMDF Converter

This repository contains a script that streamlines the standard GeoJSON files into Apple's Indoor Mapping Data Format (IMDF) compatible ones. You may read up about the IMDF in Apple's official documentation. Other third party softwares sell their service of converting floorplans to IMDF at a premium, but IMDF is essentially just a set of geojson files. You will need to use any Geojson tool (I used QGIS) to draw the geometry and georeference the shapes, and then simply run this script to transform them! Afterwards you may use Apple's IMDF sandbox to do labelling, testing and debugging to create your indoor map.

## Overview

The Indoor Mapping Data Format (IMDF) is an open standard developed by Apple for indoor location services. It provides a way to describe indoor maps, including geometry, topology, and metadata. This script converts standard GeoJSON files into Apple's IMDF compatible ones. It initializes dictionaries with predefined values for different structures like address, amenity, anchor, building, etc., and then iterates through the GeoJSON features to convert them into the IMDF compatible format. It also generates a UUID for each feature.

## How to Use

1. Clone this repository.
2. Put your Geojson files into the folder
3. Run the `geojson_2_imdf_structs.ipynb` Jupyter Notebook to process and transform the Geojsons
4. Modify the script to include your GeoJSON file and run the notebook.

## Requirements

- Python 3
- Jupyter Notebook
- UUID library

## Future Improvements

Right now the automation of mapping and referencing of IDs (eg referencing unit_ids in anchor features) is limited to features on the same floor. One would have to run the script once for each level's units, anchors, occupants, etc, and subsequently combine all features into a final geojson file.
## Overview

The Indoor Mapping Data Format (IMDF) is an open standard developed by Apple for indoor location services. It provides a way to describe indoor maps, including geometry, topology, and metadata. Other third party softwares sell their service of converting floorplans to IMDF at a premium, but IMDF can be created with abit of diligence and some automation to make life easier.

# GeoJSON to IMDF Conversion Tool Repository

This repository offers a streamlined tool for converting GeoJSON files into Apple's Indoor Mapping Data Format (IMDF) compliant format. Detailed insights about IMDF can be explored in Apple's [official documentation](https://register.apple.com/resources/indoor/program/).

## Process Overview

1. **Initial Preparation:** 
    - Utilize any GeoJSON tool, such as QGIS, to draft the geometry and georeference indoor map features. 
    - Only geojson files with non-null geometry need to be crafted and imported into this project.
  
2. **Script Execution:** 
    - Once the geojsons are ready, execute this script for transformation.
  
3. **Outputted GeoJSONs:** 
    - The resultant geojson files encompass address, amenity, anchor, building, footprint, level, occupant, opening, unit, and venue to a Transformed_Geojson folder.
    - While there are additional potential geojsons for the IMDF set, they aren't deemed essential.
  
4. **Refinement with Apple's IMDF Sandbox:** 
    - Apple's IMDF sandbox offers a graphical interface for refining, labeling, testing, and debugging your indoor map. 
    - It's paramount that the IMDF Sandbox reflects zero errors before the submission to Apple for geo-referencing or for rendering within Apple's [sample project](https://developer.apple.com/documentation/mapkit/mapkit_for_appkit_and_uikit/displaying_an_indoor_map). Sample Final IMDFs with 0 errors can be found in Final_IMDF folder.

## Further Reading
For a comprehensive understanding of IMDF, refer to the [IMDF Documentation](https://docs.ogc.org/cs/20-094/index.html).


## How to Use

1. Clone this repository.
2. Put your Geojson files into the folder
3. Run the `geojson_2_imdf_structs.ipynb` Jupyter Notebook to process and transform the Geojsons
4. Modify the file paths run the notebook.

## Requirements

- Python 3
- Jupyter Notebook
- UUID library

## Key components of the script
- Initialize dictionaries with keys and values tailored for IMDF Geojson structures (reference point). Pre-defined values may be declared here.
- Iterate through each feature in 'features' array for each QGIS Geojsons. Transform the feature with the established reference and append it to the respective dictionary's 'features' array.
- Generate UUID for each feature
- Reference building_ids, address_id and level_id for applicable features
- Use Ray-Casting algorithm (2D) to determine which unit each anchor and amenity feature resides in, and map the them to the corresponding unit_id
- Compute the centre of unit features polygons, and set them as the display point (code was commented out as it was not crucial)
- Compute the centre of opening features lines and set them as the display point
- Generate occupant geojson by creating an occupant for each anchor feature and referencing them in anchor_id.
- Save the dictionaries as geojsons.

## Limitations

In an IMDF structure, geometries coordinates consist of only longitude and latitude, but not altitude. The script is unable to automatically reference level_id in each unit feature, and unit_id in each anchor and amenity feature.

Consequently, one would have to run the script once for each level's units, anchors, occupants, etc, and subsequently combine all features into a final geojson file. Hence why a separate script was created for easier discernment, and QGIS geojsons are labelled according to which level they correspond to (see CPC4_QGIS_Geojsons).  A word of caution: re-running scripts more than necessary will rewrite the UUID of every feature each iteration, which will cause conflict when referencing IDs for buildings, address, and levels.

## Future Improvements
- Automate the combination of features from different geojsons for each level into one master geojson file. 
- To avoid having to run the script once for each level and its components, innovate a mechanism to accurately identify the level of the features for referencing.


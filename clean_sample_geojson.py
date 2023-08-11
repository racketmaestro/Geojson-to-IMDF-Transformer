import os
import json

def clean_geojson_structure(data):
    """Recursively clean the data structure to create a reference format."""
    if isinstance(data, dict):
        # If the key is 'coordinates', ensure the value is an empty array
        if "coordinates" in data.keys():
            data["coordinates"] = []
        return {key: clean_geojson_structure(value) for key, value in data.items()}
    elif isinstance(data, list):
        # If the list contains dictionaries or other lists, process them
        # But retain only the first item in the "features" array
        if len(data) > 0 and isinstance(data[0], dict) and "type" in data[0] and data[0]["type"] == "Feature":
            return [clean_geojson_structure(data[0])]
        else:
            return []
    elif isinstance(data, (str, int, float)):
        return ""
    else:
        return data  # This will retain values like 'null'

def clean_geojson_file(file_path, output_dir):
    """Clean a GeoJSON file and save the cleaned data to a new file."""
    with open(file_path, "r") as file:
        data = json.load(file)
    cleaned_data = clean_geojson_structure(data)
    base_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    cleaned_file_path = os.path.join(output_dir, f"{file_name_without_ext}_cleaned.geojson")
    with open(cleaned_file_path, "w") as file:
        json.dump(cleaned_data, file, indent=4)
    return cleaned_file_path

def main():
    input_dir = "C:\\Users\\amosk\\GitHub\\Geojson_2_IMDF_Transformer\\IMDF_Geojson_Correct Format"
    output_dir = "C:\\Users\\amosk\\GitHub\\Geojson_2_IMDF_Transformer\\IMDF_Geojson_Cleaned_Sample"
    geojson_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".geojson")]
    for file_path in geojson_files:
        cleaned_file_path = clean_geojson_file(file_path, output_dir)
        print(f"Cleaned {file_path} -> {cleaned_file_path}")

if __name__ == "__main__":
    main()

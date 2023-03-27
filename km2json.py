import kml2geojson
import os

def convert(source_path: str, destination_path: str) -> bool:
    try:
        if (os.path.isdir(destination_path) and os.path.isfile(source_path) and os.path.splitext(source_path)[1] == ".json"):
            kml2geojson.main.convert(source_path, destination_path)
            return True
        print("Something wrong with paths")
        return False
    except Exception as e:
        print(e)
        return False


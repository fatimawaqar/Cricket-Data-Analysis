import json
import os

# Project root ka path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# raw_data folder ka exact path
raw_data_path = os.path.join(BASE_DIR, "data", "raw_data")

print("Raw data path:", raw_data_path)

# raw_data ke andar files list karo
json_files = os.listdir(raw_data_path)

print("Total JSON files:", len(json_files))
print("First file name:", json_files[0])

# pehli JSON file open karo
file_path = os.path.join(raw_data_path, json_files[0])

with open(file_path, "r", encoding="utf-8") as f:
    match_data = json.load(f)

print("Keys in JSON file:")
print(match_data.keys())

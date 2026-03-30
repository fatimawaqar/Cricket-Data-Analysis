import json
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(BASE_DIR, "data", "raw_data")

json_files = os.listdir(raw_data_path)

matches = []
skipped_files = 0

for file in json_files:
    # ✅ sirf .json files lo
    if not file.endswith(".json"):
        continue

    file_path = os.path.join(raw_data_path, file)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        info = data.get("info", {})

        match_record = {
            "match_id": file.replace(".json", ""),
            "date": info.get("dates", [None])[0],
            "venue": info.get("venue"),
            "match_type": info.get("match_type"),
            "team_1": info.get("teams", [None, None])[0],
            "team_2": info.get("teams", [None, None])[1]
        }

        matches.append(match_record)

    except Exception as e:
        skipped_files += 1
        print(f"⚠️ Skipped file: {file}")

df = pd.DataFrame(matches)

output_path = os.path.join(BASE_DIR, "data", "cleaned_data", "match_info.csv")
df.to_csv(output_path, index=False)

print("✅ match_info.csv created successfully")
print("Total matches:", len(df))
print("Skipped files:", skipped_files)

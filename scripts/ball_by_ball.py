import json
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(BASE_DIR, "data", "raw_data")

json_files = os.listdir(raw_data_path)

deliveries_list = []
skipped_files = 0

for file in json_files:
    if not file.endswith(".json"):
        continue

    file_path = os.path.join(raw_data_path, file)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        innings = data.get("innings", [])

        for inning_index, inning in enumerate(innings, start=1):
            overs = inning.get("overs", [])

            for over in overs:
                over_number = over.get("over")
                deliveries = over.get("deliveries", [])

                for ball_number, delivery in enumerate(deliveries, start=1):
                    deliveries_list.append({
                        "match_id": file.replace(".json", ""),
                        "inning": inning_index,
                        "over": over_number,
                        "ball": ball_number,
                        "batter": delivery.get("batter"),
                        "bowler": delivery.get("bowler"),
                        "non_striker": delivery.get("non_striker"),
                        "runs_batter": delivery.get("runs", {}).get("batter", 0),
                        "runs_extras": delivery.get("runs", {}).get("extras", 0),
                        "runs_total": delivery.get("runs", {}).get("total", 0)
                    })

    except Exception as e:
        skipped_files += 1
        print(f"⚠️ Skipped file: {file}")

df = pd.DataFrame(deliveries_list)

output_path = os.path.join(BASE_DIR, "data", "cleaned_data", "ball_by_ball.csv")
df.to_csv(output_path, index=False)

print("✅ ball_by_ball.csv created successfully")
print("Total balls:", len(df))
print("Skipped files:", skipped_files)

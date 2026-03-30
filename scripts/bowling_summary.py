import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ball-by-ball data load
ball_by_ball_path = os.path.join(BASE_DIR, "data", "cleaned_data", "ball_by_ball.csv")
df = pd.read_csv(ball_by_ball_path)

# Bowling aggregation
bowling_summary = df.groupby("bowler").agg(
    balls=("ball", "count"),
    runs_conceded=("runs_total", "sum")
).reset_index()
# Overs & economy
bowling_summary["overs"] = bowling_summary["balls"] / 6
bowling_summary["economy"] = bowling_summary["runs_conceded"] / bowling_summary["overs"]

# CSV save
output_path = os.path.join(BASE_DIR, "data", "cleaned_data", "bowling_summary.csv")
bowling_summary.to_csv(output_path, index=False)

print("✅ bowling_summary.csv created successfully")
print(bowling_summary.head())

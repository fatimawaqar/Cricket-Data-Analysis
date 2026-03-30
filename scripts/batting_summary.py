import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ball-by-ball CSV load karo
ball_by_ball_path = os.path.join(BASE_DIR, "data", "cleaned_data", "ball_by_ball.csv")
df = pd.read_csv(ball_by_ball_path)

# Sirf valid batting balls lo
batting_df = df[df["batter"].notna()]

# Batting aggregation
batting_summary = batting_df.groupby("batter").agg(
    runs=("runs_batter", "sum"),
    balls=("ball", "count")
).reset_index()

# Strike rate calculate karo
batting_summary["strike_rate"] = (batting_summary["runs"] / batting_summary["balls"]) * 100

# CSV save 
output_path = os.path.join(BASE_DIR, "data", "cleaned_data", "batting_summary.csv")
batting_summary.to_csv(output_path, index=False)

print("✅ batting_summary.csv created successfully")
print(batting_summary.head())

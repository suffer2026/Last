import pandas as pd

# Dataset URL
url = "https://data.opencity.in/dataset/e57cd149-fd78-4853-80b8-47d3d082845e/resource/7a654494-2597-4405-8eb4-f0db760f1c1b/download/291ea394-8201-4064-8b8b-9de612edb1c0.csv"

# Read dataset
df = pd.read_csv(url)

# Clean column names
df = df.rename(columns=lambda x: x.strip().lower())

# Convert columns to proper datatype
df['date'] = pd.to_datetime(df['date'], errors='coerce')

df['temp max'] = pd.to_numeric(
    df['temp max'],
    errors='coerce'
)

df['temp min'] = pd.to_numeric(
    df['temp min'],
    errors='coerce'
)

# Remove missing values
df = df.dropna()

# Keep required columns
clean_df = df[['date', 'temp max', 'temp min']]

# Save cleaned file
clean_df.to_csv("clean_weather.csv", index=False)

print("Cleaned data saved to clean_weather.csv")
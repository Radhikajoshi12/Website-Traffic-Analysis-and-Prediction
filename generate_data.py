import pandas as pd
import numpy as np

# Generate timestamps for every minute
time = pd.date_range(start="2024-01-01", periods=500, freq="min")

# Normal traffic (random between 100-200 users)
traffic = np.random.randint(100, 200, size=500)

# Add spikes every 120 minutes
for i in range(100, 500, 120):
    traffic[i:i+5] = np.random.randint(500, 800)

# Create DataFrame
df = pd.DataFrame({
    "timestamp": time,
    "traffic": traffic
})

# Save as CSV
df.to_csv("traffic_data.csv", index=False)
print("traffic_data.csv created!")

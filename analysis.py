import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("traffic_data.csv", parse_dates=["timestamp"])

# Plot traffic over time
plt.figure(figsize=(12,5))
plt.plot(df["timestamp"], df["traffic"], label="Traffic")
plt.title("Website Traffic Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Users")
plt.legend()
plt.show()

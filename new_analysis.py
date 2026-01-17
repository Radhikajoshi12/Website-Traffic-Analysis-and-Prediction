import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("traffic_data.csv", parse_dates=["timestamp"])

# Calculate mean and standard deviation
mean_traffic = df["traffic"].mean()
std_traffic = df["traffic"].std()

# Define spikes
spike_threshold = mean_traffic + 2 * std_traffic
df["is_spike"] = df["traffic"] > spike_threshold

# Plot traffic with spikes highlighted
plt.figure(figsize=(12,5))
plt.plot(df["timestamp"], df["traffic"], label="Traffic")
plt.scatter(df["timestamp"][df["is_spike"]],
            df["traffic"][df["is_spike"]],
            color='red', label="Spike")
plt.title("Website Traffic with Spikes Highlighted")
plt.xlabel("Time")
plt.ylabel("Number of Users")
plt.legend()
plt.show()

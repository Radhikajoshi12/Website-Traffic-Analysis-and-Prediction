import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1️⃣ Load dataset
df = pd.read_csv("traffic_data.csv", parse_dates=["timestamp"])

# 2️⃣ Detect spikes in historical data
mean_traffic = df["traffic"].mean()
std_traffic = df["traffic"].std()
spike_threshold = mean_traffic + 2 * std_traffic
df["is_spike"] = df["traffic"] > spike_threshold

# 3️⃣ Prepare data for ML prediction
df["traffic_prev"] = df["traffic"].shift(1)
df.dropna(inplace=True)  # remove first row with NaN

X = df[["traffic_prev"]]
y = df["traffic"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 5️⃣ Predict future traffic
df["predicted_traffic"] = model.predict(df[["traffic_prev"]])

# 6️⃣ Check accuracy
mae = mean_absolute_error(y, df["predicted_traffic"])
print(f"Mean Absolute Error: {mae:.2f}")

# 7️⃣ Detect predicted spikes
df["predicted_spike"] = df["predicted_traffic"] > spike_threshold

# 8️⃣ Plot actual vs predicted traffic
plt.figure(figsize=(12,5))
plt.plot(df["timestamp"], df["traffic"], label="Actual Traffic")
plt.plot(df["timestamp"], df["predicted_traffic"], label="Predicted Traffic", alpha=0.7)
plt.scatter(df["timestamp"][df["predicted_spike"]],
            df["predicted_traffic"][df["predicted_spike"]],
            color='orange', label="Predicted Spike")
plt.title("Traffic Prediction with Predicted Spikes")
plt.xlabel("Time")
plt.ylabel("Number of Users")
plt.legend()
plt.show()

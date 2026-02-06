import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# STEP 2: Load the dataset
# ----------------------------
data = pd.read_csv("startup_costs.csv")
print(data)

# ----------------------------
# STEP 3: Burn rate calculation
# ----------------------------
average_burn = data["total_cost"].mean()
max_burn = data["total_cost"].max()
max_burn_month = data.loc[data["total_cost"].idxmax(), "month"]

print("\n--- Burn Rate Summary ---")
print(f"Average monthly burn rate: ${average_burn:.2f}")
print(f"Highest burn was ${max_burn} in {max_burn_month}")

# ----------------------------
# STEP 4: Cost trend visualization
# (TEMPORARILY DISABLED to avoid IDLE restart issues)
# ----------------------------
plt.figure()
plt.plot(data["month"], data["total_cost"])
plt.xlabel("Month")
plt.ylabel("Total Cost")
plt.title("Startup Monthly Burn Rate Trend")
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()   # <- keep commented for now

# ----------------------------
# STEP 5: Anomaly detection
# ----------------------------
mean_cost = data["total_cost"].mean()
std_cost = data["total_cost"].std()

threshold = mean_cost + 2 * std_cost

data["is_anomaly"] = data["total_cost"] > threshold
anomalies = data[data["is_anomaly"]]

print("\n--- Anomaly Detection ---")
print(f"Anomaly threshold: ${threshold:.2f}")

if anomalies.empty:
    print("No cost anomalies detected.")
else:
    print("Cost anomalies detected:")
    print(anomalies[["month", "total_cost"]])

# ----------------------------
# STEP 6: AI explanations
# ----------------------------
print("\n--- AI Explanations ---")

for index, row in anomalies.iterrows():
    anomaly_month = row["month"]
    anomaly_cost = row["total_cost"]

    previous_data = data.loc[:index - 1].tail(3)

    if len(previous_data) == 0:
        print(f"Not enough historical data to explain anomaly in {anomaly_month}.")
        continue

    previous_avg = previous_data["total_cost"].mean()
    percent_increase = ((anomaly_cost - previous_avg) / previous_avg) * 100

    print(
        f"In {anomaly_month}, total costs increased by "
        f"{percent_increase:.1f}% compared to the previous 3-month average."
    )

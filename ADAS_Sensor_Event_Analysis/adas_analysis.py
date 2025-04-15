import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset
adas_df = pd.read_csv("C:/Users/ASUS/Documents/vscode/ADAS_Sensor_Event_Analysis/ADAS_Triage_Mock_Data.csv")


# 3. Basic Overview
print(adas_df.head())
print(adas_df.describe())
print(adas_df.info())

# 4. Exploratory Data Analysis (EDA)
sns.set(style="whitegrid")

# Speed Distribution
plt.figure(figsize=(10, 5))
sns.histplot(adas_df['Speed_kmph'], bins=30, kde=True, color='blue')
plt.title('Speed Distribution')
plt.xlabel('Speed (km/h)')
plt.ylabel('Frequency')
plt.show()

# Obstacle Distance vs Brake Signal
np.random.seed(42)
adas_df['Obstacle_Distance_m'] = np.random.normal(loc=20, scale=5, size=len(adas_df))

plt.figure(figsize=(10, 5))
sns.boxplot(x='Brake_Applied', y='Obstacle_Distance_m', data=adas_df)
plt.title('Obstacle Distance vs Brake Applied')
plt.xlabel('Brake Applied')
plt.ylabel('Obstacle Distance (m)')
plt.show()

# Brake vs VRU Detection
vrus = adas_df.groupby(['VRU_Detected', 'Brake_Applied']).size().unstack()
vrus.plot(kind='bar', stacked=True)
plt.title('Brake Behavior When VRU Detected')
plt.xlabel('VRU Detected')
plt.ylabel('Count')
plt.show()

# 5. Insight: Potential Missed Braking Events
missed_brakes = adas_df[(adas_df['VRU_Detected'] == 1) & (adas_df['Brake_Applied'] == 0)]
print(f"\nNumber of times VRU was detected but brakes were not applied: {len(missed_brakes)}")

# 6. Sensor Confidence Analysis
np.random.seed(42)
adas_df['Sensor_Confidence'] = np.random.uniform(0.6, 1.0, size=len(adas_df))
plt.figure(figsize=(10, 5))
sns.histplot(adas_df['Sensor_Confidence'], bins=20, kde=True, color='green')
plt.title('Sensor Detection Confidence')
plt.xlabel('Confidence Score')
plt.ylabel('Frequency')
plt.show()

# 7. Save Processed Data for Dashboarding or Further Analysis
adas_df.to_csv("processed_adas_data.csv", index=False)

print("\nAnalysis complete. Processed file saved as 'processed_adas_data.csv'")



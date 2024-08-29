import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
file_path = "C:/Users/SHIVANSH/Desktop/Data capture/5/gyroscope_data.csv"
df = pd.read_csv(file_path, nrows=1000)  # Load only the first 1000 rows
df.dropna(inplace=True)

# Ensure all data is numeric, remove any non-numeric rows
df = df[pd.to_numeric(df['x'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['y'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['z'], errors='coerce').notnull()]

# Convert x, y, z columns to numeric types
df['x'] = pd.to_numeric(df['x'])
df['y'] = pd.to_numeric(df['y'])
df['z'] = pd.to_numeric(df['z'])

# Save cleaned data to a new CSV file
cleaned_file_path = 'C:/Users/SHIVANSH/Desktop/Data capture/5/cleaned_gyroscope_data.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
df.dropna(inplace=True)

# Ensure all data is numeric, remove any non-numeric rows
df = df[pd.to_numeric(df['x'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['y'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['z'], errors='coerce').notnull()]

# Convert x, y, z columns to numeric types
df['x'] = pd.to_numeric(df['x'])
df['y'] = pd.to_numeric(df['y'])
df['z'] = pd.to_numeric(df['z'])

# Save cleaned data to a new CSV file
cleaned_file_path = "C:/Users/SHIVANSH/Desktop/Data capture/5/cleaned_gyroscope_data.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")

# Step 3: Plot the data

# Plot x, y, z separately
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(df['timestamp'], df['x'], color='r')
plt.title('X-Axis Gyroscope Readings')
plt.xlabel('Timestamp')
plt.ylabel('X')

plt.subplot(3, 1, 2)
plt.plot(df['timestamp'], df['y'], color='g')
plt.title('Y-Axis Gyroscope Readings')
plt.xlabel('Timestamp')
plt.ylabel('Y')

plt.subplot(3, 1, 3)
plt.plot(df['timestamp'], df['z'], color='b')
plt.title('Z-Axis Gyroscope Readings')
plt.xlabel('Timestamp')
plt.ylabel('Z')

plt.tight_layout()
plt.show()

# Combined plot for x, y, z
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['x'], label='X', color='r')
plt.plot(df['timestamp'], df['y'], label='Y', color='g')
plt.plot(df['timestamp'], df['z'], label='Z', color='b')
plt.title('Combined Gyroscope Readings')
plt.xlabel('Timestamp')
plt.ylabel('Gyroscope Reading')
plt.legend()
plt.show()
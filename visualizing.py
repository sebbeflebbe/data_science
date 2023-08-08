import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

viz = pd.read_csv('cleaned_data.csv')
df = pd.DataFrame(viz)

# Increase figure size for better visibility
plt.figure(figsize=(15, 10))

plt.plot(df['date'], df['value'], marker='o', linestyle='-', color='b')
plt.title('Trend in Value Fluctuation')
plt.xlabel('date')
plt.ylabel('value')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45, fontsize=10)

# Show every nth date label to reduce overlap
n = 20  # Adjust this value based on your data density
visible_dates = df['date'].iloc[::n]
plt.xticks(visible_dates)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # Adjust layout for better spacing
plt.show()

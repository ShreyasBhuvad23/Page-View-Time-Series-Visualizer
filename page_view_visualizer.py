import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('page_views.csv', parse_dates=['date'])

# Preview data
print(df.head())

# Plot time series
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['views'], marker='o', linestyle='-')
plt.title('Page Views Over Time')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.grid(True)
plt.tight_layout()
plt.show()
import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Database connection parameters
db_config = {
    'host': 'Draunzer',
    'user': 'root',
    'password': '12345',
    'database': 'network_usage'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Fetch all data from the network_usage table
query = '''
    SELECT timestamp, usage_value
    FROM network_usage
'''
cursor.execute(query)
data = cursor.fetchall()

# Close the database connection
connection.close()

# Unpack the data into separate lists for timestamp and usage_value
timestamps, usage_values = zip(*data)

# Convert timestamps to datetime objects
timestamps = [datetime.strptime(str(ts), '%Y-%m-%d %H:%M:%S') for ts in timestamps]

# Extract hours, minutes, and seconds for the x-axis
time_labels = [ts.strftime('%H:%M:%S') for ts in timestamps]

# Plot the data with a time interval of 20 minutes
plt.plot(time_labels, usage_values, marker='o', linestyle='-', markersize=4)
plt.xlabel('Time (hours:minutes:seconds)')
plt.ylabel('Network Usage Value')
plt.title('Network Usage Over Time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()

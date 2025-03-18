import matplotlib.pyplot as plt

# Read the trigger times from the file
trigger_times = []
with open('trigger_times.txt', 'r') as f:
    for line in f:
        trigger_times.append(float(line.strip()))

# Generate a time axis (for demonstration, assume the experiment starts at time = 0)
# The trigger times will be plotted as vertical lines at their respective time points.
plt.figure(figsize=(10, 6))
plt.eventplot(trigger_times, orientation='horizontal', color='r', linewidth=2)

# Adding labels and title
plt.xlabel('Time (seconds)', fontsize=12)
plt.title('Trigger Events vs Time', fontsize=14)
plt.yticks([])  # Remove y-axis ticks since it's just a timeline
plt.grid(True)

# Show the plot
plt.show()


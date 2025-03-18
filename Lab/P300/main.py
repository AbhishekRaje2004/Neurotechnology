import random
import logging
from psychopy import visual, core, event
from visual_stimulus import create_stimulus, send_trigger
import time

# Create the window for displaying the chessboard
win = visual.Window([800, 600], color='black', units='pix', monitor='testMonitor')  # Use testMonitor to avoid warning

# List to store trigger times (to plot later)
trigger_times = []

# Set up the sequence of stimuli (non-targets and targets)
sequence = []
num_trials = 100  # Total number of trials

# Generate the sequence of stimuli
for i in range(num_trials):
    if random.random() < 0.2:  # Present target every 20% of the time (adjustable)
        sequence.append(('target', create_stimulus(win, flip=True)))  # Target (flipped chessboard)
    else:
        sequence.append(('non-target', create_stimulus(win, flip=False)))  # Non-target (standard chessboard)

# Initialize logging (optional)
logging.basicConfig(level=logging.INFO)

# Present stimuli
for trial_type, stimulus in sequence:
    stimulus.draw()  # Draw the stimulus (chessboard pattern)
    win.flip()  # Display the stimulus

    # Send trigger if the stimulus is a target
    if trial_type == 'target':
        trigger_time = time.time()  # Record the time when the trigger is sent
        trigger_times.append(trigger_time)  # Log the time
        print(f"Trigger sent at: {trigger_time}")  # Debugging print to ensure time is recorded
        send_trigger(1)  # Trigger code 1 for target (flip) stimulus
    
    # Wait for a brief moment (1 second or as needed)
    core.wait(1)  # You can adjust this depending on your experiment timing

    # Listen for exit key (e.g., Escape) to terminate the experiment early
    if event.getKeys(keyList=['escape']):
        break

# Close the window after the experiment
win.close()

# Debugging: Check if trigger times are logged
print(f"Total trigger times recorded: {len(trigger_times)}")  # Print the length of the trigger times list

# Write the trigger times to a file with an absolute path
file_path = 'trigger_times.txt'  # Change this path if necessary
print(f"Attempting to write to {file_path}...")

try:
    if trigger_times:  # Check if there are trigger times
        with open(file_path, 'w') as f:
            for time_point in trigger_times:
                f.write(f"{time_point}\n")
        print(f"Successfully wrote {len(trigger_times)} trigger times to {file_path}")
    else:
        print("No trigger times to write to the file.")
except Exception as e:
    print(f"Error writing to file: {e}")
core.quit()

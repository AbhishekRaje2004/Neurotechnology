import random
from psychopy import visual, core, event
from stimulus import create_stimulus, send_trigger

# Create the window for displaying the chessboard
win = visual.Window([800, 600], color='black', units='pix')

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
        send_trigger(1)  # Trigger code 1 for target (flip) stimulus
    
    # Wait for a brief moment (1 second or as needed)
    core.wait(1)  # You can adjust this depending on your experiment timing

    # Listen for exit key (e.g., Escape) to terminate the experiment early
    if event.getKeys(keyList=['escape']):
        break

# Close the window after the experiment
win.close()
core.quit()


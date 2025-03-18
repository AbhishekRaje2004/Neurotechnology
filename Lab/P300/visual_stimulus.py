import numpy as np
from psychopy import visual

# Function to create a chessboard pattern (8x8 grid)
def create_chessboard(flip=False):
    # Create a chessboard grid of black and white squares (8x8)
    board = np.zeros((8, 8))
    board[1::2, ::2] = 1  # Black squares at odd positions
    board[::2, 1::2] = 1  # Black squares at even positions

    if flip:
        # Flip the chessboard by inverting colors (flip the 1s and 0s)
        board = 1 - board
    return board

# Function to send a trigger signal to EEG system (this could be over parallel port or USB trigger)
def send_trigger(trigger_code):
    """
    Send trigger to EEG system. 
    This is a placeholder function and should be implemented according to your EEG system.
    """
    # Here you would implement the code to send a trigger to the EEG system.
    # Example for parallel port (if using the parallel port):
    # port.write(trigger_code)  # this sends the trigger code to the EEG system
    print(f"Trigger sent: {trigger_code}")
    # You can also use a USB trigger or other method to send signals to your EEG system.

# Function to create the stimulus object for chessboards
def create_stimulus(win, flip=False):
    """
    Create and return a visual stimulus object for the chessboard.
    flip: Boolean to determine if the chessboard is flipped (target) or standard (non-target).
    """
    chessboard_image = create_chessboard(flip)
    return visual.ImageStim(win, image=chessboard_image, pos=(0, 0), size=(300, 300))


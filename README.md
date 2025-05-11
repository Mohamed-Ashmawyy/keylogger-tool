# Simple Python Keylogger

This is a very basic keylogger written in Python. It records what keys you press and saves them into a text file called `keylog.txt`.

## What it does

- It listens to your keyboard in the background.
- Every key you press gets saved to a temporary list.
- Every 5 seconds, the program writes those keys into a file.
- You can stop the program any time by pressing the `ESC` key.

## Requirements

To run this keylogger, you need to have:

- Python 3 installed on your system.
- The `pynput` library installed. If you don’t have it, you can install it by >>
- open new terminal >> do this command:
- pip install pynput

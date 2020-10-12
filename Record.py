import keyboard
import pickle
from pynput import mouse
from pynput.keyboard import Key, Listener

name_file = input("Write a macro name: ")
print("""

█▀█ █▀█ █▀▀ █▀ █▀   █▀ █ █ █ █▀▀ ▀█▀   ▀█▀ █▀█   █▀ ▀█▀ ▄▀█ █▀█ ▀█▀	
█▀▀ █▀▄ ██▄ ▄█ ▄█   ▄█ █▀█ █ █▀   █     █  █▄█   ▄█  █  █▀█ █▀▄  █  


█▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █▄ █ █▀▄   ▀█▀ █▀█   █▀ ▀█▀ █▀█ █▀█
█▀▀ █▀▄ ██▄ ▄█ ▄█   ██▄ █ ▀█ █▄▀    █  █▄█   ▄█  █  █▄█ █▀▀

	""")
keyboard.wait('Shift')

""" Сохранение координат """
def dump():
	f = open(name_file + ".dat", "wb")	
	pickle.dump(d, f)
	f.close()

try:
	f = open(name_file + ".dat", "ab+") # Открывает файл координат и перезаписывает, если такой файл уже существует
	d = pickle.load(f)
	f.close()
except:
	d = [] # Если такого файла нет, то создает
	dump()

def on_move(x, y):
	d.append('Pointer moved to {0}, {1}'.format(x, y))
	dump()

def on_click(x, y, button, pressed):
	d.append("Mouse clicked at {0}, {1} with {2} as {3}".format(x,y,button,pressed))
	dump()

listener = mouse.Listener(on_move=on_move,on_click=on_click)

listener.start()

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.end:
        # Остановить
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

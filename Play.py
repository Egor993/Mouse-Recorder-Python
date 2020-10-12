from pynput import keyboard
from time import sleep
import pyautogui
import random
import pickle
from pynput.mouse import Button, Controller
import win32api, win32con
import keyboard as key

name_file = input("Write macro name: ")

set_speed = int(input("""Choose speed
1 - Low

2 - Normal

3 - Fast

"""))

if set_speed == 1:
	move_speed =  0.0050
	pressed_speed = 0.30
elif set_speed == 2:
	move_speed = 0.0015
	pressed_speed = 0.15
else:
	move_speed = 0.0005
	pressed_speed = 0.05

print("""
█▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █▄ █ █▀▄   ▀█▀ █▀█   █▀ ▀█▀ █▀█ █▀█
█▀▀ █▀▄ ██▄ ▄█ ▄█   ██▄ █ ▀█ █▄▀    █  █▄█   ▄█  █  █▄█ █▀▀
""")

""" Открывает координаты и сохраняет в переменную point """
file = open(name_file + ".dat", "rb")
point = pickle.load(file)
file.close()
set_pos = 0

mouse = Controller()

def move(s):
	return s.split(' to ')[1].rsplit(', ')

def click(s):
	return s.split(' at ')[1].rsplit(' with ')[0].rsplit(', ')

break_program = False
def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        listener.stop()
        return False

""" Воспроизведение скрипта """
with keyboard.Listener(on_press=on_press) as listener:
	try:
		while break_program == False:

			if "Pointer moved" in point[set_pos]: # Каждый раз проверяет, есть ли в точке "Pointer moved".
				# Если это так, выполняет программу и увеличивает point на 1.
				sleep(move_speed) # Отвечает за скорость движения курсора
				n = move(point[set_pos])
				win32api.SetCursorPos((int(n[0]),int(n[1])))
				set_pos += 1		

			elif "Button.left as True" in point[set_pos]:
				sleep(pressed_speed) # Отвечает за скорость клика
				mouse.press(Button.left)
				set_pos += 1
				
			elif "Button.left as False" in point[set_pos]:
				sleep(pressed_speed)
				mouse.release(Button.left)
				set_pos += 1			

			elif "Button.right as True" in point[set_pos]:
				sleep(pressed_speed)
				mouse.press(Button.right)
				set_pos += 1				

			elif "Button.right as False" in point[set_pos]:
				sleep(pressed_speed)
				mouse.release(Button.right)
				set_pos += 1

		listener.join()
	except:
	 	print("Done")

import pyautogui
import time
time.sleep(5)
delay = 0.02
for _ in range(100):
    pyautogui.press('tab')
    time.sleep(delay)
    pyautogui.press('-')
    time.sleep(delay)
    pyautogui.press('left')
    time.sleep(delay)

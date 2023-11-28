try:
    import pyautogui as pag
    import time
except ImportError:
    print("Install the libraries pyautogui and timewith the following command: pip install --user pyautogui, time")
print("The programm is running..")

while True:
    pag.move(0, 1)
    print(pag.position())
    pag.move(0,-1)
    print(pag.position())
    time.sleep(10)
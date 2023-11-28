import keyboard
import time

def Hold_key(key, seconds):
    keyboard.press(key)
    time.sleep(seconds)
    keyboard.release(key)

def Press_key(key):
    keyboard.send(key)

def Release_key(key):
    keyboard.release(key)


def Press_key_for_time(key, seconds):
    time_finish=time.time()+seconds
    while time.time() < time_finish:
        keyboard.send(key)

def Release_key_for_time(key, seconds):
    time_finish=time.time()+seconds
    while time.time() < time_finish:
        keyboard.release(key)


def Hold_all_keys(seconds):
    time_finish=time.time()+seconds
    while time.time() < time_finish:
        [keyboard.send(i) for i in range (84)]
def Press_all_keys():
    [keyboard.send(i) for i in range (84)]

def Release_all_keys():
    [keyboard.release(i) for i in range (84)]


def main():
    number_inputs=int(input("How many different commands do you want to do?"))
    list_commands=[]
    doesnt_need_key=["hak", "pak", "rak"]
    doesnt_need_seconds=["pk", "rk", "pak", "rak"]
    
    for i in range(number_inputs):
        print("Please select between hold key, press key, release key, press key for time, release key for time, hold all keys, press all keys and release all keys ")
        mode=input("hk, pk, rk, pkft, rkft, hak, pak, rak:")
        
        if mode not in doesnt_need_key:
            key=input("Select key (lowercase):")
            list_commands.insert(1, key)
        
        if mode not in doesnt_need_seconds:
            seconds=int(input("How many seconds:"))
            list_commands.insert(2, seconds)
        
        trigger=input("Which key will trigger these commands? (lowercase)")

        list_commands.insert(0, mode)
    keyboard.wait(trigger)
    for i in range(number_inputs):
        mode=list_commands[i*2]
        key=list_commands[(i*2)+1]
        seconds=list_commands[(i*2)+2]

        if mode == "hk":
            Hold_key(key, seconds)

        elif mode == "pk":
            Press_key(key)

        

      


main()





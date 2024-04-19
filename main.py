from pynput import keyboard, mouse
import time
import os


is_toggled = False
mouse_controller = mouse.Controller()
COMBINATION = {keyboard.Key.f8}
current_keys = set()


def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)
        if COMBINATION.issubset(current_keys):
            global is_toggled
            is_toggled = not is_toggled

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass 

def main():
    os.system('cls')
    print("Welcome to Bernso's autoclicker!\n\nInformation:\n - The autoclicker is toggleable, you do not hold down the keybind.\n - The keybind to start the autoclicker is 'F8'\n - The deafult delay for this autoclicker is: 0.0001 seconds\n - If the delay is set to 0 IT WILL LAG YOUR COMPUTER and most if not all of your inputs WILL be delayed\n\nWould you like to add a delay? (y/n): ")
    user_input = input()
    if user_input.lower() == 'y':
        delay = float(input("\nEnter the delay in seconds: "))
        print(f'Your delay is: {delay}')
    elif user_input.lower() == 'n':
        delay = 0.0001
        print(f"\nThe delay has automatically been set to: {delay}")
    else:
        print("\nInvalid input. When this text disappears the program has been restarted.\nRestarting...")
        time.sleep(2)
        main()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            if is_toggled:
                mouse_controller.press(mouse.Button.left)
                mouse_controller.release(mouse.Button.left)
                time.sleep(delay)

        listener.join()
        
if __name__ == "__main__":
    main()
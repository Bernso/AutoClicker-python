from pynput import keyboard, mouse
import time, os, customtkinter as tk, requests, webbrowser, threading

# Creates a folder to store the icon
Icon = "Icon"
if os.path.exists(Icon):
    print("'Icon' folder already exists")
else:
    print("Creating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

def open_discord(event):
    webbrowser.open_new("https://discord.gg/k5HBFXqtCB")

def download_ico(url, save_path):
    
    if os.path.exists("Icon/Arhururan.ico"):
            print("Icon has already been downloaded")  
    else:
        try:
            response = requests.get(url)
            status_code = response.status_code
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("ICO file downloaded successfully!")
        except Exception as e:
            print(f"Failed to download ICO file.\nError: {e}\n\n")
            input()
        if status_code != 200:
            print("Failed to download ICO file.\n\n")
            input()

# Settings
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
    
def clicking():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        
        while True:
            if is_toggled:
                delay = get_delay()
                if delay != float(delay):
                    print("Please restart the program.")
                    break
                else:
                    
                    if stateText.cget('text') != "Active":
                        stateText.configure(text="Active")
                    
                    mouse_controller.press(mouse.Button.left)
                    mouse_controller.release(mouse.Button.left)
                    
                    time.sleep(delay)
            else:
                # Update stateText label
                if stateText.cget('text') != "Not active":
                    stateText.configure(text="Not active")
                time.sleep(0.1)
                
        listener.join()

def get_delay():
    delay_str = delayBox.get()  # Get the string input from the entry widget
    try:
        delay_float = float(delay_str)  # Convert the string to a float
        # Now you have the float value, you can use it as needed
        #print("Current delay:", delay_float)
        return delay_float
        # You can use delay_float wherever you need it in your code
    except ValueError:
        # Handle the case where the input cannot be converted to a float
        input("Invalid input. Please enter a valid float value.")
        app.destroy()

try:
    ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Arhururan.ico"
    save_path = os.path.join(Icon, "Arhururan.ico")  # Full file path including directory
    download_ico(ico_url, save_path)
    print("ICO file download process completed.\n\n")
except Exception as e:
    print(f"Failed to download ICO file.\nError: {e}\n\n")
    input()

# To get the delay value: delay.get() 

app = tk.CTk()
app.geometry('450x250')
app.title('AutoClicker by Bernso')
app.iconbitmap(r"Icon/Arhururan.ico")


stateText = tk.CTkLabel(app, text = "Not active", font = ('helvetica', 20, 'bold'))
stateText.pack(padx = 10, pady = 10)

delayBox = tk.CTkEntry(app, placeholder_text = "Delay (must be a float value)", height = 30, width = 300, placeholder_text_color = '#000000')
delayBox.pack(padx = 10, pady = 10)

infoText = tk.CTkLabel(app, text = "When changing the value of the delay,\nmake sure you have turned off the autoclicker. (F8)")
infoText.pack(padx = 10, pady = 10)

supportText = tk.CTkLabel(app, text = "If you are having trouble join the discord for help:\nhttps://discord.gg/k5HBFXqtCB\n\n(click the link)", font=('helvetica', 14, 'italic'))
supportText.bind("<Button-1>", open_discord)
supportText.pack(pady = 20)


if __name__ == '__main__':
    threading.Thread(target=clicking, daemon=True).start()
    app.mainloop()
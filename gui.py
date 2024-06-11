from tkinter import *
from tkinter.ttk import Combobox

import customtkinter
import psutil
import viewbot
import threading

# Configuration
THEME = 'light'
RES = '450x300'

# Globals
viewbot_running = False
viewbot_thread = None
stop_flag = threading.Event()

def update_cpu_label():
    global cpu_percent_label
    cpu_percent = psutil.cpu_percent()
    cpu_percent_label.config(text=f'CPU: {cpu_percent}%')
    # Schedule the function to run again after 1000 milliseconds (1 second)
    cpu_percent_label.after(1000, update_cpu_label)

def update_ram_label():
    global ram_percent_label
    ram_percent = psutil.virtual_memory().percent
    ram_percent_label.config(text=f'RAM: {ram_percent}%')
    # Schedule the function to run again after 1000 milliseconds (1 second)
    ram_percent_label.after(1000, update_ram_label)

def increment():
    current_value = int(number_of_viewers.get())
    number_of_viewers.set(current_value + 1)

def decrement():
    current_value = int(number_of_viewers.get())
    if current_value > 0:
        number_of_viewers.set(current_value - 1)

def on_mousewheel(event):
    if event.delta > 0 or event.num == 4:
        increment()
    elif event.delta < 0 or event.num == 5:
        decrement()

def create_method_frame(master):
    method_frame = Frame(master=master)
    method_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    method_label = Label(master=method_frame, text="Method")
    method_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    method_label_var = StringVar()
    method_label_var.set('web proxy')
    method_box = Combobox(master=method_frame, values=['web proxy', 'personal proxy'], textvariable=method_label_var, state='disabled', )
    method_box.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    return method_frame, method_label_var

def create_platform_frame(master):
    platform_frame = Frame(master=master,highlightthickness=1, highlightbackground="black", bd=1, height=100, width=500)
    platform_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    platform_label = Label(master=platform_frame, text="Platform")
    platform_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    platform_box = Combobox(master=platform_frame, values=['twitch', 'kick'], textvariable=platform)
    platform_box.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # CPU / RAM
    global cpu_percent_label 
    cpu_percent_label = Label(platform_frame, text='CPU: -')
    cpu_percent_label.grid(row=1, column=1, padx=50, pady=10)
    update_cpu_label() # Start updating the CPU label

    global ram_percent_label 
    ram_percent_label = Label(platform_frame, text='RAM: -')
    ram_percent_label.grid(row=2, column=1, padx=50, pady=10)
    update_ram_label() # Start updating the RAM label
    return platform_frame, platform

def create_channel_entry(platform_frame):
    channel_label = Label(master=platform_frame, text="Channel Name")
    channel_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    channel_entry = Entry(master=platform_frame, textvariable=channel_name)
    channel_entry.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

def create_viewers_entry(platform_frame):
    viewers_label = Label(master=platform_frame, text="Viewers:")
    viewers_label.grid(row=4, column=0, padx=8, pady=10, sticky="w")

    viewers_entry = Spinbox(platform_frame, textvariable=number_of_viewers, from_=0, to=100)
    viewers_entry.grid(row=4, column=0, padx=60, sticky='e')

    # Bind mouse wheel events
    viewers_entry.bind("<MouseWheel>", lambda event: on_mousewheel(event)) 

def start_viewbot():
    global viewbot_thread
    stop_flag.clear()
    platform_value = platform.get()
    channel_value = channel_name.get()
    viewers_value = number_of_viewers.get()
    viewbot_thread = threading.Thread(target=viewbot.start_viewbot, args=(stop_flag, platform_value, channel_value, viewers_value))
    viewbot_thread.start()

def stop_viewbot():
    global viewbot_thread, stop_flag
    if viewbot_thread is not None and viewbot_thread.is_alive():
        stop_flag.set()
        viewbot_thread.join()

def toggle_viewbot(button):
    if viewbot_thread is None or not viewbot_thread.is_alive():
        button.config(text='Stop')
        start_viewbot()
    else:
        button.config(text='Start')
        stop_viewbot()

def create_control_buttons(platform_frame):
    start_button = Button(master=platform_frame, text="Start", width=10, command=lambda: toggle_viewbot(start_button))
    start_button.grid(row=4, column=1, padx=20, pady=(0, 20))

def main():
    customtkinter.set_appearance_mode(THEME)
    app = customtkinter.CTk()
    app.geometry(RES)
    app.resizable(False, False)
    app.iconbitmap('icon.ico')
    app.title('Viewbot')

    # Initialize Tkinter variables
    global platform, method, channel_name, number_of_viewers
    platform = StringVar(value='twitch')
    method = StringVar(value='web proxy')
    channel_name = StringVar(value='')
    number_of_viewers = IntVar(value=0)


    method_frame, method_box_var = create_method_frame(app) 
    platform_frame, platform_box_var = create_platform_frame(app)

    create_channel_entry(platform_frame)
    create_viewers_entry(platform_frame)  
    create_control_buttons(platform_frame)

    app.mainloop()

if __name__ == '__main__':
    main()

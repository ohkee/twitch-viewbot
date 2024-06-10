from tkinter import *
import customtkinter

# Configuration
THEME = 'light'

def handle_enter(event):
    text = entry_text.get()
    print("Entered text:", text)
    entry.configure(state="disabled")

if __name__ == '__main__':
    # Creates app
    customtkinter.set_appearance_mode(THEME)
    app = customtkinter.CTk()
    app.geometry('800x600')
    app.title('VIEWBOT')

    # Method
    method_frame = customtkinter.CTkFrame(master=app)
    method_frame.grid(row=1, column=0, padx=(0,50), pady=(20, 10), sticky="nsew")
    method_frame.grid_columnconfigure(0, weight=1)  # make column 0 expandable

    method_label = customtkinter.CTkLabel(master=method_frame, text="Method")
    method_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    method_label_var = StringVar()
    method_label_var.set('web proxy')
    method_box = customtkinter.CTkComboBox(master=method_frame, values=['web proxy', 'premium proxy (must have proxies)'], variable=method_label_var)
    method_box.grid(row=1, column=0, padx=10, pady=(10 , 10), sticky="ew")

    # Platform
    platform_frame = customtkinter.CTkFrame(master=app)
    platform_frame.grid(row=0, column=0, padx=(0,50), pady=(20, 10), sticky="nsew")
    platform_frame.grid_columnconfigure(0, weight=1)  # make column 0 expandable

    platform_label = customtkinter.CTkLabel(master=platform_frame, text="Platform")
    platform_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")

    platform_box_var = StringVar()
    platform_box_var.set('twitch')
    platform_box = customtkinter.CTkComboBox(master=platform_frame, values=['twitch', 'kick'], variable=platform_box_var)
    platform_box.grid(row=1, column=0, padx=10, pady=(10 , 10), sticky="ew")

    # Channel 
    channel_label = customtkinter.CTkLabel(master=platform_frame, text="Channel Name")
    channel_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    channel_entry = customtkinter.CTkEntry(master=platform_frame)
    channel_entry.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

    # Entry for viewers
    viewers_label = customtkinter.CTkLabel(master=platform_frame, text="Number of Viewers")
    viewers_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    viewers_entry = customtkinter.CTkEntry(master=platform_frame)
    viewers_entry.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="ew")

    # Start and Stop buttons
    start_button = customtkinter.CTkButton(master=platform_frame, text="Start", width=60,height=20, corner_radius=0, fg_color="#4CAF50", hover_color="#45A049", text_color="white")
    start_button.grid(row=4, column=1, padx=10, pady=(5, 10))

    stop_button = customtkinter.CTkButton(master=platform_frame, text="Stop", width=60, height=20, corner_radius=0, fg_color="#F44336", hover_color="#D32F2F", text_color="white")
    stop_button.grid(row=4, column=2, padx=0, pady=(5, 10))


    # Runs the app
    app.mainloop()

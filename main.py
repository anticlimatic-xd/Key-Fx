#Version 1.0.1
#Author: anticlimatic-xd
#Purpose: Personalize keyboard with sfx

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import config
from config import SPADX, BPADX, PADY
import event_handler


class app:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KeyFX 0.1.1")
        self.root.geometry("300x50")
        self.root.resizable(False, False) #Create the root window

        self.create_toolbar()

        self.root.mainloop()



    def create_volume_window(self):
        if not config.window_flags["Volume"]: #Skip everything if there's already 1 volume window
            config.window_flags["Volume"] = True #Set the flag to true

            volume_window = tk.Toplevel()
            volume_window.title("Volume")
            volume_window.geometry("195x65")
            volume_window.resizable(False, False) #Create the toplevel window

            def set_volume(volume):
                config.volume = volume 

            
            curr_vol_lbl = ttk.Label(master=volume_window, text="Current volume:")
            vol_spbox = ttk.Spinbox(master=volume_window,  from_=0, to=100, wrap=True, command=lambda: set_volume(int(vol_spbox.get()) / 100))
            #Create the widgets
            vol_spbox.set(int(config.volume * 100))

            curr_vol_lbl.grid(column=0, row=0, padx=BPADX, pady=PADY)
            vol_spbox.grid(column=0, row=1, padx=BPADX, pady=PADY) #Place them

            def on_enter(_):
                try:
                    get_volume = int(vol_spbox.get())
                    if get_volume > 100 or get_volume < 0:
                        pass
                    else:
                        set_volume(get_volume / 100)
                except ValueError:
                    pass

            vol_spbox.bind("<Return>", on_enter)


            def on_close():
                config.window_flags["Volume"] = False
                volume_window.destroy() #Set the flag to false and close the window on close

            volume_window.protocol("WM_DELETE_WINDOW", on_close) #Call on_close()



    def create_soundpack_window(self):


        if not config.window_flags["Soundpack"]: #For the category choice, check if the category flag is up
            config.window_flags["Soundpack"] = True #Set the flag to true if the flag is false

            soundpack_window = tk.Toplevel()
            soundpack_window.title("Soundpack")
            soundpack_window.geometry("305x90") #Create a new toplevel
            soundpack_window.resizable(False, False)

            soundpack_frm = tk.Frame(master=soundpack_window)
            button_frm = tk.Frame(master=soundpack_window) #Create new frames
        
            
            
            current_category = tk.StringVar(master=soundpack_frm) #Create a stringvar for the category combobox
            category_cbbox = ttk.Combobox(master=soundpack_frm, state="readonly", width=20, values=list(config.keyboard_sounds.keys()), textvariable=current_category)

            current_soundpack = tk.StringVar(master=soundpack_frm) #Create a stringvar for the soundpack combobox
            soundpack_cbbox = ttk.Combobox(master=soundpack_frm, state="readonly", width=20,  textvariable=current_soundpack)



            soundpack_confirm_btn = ttk.Button(
            master=button_frm, 
            width=9,
            text="Start!", 
            command=lambda: event_handler.run(current_category.get(), current_soundpack.get())
            ) #Create a confirm button
            
            stop_btn = ttk.Button(
            master=button_frm, 
            width=9, 
            text="Stop", 
            command=event_handler.deactivate
            ) #Create a stop button

            soundpack_frm.grid(sticky="n", column=0, row=0, padx=SPADX, pady=0)
            button_frm.grid(sticky="s", column=0, row=1, padx=SPADX, pady=0)

            category_cbbox.grid(column=0, row=0, padx=SPADX, pady=PADY)
            soundpack_cbbox.grid(column=1, row=0, padx=SPADX, pady=PADY)

            soundpack_confirm_btn.grid(column=0, row=1, padx=SPADX, pady=PADY)
            stop_btn.grid(column=1, row=1, padx=SPADX, pady=PADY) #Place the widgets

            

            def on_category_select(_):
                if current_category.get() in config.keyboard_sounds: #If the category is in the keyboard_sounds categories
                    soundpack_cbbox["values"] = list(config.keyboard_sounds[current_category.get()].keys()) #Set the values to the category's ones
                    soundpack_cbbox.set("")
                    soundpack_cbbox.current(0) #Set the first value

            category_cbbox.bind("<<ComboboxSelected>>", on_category_select)





            def on_close():
                config.window_flags["Soundpack"] = False
                event_handler.deactivate() #Deactivate
                soundpack_window.destroy() #Set the flag to false and destroythe window on close

            soundpack_window.protocol("WM_DELETE_WINDOW", on_close) #Call on_close()

    def message_user(self):
        messagebox.showinfo("Currently unavailable", "For now, this is is currently unavailable")        


    def create_toolbar(self): #Create the toolbar
        tool_bar_frm = ttk.Frame(master=self.root) #Create the frame for the toolbar

        select_pack_btn = ttk.Button(master=tool_bar_frm, command=self.create_soundpack_window, text="Select a sound pack", width=19)
        vol_btn = ttk.Button(master=tool_bar_frm, command=self.create_volume_window, text="Volume", width=8)
        custom_btn = ttk.Button(master=tool_bar_frm, command=self.message_user, text="Custom packs", width=13) #Creating the buttons for different options

        tool_bar_frm.grid(column=0, row=0, padx=10, pady=PADY)
        vol_btn.grid(row=0, column=0, padx=SPADX, pady=PADY)
        custom_btn.grid(row=0, column=1, padx=SPADX, pady=PADY)
        select_pack_btn.grid(row=0, column=2, padx=SPADX, pady=PADY) #Place it all



#create_toolbar()

gog = app()


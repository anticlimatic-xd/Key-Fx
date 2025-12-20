import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import config
from config import SPADX, BPADX, PADY
import Keyboard_clicks


class app:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KeyFX")
        self.root.geometry("300x70")
        self.root.resizable(False, False) #Create the root window

        self.create_toolbar()

        self.root.mainloop()




    def test_cmd(self):
        print("Everything works!")


    def test_4(self,x,y,j):
        print(x,y,j)


    def create_volume_window(self):
        if not config.window_flags["Volume"]: #Skip everything if there's already 1 volume window
            config.window_flags["Volume"] = True #Set the flag to true

            volume_window = tk.Toplevel()
            volume_window.title("Volume")
            volume_window.geometry("195x70")
            volume_window.resizable(False, False) #Create the toplevel window

            curr_vol_lbl = ttk.Label(master=volume_window, text="Current volume:")
            vol_spbox = ttk.Spinbox(master=volume_window, textvariable=config.volume, from_=0, to=100, wrap=True)

            curr_vol_lbl.grid(column=0, row=0, padx=BPADX, pady=PADY)
            vol_spbox.grid(column=0, row=1, padx=BPADX, pady=PADY)


            def on_close():
                config.window_flags["Volume"] = False
                volume_window.destroy() #Set the flag to false and close the window on close

            volume_window.protocol("WM_DELETE_WINDOW", on_close) #Call on_close()



    def create_soundpack_window(self):


        if not config.window_flags["Soundpack"]: #For the category choice, check if the category flag is up
            config.window_flags["Soundpack"] = True #Set the flag to true if the flag is false

            soundpack_window = tk.Toplevel()
            soundpack_window.title("Soundpack")
            soundpack_window.geometry("375x70") #Create a new toplevel


            soundpack_frm = tk.Frame(master=soundpack_window)
        
            
            
            current_category = tk.StringVar(master=soundpack_frm)
            category_cbbox = ttk.Combobox(master=soundpack_frm, state="readonly", width=20, values=list(config.keyboard_sounds.keys()), textvariable=current_category)

            current_soundpack = tk.StringVar(master=soundpack_frm)
            soundpack_cbbox = ttk.Combobox(master=soundpack_frm, state="readonly", width=20,  textvariable=current_soundpack)



            soundpack_confirm_btn = ttk.Button(
            master=soundpack_frm, 
            width=9,
            text="Start!", 
            command=lambda: Keyboard_clicks.run(current_category.get(), current_soundpack.get())
            )
            
            stop_btn = ttk.Button(
            master=soundpack_frm, 
            width=9, 
            text="Stop", 
            command=Keyboard_clicks.deactivate
            )

            soundpack_frm.grid(sticky="n", column=0, row=0, padx=SPADX, pady=PADY)
            category_cbbox.grid(column=0, row=0, padx=SPADX, pady=PADY)
            soundpack_cbbox.grid(column=1, row=0, padx=SPADX, pady=PADY)
            soundpack_confirm_btn.grid(column=0, row=1, padx=SPADX, pady=PADY)
            stop_btn.grid(column=1, row=1, padx=SPADX, pady=PADY)

            

            def on_category_select(self):
                if current_category.get() in config.keyboard_sounds:
                    soundpack_cbbox["values"] = list(config.keyboard_sounds[current_category.get()].keys())
                    soundpack_cbbox.set("")
                    soundpack_cbbox.current(0)

            category_cbbox.bind("<<ComboboxSelected>>", on_category_select)




            def on_close():
                config.window_flags["Soundpack"] = False
                soundpack_window.destroy() #Set the flag to false and close the window on close

            soundpack_window.protocol("WM_DELETE_WINDOW", on_close) #Call on_close()


    def create_toolbar(self): #Create the toolbar
        tool_bar_frm = ttk.Frame(master=self.root) #Create the frame for the toolbar

        select_pack_btn = ttk.Button(master=tool_bar_frm, command=self.create_soundpack_window, text="Select a sound pack", width=19)
        vol_btn = ttk.Button(master=tool_bar_frm, command=self.create_volume_window, text="Volume", width=8)
        custom_btn = ttk.Button(master=tool_bar_frm, command=self.test_cmd, text="Custom packs", width=13) #Creating the buttons for different options

        tool_bar_frm.grid(column=0, row=0, padx=10, pady=PADY)
        vol_btn.grid(row=0, column=0, padx=SPADX, pady=PADY)
        custom_btn.grid(row=0, column=1, padx=SPADX, pady=PADY)
        select_pack_btn.grid(row=0, column=2, padx=SPADX, pady=PADY) #Packing it all



#create_toolbar()

gog = app()

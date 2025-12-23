import keyboard
from pygame import mixer

import config

keyboard_events = {"a", "b", "c"} #Empty list of events
running = False
hook = None
mixer.init()


def cycle_events(event):
    keyboard_events.pop()
    keyboard_events.add(str(event))




def handle_event(event, category: str, soundpack: str):
    # This function triggers whenever a key is pressed/released and if the event wasn't already registered

    press_sfx = mixer.Sound(config.keyboard_sounds[category][soundpack][0])
    release_sfx = mixer.Sound(config.keyboard_sounds[category][soundpack][1])


    if event.event_type == "down":
        if str(event) in keyboard_events:
            pass
        else:
            press_sfx.play()
            print(event, category, soundpack)
            print(keyboard_events)
            cycle_events(event)



    elif event.event_type == "up":
        if str(event) in keyboard_events and mixer.get_busy():
            pass
        else:
            release_sfx.play()
            print(event, category, soundpack)
            print(keyboard_events)
            cycle_events(event)

    

def run(category: str, soundpack: str):
    global hook

    if config.is_running:
        return None #If the thread is running, exit
    
    config.is_running = True #Set the flag to true
    hook = keyboard.hook(lambda event: handle_event(event, category, soundpack)) #Hook the hook


def deactivate():
    global hook

    config.is_running = False #Set the thread flag to false

    if hook is not None: #If the hook is something other than none...
        keyboard.unhook(hook) 
        hook = None #Unhook and set to none



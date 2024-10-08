# Smoke and Algorithms - Project 2024 SECont
# Main file; Organizing file for calling the starting level

# Initialize Variables
default notes = Notes([])
default show_textbox = True
default gallery = Pictures([])
define medievilColor = "#e46b6bff" # Text color used everytime "Medievil" is mentioned in dialogue
default current_location = 0 # -1 = Error, 0 = Dorms, 1 = University
default mouse_index = 0
default hide_map = False

init python:
    offset = renpy.random.randint(0,10)

# Splashscreen thats been shown after opening the game before the main menu
label splashscreen:
    scene black
    with Pause(1)
    show text "Social Engineering Group presents"
    with dissolve
    with Pause(2)
    hide text
    with dissolve
    with Pause(1)
    return

# Label called when player tries to use map, but it's disabled
label map_disabled:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map
    with dissolve
    "You cannot leave right now!"
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    with dissolve
    if USB_placed_0 == True and before_office == False:
        jump menu_outside
    elif have_USB == False:
        jump before_the_office
    elif infront_facility == True:
        jump menu_outside
    elif current_location == "before_office":
        jump before_the_office
    return

# Label "start" is being called by renpy automatically after starting the game
label start:
    $ randomize_indices()
    $ gallery.add_data(["gallery_meme"], False)
    jump level_0_start
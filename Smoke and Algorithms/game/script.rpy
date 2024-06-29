#Smoke and Algorithms - Project 2024 SECont
# Organizing file for calling the starting level

default notes = Notes([])
default show_textbox = True
default gallery = Pictures([])
default hide_map = False

label map_disabled:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map
    with dissolve
    "You cannot leave right now."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    with dissolve
    return

label start:
    jump level_0_start
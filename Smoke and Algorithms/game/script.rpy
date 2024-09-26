#Smoke and Algorithms - Project 2024 SECont
# Organizing file for calling the starting level

default notes = Notes([])
default show_textbox = True
default gallery = Pictures([])
define medievilColor = "#e46b6bff"
default current_location = 0 # -1 = Error, 0 = Dorms, 1 = University
default mouse_index = 0
default hide_map = False

init python:
    offset = renpy.random.randint(0,10)

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
    return

label start:
    $ randomize_indices()
    $ gallery.add_data(["gallery_meme"], False)
    jump level_0_start
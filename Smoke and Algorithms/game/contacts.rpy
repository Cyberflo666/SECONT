# File contains dialogues for the contacts-screen on the phone
default hide_textbox = False
default show_image_buttons = True



label call_alex:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    A "Are you blind? I'm standing right next to you, Haha."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
    with dissolve
    return

label call_leonie:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    if USB_placed_0 == True and before_office == False:
        "You lost the USB? Should have know you two would mess it up. Just come back and i'll give you another one."
        $ have_USB = True
    elif have_USB == False:
        "You lost the USB? Should have know you two would mess it up. Wait a sec I'll send you a copy of the mallware to install on a spare USB."
        $ have_USB = True
    elif leonie_away == True:
        "Why are you calling for no reason?" 
    else:    
        L "Hey, I'm right here [PN]."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    if USB_placed_0 == True and before_office == False:
        jump get_another_USB
    elif have_USB == False:
        jump install_malware
    elif infront_facility == True:
        jump menu_outside
    elif infront_facility == False:
        jump before_the_office
    show screen phone_hand_contact
    with dissolve
    return

label call_felix:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    "Beep beep beep."
    "..."
    "It seems like noone answers the phone."
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
    with dissolve
    return

screen call_screen:
    add Solid("#00000000")
    zorder 1
    modal False

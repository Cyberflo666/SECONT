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
    return

label call_leonie:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    L "Hey, I'm right here [PN]"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
    return

label call_felix:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_contact
    with dissolve
    "beep beep beep"
    "..."
    "It seems like noone answers the phone"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    show screen phone_hand_contact
    return

screen call_screen:
    add Solid("#00000000")
    zorder 1
    modal False

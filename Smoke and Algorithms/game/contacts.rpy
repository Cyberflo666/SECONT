# File contains dialogues for the contacts-screen on the phone

label call_alex:
    $ show_textbox = True
    show screen call_screen
    hide screen phone_hand_contact
    with dissolve
    A "Are you blind? I'm standing right next to you, Haha."
    hide screen call_screen
    show screen phone_hand_contact
    with dissolve
    $ show_textbox = False
    return

label call_leonie:
    $ show_textbox = True
    hide screen phone_hand_contact
    with dissolve
    L "Hey, I'm right here [PN]"
    show screen phone_hand_contact
    with dissolve
    $ show_textbox = False
    return

label call_felix:
    $ show_textbox = True
    hide screen phone_hand_contact
    with dissolve
    "beep beep beep"
    "..."
    "It seems like noone answers the phone"
    show screen phone_hand_contact
    with dissolve
    $ show_textbox = False
    return

screen call_screen:
    add Solid("#00000000")
    modal False

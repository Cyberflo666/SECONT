# File contains dialogues for the contacts-screen on the phone

label call_alex:
    hide screen phone_hand_contact
    with dissolve
    A "Are you blind? I'm standing right next to you, Haha."
    show screen phone_hand_contact
    with dissolve
    return

label call_leonie:
    hide screen phone_hand_contact
    with dissolve
    L "Hey, I'm right here [PN]"
    show screen phone_hand_contact
    with dissolve
    return

label call_felix:
    hide screen phone_hand_contact
    with dissolve
    "beep beep beep"
    "..."
    "It seems like noone answers the phone"
    show screen phone_hand_contact
    with dissolve
    return
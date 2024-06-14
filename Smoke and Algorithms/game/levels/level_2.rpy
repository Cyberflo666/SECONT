label level_2_start:
    play music main_music1 volume 0.1
    scene bg new kitchen 
    "you gather around the kitchen table while opening up your laptop"
    "You walk over and gather around a table while opening up your laptop."
    scene laptop
    A "I think it's best if we start by looking up what exactly Medievil is."
    call screen laptop_screen
    ""

label website1_button:
    show screen website1_screen
    "something useless"
    call screen website1_screen
    jump website1_screen
    "muss hier was hin"
label website2_button:
    PC "Here is something about a lab at our university. According to these news it was offered to Medievil for research."
    L "Maybe we should check it out."
    A "You think we have access?"
    L "I think we can get it if we really want."
    jump website2_screen
label website3_button:
    PC "Our good friend Mr Anderson had a meeting today"
    A "With whom."
    PC "Someone called Gill Cameron"
    L "Never heard of him"
    A "But maybe worth a look. We could try finding him on brainrot"
    jump website3_screen

label website1_screen:
    call screen website1_screen
label website2_screen:
    call screen website2_screen
label website3_screen:
    call screen website3_screen

#label empty_label1:
    #jump empty_label
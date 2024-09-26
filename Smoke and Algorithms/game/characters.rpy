# Smoke and Algorithms - Project 2024 SECont
# This file contains all characters and their corresponding images

#Characters
define narrator = Character(            what_italic=True, what_outlines=[(0, "#080808", 5, 5)])
define PC = Character("[PN]",           what_prefix='"', what_suffix='"', who_color="#ffffff", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define A = Character("Alex",            what_prefix='"', what_suffix='"', who_color="#27e700", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define F = Character("Felix",           what_prefix='"', what_suffix='"', who_color="#2469ff", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define L = Character("Leonie",          what_prefix='"', what_suffix='"', who_color="#FF7F50", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define J = Character("Janitor",         what_prefix='"', what_suffix='"', who_color="#AA4473", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define R = Character("Receptionist",    what_prefix='"', what_suffix='"', who_color="#44aa99", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define S1 = Character("Secretary",      what_prefix='"', what_suffix='"', who_color="#b60000", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define S2 = Character("Security",       what_prefix='"', what_suffix='"', who_color="#686868", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])
define JA = Character("Joe Arnold",     what_prefix='"', what_suffix='"', who_color="#dacb00", who_bold=True, who_outlines=[(3, "#000000", 0, 0)], what_outlines=[(0, "#080808", 5, 5)])

# Character Sprites
# Leonie
image leonie neutral:
    "images/characters/leonie/leonie neutral.png"
    zoom 0.25
image leonie happy:
    "images/characters/leonie/leonie happy.png" 
    zoom 0.25
image leonie surprised:
    "images/characters/leonie/leonie surprised.png"
    zoom 0.25
image leonie sad:
    "images/characters/leonie/leonie sad.png"
    zoom 0.25
image leonie serious:
    "images/characters/leonie/leonie serious.png"
    zoom 0.25
image leonie thinking:
    "images/characters/leonie/leonie thinking.png"
    zoom 0.25

# Alex
image alex neutral:
    "images/characters/player/male/pcm neutral.png"
    zoom 1.4
image alex happy:
    "images/characters/player/male/pcm happy.png"
    zoom 1.4
image alex surprised:
    "images/characters/player/male/pcm surprised.png"
    zoom 1.4
image alex smile:
    "images/characters/player/male/pcm smile.png"
    zoom 1.4
image alex serious1:
    "images/characters/player/male/pcm serious1.png"
    zoom 1.4
image alex serious2:
    "images/characters/player/male/pcm serious2.png"
    zoom 1.4
image alex serious2left:
    "images/characters/player/male/pcm serious2 left.png"
    zoom 1.4
image alex angry:
    "images/characters/player/male/pcm angry.png"
    zoom 1.4
image alex angryleft:
    "images/characters/player/male/pcm angry left.png"
    zoom 1.4
image alex neutralleft:
    "images/characters/player/male/pcm neutral left.png"
    zoom 1.4
image alex happyleft:
    "images/characters/player/male/pcm happy left.png"
    zoom 1.4
image alex surprisedleft:
    "images/characters/player/male/pcm surprised left.png"
    zoom 1.4
image alex smileleft:
    "images/characters/player/male/pcm smile left1.png"
    zoom 1.4
transform alex_right:
    xalign 1.65
    yalign -0.8
transform alex_midleft:
    xalign  0.15
    yalign -0.8
transform alex_left:
    xalign -1
    yalign -0.8

# Felix
image felix running:
    "images/characters/felix/felix running scared.png"
    zoom 0.8

image felix shouting:
    "images/characters/felix/felix shouting.png"
    zoom 0.8
transform felix_right:
    zoom 0.6
    xalign 0.9
    ypos 60

# Janitor
image janitor neutral1:
    "images/characters/janitor/janitor neutral1.png"
    zoom 0.85
image janitor neutral2:
    "images/characters/janitor/janitor neutral2.png"
    zoom 0.85
image janitor smile:
    "images/characters/janitor/janitor smile.png"
    zoom 0.85
image janitor thinking:
    "images/characters/janitor/janitor thinking.png"
    zoom 0.85
image janitor angry:
    "images/characters/janitor/janitor angry.png"
    zoom 0.85
transform janitor_right:
    xalign 1.1
    yalign 1.0
transform janitor_middle:
    xalign 0.5
    yalign 1.0

#Receptionist
image receptionist friendly:
    zoom 0.55
    "images/characters/Receptionist (Male)/friendly.png"
image receptionist neutral:
    zoom 0.55
    "images/characters/Receptionist (Male)/neutral.png"
image receptionist suspicious:
    "images/characters/Receptionist (Male)/suspicious.png"
    zoom 0.55

transform receptionist_right:
    xalign 1.0
    yalign 1.0

#Secretary
image secretary angry:
    "images/characters/Secretary (Female)/angry.png"
image secretary neutral:
    "images/characters/Secretary (Female)/neutral.png"
image secretary friendly:
    "images/characters/Secretary (Female)/friendly.png"
image secretary suspicious:
    "images/characters/Secretary (Female)/suspicious.png"
image secretary thinking:
    "images/characters/Secretary (Female)/thinking.png"

transform secretary_right:
    ypos 1300
    xalign 1.2
transform secretary_right_smile:
    ypos 1250
    xalign 1.2
    zoom 0.95
transform security:
    yalign 0.4
    xalign 0.5

label janitor_look(trust):
    if (trust > 75 ):
        show janitor thinking at janitor_right
        with dissolve
    elif (trust > 40):
        show janitor neutral1 at janitor_right
        with dissolve
    else:
        show janitor angry at janitor_right
        with dissolve

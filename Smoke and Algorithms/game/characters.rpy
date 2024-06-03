# Smoke and Algorithms - Project 2024 SECont
# This file contains all characters and their corresponding images

# Characters
define A = Character("Alex", what_prefix='"', what_suffix='"', color="7FFF00")
define F = Character("Felix", what_prefix='"', what_suffix='"', color="00008B")
define L = Character("Leonie", what_prefix='"', what_suffix='"', color="FF7F50")
define J = Character("Janitor", what_prefix='"', what_suffix='"', color="AA4473")

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
transform alex_right:
    xalign 1.65
    yalign -0.8
transform alex_midleft:
    xalign 0.15
    yalign -0.8

# Felix
image felix running:
    "images/characters/felix/felix running scared.png"
    zoom 0.8

image felix shouting:
    "images/characters/felix/felix shouting.png"
    zoom 0.8

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

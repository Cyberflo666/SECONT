# Smoke and Algorithms - Project 2024 SECont
# This file contains all characters and their corresponding images

# Characters
define A = Character("Alex", what_prefix='"', what_suffix='"', color="7FFF00")
define F = Character("Felix", what_prefix='"', what_suffix='"', color="00008B")
define L = Character("Leoni", what_prefix='"', what_suffix='"', color="FF7F50")
define J = Character("Janitor", what_prefix='"', what_suffix='"', color="AA4473")

# Character Sprites
# Leoni
image leoni neutral:
    "images/characters/Leoni/Images/portrait/leoni neutral.png"
    zoom 0.25
image leoni happy:
    "images/characters/Leoni/Images/portrait/leoni happy.png"
    zoom 0.25
image leoni surprised:
    "images/characters/Leoni/Images/portrait/leoni surprised.png"
    zoom 0.25
image leoni sad:
    "images/characters/Leoni/Images/portrait/leoni sad.png"
    zoom 0.25
image leoni serious:
    "images/characters/Leoni/Images/portrait/leoni serious.png"
    zoom 0.25
image leoni thinking:
    "images/characters/Leoni/Images/portrait/leoni thinking.png"
    zoom 0.25

# Alex
image alex neutral:
    "images/characters/Player/Male/pcm neutral.png"
    zoom 1.4
image alex happy:
    "images/characters/Player/Male/pcm happy.png"
    zoom 1.4
image alex surprised:
    "images/characters/Player/Male/pcm surprised.png"
    zoom 1.4
image alex smile:
    "images/characters/Player/Male/pcm smile.png"
    zoom 1.4
transform alex_right:
    xalign 1.65
    yalign -0.8
transform alex_midleft:
    xalign 0.15
    yalign -0.8

# Janitor
image janitor neutral1:
    "images/characters/Janitor/janitor neutral1.png"
    zoom 0.85
image janitor neutral2:
    "images/characters/Janitor/janitor neutral2.png"
    zoom 0.85
image janitor smile:
    "images/characters/Janitor/janitor smile.png"
    zoom 0.85
image janitor thinking:
    "images/characters/Janitor/janitor thinking.png"
    zoom 0.85
transform janitor_right:
    xalign 1.1
    yalign 1.0
transform janitor_middle:
    xalign 0.5
    yalign 1.0

label level_3_start:
    scene facility night afar bg
    show leonie neutral at left
    show alex neutral at alex_right
    with dissolve

    "As the sun starts to set, your team arrives at the facility where {color=[medievilColor]}Medievil{/color} probably conducts tons of unethical experiments and also where Bob Anderson works."

    show leonie serious at left
    with dissolve
    L "With the access code Bob unknowingly gave us, we should be able to enter via the back entrance."

    show alex serious1 at alex_right
    with dissolve
    A "Although it's probably emptier than at day, there are still a few people going in and out of the building. We have to be careful."

    "While staying at a save distance from the facility, Leonie examines the building."

    show leonie sad at left
    with dissolve
    L "It's no use. From here I can't really make out their methods of security."

    PC "Ok, let's go in then and take a closer look. That's what we have the codes for."

    show facility night close bg
    "With Leonie leading, the three of you go towards the back entrance and towards the pin pad. None of the few people here seem to pay attention to you."

    show leonie thinking at left
    with dissolve
    L "..."

    show leonie happy at left
    with dissolve
    L "Yes, the code worked."

    show facility hallway bg
    "With the door open, you sneakily follow the hallways towards the office areas. The hallways are almost completely void of any employees."

    show leonie serious at left
    with dissolve
    "Leonie whispers:"
    L "Wait, here it says that Bobs office and all the other important spaces are all in this area."

    show alex happy at alex_right
    with dissolve
    A "Sweet, let's go..."

    show leonie surprised at left
    with dissolve
    L "Wait!"
    "Leonie grabs Alex by his shirt and pulls him back behind the corner."

    show leonie serious at left
    with dissolve
    L "The following area seems to be secured by cameras and guards and you almost walked right into their field of view."

    show alex surprised at alex_right
    with dissolve
    A "Oh crap, thanks Leonie."

    show leonie neutral at left
    with dissolve
    L "Additionally, it seems as if we can't really get any further anyways. Do you see that door up ahead. It requires a key card to get through that we don't have."

    PC "I'm not sure how we are supposed to get our hands on one of these."

    show alex smile at alex_right
    with dissolve
    A "I don't think we have to."

    show leonie thinking at left
    with dissolve
    L "What do you mean."

    show alex neutral at alex_right
    with dissolve
    A "\'Tailgaiting\'. We follow one of the employees through the door and pretend we belong here. I think most people would believe us and just hold the door open for us like we were other employees."

    $ gloss_tailgating_seen = True

    show leonie serious at left
    with dissolve
    L "Great idea. So we have to come back during day for this to work."

    PC "Yup, let's do this"

    scene black
    with dissolve
    "Your group returns the way you came in and goes home without any incidents."

    "The next day during breakfast, you talk about your approach."
    scene bg new kitchen
    show alex neutral at alex_right
    show leonie thinking at left
    with dissolve
    L "I think I'm going to stay here. There were cameras all over the office spaces and if I stay here, I could give you support from afar."

    show leonie serious at left
    with dissolve
    L "Take this USB-Drive. If you manage to plug it into their security network, I get access to the cameras and can give you directions."

    PC "Hmm, this seems useful. Alright, everything set for todays infiltration?"

    show alex smile at alex_right
    with dissolve
    A "Yes."

    show leonie happy at left
    with dissolve
    L "Yup."

    scene black
    with dissolve
    "With Leonie staying home, only Alex and you go towards the facility."

    scene facility day afar bg
    show alex serious1 at alex_right
    with dissolve
    "You find yourself at the spot you were yesterday."

menu:
    "Take the main entrance.":
        pass
    "Take the back entrance.":
        pass
    "Observe the people entering the building.":
        pass
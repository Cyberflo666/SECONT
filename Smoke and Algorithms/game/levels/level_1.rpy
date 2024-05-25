label level_1_start:
    scene bg dorm_room
    with dissolve

    A "We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."

    menu:
        "Yes, we should go to the police and hand them the drive, they will know what to do":
            jump choice_1_1_police
        "He must have left us some info on how to get access to this data. Let's take a look into his room":
            jump choice_1_1_room

label choice_1_1_police:
    scene bg police_station
    with fade

    "You decide to take the drive to the police. They will know what to do with it."

    "The group heads to the local police station and hands over the flash drive."

    PC "Officer, we found this drive. We believe it contains important information."

    "The police take the flash drive as evidence. Weeks go by, and nothing more is heard about the case or Felix."

    "...or of Felix."

    "Weeks later, a small article buried in a conspiracy theory tabloid catches [PN]'s eye. The headline reads: 'Shocking Discovery: Human DNA Found in Dog Food.'"

    "A chill runs down [PN]'s spine. The article details a bizarre finding at a local pet food factory, a trace of human genetic material amidst the meat and grains. The source of the DNA remains unknown, the investigation ongoing."

    "[PN] can't shake the feeling that this is somehow connected to Felix, to BioSyn, to the cryptic warning he delivered that fateful night. But without proof, it's just another unsolved mystery, a whisper in the wind."

    "The weight of regret settles heavily on [PN]'s shoulders. The choice to ignore Felix's plea, to prioritize safety over friendship, has left a bitter taste in [hishers] mouth. The story ends not with a bang, but with a whimper, a silent echo of what could have been."

    "Game Over"
    return

label choice_1_1_room:
    scene bg dorm_hallway

    PC "Felix must have left some clues in his room. Let's go check it out."

    "The group steps out into the hallway and heads towards Felix's room, but finds it locked."

    L "As I expected. Too bad he's too paranoid to leave his door open like the rest of us."

    jump choice_1_1_done

label choice_1_1_done:
    scene bg dorm_hallway_locked_door
    with dissolve

    A "So, anyone got a clue as to how we're going to get into his room?"

    menu:
        "We should take a look at his windows":
            jump choice_1_2_windows
        "Maybe we can get help from the Janitor":
            jump choice_1_2_janitor
        "Try to pick the lock":
            jump choice_1_2_lockpick

label choice_1_2_windows:
    scene bg dorm_outside
    with fade

    PC "His windows. If they're still open, Leoni can climb up there and open the door from inside."

    L "What... Are you serious? Climb up? What if I fall?"

    A "It's a good idea, Leoni. You're the most athletic of us. You can do this."

    L "Fine, but if I break my neck, it's on you."

    "The group heads outside and looks up at Felix's window. It's slightly ajar."

    PC "Look, it's open! Leoni, can you make it?"

    L "I think so. Just give me a boost."

    "With some help, Leoni climbs up and slips through the window."

    scene bg dorm_hallway_locked_door
    with dissolve

    "A moment later, the door unlocks from the inside. Leoni opens it with a grin."

    L "Told you I could do it."

    jump choice_1_1_done_success

label choice_1_2_janitor:
    scene bg dorm_hallway
    with fade

    PC "The janitor has keys to all the rooms. Maybe we can get him to unlock Felix's door for us."

    L "Good idea. Let's find him."

    scene bg dorm_janitor_room
    with dissolve

    "The group heads down to the janitor's office. After a bit of knocking, the janitor opens the door."

    Janitor "What do you kids want?"

    PC "We need to get into Felix's room. It's really important. Can you help us?"

    Janitor "Felix's room, huh? That kid's always been a bit strange... Alright, I'll help you, but this better not get me in trouble."

    scene bg dorm_hallway_locked_door
    with dissolve

    "The janitor follows the group back to Felix's room and unlocks the door."

    Janitor "There you go. Be quick about whatever you're doing."

    jump choice_1_1_done_success

label choice_1_2_lockpick:
    scene bg dorm_hallway_locked_door
    with fade

    PC "Can one of you pick locks? Shouldn't be too hard, right?"

    L "I've never done it before, but I've seen it in movies. How hard can it be?"

    A "Do we even have anything to pick the lock with?"

    PC "I think I have a hairpin. Will that work?"

    L "Worth a shot. Hand it over."

    "Leoni takes the hairpin and starts working on the lock. After a few tense minutes, there's a click."

    L "Got it!"

    "The door swings open, revealing Felix's room."

    jump choice_1_1_done_success

label choice_1_1_done_success:
    scene bg felix_room
    with fade

    "The group steps into Felix's room, looking around carefully. The room is cluttered with papers and various gadgets."

    PC "Alright, let's find whatever Felix left for us. Start searching."

    A "Check the desk. He might have left some notes or something."

    L "I'll look through the drawers."

    "The group starts searching the room, hoping to find the key to unlocking the information on the drive."

    return

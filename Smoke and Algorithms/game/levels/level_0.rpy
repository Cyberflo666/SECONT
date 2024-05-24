#Smoke and Algorithms - Project 2024 SECont


define PC = Character("[PN]", what_prefix='"', what_suffix='"')
default PN = "Robert Paulson"
default gender = "neutral"
default heshe = "they"
default himher = "them"
default hishers = "their"
define A = Character("Alex", what_prefix='"', what_suffix='"', color="7FFF00")
define F = Character("Felix", what_prefix='"', what_suffix='"', color="00008B")
define L = Character("Leoni", what_prefix='"', what_suffix='"', color="FF7F50")
define J = Character("Janitor", what_prefix='"', what_suffix='"', color="AA4473")

label level_0_start:

    scene introduction and name
    "Buckle up for a journey where trust is a weapon, truth is a labyrinth, and the choices you make could unravel a conspiracy that reaches far beyond the walls of your imagination"

    $ PN = renpy.input("Enter your name.", "Robert Paulson", length=15, exclude=" 0123456789+=,.?!<>[]{}").strip() 
    menu:
        "Are you..."
        "Male":
            $ gender = "male"
            $ heshe = "he"
            $ himher = "him"
            $ hishers = "his"
        "Female":
            $ gender = "female"
            $ heshe = "she"
            $ himher = "her"
            $ hishers = "hers"
        "Non-Binary":
            $ gender = "neutral" 
    "Welcome [PN]. Let's get on with the story."




label dorm_1:

    scene dorm room

    scene A DORM ROOM - LATE AFTERNOON

    "The late afternoon sun filters through the blinds, casting long shadows across a cluttered dorm room. Books, papers, and empty snack wrappers are scattered haphazardly across the floor, a testament to the chaotic energy of finals week."
    
    "[PN], [hishers] dark hair pulled into a messy bun, sits hunched over [hishers] laptop, the glow of the screen illuminating the intricate henna tattoos on [hishers] left hand."

    PC "I can't focus. Complex systems theory is proving to be...well, complex. My eyes glaze over the lines of code and algorithms, and my mind starts to drift."

    "Alex, sprawled across the floor amidst a sea of open books, lets out a dramatic sigh."

    A "Okay, I officially surrender to the forces of academia. My brain is officially mush."

    "[PN] chuckles, a welcome distraction from [hishers] studies."

    PC "Don't worry, Alex. We're almost through this. Just a few more hours of this delightful torture."

    "Alex groans dramatically, then reaches for a half-eaten slice of pizza."

    A "If caffeine and sugar were the keys to academic success, we'd all be Nobel laureates by now."

    "A comfortable silence settles over the room, punctuated only by the rhythmic tapping of Leoni's keyboard from her beanbag chair in the corner."

    L "Hey, have either of you seen Felix today? He hasn't answered any of my texts."

    "Alex sits up, a mischievous glint in his eyes."

    A "Oh, you know Felix. He's probably off chasing UFOs or decoding secret messages in the cafeteria's meatloaf."

    "[PN] smiles, but the worry doesn't quite fade. Felix, their conspiracy-obsessed friend, had been acting strangely lately. His usual playful banter had taken on a darker tone, his excitement about his BioSyn internship replaced by a growing unease."

    A "Actually, now that you mention it... he seemed a little freaked out this morning. Almost like he was...scared"

    L "Scared? Of what?"

    A "I don't know. He was mumbling something about his internship at BioSyn, some experiment called NeuroMend... It was all very cryptic."

    "Suddenly, the dorm room door is thrown open, slamming against the wall with a resounding crash."

    "Felix bursts into the room, his eyes wide with terror, his chest heaving as if he'd been running for miles. His usually meticulously styled hair was a tangled mess, and his clothes were rumpled and stained."

    F "(Gasping for air, his voice barely a whisper) BioSyn! They're not what they seem. This... this is everything. Trust no one."

    "With trembling hands, he thrusts a battered flash drive into [PN]'s hand, then turns and flees, disappearing into the dimly lit hallway."

    "The air crackles with tension, and a million thoughts race through my mind. What was that all about? Why is Felix so scared? What's on this flash drive? The flash drive feels heavy in [PN]'s hand."

    "[PN] looks between Alex and Leoni, weighing her options."

menu:
    "(you raise your concern) Do you think we should go after him?":
        jump choice1_follow
    
    "(Leoni pushing up her glasses) Or maybe we should see what's on this drive first?":
        jump choice1_check

    "This could be dangerous. Maybe we shouldn't get involved.":
        jump choice1_ignore

label choice1_follow:

        $ menu_flag = True

        PC "We can't just let him run off like that. He's obviously terrified. Something's wrong."
        "[PN] rushes out the door, following the direction Felix took. Alex and Leoni exchange a worried glance before hurrying after [himher]."

        jump choice1_done

label choice1_check:

        $ menu_flag = True

        PC "He said this was important. Maybe it has answers. Leoni, can you take a look?"
        "Leoni nods, taking the flash drive from [PN]. She plugs it into her laptop and begins examining its contents."

        jump choice1_done

label choice1_ignore:

        $ menu_flag = False

        A "(His eyes widening in disbelief) Are you serious? [PN], Felix is our friend. We can't just abandon him!"

        L "Besides, curiosity is killing me. I want to know what's on that drive."

        "[PN] hesitates, torn between caution and concern for [hishers] friend."

label choice1_done:

    "At this point the fork is Storygame (Option 1), Minigame (Option 2) and Sideline (Option 3)"
    jump level_1_start
    return 
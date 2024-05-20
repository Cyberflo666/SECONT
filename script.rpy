# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define A = Character("Alex",color="7FFF00")
define P = Character("Player",color="DC143C")
define F = Character("Felix",color="00008B")
define L = Character("Leoni",color="FF7F50")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dorm room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    scene A DORM ROOM - LATE AFTERNOON

    "The late afternoon sun filters through the blinds, casting long shadows across a cluttered dorm room. Books, papers, and empty snack wrappers are scattered haphazardly across the floor, a testament to the chaotic energy of finals week."
    
    "PLAYER, her dark hair pulled into a messy bun, sits hunched over her laptop, the glow of the screen illuminating the intricate henna tattoos on her left hand."

    P "I can't focus. Complex systems theory is proving to be...well, complex. My eyes glaze over the lines of code and algorithms, and my mind starts to drift."

    "Alex, sprawled across the floor amidst a sea of open books, lets out a dramatic sigh."

    A "Okay, I officially surrender to the forces of academia. My brain is officially mush."

    "PLAYER chuckles, a welcome distraction from her studies."

    P "Don't worry, Alexa. We're almost through this. Just a few more hours of this delightful torture."

    "Alex groans dramatically, then reaches for a half-eaten slice of pizza."

    A "If caffeine and sugar were the keys to academic success, we'd all be Nobel laureates by now."

    "A comfortable silence settles over the room, punctuated only by the rhythmic tapping of Leoni's keyboard from his beanbag chair in the corner."

    L "Hey, have either of you seen Felix today? He hasn't answered any of my texts."

    "Anya sits up, a mischievous glint in her eyes."

    A "Oh, you know Felix. He's probably off chasing UFOs or decoding secret messages in the cafeteria's meatloaf."

    "PLAYER smiles, but the worry doesn't quite fade. Felix, their conspiracy-obsessed friend, had been acting strangely lately. His usual playful banter had taken on a darker tone, his excitement about his BioSyn internship replaced by a growing unease."

    A "Actually, now that you mention it... he seemed a little freaked out this morning. Almost like he was...scared"

    L "Scared? Of what?"

    A "I don't know. He was mumbling something about his internship at BioSyn, some experiment called NeuroMend... It was all very cryptic."

    "Suddenly, the dorm room door is thrown open, slamming against the wall with a resounding crash."

    "Felix bursts into the room, his eyes wide with terror, his chest heaving as if he'd been running for miles. His usually meticulously styled hair was a tangled mess, and his clothes were rumpled and stained."

    F "(Gasping for air, his voice barely a whisper) BioSyn! They're not what they seem. This... this is everything. Trust no one."

    "With trembling hands, he thrusts a battered flash drive into PLAYERS's outstretched palm."

    menu:

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        e "Games without menus are called kinetic novels, and there are dozens of them available to play."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
    return 


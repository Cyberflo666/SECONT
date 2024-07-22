#Smoke and Algorithms - Project 2024 SECont 

default PN = "Max"
default gender = "neutral"
default heshe = "they"
default himher = "them"
default hishers = "their"


# Level related variables:
define follow = False
define check = False
define ignore = False


label level_0_start:
    play music suspense_music1 volume loudness
    
    "Buckle up for a journey where trust is a weapon, truth is a labyrinth, and the choices you make could unravel a conspiracy that reaches far beyond the walls of your imagination."

    $ PN = renpy.input("Enter your name.", "Max", length=15, exclude=" 0123456789+=,.?!<>@[]{}").strip() 
    
#    menu:
#        "Are you..."
#        "A Boy":
#            $ gender = "male"
#            $ heshe = "he"
#            $ himher = "him"
#            $ hishers = "his"
#        "A Girl":
#            $ gender = "female"
#            $ heshe = "she"
#            $ himher = "her"
#            $ hishers = "hers"
#        "Non-Binary":
#            $ gender = "neutral" 
    "Welcome [PN]. Let's get on with the story."



label dorm_1:
    play music funky_music1 volume loudness fadeout 1.0
    scene bg new kitchen
    with dissolve

    "The late afternoon sun filters through the blinds, casting long shadows across a cluttered dorm room. Books, papers, and empty snack wrappers are scattered haphazardly across the floor, a testament to the chaotic energy of finals week."
    
    "You sit hunched over your laptop, the glow of the screen illuminating the intricate henna tattoos on your left hand."

    PC "I can't focus. Complex systems theory is proving to be... well, complex."

    show alex neutral at alex_right
    with dissolve 

    "Alex, sprawled across the floor amidst a sea of open books, lets out a dramatic sigh."

    show alex smile at alex_right
    with dissolve 

    A "Okay, I officially surrender to the forces of academia. My brain is officially mush."

    "You chuckle, a welcome distraction from your studies."

    PC "Don't worry, Alex. We're almost through this. Just a few more hours of this delightful torture."
    
    "Alex groans dramatically, then reaches for a half-eaten slice of pizza."

    show alex neutral at alex_right
    with dissolve 

    A "If caffeine and sugar were the keys to academic success, we'd all be Nobel laureates by now."
    
    show leonie neutral at left
    with dissolve 

    "A comfortable silence settles over the room, punctuated only by the rhythmic tapping of Leonie's keyboard from her beanbag chair in the corner."

    show leonie sad at left
    with dissolve

    L "Hey, have either of you seen Felix today? He hasn't answered any of my texts."

    "Alex sits up, a mischievous glint in his eyes."

    show alex smile at alex_right
    with dissolve 

    A "Oh, you know Felix. He's probably off chasing UFOs or decoding secret messages in the cafeteria's meatloaf."

    "You smile, but the worry doesn't quite fade. Felix, their conspiracy-obsessed friend, had been acting strangely lately. His usual playful banter had taken on a darker tone, his excitement about his internship at {color=[medievilColor]}Medievil{/color} replaced by a growing unease."

    show alex serious2 at alex_right
    with dissolve

    A "Actually, now that you mention it... he seemed a little freaked out this morning. Almost like he was... scared."

    show leonie surprised at left
    with dissolve 

    L "Scared? Of what?"
    show alex serious1 at alex_right
    with dissolve

    A "I don't know. He was mumbling something about his internship at {color=[medievilColor]}Medievil{/color}, some experiment called \"NeuroMend\"... It was all very cryptic."

    hide alex
    hide leonie
    with dissolve

    stop music
    "Suddenly, the dorm room door is thrown open, slamming against the wall with a resounding crash."

    show felix running at center
    with dissolve 

    "Felix bursts into the room, his eyes wide with terror, his chest heaving as if he'd been running for miles. His usually meticulously styled hair was a tangled mess, and his clothes were rumpled and stained."

    show felix shouting at center 
    with dissolve

    "Felix gasps for air, his voice barely a whisper"

    F " {color=[medievilColor]}Medievil{/color}! They're not what they seem. This... this is everything. Trust no one."

    "With trembling hands, he thrusts a battered flash drive into your hand, then turns and flees, disappearing into the dimly lit hallway."

    hide felix
    with dissolve

    play music mystery_music1 volume loudness 
    "The air crackles with tension, and a million thoughts race through your mind. What was that all about? Why is Felix so scared? What's on this flash drive? It feels heavy in your hand."

    show alex surprised at alex_right
    show leonie surprised at left
    with dissolve 

menu:
    "Try to go after him.":
        PC "We can't just let him run off like that. He's obviously terrified. Something's wrong."
        jump choice0_follow
    
    "Look what is on the drive he handed to you.":
        PC "He said this was important. Maybe it has answers. Leoni, can you take a look?"
        jump choice0_check

    "Try not to get involved.":
        PC "This looks like it could be dangerous. Maybe we should stay out of it."
        jump choice0_ignore
        


label choice0_ignore:

        scene bg new kitchen
        with dissolve

        show alex serious2 at alex_right
        with dissolve

        A "Are you serious? [PN], Felix is our friend. We can't just abandon him!"

        show leonie thinking at left
        with dissolve

        L "Besides, curiosity is killing me. I want to know what's on that drive."

        "You're hesitatant, torn between caution and concern for your friend."

        show alex neutral at alex_right
        with dissolve

        A "Exactly! And that's why we need to find out. Come on, [PN], let's go after him."

        show leonie serious at left
        with dissolve
   
        L "I'll stay here and see if I can find anything on the drive. Maybe it'll give us some clues."

        "You hesitate, torn between caution and concern for your friend. But the weight of the unknown proves too heavy. You sink back onto your bed, a sense of unease settling in."

        show alex surprised at alex_right 
        with dissolve

        A "Seriously? We're just going to let him disappear? What if he's in real trouble?"

        PC "I... I don't know what to do. I'm scared."

        "Leonie looks up from her laptop, her expression a mix of concern and determination."

        show leonie sad at left
        with dissolve

        L "I'm not finding anything on this drive yet. It's encrypted. But I'll keep trying. In the meantime, maybe we should just... wait and see?"

        hide alex

        hide leonie

        "Hours turn into days, and Felix remains missing. The unanswered questions gnaw at you, a constant reminder of your inaction. The flash drive remains a mystery, its secrets locked away."

        "Weeks later, a small article buried in a conspiracy theory tabloid catches your eyes. The headline reads: 'Shocking Discovery: Human DNA Found in Dog Food.'"

        "A chill runs down your spine. The article details a bizarre finding at a local pet food factory, a trace of human genetic material amidst the meat and grains. The source of the DNA remains unknown, the investigation ongoing."

        "You can't shake the feeling that this is somehow connected to Felix, to {color=[medievilColor]}Medievil{/color}, to the cryptic warning he delivered that fateful night. But without proof, it's just another unsolved mystery, a whisper in the wind."

        "The weight of regret settles heavily on your shoulders. The choice to ignore Felix's plea, to prioritize safety over friendship, has left a bitter taste in your mouth. The story ends not with a bang, but with a whimper, a silent echo of what could have been."

        jump game_over 
 
label choice0_check:

        scene bg new kitchen
        show leonie sad at left
        show alex serious1 at alex_right
        with dissolve

        show leonie serious at left
        with dissolve
        
        "Leonie nods, taking the flash drive from you. She plugs it into her laptop and begins examining its contents."

        "Her fingers fly across the keyboard, a series of complex commands appearing on the screen."

        L "It's encrypted... heavily. This isn't something I can crack easily. We'll need more information, maybe something in Felix's room can help."

        PC "His room? You think he might have left something behind?"


        jump level_1_start

label choice0_follow:
        scene bg hallway blur
        with dissolve

        "You rush out of the door, following the direction Felix took. Alex and Leonie exchange a worried glance before hurrying after you."

        "The hallway is dimly lit, the air heavy with the scent of stale pizza and disinfectant. Felix is nowhere to be seen. you quicken your pace, as your heart is pounding harder and harder."

        A "Felix! Where are you?"

        "Their voices echo down the empty corridor, but there's no response. They search every nook and cranny, every possible hiding spot, but Felix is gone."

        PC "Damn it! We lost him."

        "Defeated, they return to the dorm room, the silence amplifying their worry. Leonie picks up the flash drive Felix left behind, a sense of urgency washing over her."

        L "We have to figure out what's on this drive. Maybe it holds the answers to where Felix went and what he's so scared of."

        $ follow = False

        $ check = True

        jump choice0_check


return 
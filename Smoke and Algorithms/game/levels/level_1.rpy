$ renpy.include("inventory.rpy")

#Smoke and Algorithms - Project 2024 SECont

define window_not_done = True
define lock_not_done = True
define book_seen = False
define poster_seen = False
define calendar_seen = False
define map_seen = False
define newspaper_seen = False



label level_1_start:
    scene bg common area
    with dissolve

    show alex neutral:
        xalign 1.65
        yalign -0.8

    show leoni neutral at left
    with dissolve


    A "We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."

menu:
    "Yes, we should go to the police and hand them the drive, they will know what to do":
        jump choice_1_1_police
    
    "He must have left us some info on how to get access to this data. Let's take a look into his room":
        jump choice_1_1_room

label choice_1_1_police:
    show bg police
    with dissolve

    "The police take the flash drive as evidence and you don't ever hear anything of the case again."
    "...or of Felix."
    jump game_over

label choice_1_1_room:
    show bg hallway
    with dissolve

    "You step out into the hallway and head towards Felix's room but find out that it's locked."
    show bg felix door
    show leoni serious at left
    L "As I expected, too bad he is too paranoid to let his door open like the rest of us."
    jump choice_1_1_done

label choice_1_1_done:
    show bg felix door
    show leoni neutral at left
    show alex smile at alex_right
    with dissolve

    A "So. Anyone's got a clue as to how we're going to get into his room"

label menu_1_2:
    show bg felix door
    show leoni neutral at left
    show alex neutral at alex_right
    with dissolve

menu:
    "Take a look at his windows" if window_not_done:
        PC "His windows, if they're still open, Leonie can climb up there and open the door from inside"
        show leoni surprised at left
        with dissolve

        L "What..."
        show alex happy at alex_right
        with dissolve

        A "Good idea, you're probably the smallest one of us so you're most likely to fit through"
        show leoni thinking at left
        with dissolve

        L "Well if you insist it's worth a try i guess"
        jump choice_1_2_windows


    "Get help from the Janitor":
        PC "The janitor probably has a master key. Maybe we can ask him for help?"
        show leoni thinking at left
        with dissolve

        L "If he opens up random rooms by request, he'd be a pretty poor janitor."

        show alex neutral at alex_right
        with dissolve

        A "Right, but maybe we can trick or pay him."

        show leoni neutral at left
        with dissolve

        L "Or steal his key"
        PC "Really???"

        show leoni serious at left
        with dissolve

        L "Its an emergency. And it's not like we're going to keep it"
        jump choice_1_2_janitor

    "Pick the lock" if lock_not_done:
        PC "Can one of you pick locks. Shouldn't be too hard right?"
        show leoni serious at left
        with dissolve

        L "I have a few paper clips in my room we could use, but no idea how to pick a lock with the."
        show alex happy at alex_right
        with dissolve

        A "Me neither, but we can look up a tutorial on the internet. Should be fine."
        PC "If Leonie has enough paper clips to spare"
        jump choice_1_2_lock_pick

label choice_1_2_windows:
    scene bg windows
    with dissolve

    "Looks like luck is not on your side today. The window to his room is closed and there is no way to open it except brute force."
    "Since you neither want to break your friends window nor get in trouble with the janitor you decide to look for another way in."
    $ window_not_done = False
    jump menu_1_2

label choice_1_2_lock_pick:
    "After dismanteling 13 paper clips and watching the tutorial for the 6th time you decide that there may yet be a better way to get inside."
    $ lock_not_done = False
    jump menu_1_2

label choice_1_2_janitor:
menu:
    "Try to impersonate as Felix to get him to open the door" :
        PC "I think you have the best chances Alex"
        show alex neutral at alex_right
        with dissolve

        A "Yeaaah, im not so sure about that"
        show leoni thinking at left
        with dissolve

        L "Dont be so humble. Your the most charismatic out of us and your Felix impression is unmatched. Besides you look the most like him"
        show alex smile at alex_right
        with dissolve

        A "Thats great and all but I think we're counting on him not knowing who felix is, because otherwise we're screwed"
        PC "Either way you're our best shot and we need to get into this room"
        show leoni neutral at left
        with dissolve

        L "And since we a re Felixe's room mates we can back up your story"
        show alex neutral at alex_right
        with dissolve

        A "Alright alright I'll do it but you better have my back"
        show leoni happy at left
        with dissolve

        L "Sure thing Felix"
        A "Ha Ha"
        show bg hallway
        with dissolve

        "All three of you head out to find the janitor. Traversing the building you see him in a hallway heading your dircetion"
        PC "Showtime Alex."
        A "Pshhh."
        "You approach the janitor trying to hide your true intentions"
        show janitor neutral1 at janitor_right
        show alex neutral at alex_midleft
        with dissolve

        A "Excuse me, my name is Felix and I wanted to ask if you can open my room for me. It looks like I've lost my key"

        show janitor thinking at janitor_right
        with dissolve

        J "(he looks at you slightly annoyed and suspicious) whats your last name?"
        A "Felixson" 
        show janitor neutral2 at janitor_right
        with dissolve

        J "One second.\" (he checks his phone for a few moments) \"You're from room 014?"
        A "Yes."
        J "And you two are?"
        show leoni neutral at left
        with dissolve

        L "Leonie."
        PC "[PN]."
        L "His roommates"
        "(he checks his phone again:)"
        show janitor thinking at janitor_right
        with dissolve

        J "Ah okay I see. Well, lets go to your room shall we."
        show bg felix door
        "The four of you go to felix's room where the janitor opens the door for you."
        show janitor neutral1 at janitor_right
        with dissolve

        J "So about a replacement key..."
        show alex smile at alex_midleft
        with dissolve

        A "That wont be necessary. I've just got a message from a friend who found my key. Seems like i forgot them at his place."
        show janitor angry at janitor_angry_right
        with dissolve
        J "And you didn't think of that before?."

        A "Well... "
        show alex neutral at alex_midleft
        with dissolve

        A "Apperently not."
        show janitor thinking at janitor_right
        with dissolve

        "the janitor looks at Alex with disapprovement"
        A "Still. Thanks a lot for helping me out."
        J "Just don't lose them again you hear me"
        A "I promise"
        show janitor smile at janitor_right
        with dissolve

        "He takes his leave and you gained access to Felix's room:"
        hide janitor
        with dissolve

    
    "Bribe the janitor":
        show alex smile at alex_right
        with dissolve

        A "Everyone is vulnerable to money"
        A "If I offer him a few bucks he surely won't say no to lending us his keys for a minute"
        PC "All right Alex, you have my trust"
        show bg hallway
        hide alex
        with dissolve

        "Alex leaves behind the corner and heads to the janitor."
        "You hear a loud exchange of words and soon after Alex returns defeated"
        show alex neutral at alex_right
        with dissolve

        A "He said wasn't taking any money from me"

        show leoni sad at left
        with dissolve

        L "Damn, I suspect he won't fall for any of our tricks now"
        jump game_over

    "Steal the keys from the janitor":
        PC "How about I go grab his keys"
        show alex neutral at alex_right
        with dissolve

        A "I'm not so sure this is a good idea"
        PC "Leave it to me. I've seen it in plenty of movies"
        scene bg hallway
        with dissolve


        show janitor neutral2 at janitor_middle
        with dissolve

        "As you approach the janitor you stumble in front of him on purpose, fall right onto him and get a hold of his key chain"

        show janitor angry at janitor_angry_middle
        show bg hallway blur
        with vpunch

        "The victorious spirits start rushing to your brain, but as you pull on his keys they won't come loose"
        scene bg stars
        with vpunch

        "The janitor, visibly furious of what stunt you're trying to pull off here, grabs you by the shirt and shoves you against the wall"
        jump game_over

label felix_room:
    scene bg felix room
    show alex neutral at alex_right
    show leoni neutral at left
    with dissolve


    L "Wow, this room is quite messy."

    show alex smile at alex_right
    with dissolve

    A "Well, Felix did leave in a rush."
    PC "Let's focus on why we're here. We don't have time to waste. Who knows if and when the janitor will return to lock the door."
    
    show alex neutral at alex_right
    with dissolve

    A "What exactly are we looking for, anyway?"

    show leoni thinking at left
    with dissolve

    L "Typically, people choose passwords they can easily remember. Given Felix's conspiratorial nature, I doubt he has something simple like \"qwerty\" , \"123456\" or \"password.\" Let's look around for any hints."

label felix_room_menu:

    scene bg felix room
    show screen felixes_bin
    show screen felixes_bed
    show screen felixes_pc
    show screen felixes_notebook
    show screen felixes_map
    show screen felixes_wall1
    show screen felixes_wall2
    show screen felixes_wall3
    show screen phone_icon
    with dissolve

    "use your phone to crack the password"
menu:
    

    "Pull the phone out to crack the password":
        jump phone_minigame
        #add minigame

label notebooks:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f notebooks zoom
    with dissolve

    "Looking through his books you find a few books about cyber security, one book about the fall of the roman empire and a few books about conspiracy theories."
    "One worn down book especially catches your sight. It's about the [[9/11] attacks and seems to have quite a few sticky notes and annotations in it."
    $ book_seen = True
    jump felix_room_menu
label bin:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f bin zoom
    with dissolve

    "You close your nose with your fingers as you lean down uppon the trash bin. This is not the day to be pettily. You force yourself to take aside some old pizza crusts and used tissues."
    "After the bin is empty you accept that you'll probably only find trash and put the garbage back into the bin."
    jump felix_room_menu
label bed:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f bed zoom
    with dissolve

    "Under Felix's bed located, are some dirty clothes, empty bottles, and spiderwebs"
    jump felix_room_menu
label wall2:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f wall2 zoom
    with dissolve

    "you catch sight of a portal poster. The following quote sticks out:\"the cake is a lie\""
    $ poster_seen = True
    jump felix_room_menu
label wall3:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f wall3 zoom
    with dissolve

    "your eyes meet a Calendar with marked dates. A red circled date [[04/17] labeld with \"Half Life 3\" stands out"
    $ calendar_seen = True
    jump felix_room_menu
label map:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f map zoom
    with dissolve

    "You catch sight of a Nevada map, with multiple pins on an specific Area. Written beneath it reads [[Area51]"
    $ map_seen = True
    jump felix_room_menu
label wall1:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f wall1 zoom
    with dissolve

    "you see some hung up newspaper articles about some apparent proof that the earth is actually flat"
    $ newspaper_seen = True
    jump felix_room_menu
label pc:
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_icon
    scene bg f pc zoom
    with dissolve

    "you try to get access to his PC but it's password protected"
    L "who would have thought"
    jump felix_room_menu


label phone_minigame:    
label password_cracked:
    show leoni happy at left
    with dissolve

    L "Nice that did it. Time to see why he was so stressed out."
    "You see Felix's notes about his work at biosync. At first there is nothing unusual but the deeper you go, the more distressed the writing becomes. He seems to have discovered some kind of conspiracy about the implants from biosync. One name pops up several times throughout the files. \"Bob Anderson\""
    PC "Is he talking about the implants from biosync? I thought they're used to treat diseases"
    show alex neutral at alex_right
    with dissolve

    A "Neurological disorders, yes."
    show leoni neutral at left
    with dissolve

    L "Well, according to him biosync is looking to use them for something else, but he doesn't specify what. Only that its about profit and he thinks its dangerous."
    show alex surprised at alex_right
    with dissolve

    A "And whats up whit Bob Anderson. Any clue who that guy is."
    show leoni serious at left
    with dissolve

    L "Looks like he's Felixes supervisor or something."
    PC "Is this shit real or is Felix just getting too far into his conspiracy obsession."
    show alex neutral at alex_right
    with dissolve

    A "I dont know, but he seemd really scared today. Maybe there is really more to it"
    show leoni neutral at left
    with dissolve

    L "Yeah. I've never seen him like that before. Do you think they were onto him. I mean why would he give us the flash drive in such a hurry. Maybe he's been kidnapped."
    show alex neutral at alex_right
    with dissolve

    A "Thats a pretty big jump your taking dont you think. From what we know there is no hard evidence against biosync and Felix is not known to be the most rational person."
    show leoni thinking at left
    with dissolve

    L "Yes yes but he's not here and he hasn't answered any of our calls. Do you not think that's odd even form him."
    PC "Maybe he wants us to investigate biosyn. I mean what else is the drive good for other than raising our suspicion."
    show alex neutral at alex_right
    with dissolve

    A "If you think there is actually something messed up going on than maybe going to the police should be our next move."

menu:
    "Go to the police with the information you got":
        "You go to the police and show them the information you got from the drive. They ask you questions about Felix and the answers make it sound like Felix is making this whole story up."
        "The fact that you have no hard evidence to show also doesn't help. In the end the police claims the drive as property of biosync and puts out a missing person report"
        show leoni neutral at left
        with dissolve

        L "Good thing I made a copy of everything so we didn't lose anything."
        show alex neutral at alex_right
        with dissolve

        A "At least now we know that the police wont be much help against biosync. Looks like we're on our own"
        jump investigate_biosync

    "Investigate on your own what is happening at biosync":
        jump investigate_biosync

label investigate_biosync:
    "to be continued"


label game_over:
    scene kommt noch
    show alex laughing:
        zoom 6.0
        xalign 0.5
        yalign 0.24
    "YOU DIED"

return
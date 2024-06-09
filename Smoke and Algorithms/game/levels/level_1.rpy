$ renpy.include("inventory.rpy")

#Smoke and Algorithms - Project 2024 SECont

define window_not_done = True
define lock_not_done = True
define book_seen = False
define poster_seen = False
define calendar_seen = False
define map_seen = False
define newspaper_seen = False
define password_icon = True

define trust = 40
define trust_delta = 20

label level_1_start:
    show alex serious2 at alex_right
    A "We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."

menu:
    "Yes, we should go to the police and hand them the drive, they will know what to do":
        jump choice_1_1_police
    
    "He must have left us some info on how to get access to this data. Let's take a look into his room":
        jump choice_1_1_room

label choice_1_1_police:
    scene bg police station
    with dissolve

    "The police take the flash drive as evidence and you don't ever hear anything of the case again."
    "...or of Felix."
    jump game_over

label choice_1_1_room:
    scene bg felix door
    with dissolve

    "You step outside the kitchen and head towards Felix's room but find out that it's locked."
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    L "As I expected, too bad he is too paranoid to let his door open like the rest of us."
    jump choice_1_1_done

label choice_1_1_done:
    show bg felix door
    show alex serious2 at alex_right
    with dissolve

    A "So. Anyone's got a clue as to how we're going to get into his room"

label menu_1_2:
    show bg felix door
    show leonie sad at left
    show alex serious2 at alex_right
    with dissolve

play music main_music1 volume loudness fadeout 1.0
menu:
    "Take a look at his windows" if window_not_done:
        PC "His windows, if they're still open, Leonie can climb up there and open the door from inside"
        show leonie surprised at left
        with dissolve

        L "What..."
        show alex happy at alex_right
        with dissolve

        A "Good idea, you're probably the smallest one of us so you're most likely to fit through"
        show leonie thinking at left
        with dissolve

        L "Well if you insist it's worth a try i guess"
        jump choice_1_2_windows


    "Get help from the Janitor":
        PC "The janitor probably has a master key. Maybe we can ask him for help?"
        show leonie thinking at left
        with dissolve

        L "If he opens up random rooms by request, he'd be a pretty poor janitor."

        show alex neutral at alex_right
        with dissolve

        A "Right, but maybe we can trick or pay him."

        show leonie neutral at left
        with dissolve

        L "Or steal his key"
        PC "Really???"

        show leonie serious at left
        with dissolve

        L "Its an emergency. And it's not like we're going to keep it"
        jump choice_1_2_janitor

    "Pick the lock" if lock_not_done:
        PC "Can one of you pick locks. Shouldn't be too hard right?"
        show leonie serious at left
        with dissolve

        L "I have a few paper clips in my room we could use, but no idea how to pick a lock with them."
        show alex happy at alex_right
        with dissolve

        A "Me neither, but we can look up a tutorial on the internet. Should be fine."
        PC "If Leonie has enough paper clips to spare"
        jump choice_1_2_lock_pick

label choice_1_2_windows:
    scene bg window view
    with dissolve

    "Looks like luck is not on your side today. The window to his room is closed and there is no way to open it except brute force."
    "Since you neither want to break your friends window nor get in trouble with the janitor you decide to look for another way in."
    $ window_not_done = False
    jump menu_1_2

label choice_1_2_lock_pick:
    scene bg felix door
    "After dismanteling 13 paper clips and watching the tutorial for the 6th time you decide that there may yet be a better way to get inside."
    $ lock_not_done = False
    jump menu_1_2

label choice_1_2_janitor:
menu:
    "Try to impersonate as Felix to get him to open the door" :
        jump help_from_janitor
    
    "Bribe the janitor":
        show alex smile at alex_right
        with dissolve

        A "Everyone is vulnerable to money"
        A "If I offer him a few bucks he surely won't say no to lending us his keys for a minute"
        PC "All right Alex, you have my trust"
        scene bg hallway
        with dissolve

        "All of you head into the hallway and Alex leaves behind the corner to find the janitor."
        show leonie thinking at left
        with dissolve

        "You hear a loud exchange of words and soon after Alex returns defeated"
        show alex serious1 at alex_right
        with dissolve

        A "He said wasn't taking any money from me"

        show leonie sad at left
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

        show janitor angry #at janitor_angry_middle
        show bg hallway blur
        with vpunch

        "The victorious spirits start rushing to your brain, but as you pull on his keys they won't come loose"
        scene bg stars
        with vpunch

        "The janitor, visibly furious of what stunt you're trying to pull off here, grabs you by the shirt and shoves you against the wall"
        jump game_over_police


label help_from_janitor:
    PC "I think you have the best chances Alex"
    show alex serious1 at alex_right
    with dissolve

    A "Yeaaah, im not so sure about that"
    show leonie thinking at left
    with dissolve

    L "Dont be so humble. Your the most charismatic out of us and your Felix impression is unmatched. Besides you look the most like him"
    show alex serious2 at alex_right
    with dissolve

    A "Thats great and all but I think we're counting on him not knowing who felix is, because otherwise we're screwed"
    PC "Either way you're our best shot and we need to get into this room"
    show leonie neutral at left
    with dissolve

    L "And since we a re Felixe's room mates we can back up your story"
    show alex neutral at alex_right
    with dissolve

    A "Alright alright I'll do it but you better have my back"
    show leonie happy at left
    with dissolve

    L "Sure thing Felix"
    show alex serious1 at alex_right
    with dissolve

    A "Ha Ha"
    scene bg hallway
    with dissolve

    "All three of you head out to find the janitor. Traversing the building you see him in a hallway heading your dircetion"
    PC "Showtime Alex."
    show leonie serious at left
    show alex neutral at alex_right
    with dissolve

    L "Pay attention to what he's saying and react accordingly"
    show alex serious1 at alex_right
    with dissolve

    A "Pshhh i know."
    hide leonie
    hide alex
    with dissolve
    "Alex approaches the janitor trying to hide his true intentions"
    show janitor neutral2 at janitor_right
    show alex smileleft at alex_left
    with dissolve

    A "Excuse me, my name is Felix and I wanted to ask if you can open my room for me. It looks like I've lost my key"
    
    show janitor neutral1 at janitor_right
    with dissolve
    show screen round_rect(trust)
    with dissolve

    menu:
        J "Is this urgent? I'm already on my way to help with the printers and I've got my hands full of work."
        "Understanding that his hands  are full":
            show alex surprisedleft at alex_left
            with dissolve
            A "Jm sorry that your hands are full of work however I really have to get into my room and I can't find my keys. Our assignment is due in an hour and we need a book in my room to complete it"
            $ trust += trust_delta
        
        "Should be easy":
            show alex happyleft at alex_left
            with dissolve
            A "unfortunately I've somehow lost or misplaced my keys and I have to get in. Unlocking a door shouldnt take all too long."
            $ trust -= trust_delta

        "Its very urgent":
            show alex surprisedleft at alex_left
            with dissolve
            A "please help us this is very urgent. I've miss placed my key and there are things inside my room I really need"
            $ trust -= trust_delta
 

    call janitor_look(trust)
    show screen round_rect(trust)

    menu:
        J "Have you tried looking for your key? How about tracing back your last steps?"
        "Already looked":
            show alex smileleft at alex_left
            with dissolve
            A "We already looked in our dorms but found nothing"
            $ trust -= trust_delta

        "traced back every step":
            show alex neutralleft at alex_left
            with dissolve
            A "The first thing we did was trace back every one of our steps"
            $ trust += trust_delta

        "isn't this your job to help":
            show alex serious2left at alex_left
            with dissolve
            A "Isn't this your job, now go and help us"
            $ trust -= trust_delta

    call janitor_look(trust)
    show screen round_rect(trust)

    menu:
        J "Let me see your ID. I can't just give out access without verifying this kinda stuff."
        "that's personal information":
            show alex angryleft at alex_left
            with dissolve
            A "No, you have no right to see personal information like that"
            $ trust -= trust_delta
        
        "Left the ID at my parents place":
            show alex surprisedleft at alex_left
            with dissolve
            A "Im soo sorry, I left my ID at my parent's over the weekend. Maybe you could make an exception"
            $ trust += trust_delta

        "lost it":
            show alex surprisedleft at alex_left
            with dissolve
            A "Ive lost it a couple of days ago im sorry."
            $ trust -= trust_delta

    call janitor_look(trust)
    show screen round_rect(trust)

    menu:
        J " Well, I'm not so sure if I'll be able to let you in then . I don't want to get in trouble with Mrs Mill again."
        "I wont tell anyone":
            show alex neutralleft at alex_left
            with dissolve
            A "I won't rat you out. Come on just help me this one time"
            $ trust -= trust_delta

        "I'll explain to Mrs Mill":
            show alex serious2left at alex_left
            with dissolve
            A "That won't be a problem, I'll call Mrs Mill first thing tomorrow to explain the situation"
            $ trust += trust_delta

        "the office would understand":
            show alex serious2left at alex_left
            with dissolve
            A "I'm sure the office will understand you helping out a student in need"
            $ trust -= trust_delta

    call janitor_look(trust)
    show screen round_rect(trust)
    
    if trust > 75:
        J "Well you seem to be honest."
        J "Lets go to your room then shall we."
        hide screen round_rect
        jump janitor_trust
    else:
        hide screen round_rect
        J "Your not going to fool me. Who are you really"
        scene bg hallway
        "After being pressured by the janitor alex admits he is not felix and gets kicked out of the building and his rental contract."
        jump game_over

label janitor_trust:
    show bg felix door 
    show janitor neutral2 at janitor_right
    show leonie happy at left
    show alex smile at alex_midleft
    with dissolve

    "The four of you go to felix's room where the janitor opens the door for you."
    show janitor neutral1 at janitor_right
    with dissolve

    J "So about a replacement key..."
    show alex happy at alex_midleft
    with dissolve

    A "That wont be necessary. I've just got a message from a friend who found my key. Seems like i forgot them at his place."
    show janitor angry #at janitor_angry_right
    with dissolve
    J "And you didn't think of that before?."
    show alex serious1 at alex_midleft
    with dissolve

    A "Well... "

    A "Apperently not"

    "the janitor looks at Alex with disapprovement"
    show alex smile at alex_midleft
    with dissolve

    A "Still. Thanks a lot for helping me out"
    show janitor thinking at janitor_right
    with dissolve

    J "Just don't lose them again you hear me"
    show alex neutral at alex_midleft
    with dissolve

    A "I promise"
    show janitor neutral2 at janitor_right
    with dissolve

    "He takes his leave and you gained access to Felix's room"
    hide janitor
    with dissolve


play music suspense_music1 volume loudness fadeout 1.0
label felix_room:
    scene bg felix room
    with dissolve

    "As you go through the door a gust of bad air comes your way"
    show alex serious1 at alex_right
    show leonie serious at left
    with dissolve


    L "Wow, this room is quite messy. And it smells like something died in here"

    show alex neutral at alex_right
    with dissolve

    A "Well, we know Felix and he did leave in quite a rush"
    PC "Let's focus on why we're here. We don't have time to waste. Who knows if and when the janitor will return to lock the door."
    
    show alex serious2 at alex_right
    with dissolve

    A "What exactly are we looking for, anyway?"

    show leonie thinking at left
    with dissolve

    L "Typically, people choose passwords they can easily remember. Given Felix's conspiratorial nature, I doubt he has something simple like \"qwerty\" , \"123456\" or \"password.\" Let's look around for any hints."

    scene bg felix room
    "Investigate the room with your mouse"
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
    jump felix_room_menu

"""
menu:
    "Pull the phone out to crack the password":
        #add minigame
"""

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

    "You close your nose with your fingers as you lean down uppon the trash bin. This is not the day to be petty. You force yourself to take aside some old pizza crusts and used tissues."
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
    $ password_icon = False
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    hide screen phone_hand
    show screen phone_icon
    show leonie happy at left
    show alex neutral at alex_right
    with dissolve


    play music mystery_music1 volume loudness fadeout 1.0
    L "Nice that did it. Time to see why he was so stressed out."
    "You see Felix's notes about his work at biosync. At first there is nothing unusual but the deeper you go, the more distressed the writing becomes. He seems to have discovered some kind of conspiracy about the implants from biosync. One name pops up several times throughout the files. \"Bob Anderson\""
    PC "Is he talking about the implants from biosync? I thought they're used to treat diseases"
    show alex serious1 at alex_right
    with dissolve

    A "Neurological disorders, yes."
    show leonie neutral at left
    with dissolve

    L "Well, according to him biosync is looking to use them for something else, but he doesn't specify what. Only that its about profit and he thinks its dangerous."
    show alex surprised at alex_right
    with dissolve

    A "And whats up whit Bob Anderson. Any clue who that guy is."
    show leonie serious at left
    with dissolve

    L "Looks like he's Felixes supervisor or something."
    PC "Is this shit real or is Felix just getting too far into his conspiracy obsession."
    show alex neutral at alex_right
    with dissolve

    A "I dont know, but he seemd really scared today. Maybe there is really more to it"
    show leonie neutral at left
    with dissolve

    L "Yeah. I've never seen him like that before. Do you think they were onto him. I mean why would he give us the flash drive in such a hurry. Maybe he's been kidnapped."
    show alex serious1 at alex_right
    with dissolve

    A "Thats a pretty big jump your taking dont you think. From what we know there is no hard evidence against biosync and Felix is not known to be the most rational person."
    show leonie thinking at left
    with dissolve

    L "Yes yes but he's not here and he hasn't answered any of our calls. Do you not think that's odd even form him."
    PC "Maybe he wants us to investigate biosyn. I mean what else is the drive good for other than raising our suspicion."
    show alex neutral at alex_right
    with dissolve

    A "If you think there is actually something messed up going on than maybe going to the police should be our next move."

menu:
    "Go to the police with the information you got":
        scene bg police station
        "You go to the police and show them the information you got from the drive. They ask you questions about Felix and the answers make it sound like Felix is making this whole story up."
        "The fact that you have no hard evidence to show also doesn't help. In the end the police claims the drive as property of biosync and puts out a missing person report"
        show leonie serious at left
        with dissolve

        L "Good thing I made a copy of everything so we didn't lose anything."
        show alex serious1 at alex_right
        with dissolve

        A "At least now we know that the police wont be much help against biosync. Looks like we're on our own"
        jump investigate_biosync

    "Investigate on your own what is happening at biosync":
        jump investigate_biosync

label investigate_biosync:
    "to be continued"


label game_over:
    play music funky_music1 volume 1
    scene kommt noch
    show alex laughing:
        zoom 6.0
        xalign 0.5
        yalign 0.24
    "YOU DIED"

label game_over_police:
    scene bg jail 
    show alex laughing:
        zoom 6.0
        xalign 0.5
        yalign 0.24
    "YOU DIED"

return
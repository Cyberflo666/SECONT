$ renpy.include("inventory.rpy")

#Smoke and Algorithms - Project 2024 SECont

# Level related variables:
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
    with dissolve
    A "We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."

menu:
    "Take the drive to the police":
        PC "Yes, we should go to the police and hand them the drive, they will know what to do"
        jump choice_1_1_police
    
    "Take a look at his room to find more information":
        PC "He must have left us some info on how to get access to this data. Let's take a look into his room"
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

    "Lady Luck isn't on your side. The window is closed tight, and there's no way in without brute force."
    "You decide against breaking the window or angering the janitor, so you start looking for another way in."
    $ window_not_done = False
    jump menu_1_2

label choice_1_2_lock_pick:
    scene bg felix door
    "After mangling thirteen paper clips and rewatching the tutorial six times, you conclude there might be a better way inside."
    $ lock_not_done = False
    jump menu_1_2

label choice_1_2_janitor:
    $ gloss_bribery_seen = True
    $ gloss_impersonation_seen = True
menu:
    "Impersonate Felix to get the janitor to open the door":
        PC "Maybe one of us should pretend to be Felix and ask him to open the door."
        jump help_from_janitor
    
    "Bribe the janitor":
        PC "Do you think he's the type who'd take a bribe?"
        show alex smile at alex_right
        with dissolve

        A "Sure, everyone has a price. A few bucks should do the trick."
        PC "Alright, Alex. You have my blessing."
        scene bg hallway
        with dissolve

        "You head into the hallway, and Alex disappears around the corner to find the janitor."
        show leonie thinking at left
        with dissolve

        "You hear a heated exchange, and Alex returns looking defeated."
        show alex serious1 at alex_right
        with dissolve

        A "He wouldn't take my money."

        show leonie sad at left
        with dissolve

        L "Damn. I doubt he'll fall for any of our other tricks now."
        jump game_over

    "Steal the keys from the janitor":
        PC "How about I try to grab his keys?"
        show alex neutral at alex_right
        with dissolve

        A "I'm not so sure about that..."
        PC "Leave it to me. I've seen it done in plenty of movies."
        scene bg hallway
        with dissolve

        show janitor neutral2 at janitor_middle
        with dissolve

        "You approach the janitor and 'accidentally' stumble into him, grabbing his keychain."

        show janitor angry #at janitor_angry_middle
        show bg hallway blur
        with vpunch

        "Victory seems within reach, but the keys won't budge."
        scene bg stars
        with vpunch

        "The janitor, furious at your clumsy attempt, grabs your shirt and slams you against the wall."
        jump game_over_police


label help_from_janitor:
    PC "Alex, I think you're our best bet here."
    show alex serious1 at alex_right
    with dissolve

    A "Yeah, I'm not so convinced about that..."
    show leonie thinking at left
    with dissolve

    L "Don't sell yourself short. You're the smoothest talker of the bunch, and your Felix impression is dead-on. Plus, you even look a little bit like him."
    show alex serious2 at alex_right
    with dissolve

    A "That's all fine and dandy, but this whole plan falls apart if the janitor actually *knows* Felix."
    PC "We don't have many options, and we *need* to get into that room. You're our best shot."
    show leonie neutral at left
    with dissolve

    L "And remember, we're Felix's roommates. We can back up your story."
    show alex neutral at alex_right
    with dissolve

    A "Fine, fine. I'll do it. But if this blows up in our faces, it's on you two."
    show leonie happy at left
    with dissolve

    L "Good luck, 'Felix'!"
    show alex serious1 at alex_right
    with dissolve

    A "Very funny."
    scene bg hallway
    with dissolve

    "The three of you head out in search of the janitor. As you navigate the maze-like building, you spot him in a nearby hallway."
    PC "Showtime, Alex. Don't mess this up."
    show leonie serious at left
    show alex neutral at alex_right
    with dissolve

    L "Remember, pay attention to what he says and respond accordingly. Stay cool."
    show alex serious1 at alex_right
    with dissolve

    A "Yeah, yeah. I've got this."
    hide leonie
    hide alex
    with dissolve
    "Alex approaches the janitor, putting on his best 'Felix' act."
    show janitor neutral2 at janitor_right
    show alex smileleft at alex_left
    with dissolve

    A "Hey there! Felix here. Listen, could you possibly unlock my room for me? I seem to have lost my key."
    
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
            A "Unfortunately I've somehow lost or misplaced my keys and I have to get in. Unlocking a door shouldnt take all too long."
            $ trust -= trust_delta

        "Its very urgent":
            show alex surprisedleft at alex_left
            with dissolve
            A "Please help us this is very urgent. I've miss placed my key and there are things inside my room I really need"
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

        "Traced back every step":
            show alex neutralleft at alex_left
            with dissolve
            A "The first thing we did was trace back every one of our steps"
            $ trust += trust_delta

        "Isn't this your job to help":
            show alex serious2left at alex_left
            with dissolve
            A "Isn't this your job, now go and help us"
            $ trust -= trust_delta

    call janitor_look(trust)
    show screen round_rect(trust)

    menu:
        J "Let me see your ID. I can't just give out access without verifying this kinda stuff."
        "That's personal information":
            show alex angryleft at alex_left
            with dissolve
            A "No, you have no right to see personal information like that"
            $ trust -= trust_delta
        
        "Left the ID at my parents place":
            show alex surprisedleft at alex_left
            with dissolve
            A "Im soo sorry, I left my ID at my parent's over the weekend. Maybe you could make an exception"
            $ trust += trust_delta

        "Lost it":
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

        "The office would understand":
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

    "The four of you arrive at Felix's room, and the janitor unlocks the door."
    show janitor neutral1 at janitor_right
    with dissolve

    J "So, about getting you a replacement key..."
    show alex happy at alex_midleft
    with dissolve

    A "Oh, that won't be necessary. A friend just texted me. Seems I left my keys at their place after all."
    show janitor angry #at janitor_angry_right
    with dissolve
    J "You couldn't have figured that out *before* I dragged myself all the way over here?"
    show alex serious1 at alex_midleft
    with dissolve

    A "Well..."

    A "...apparently not."

    "The janitor shoots Alex a disapproving look."
    show alex smile at alex_midleft
    with dissolve

    A "But hey, thanks for the help anyway."
    show janitor thinking at janitor_right
    with dissolve

    J "Just try not to lose them again, okay?"
    show alex neutral at alex_midleft
    with dissolve

    A "I promise."
    show janitor neutral2 at janitor_right
    with dissolve

    "He leaves, and you've successfully gained access to Felix's room."
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
    show screen phone_icon

label felix_room_menu:
    scene bg felix room
    call show_felix_room_interactables
    with dissolve
    "use your phone to crack the password"
    jump felix_room_menu

"""
menu:
    "Pull the phone out to crack the password":
        #add minigame
"""

label notebooks:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f notebooks zoom
    with dissolve

    "Looking through his books you find a few books about cyber security, one book about the fall of the roman empire and a few books about conspiracy theories."
    "One worn down book especially catches your sight. It's about the [[9/11] attacks and seems to have quite a few sticky notes and annotations in it."
    $ book_seen = True
    $ notes.add_data(NoteData("info: 9/11"))
    show screen phone_icon
    jump felix_room_menu

label bin:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f bin zoom
    with dissolve

    "You close your nose with your fingers as you lean down uppon the trash bin. This is not the day to be petty. You force yourself to take aside some old pizza crusts and used tissues."
    "After the bin is empty you accept that you'll probably only find trash and put the garbage back into the bin."
    show screen phone_icon
    jump felix_room_menu

label bed:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f bed zoom
    with dissolve

    "Under Felix's bed located, are some dirty clothes, empty bottles, and spiderwebs"
    show screen phone_icon
    jump felix_room_menu

label wall2:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall2 zoom
    with dissolve

    "you catch sight of a portal poster. The following quote sticks out:\"the cake is a lie\""
    $ poster_seen = True
    $ notes.add_data(NoteData("info: \"the cake is a lie\""))
    show screen phone_icon
    jump felix_room_menu

label wall3:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall3 zoom
    with dissolve

    "your eyes meet a Calendar with marked dates. A red circled date [[04/17] labeld with \"Half Life 3\" stands out"
    $ calendar_seen = True
    $ notes.add_data(NoteData("info: 04/17 Half Life 3 release"))
    show screen phone_icon
    jump felix_room_menu

label map:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f map zoom
    with dissolve

    "You catch sight of a Nevada map, with multiple pins on an specific Area. Written beneath it reads [[Area51]"
    $ map_seen = True
    $ notes.add_data(NoteData("info: Area 51"))
    show screen phone_icon
    jump felix_room_menu

label wall1:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall1 zoom
    with dissolve

    "you see some hung up newspaper articles about some apparent proof that the earth is actually flat"
    $ newspaper_seen = True
    show screen phone_icon
    jump felix_room_menu

label pc:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f pc zoom
    with dissolve

    "you try to get access to his PC but it's password protected"
    L "who would have thought"
    show screen phone_icon
    jump felix_room_menu


label phone_minigame:    
label password_cracked:
    $ password_icon = False
    call hide_felix_room_interactables
    hide screen phone_hand
    show screen phone_icon
    show leonie happy at left
    show alex neutral at alex_right
    with dissolve


play music mystery_music1 volume loudness fadeout 1.0
label password_cracked:
    $ password_icon = False
    call hide_felix_room_interactables
    hide screen phone_hand
    show screen phone_icon
    show leonie happy at left
    show alex neutral at alex_right
    with dissolve

    L "Nailed it! Now let's see what has Felix so spooked."
    "You delve into Felix's notes on his work at Medievil. At first, everything seems normal, but the deeper you dig, the more frantic and desperate his writing becomes. It appears he stumbled upon some kind of conspiracy surrounding Medievil's implants. One name keeps popping up: 'Bob Anderson.'"
    PC "He's talking about those Medievil implants? I thought those were supposed to treat diseases."
    show alex serious1 at alex_right
    with dissolve

    A "Neurological disorders, to be specific."
    show leonie neutral at left
    with dissolve

    L "Well, according to Felix, Medievil has something else in mind for these implants. He doesn't elaborate, just mentions it's all about profit and that he believes they're dangerous."
    show alex surprised at alex_right
    with dissolve

    A "And who's this Bob Anderson guy? Any idea?"
    show leonie serious at left
    with dissolve

    L "Looks like he's Felix's supervisor or something."
    PC "Is this for real, or is Felix just going down another conspiracy rabbit hole?"
    show alex neutral at alex_right
    with dissolve

    A "I don't know, but he seemed genuinely terrified earlier. Maybe there's more to this than we thought."
    show leonie neutral at left
    with dissolve

    L "Definitely. I've never seen him like that. Do you think they were onto him? Why else would he dump that flash drive on us and take off? Maybe he's been kidnapped."
    show alex serious1 at alex_right
    with dissolve

    A "Hold on, let's not jump to conclusions. We don't have any hard evidence against Medievil, and Felix isn't exactly known for his levelheadedness."
    show leonie thinking at left
    with dissolve

    L "True, but he's gone, and he's not answering his phone. That's not like him, even for Felix."
    PC "Maybe he wants us to look into Medievil. I mean, what else would he give us this flash drive for, if not to raise our suspicions?"
    show alex neutral at alex_right
    with dissolve

    A "If you really think something shady is going on, maybe we should go to the police."

menu:
    "Go to the police with the information you got":
        scene bg police station
        "You take the information from the flash drive to the police. They grill you about Felix, and your answers make it sound like he's fabricated the whole thing."
        "Without any hard evidence, your story falls flat. The police confiscate the drive, claiming it's Medievil property, and file a missing person report for Felix."
        show leonie serious at left
        with dissolve

        L "At least I made a copy of everything, so we haven't lost all hope."
        show alex serious1 at alex_right
        with dissolve

        A "Well, that was a bust. Looks like the police aren't going to help us against Medievil. We're on our own now."
        L "Let's head back to the dorm and figure out our next move."
        PC "My laptop's still in the kitchen. Let's regroup there."

        jump level_2_start

    "Investigate on your own what is happening at Medievil":
        scene bg felix room
        show leonie thinking at left 
        show alex serious1 at alex_right
        with dissolve 
        PC "Alright then, let's do some digging on Medievil. We'll have more space to spread out in the kitchen."
        show alex serious2 at alex_right
        with dissolve
        A "Agreed. We need to move quickly. Who knows what's happened to Felix..."
        show leonie thinking at left 
        with dissolve 
        L "Medievil's a pretty big company. We should be able to find plenty of information online."
        PC "I'll handle the research since I left my laptop back in the kitchen."
        PC "Then we can follow up on Felix's lead and get to the bottom of this."
        with dissolve
        jump level_2_start



label game_over:
    play music funky_music1 volume 1
    scene kommt noch
    show alex laughing:
        zoom 6.0
        xalign 0.5
        yalign 0.24
    "YOU DIED"
return

label game_over_police:
    scene bg jail 
    show alex laughing:
        zoom 6.0
        xalign 0.5
        yalign 0.24
    "YOU DIED"
return
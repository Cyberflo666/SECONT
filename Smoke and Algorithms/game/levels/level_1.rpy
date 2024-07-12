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

    "Alex's voice is filled with a mix of concern and determination. He runs a hand through his hair, a nervous gesture that betrays his usual laid-back demeanor."

menu:
    "Take the drive to the police":
        PC "Yes, we should go to the police and hand them the drive. They will know what to do."

        "The words feel heavy as they leave your mouth. A part of you wants to believe that the authorities can handle this, that they can find Felix and bring him to safety. But doubt gnaws at the edges of your resolve."

        jump choice_1_1_police
    
    "Take a look at his room to find more information":
        PC "He must have left us some info on how to get access to this data. Let's take a look in his room."

        "A spark of hope flickers in your eyes. Maybe Felix, in his paranoia, has left behind a clue that can help you unlock the secrets of the flash drive."

        jump choice_1_1_room

label choice_1_1_police:
    scene bg police station
    with dissolve

    "The sterile atmosphere of the police station is a stark contrast to the cozy chaos of your dorm room. The fluorescent lights buzz overhead, casting harsh shadows on the worn linoleum floor. A sense of dread settles in your stomach as you hand over the flash drive to the stone-faced officer."

    "The officer's questions are sharp and relentless, probing for inconsistencies in your story. You stumble over your words, the weight of the situation bearing down on you. Without Felix to back you up, your account of his cryptic warning and sudden disappearance sounds increasingly far-fetched."

    "The officer's expression remains impassive as he informs you that they'll look into it. But you know, deep down, that this is the end of the line. The flash drive, the only tangible link to Felix and the truth, is now out of your hands."

    "As you leave the police station, the city lights blur into a kaleidoscope of despair. The silence is deafening, broken only by the echoes of your own footsteps. A sense of helplessness washes over you. You have failed Felix."

    "...or of Felix."

    jump game_over


label choice_1_1_room:
    scene bg felix door
    with dissolve

    "You approach Felix's door, its dark wood surface a blank canvas of mystery. The doorknob feels cold and unyielding under your touch. A sense of unease washes over you as you realize that the only way to find answers is to breach the sanctuary of your missing friend."

    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    L "As I expected. Too bad he's too paranoid to leave his door open like the rest of us."

    "Leoni's voice is laced with a hint of frustration, but her eyes betray a deeper worry. She glances at you and Alex, seeking reassurance in the face of the unknown."

    A "Let's not waste time. We need to find a way in."

    "Alex's voice is firm, his tone brooking no argument. He steps forward and examines the doorknob, his fingers tracing the intricate carvings."

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

    "You turn to Alex, your voice filled with a hopeful plea. He's always been the most charismatic of the three of you, a natural chameleon who can blend into any situation."

    show alex serious1 at alex_right
    with dissolve

    A "Yeah, I'm not so convinced about that..."

    "Alex runs a hand through his hair, his eyes darting nervously between you and Leoni. He's not thrilled about the idea of impersonating Felix, but the urgency of the situation is sinking in."

    show leonie thinking at left
    with dissolve

    L "Don't sell yourself short. You're the smoothest talker of the bunch, and your Felix impression is dead-on. Plus, you even look a little bit like him."

    "Leoni's voice is encouraging, her smile warm and reassuring. She places a hand on Alex's shoulder, her touch a silent gesture of support."

    show alex serious2 at alex_right
    with dissolve

    A "That's all fine and dandy, but this whole plan falls apart if the janitor actually *knows* Felix."

    "Alex's voice is laced with worry, his eyes wide with apprehension. The thought of being caught red-handed sends a shiver down your spine."

    PC "We don't have many options, and we *need* to get into that room. You're our best shot."

    "Your words are firm, your determination unwavering. You know that the stakes are high, but you also trust in Alex's ability to pull this off."

    show leonie neutral at left
    with dissolve

    L "And remember, we're Felix's roommates. We can back up your story."

    "Leoni's voice is steady, her confidence contagious. Alex takes a deep breath, his shoulders squaring with resolve."

    show alex neutral at alex_right
    with dissolve

    A "Fine, fine. I'll do it. But if this blows up in our faces, it's on you two."

    "Alex's voice is tinged with resignation, but a hint of excitement flickers in his eyes. He thrives on challenges, and this one is shaping up to be a doozy."

    show leonie happy at left
    with dissolve

    L "Good luck, 'Felix'!"

    "Leoni's playful jab earns her a mock glare from Alex."

    show alex serious1 at alex_right
    with dissolve

    A "Very funny."

    scene bg hallway
    with dissolve

    "The three of you head out in search of the janitor. The dorm hallways are strangely quiet, the usual buzz of student activity replaced by an eerie silence. Every creak of the floorboards and every flicker of the fluorescent lights amplifies your anxiety."

    "As you round a corner, you spot the janitor in the distance, his hunched figure silhouetted against the dim glow of a vending machine."

    PC "Showtime, Alex. Don't mess this up."

    "You squeeze Alex's arm, a silent message of encouragement."

    show leonie serious at left
    show alex neutral at alex_right
    with dissolve

    L "Remember, pay attention to what he says and respond accordingly. Stay cool."

    "Leoni's voice is low and serious, her eyes boring into Alex's. She's not one to mince words when the stakes are high."

    show alex serious1 at alex_right
    with dissolve

    A "Yeah, yeah. I've got this."

    "Alex takes a deep breath, plastering a confident smile on his face. He walks towards the janitor, his footsteps echoing in the empty hallway."

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

    "The tension in the air dissipates as the janitor's key turns in the lock. The door swings open, revealing the dimly lit interior of Felix's room."

    J "Alright, there you go. But seriously, try not to lose your keys again."

    "The janitor's tone is stern, but a hint of amusement flickers in his eyes. He seems to have enjoyed Alex's performance, despite his initial skepticism."

    show alex happy at alex_midleft
    with dissolve

    A "Thanks, I appreciate it. You're a lifesaver."

    "Alex flashes a charming smile, his Felix impersonation still firmly in place."

    show janitor thinking at janitor_right
    with dissolve

    "The janitor nods, a hint of a smile tugging at the corner of his lips. He turns to leave, but pauses for a moment, as if considering something."

    J "Hey, if you need anything else, just let me know. I'm always here to help."

    "His words are unexpected, a surprising departure from his usual gruff demeanor. You exchange a look with Leoni and Alex, a shared sense of astonishment washing over you."

    show alex neutral at alex_midleft
    with dissolve

    A "Will do. Thanks again."

    "The janitor nods once more and disappears down the hallway, leaving you and your friends standing at the threshold of Felix's room."

    hide janitor
    with dissolve

play music suspense_music1 volume loudness fadeout 1.0

label felix_room:
    scene bg felix room
    with dissolve

    "As you step into Felix's room, a wave of stale air washes over you, carrying the faint scent of unwashed laundry and computer dust. The room is a chaotic mess, a testament to Felix's eccentric personality."

    show alex serious1 at alex_right
    show leonie serious at left
    with dissolve

    L "Wow, this room is a disaster. Did a tornado pass through here?"

    "Leoni wrinkles her nose in disgust, her eyes scanning the piles of clothes, books, and electronic gadgets strewn across the floor."

    A "You should see my room."

    "Alex grins, his eyes twinkling with amusement. He gestures around the room, taking in the chaotic scene with a sense of familiarity."

    PC "Let's focus on why we're here. We don't have time to waste. Who knows if and when the janitor will return to lock the door."

    "You step further into the room, your eyes adjusting to the dim light filtering through the drawn curtains. A sense of urgency grips you as you realize that time is of the essence."

    show alex serious2 at alex_right
    with dissolve

    A "What exactly are we looking for, anyway?"

    "Alex's question is a valid one. Without a clear goal, your search could easily become a fruitless endeavor."

    show leonie thinking at left
    with dissolve

    L "Typically, people choose passwords they can easily remember. Given Felix's conspiratorial nature, I doubt he has something simple like \"qwerty\", \"123456\", or \"password\"."

    "Leoni's voice is thoughtful, her eyes scanning the room for any potential clues."

    L "Let's look around for any hints. Maybe he left a note with his password or something."

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

    "Rifling through the haphazard stacks of books on Felix's desk, you find a motley collection of titles. A few well-worn volumes on cybersecurity are wedged between dog-eared conspiracy theory tomes and a weathered copy of 'The Decline and Fall of the Roman Empire'."

    "One book in particular catches your eye – a battered paperback about the 9/11 attacks, its pages filled with scribbled notes and highlighted passages. A sense of unease washes over you as you realize this might be more than just a casual interest for Felix."

    $ book_seen = True
    $ notes.add_data(NoteData("info: 9/11"))
    show screen phone_icon
    jump felix_room_menu

label bin:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f bin zoom
    with dissolve

    "A wave of stale pizza and unidentifiable funk assaults your nostrils as you gingerly lift the lid of Felix's overflowing trash bin. You rummage through crumpled energy drink cans, discarded takeout containers, and a suspicious-looking sock. Nothing of note, just the remnants of a caffeine-fueled conspiracy bender."

    show screen phone_icon
    jump felix_room_menu

label bed:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f bed zoom
    with dissolve

    "Peering under Felix's unmade bed, you see a landscape of dust bunnies, a stray sock, and a few crumpled-up energy bar wrappers. It looks like the cleaning fairy hasn't visited this corner of the room in a while."

    show screen phone_icon
    jump felix_room_menu

label wall2:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall2 zoom
    with dissolve

    "A faded poster from the video game Portal hangs crookedly on the wall. The iconic image of a cake and the ominous phrase 'the cake is a lie' stares back at you, a stark reminder of the deception and manipulation that often lurk beneath a seemingly harmless facade."

    $ poster_seen = True
    $ notes.add_data(NoteData("info: \"the cake is a lie\""))
    show screen phone_icon
    jump felix_room_menu

label wall3:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall3 zoom
    with dissolve

    "A tattered calendar hangs on the wall, its dates marked with a chaotic array of scribbles and doodles. One date, April 17th, is circled in red ink with the words 'Half Life 3' scrawled beside it. A pang of sympathy hits you – poor Felix, still clinging to the hope of a sequel that will probably never come."

    $ calendar_seen = True
    $ notes.add_data(NoteData("info: 04/17 Half Life 3 release"))
    show screen phone_icon
    jump felix_room_menu

label map:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f map zoom
    with dissolve

    "A large map of Nevada is pinned to the wall, its surface littered with red pushpins clustered around a mysterious location. A handwritten note beneath the map reads 'Area 51,' its letters shaky and uneven. A shiver runs down your spine as you contemplate the implications of Felix's obsession with this infamous site."

    $ map_seen = True
    $ notes.add_data(NoteData("info: Area 51"))
    show screen phone_icon
    jump felix_room_menu

label wall1:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f wall1 zoom
    with dissolve

    "Newspaper clippings plaster another section of the wall, their headlines screaming about the flat earth conspiracy. The articles are filled with diagrams, equations, and wild accusations against NASA and other scientific institutions. You shake your head in disbelief, wondering how deep Felix has fallen down this particular rabbit hole."

    $ newspaper_seen = True
    show screen phone_icon
    jump felix_room_menu

label pc:
    call hide_felix_room_interactables
    hide screen phone_icon

    scene bg f pc zoom
    with dissolve

    "The glow of Felix's computer screen beckons you closer. You settle into his worn-out desk chair, your fingers hovering over the keyboard. The familiar login screen appears, demanding a password. You hesitate, a wave of uncertainty washing over you. What secrets lie hidden within this digital fortress?"

    L "Who would have thought?"

    "Leoni's voice is laced with sarcasm, her eyes rolling playfully. She leans over your shoulder, peering at the screen with a curious glint in her eyes."

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

    play music mystery_music1 volume loudness fadeout 1.0

    L "Nailed it! Now let's see what has Felix so spooked."

    "Leoni's voice is triumphant, her eyes gleaming with satisfaction. A wave of relief washes over you as the password barrier crumbles, granting you access to Felix's digital world."

    "You huddle around Leoni's laptop, the screen illuminating your faces with an eerie glow. Felix's notes on his work at Medievil fill the screen, a chaotic jumble of scientific jargon, frantic scribbles, and desperate pleas for help."

    PC "He's talking about those Medievil implants? I thought those were supposed to treat diseases."

    "Your voice is laced with confusion. The pieces of the puzzle are starting to come together, but the picture they paint is disturbing."

    show alex serious1 at alex_right
    with dissolve

    A "Neurological disorders, to be specific. But Felix seems to think they're up to something else."

    "Alex's voice is grave, his gaze fixed on the screen. The room falls silent as you absorb the chilling implications of Felix's notes."

    show leonie neutral at left
    with dissolve

    L "According to Felix, Medievil has something else in mind for these implants. He doesn't elaborate, just mentions it's all about profit and that he believes they're dangerous."

    "Leoni's voice is steady, but a tremor betrays her unease. The air crackles with a sense of impending danger."

    show alex surprised at alex_right
    with dissolve

    A "And who's this Bob Anderson guy? Any idea?"

    "Alex's question hangs in the air, unanswered. The name Bob Anderson echoes in your mind, a sinister specter lurking in the shadows."

    show leonie serious at left
    with dissolve

    L "Looks like he's Felix's supervisor or something. A real piece of work, if Felix's notes are anything to go by."

    "Leoni's voice drips with disdain, her disgust for this mysterious figure evident."

    PC "Is this for real, or is Felix just going down another conspiracy rabbit hole?"

    "Doubt creeps into your voice. You want to believe in Felix, in his instincts, but the sheer outlandishness of his claims makes you question his sanity."

    show alex neutral at alex_right
    with dissolve

    A "I don't know, but he seemed genuinely terrified earlier. Maybe there's more to this than we thought."

    "Alex's voice is a mix of skepticism and concern. He wants to dismiss Felix's fears as unfounded paranoia, but the memory of his friend's terrified face lingers in his mind."

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
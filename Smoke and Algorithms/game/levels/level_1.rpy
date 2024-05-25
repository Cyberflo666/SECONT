#Smoke and Algorithms - Project 2024 SECont

define window_not_done = True
define lock_not_done = True




label level_1_start:
    scene bg dorm room
    A "\"We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."
    
menu:
    "Yes, we should go to the police and hand them the drive, they will know what to do":
        jump choice_1_1_police
    
    "He must have left us some info on how to get access to this data. Let's take a look into his room":
        jump choice_1_1_room

label choice_1_1_police:
    "The police take the flash drive as evidence and you don't ever hear anything of the case again."
    "...or of Felix."
    "Game Over"
    return

label choice_1_1_room:
    "You step out into the hallway and head towards Felix's room but find out that it's locked."
    L "As I expected, too bad he is too paranoid to let his door open like the rest of us."
    jump choice_1_1_done

label choice_1_1_done:
    A "So. Anyone's got a clue as to how we're going to get into his room"

label menu_1_2:
menu:
    "Take a look at his windows" if window_not_done:
        PC "His windows, if they're still open, Leonie can climb up there and open the door from inside"
        L "What..."
        A "Good idea, you're probably the smallest one of us so you're most likely to fit through"
        L "Well if you insist it's worth a try i guess"
        jump choice_1_2_windows


    "Get help from the Janitor":
        PC "The janitor probably has a master key. Maybe we can ask him for help?"
        L "If he opens up random rooms by request, he'd be a pretty poor janitor."
        A "Right, but maybe we can trick or pay him."
        L "Or steal his key"
        PC "Really???"
        L "Its an emergency. And it's not like we're going to keep it"
        jump choice_1_2_janitor

    "Pick the lock" if lock_not_done:
        PC "Can one of you pick locks. Shouldn't be too hard right?"
        L "I have a few paper clips in my room we could use, but no idea how to pick a lock with the."
        A "Me neither, but we can look up a tutorial on the internet. Should be fine."
        PC "If Leonie has enough paper clips to spare"
        jump choice_1_2_lock_pick

label choice_1_2_windows:
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
    "Try to impersonate as Felix to get him to opne the door" :
        PC "I think you have the best chances Alex"
        A "Yeaaah, im not so sure about that"
        L "Dont be so humble. Your the most charismatic out of us and your Felix impression is unmatched. Besides you look the most like him"
        A "Thats great and all but I think we're counting on him not knowing who felix is, because otherwise we're screwed"
        PC "Either way you're our best shot and we need to get into this room"
        L "And since we are Felixe's room mates we can back up your story"
        A "Alright alright I'll do it but you better have my back"
        L "Sure thing Felix"
        A "Ha Ha"
        "All three of you head out to find the janitor. Traversing the building you see him in a hallway heading your dircetion"
        PC "Showtime Alex."
        A "Pshhh."
        "You approach the janitor trying to hide your true intentions"
        A "Excuse me, my name is Felix and I wanted to ask if you can open my room for me. It looks like I've lost my key"
        J "(he looks at you slightly annoyed and suspicious) whats your last name?"
        A "******" 
        J "One second.\" (he checks his phone for a few moments) \"You're from room 014?"
        A "Yes."
        J "And you two are?"
        L "Leonie."
        PC "[PN]."
        L "His roommates"
        "(he checks his phone again:)"
        J "Ah okay I see. Well, lets go to your room shall we."
        "The four of you go to felix's room where the janitor opens the door for you."
        J "So about a replacement key..."
        A "That wont be necessary. I've just got a message from a friend who found my key. Seems like i forgot them at his place."
        J "And you didn't think of that before?."
        A "Well... "
        A "Apperently not."
        "the janitor looks at Alex with disapprovement"
        A "Still. Thanks a lot for helping me out."
        J "Just don't lose them again you hear me"
        A "I promise"
        "He takes his leave and you gained access to Felix's room:"
    
    "Bribe the janitor":
        A "Everyone is vulnerable to money"
        A "If I offer him a few bucks he surely won't say no to lending us his keys for a minute"
        PC "All right Alex, you have my trust"
        "Alex leaves behind the corner and heads to the janitor."
        "You hear a loud exchange of words and soon after Alex returns defeated"
        A "He said wasn't taking any money from me"
        L "Damn, I suspect he won't fall for any of our tricks now"
        jump game_over

    "Steal the keys from the janitor":
        PC "How about I go grab his keys"
        A "I'm not so sure this is a good idea"
        PC "Leave it to me. I've seen it in plenty of movies"
        "As you approach the janitor you stumble in front of him on purpose, fall right onto him and get a hold of his key chain"
        "The victorious spirits start rushing to your brain, but as you pull on his keys they won't come loose"
        "The janitor, visibly furious of what stunt you're trying to pull off here, grabs you by the shirt and shoves you against the wall"
        jump game_over

label felix_room:
    L "Wow, this room is quite messy."
    A "Well, Felix did leave in a rush."
    PC "Let's focus on why we're here. We don't have time to waste. Who knows if and when the janitor will return to lock the door."
    A "What exactly are we looking for, anyway?"
    L "Typically, people choose passwords they can easily remember. Given Felix's conspiratorial nature, I doubt he has something simple like \"qwerty\" , \"123456\" or \"password.\" Let's look around for any hints."

menu:
    "Look through his notebooks":
        "you find a big conspiracy theory book, that is sticking out [[9/11]"
        jump felix_room

    "Search through his bin":
        "you find only trash, some empty packaging"
        jump felix_room

    "Search under his bed":
        "dirty clothes, empty bottles, and spiderwebs are the only things facing you"
        jump felix_room

    "Look at his posters":
        "you catch sight of a portal poster. The following quote sticks out:\"the cake is a lie\""
        jump felix_room

    "Look at the pictures on the shelf":
        "your eyes meet a Calnder with marked dates. A red circled date [[04/17] labeld with mothers birthday stands out"
        jump felix_room

    "Examine the map":
        "You catch sight of a Nevada map, with multiple pins on an [[Area51]"
        jump felix_room

    "Pull the phone out to crack the password":
        jump phone_minigame
        #add minigame
       
label game_over:
    "YOU DIED"

return
#Smoke and Algorithms - Project 2024 SECont

label level_1_start:
    scene bg dorm room
    A "\"We have to get our hands on the info inside this drive. Felix wouldn't have just handed it to us if this wasn't important to him."
    
menu:
    "Yes, we should go to the police and hand them the drive, they will know what to do":
        jump choice_1_1_police
    
    "He must have left us some info on how to get access to this data. Let's take a look into his room":
        jump choide_1_1_room

label choice_1_1_police:
    "The police take the flash drive as evidence and you don't ever hear anything of the case again."
    "...or of Felix."
    "Game Over"
    return

label choice_1_1_room:
    "You step out into the hallway and head towards Felix's room but find out that it's locked."
    L "As I expected, too bad he is too paranoid too let his door open like the rest of us."
    jump choice_1_1_done

label choice_1_1_done:
    A "So. Anyone's got a clue as to how we're going to get into his room"

menu:
    "We should take a look at his windows":
        PC "His windows, if they're still open, Leoni can climb up there and open the door from inside"
        L "What..."
        A "Good idea, "

    "Maybe we can get help from the Janitor":
        PC "The janitor"

    "Try to pick the lock":
        PC "Can one of you pick locks. Shouldn't be too hard right?"

return
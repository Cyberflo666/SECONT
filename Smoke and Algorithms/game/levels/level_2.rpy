define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define new_objectives_not_heard = True
define search_visited = False
define bob_visited = False
define open_gil_post = False
define gil_visited = False
default lab_seen = False
default uni_access_denied = False
default dumpster_doven = False
default dumpster2_doven = False
default player_warned = False
default rat_seen = False
default medical_tools_seen = False
default symbols_seen = False 
default left_pc_seen = False 
default left_wall_seen = False 
default trash_seen = False
default dumpster_explained = False
default machine_struck_counter = 0
default snack_gotten = False

label level_2_start:
    play music main_music1 volume 0.1
    scene bg new kitchen 
    
    "You walk over and gather around a table while opening up your laptop."
    scene bg laptop full
    L "What exactly is our plan now? What are we doing with the information we find?"
    PC "We could go to the facility Bob Anderson works at and look for Felix?"
    PC "I also don't think that we have access to his workplace and we probably won't find it just sitting on some website."
    L "If that is the problem we could try to write a phishing email to Bob Anderson so that he grants us access."
    A "Do you think it's realistic that we can convince him to do that?"
    L "Depends on what we fin out about Bob Anderson's background. Maybe we there is something we can use on his social media or some {color=[medievilColor]}Medievil{/color} web page?"
    PC "Either way we should do some research on him."

label research:
    scene bg laptop full
    show screen phone_icon
    show screen laptop_screen
    with dissolve
    $ show_textbox = False
    ""
    jump empty_label

label warning:
    $ show_image_buttons = False
    $ player_warned = True
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Are you sure we have enough information for a phishing mail?"
    with dissolve
    $ show_image_buttons = True
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    return
label social_button_1:
    $ show_image_buttons = False
    $ show_textbox = True
    if search_visited == False:
        show screen social_screen_search
        PC "Maybe we should look up Bob Anderson."
        $ show_image_buttons = True
        show screen social_screen_search
        $ show_textbox = False
        $ search_visited = True
        jump empty_label
    elif search_visited == True:
        $ show_image_buttons = True
        show screen social_screen_search
        $ show_textbox = False
        jump empty_label

label social_button_2:
    $ show_image_buttons = False
    $ show_textbox = True
    if bob_visited == False:
        show screen social_screen_bob
        PC "Interesting profile."
        L "Good that he isn't private."
        A "What a good looking man."
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        $ bob_visited = True
        jump empty_label
    elif bob_visited == True:
        $ show_image_buttons = True
        show screen social_screen_bob
        $ show_textbox = False
        jump empty_label

label social_button_3:
    show screen social_screen_gill
    $ show_image_buttons = False
    $ show_textbox = True
    if open_gil_post == False:
        PC "Who is that person? "
        L "He seems like an important person"
        A "Well then, let's check that guy out"
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        $ open_gil_post = True
        jump empty_label
    elif open_gil_post == True:
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        jump empty_label

label social_button_4:
    $ show_image_buttons = False
    $ show_textbox = True
    if gil_visited == False:
        show screen social_screen_gill
        PC "Interesting profile."
        L "So this is gill."
        A "He has a nice looking house."
        PC "Even with a street sign."
        L "You want to go after him?"
        A "If he has something to do with Mr. Anderson we might get something useful from him."
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        $ gil_visited = True
        jump empty_label
    elif gil_visited == True:
        $ show_image_buttons = True
        show screen social_screen_gill
        $ show_textbox = False
        jump empty_label


label website1_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_1_not_seen = False
    show screen website1_screen
    PC "Apparently {color=[medievilColor]}Medievil{/color} is getting funds from our city."
    A "Is there a reason?"
    L "Not really. Just for stronger industry and more workplaces."
    $ show_image_buttons = True
    show screen website1_screen
    $ show_textbox = False
    jump empty_label
    ""
label website2_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_2_not_seen = False
    show screen website2_screen
    PC "Here is something about a lab at our university. According to these news it was offered to {color=[medievilColor]}Medievil{/color} for research."
    L "Maybe we should check it out."
    A "You think we have access?"
    L "I think we can get it if we really want."
    $ show_image_buttons = True
    call websearch_done
    show screen website2_screen
    $ show_textbox = False
    jump empty_label
    ""
label website4_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_3_not_seen = False
    show screen website4_screen
    PC "Here's something interesting."
    A "What?"
    PC "The location of Mr. Andersons Office."
    L "Maybe we should pay him a visit."
    $ show_image_buttons = True
    call websearch_done
    show screen website4_screen
    $ show_textbox = False
    jump empty_label
    ""

label website1_call:
    show screen website1_screen
    ""
    jump empty_label
label website2_call:
    show screen website2_screen
    ""
    jump empty_label
label website3_call:
    show screen website3_screen
    ""
    jump empty_label
label website4_call:
    show screen website4_screen
    ""
    jump empty_label
label websearch_done:
    if not website_2_not_seen and not website_3_not_seen:
        $ renpy.notify("You have new objectives on your map.")
    return

label dumpsterdive:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    
    PC "Let's head to Bob Andersons office. I wonder what we can find there."
   

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We don't have to step in. We can stay outside and do dumpsterdiving, to find out more information."
        show leonie surprised at left
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right
        with dissolve
        A "People often times throw away sensitive information without disposing of it correctly. If we look at the trash we could find something compromising that could get us a lead."
        "You, Alex and Leoni go to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg back office #its dark outside
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    PC "Hmm, the building seems bigger than described on the internet."
    show leonie happy at left
    with dissolve

    L "Yes but luckily the garbage bins are directly over there."
    show alex angry at alex_right
    with dissolve

    A "I think someone has to look out for anyone incoming, not that they see us searching through the trash as thats pretty suspicious. Ill take on the role and whistle loudly to warn you."
    PC "Thank you bro. Let's get going then."

    scene bg wastepaper 

    jump dumpster_diving_minigame_start

label after_dumpsterdive:
    $ show_textbox = True
    scene bg back office
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a receipt from the (name)."
    L "Isn't that the super fancy expensive restaurant where only celebrities and rich people go?"
    A "Yup ive heard a lot of wild things about that restaurant. You're right, only the higher classes can afford it."
    PC "Seems like Bob Anderson went there with someone."
    L "I wonder who he went there with. The food and drinks definitely look like for 2 people."
    $ gloss_dumpster_seen = True
    $ dumpster_doven = True

    jump research 

label dumpsterdive2:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Well then i suggest we should head out to Gill's place and investigate there."

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We don't have to step in. We can stay outside and do dumpster diving, to find out more information."
        show leonie surprised at left
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right
        with dissolve
        A "People often times throw away sensitive information without disposing of it correctly. If we look at the trash we could find something compromising that could get us a lead."
        "You, Alex and Leoni go to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft

    #scene bg gilshouse #its dark outside
    scene bg gill house front
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    PC "Wow what a beautiful looking house."
    show leonie happy at left
    with dissolve

    L "Are we sure Gill is a bad guy? no way an evil person has such a wonderful house."
    show alex neutral at alex_right
    with dissolve
    A "Well in movies the bad guys tend to own a more expensive house, since they earn more money through illegal ways, than the average people do."

    PC "I suggest we should just go ahead and start, the more time we spend here the more suspicion we raise."

    show alex happy at alex_right 
    with dissolve 

    A "Alright, let's get digging then."

    show leonie neutral at left
    with dissolve
    L "Digging into trash... yippee."

    show alex angry at alex_right
    with dissolve
    A "Well if you're not so enthusiastic about it then I suggest you look out and warn us in case anyone comes here. Me and [PN] will go on then don't worry."

    show leonie sad at left 
    with dissolve

    L "Mhmm."

    scene bg gill dumpster 
    jump dumpster_diving_minigame2_start

label after_dumpsterdive2:
    $ show_textbox = True
    scene bg gill house front
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a note from Gill."
    L "Says something about a handover."
    A "Interesting."
    PC "I wonder if this can be of any use for us."
    $ gloss_dumpster_seen = True
    $ dumpster2_doven = True
    jump research 




    


label lab_access_denied:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "The security is alert of your attempted intrusion. They will surely not let you near the lab again."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label lab_visited:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You have already seen everything there is to see here."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label dumpster_empty:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You already have all the information from this garbage."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label visitlab:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Fine I'll suggest that we head to the university lab then. The lab is in a part of the campus that practically never gets used so that's quite shady."
    show leonie thinking at left 
    with dissolve

    L "Good point, but maybe they just don't want to disturb others with their noises or get distracted?"
    show alex neutral at alex_right
    with dissolve

    A "Or maybe they want to keep their activities hidden."
   
    PC "Damn dude, you almost sound like Felix."
    show alex serious2 at alex_right
    with dissolve

    A "I really wonder where he is, I miss that little fella. We should get going for his sake."

    hide alex 
    hide leonie
    with dissolve
    scene black
    with dissolve

    "You head out to the university to find the lab the article mentioned."

    scene bg uni hallway
    with dissolve
    show leonie thinking at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    show alexserious2 at alex_right
    with dissolve

    A "I've never been at this part of the university."

    show leonie neutral at left
    with dissolve

    L "Well our campus is quite big and none of us were here. Barely anyone is ever here to be exact."

    PC "This part does seem more grim and gloomy."

    show alex angry at alex_right
    with dissolve

    A "Since you all seem so scared I guess I'll take the lead and get us going."

    hide alex 
    hide leonie 

    "You head to the door of the lab, and see that there's a pin needed to unlock the door."

label lab_entry_choice:
    scene bg medievil front lab 
    with dissolve

    show leonie thinking at left
    with dissolve
    show alex neutral at alex_right 
    with dissolve

    L "What should we do now?"

    menu: 
        "Wait for someone to enter the lab in disguise.":
            show leonie neutral at left
            with dissolve
            L "Maybe we can wait until someone opens the door for us."
            show alex serious1 at alex_right
            with dissolve
            A "And then sneak inside without them noticing. Really!?"
            show leonie serious at left
            with dissolve
            L "No, we simply watch what they input and then wait for them to leave."
            show alex neutral at alex_right
            with dissolve
            A "We would have to wait quite far away to stay hidden."
            PC "That's fine. I have binoculars at home i can get."
            show leonie happy at left
            with dissolve
            L "And we will find a good spot for observation."
            scene black
            with dissolve
            "The three of you split up. Alex and Leonie search for a location that has a line of sight to the door while still being far enough away to not raise suspicions while you get your binoculars from home."
            jump lab_wait
        "Ask around to get access.":
            $ uni_access_denied = True
            hide leonie
            hide alex
            with dissolve
            "You ask the first person you see trying to enter to give you access."
            "They deny your request and notifiy the security about your presence."
            "Because you dont want to meddle with them any further you decide to return home and continue your research."
            jump research
        "Get a snack from the nearby vending machine" if snack_gotten == False:
            hide leonie
            hide alex
            show bg vending machine 1
            with dissolve
            $ snack_gotten = True
            "Researching all day made you kinda hungry and since there is nothing else nearby you decide to get a snack from the local wending machine."
            "After paying 1,20$ for an overpriced chocolate bar you watch as your snack gets stuck in the spiral of a lower row."
            jump wending_maschine

label wending_maschine:
    menu:
        "Shake the vending machine to get your snack" if machine_struck_counter == 0:
            $ machine_struck_counter += 1
            "You begin shaking the machine but the bar doesn't move."
            jump wending_maschine

        "Shake the wending machine even harder to get your snack" if machine_struck_counter == 1:
            #$ machine_struck_counter += 1
            "Again you shake the machine like a maniac and though the bar doesn't move you get noticed by a guy who was about to enter the lab."
            "You try to play it off but the person informs the security about your fight with the machine and even though you stay low for the next half hour they won't take their eyes off you."
            "Since the entire facility is now alert to your presence you decide to head home and continue your investigation from there."
            jump research
        "Return to the lab door to figure out a way to get in":
            "You surrender your snack and your dignity to the machine and continue your mission."
            jump lab_entry_choice

label lab_wait:
    $ gloss_tailgating_seen = True
    scene bg uni hallway #need better spot than hallway
    with dissolve
    "As you return you got to the location Leonie sent you. A desk at the snack machine with four chairs."
    show leonie neutral at left
    show alex neutral at alex_right
    with dissolve
    "You sit down and wait for what feels like an eternity until..."
    show alex surprised at alex_right
    with dissolve
    A "Guys look. We caught one."
    show leonie serious at left
    with dissolve
    L "Quiet, we don't want him to notice us. Just observe what he presses."
    show alex serious1 at alex_right
    with dissolve
    scene bg pinpad binoculars
    with dissolve
    "You see an ominous person walking up to the door. He does not look like any university employee you know."
    "You watch as he puts his hand on the pinboard and inputs: \n '4' '7' '1' '9' '6' '5'."
    "While you observe, you whisper to your friends what you see."
    scene bg uni hallway
    with dissolve
    show alex serious2 at alex_right
    with dissolve
    A "Is that all?"
    PC "Yup. The door is open."
    show leonie happy at left
    with dissolve
    L "Great. Now we just have to wait until he leaves."
    show alex smile at alex_right
    with dissolve
    A "Perfect. I needed a break after all the previous waiting."
    PC "You can follow him if you want, but don't expect us to follow."
    show alex happy at alex_right
    with dissolve
    A "Nah I'm good. Just kidding."
    show leonie thinking at left
    with dissolve
    L "We should change locations to avoid getting his attention. It could make him suspicious if we were still here when he leaves."
    show alex neutral at alex_right
    with dissolve
    A "We could wait outside for him to exit."
    show leonie serious at left
    with dissolve
    L "Ok. Alex and I wait at the front and you wait at the back."
    PC "Roger that."
    scene black # could be changed to uni backside instead if we have the image
    with dissolve
    "You get into position and start waiting."
    "After a short while you get a message from Alex telling you to get to the lab."
    "When you approach the lab you see your friends in front of the open door."
    scene bg medievil front lab
    with dissolve
    
    show leonie neutral at left
    show alex neutral at alex_right
    with dissolve
    PC "I assume he left."
    show alex smile at alex_right
    with dissolve
    A "No he invited us in."
    show leonie sad at left
    with dissolve
    "..."
    show leonie neutral at left
    with dissolve
    L "Anyways."
    "Upon entering the lab the three of you start to investigate." 
    scene bg medievil lab
    with dissolve
    L "Let's take a look around this lab."

label inside_lab:
    if rat_seen and left_pc_seen and left_wall_seen and symbols_seen and trash_seen:
        jump inside_lab_done
    $ show_textbox = False
    scene bg medievil lab
    show screen left_cage
    show screen left_pc
    show screen left_wall
    show screen symbol_screen
    show screen right_cage
    show screen right_pc
    show screen trash
    with dissolve
    #show screen medical_tools

    $ hide_map = True
    show screen phone_icon
    with moveinright
    jump empty_label


label rat_in_cage_left:
    call hide_lab_screens
    scene bg left cage zoom
    with dissolve 
    $ show_textbox = True
    $ mail_1_text_unlocked[3] = 1
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water and some obstacles for the animal to walk around"
    $ show_textbox = False
    $ rat_seen = True
    jump inside_lab
label left_pc_stats:
    call hide_lab_screens
    scene bg left pc zoom
    with dissolve 
    $ show_textbox = True
    "You look at the pic and see suspicious stats. You see percentages, probabilities and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab
label left_wall_obj:
    call hide_lab_screens
    scene bg left wall zoom
    with dissolve
    $ show_textbox = True
    "Searching on the left cupboard you find some chemicals and medical tools alongside what looks like a few of {color=[medievilColor]}Medievil{/color}s implants but way smaller."
    $ show_textbox = False
    $ left_wall_seen = True 
    jump inside_lab
label symbols_on_screen:
    call hide_lab_screens
    scene bg monitor zoom
    with dissolve
    $ show_textbox = True
    "You see a screen with three symbols. A arrow pointing left another pointing right and a circle between them. They seem to be lighting up on random. When observing them a bit more you notice that only one of the is active at a time."
    $ show_textbox = False
    $ symbols_seen = True
    jump inside_lab
label rat_in_cage_right:
    call hide_lab_screens
    scene bg right cage zoom
    with dissolve
    $ show_textbox = True
    $ mail_1_text_unlocked[3] = 1
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water and some obstacles for the animal to walk around."
    $ show_textbox = False
    $ rat_seen = True
    jump inside_lab
label right_pc_stats:
    call hide_lab_screens
    scene bg right pc zoom
    with dissolve
    $ show_textbox = True
    "You look at the pic and see suspicious stats. You see percentages, probabilities and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab
label empty_trash:
    call hide_lab_screens
    scene bg trash zoom
    with dissolve
    $ show_textbox = True
    "You look in and realise the bin is empty."
    $ show_textbox = False
    $ trash_seen = True
    jump inside_lab 

#label used_medical_tools:
    #call hide_lab_screens
    #show  medical tools
    #$ show_textbox = True
    #"Searching on a desk you find some chemicals and medical tools alongside what looks like a few of medievils implants but way smaller."
    #$ show_textbox = False
    #$ medical_tools_seen = True
    #jump inside_lab
label inside_lab_done:
    call hide_lab_screens
    scene bg medievil lab
    with dissolve
    $ show_textbox = True
    show leonie neutral at left
    show alex neutral at alex_right
    with dissolve
    PC "The symbols on the screen. Do they show the movement of the rat?"

    show leonie serious at left
    with dissolve
    L "It looks like it. But its a bit offset. Like the screen knows what the rat will do before it does it."

    PC "Why would {color=[medievilColor]}Medievil{/color} develop something like that?"

    show alex serious1 at alex_right
    with dissolve
    A "From what i know that is nothing that they're advertising so it's probably not for the world to know."

    show leonie sad at left
    with dissolve
    L "That can't be good. Looks like Felix was onto something for real."

    PC "In any case I think we shouldn't stick around in here any longer than we need to."

    show alex serious2 at alex_right
    with dissolve
    A "Agreed."
    hide screen phone_icon
    scene black
    with dissolve
    "As you leave the lab you make sure that everything is left like you found it when you entered. After that you head out the back entrance and venture on home."
    $ lab_seen = True
    with dissolve
    $ hide_map = False
    jump research

label empty_label:
    ""
    $ renpy.notify("all good")
    jump empty_label
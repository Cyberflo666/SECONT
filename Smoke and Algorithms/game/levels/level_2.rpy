define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define new_objectives_not_heard = True
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

label level_2_start:
    play music main_music1 volume 0.1
    scene bg new kitchen 
    "you gather around the kitchen table while opening up your laptop"
    "You walk over and gather around a table while opening up your laptop."
    scene bg laptop full
    A "I think it's best if we start by looking up what exactly Medievil is."

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
label website1_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_1_not_seen = False
    show screen website1_screen
    PC "Apparently Medievil is getting funds from our city."
    A "Is there a reason?"
    L "Not really. Just for stronger industry and more workplaces"
    $ show_image_buttons = True
    call websearch_done
    show screen website1_screen
    $ show_textbox = False
    jump empty_label
    ""
label website2_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_2_not_seen = False
    show screen website2_screen
    PC "Here is something about a lab at our university. According to these news it was offered to Medievil for research."
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
    PC "Here's something intersesting."
    A "What?"
    PC "The location of Mr. Andersons Office."
    L "Maybe w should pay him a visit."
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
        PC ""
        $ renpy.notify("you have new objectives on your map")
    return
label new_objectives:
    $ show_textbox = True
    $ show_image_buttons = False
    $ new_objectives_not_heard = False
    L "It's good that we were able to learn a lot about Mr. Anderson. How are we going to proceed, though?"
    PC "I believe Anderson should be our priority since he is the link between Medievil and Felix."
    L "How about we use the information we've gathered to infiltrate them?"
    A "Isn't that a bit too hasty? We don't know much about the building or Bob Anderson."
    PC "Going in without a proper plan could be very risky. They'd be onto us quickly. Let's weigh all the options first."
    L "We could also write a phishing email to gather more intel on Bob Anderson and his building. We could stay and dig deeper into Bob Anderson's background.Maybe check his social media?"
    A "Alternatively, we could go dumpster diving near his facility.how about we look into the university's partnered lab?What do you think we should do first?"
    $ show_textbox = False
    $ show_image_buttons = True
    jump research

label dumpsterdive:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    
    PC "Lets head to Bob Andersons office. I wonder what we can find there."
   

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? Its not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We dont have to step in. We can stay outside and do dumpsterdiving, to find out more information."
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

    scene bg officebehind #its dark outside
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    PC "Hm the building seems smaller than described on the internet"
    show leonie happy at left
    with dissolve

    L "Well that means we dont have to search for too much. Look, the garbage bins are directly over there."
    show alex angry at alex_right
    with dissolve

    A "I think someone has to look out for anyone incoming, not that they see us searching through the trash as thats pretty suspicious. Ill take on the role and whistle loudly to warn you."
    PC "Thank you bro. Lets get going then"

    scene bg wastepaper 

    jump dumpster_diving_minigame_start

label after_dumpsterdive:
    $ show_textbox = True
    scene bg officebehind
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a receipt from the (name)."
    L "Isnt that the super fancy expensive restaurant where only celebreties and rich people go?"
    A "Yup ive heard alot of wild things about that restaurant. Youre right, only the higher classes can afford it"
    PC "Seems like Bob Anderson went there with someone"
    L "I wonder who he went there with. The food and drinks definetly look like for 2 people"
    $ gloss_dumpster_seen = True
    $ dumpster_doven = True

    jump research 

label dumpsterdive2:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Well then i suggest we should head out to Gills place and investigate there."

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? Its not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We dont have to step in. We can stay outside and do dumpsterdiving, to find out more information."
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
    scene bg facility 1
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    PC "Wow what a beautiful looking house"
    show leonie happy at left
    with dissolve

    L "Are we sure Gil is a bad guy? no way an evil person has such a wonderful house"
    show alex neutral at alex_right
    with dissolve
    A "Well in movies the bad guys tend to own a more expensive house, since they earn more money through illegal ways, than the average people do."

    PC "I suggest we should just go ahead and start, the more time we spend here the more suspicioun we raise"

    show alex happy at alex_right 
    with dissolve 

    A "alright lets get digging then"

    show leonie sad at left
    with dissolve
    L "digging into trash ... yippie"

    show alex angry at alex_right
    with dissolve
    A " well if youre not so enthusiastic about it then i suggest you look out and warn us incase anyone comes here. Me and [PN] will go on then dont worry"

    show leonie happy at left 
    with dissolve

    L "mhm"

    scene bg wastepaper 
    jump dumpster_diving_minigame2_start

label after_dumpsterdive2:
    $ show_textbox = True
    scene bg officebehind
    with dissolve
    show leonie happy at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright
    A "Nice one, that's more like what we're looking for. Now what does it say?"
    PC "It's a note from gil."
    L "Says something about a handover."
    A "Interesting"
    PC "I wonder if this can be of any use for us"
    $ gloss_dumpster_seen = True
    $ dumpster2_doven = True
    jump research 




    


label lab_access_denied:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "The security is alert of your attemted inrusion. They will surely not let you near the lab again."
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

    PC "Fine ill suggest that we head to the university lab then. The lab is in a part of the campus that practically never gets used so thats quite shady"
    show leonie thinking at left 
    with dissolve

    L "Good point but maybe they just dont want to disturb others with their noises or get distracted?"
    show alex neutral at alex_right
    with dissolve

    A "Or maybe they want to keep their activities hidden."
   
    PC "damn dude you almost sound like Felix"
    show alex serious2 at alex_right
    with dissolve

    A "I really wonder where he is, i miss that little fella. We should get going for his sake."

    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg uni hallway
    with dissolve
    show leonie thinking at left
    with  moveinleft
    show alex neutral at alex_right
    with  moveinright

    show alexserious2 at alex_right
    with dissolve

    A "Ive never been at this part of the university."

    show leonie neutral at left
    with dissolve

    L "Well our campus is quite big and none of us were here. Barely anyone is ever here to be exact."

    PC "This part does seem more grim and gloomy."

    show alex angry at alex_right
    with dissolve

    A "Since you all seem so scared i guess ill take the lead and get us going"

    hide alex 
    hide leonie 

    "You head to the door of the lab, and see that theres a pin needed to unlock the door "

    scene bg medievil lab front 
    with dissolve

    show leonie thinking at left
    with dissolve
    show alex neutral at alex_right 
    with dissolve

    L "What should we do now?"

    menu: 
        "Wait for someone to enter the lab in disguise":
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
            PC "Thats fine. I have binoculars at home i can get."
            show leonie happy at left
            with dissolve
            L "And we will find a good spot for observation"
            scene black
            with dissolve
            "The three of you split up. Alex and leonie search for a location that has line of sight to the door while still being far enough away to not raise suspicion while you get your binoculars from home."
            jump lab_wait
        "Ask around to get access":
            $ uni_access_denied = True
            hide leonie
            hide alex
            with dissolve
            "You ask the first person you see trying to enter to give you access."
            "They deny your request and notifiy the security about your presence."
            "Because you dont want to meddle with them any further you decide to return home and continue your research."
            jump research

label lab_wait:
    $ gloss_tailgating_seen = True
    scene bg uni hallway #need better spot than hallway
    with dissolve
    "As you return you got to the location leonie sent you. A desk at the snack maschine with four chairs."
    show leonie neutral at left
    show alex neutral at alex_right
    with dissolve
    "You sit down and wait for what feels like eternity until..."
    show alex surprised at alex_right
    with dissolve
    A "Guys look. We caught one."
    show leonie serious at left
    with dissolve
    L "Quiet, we don't want him to notice us. Just oserve what he presses."
    show alex serious1 at alex_right
    with dissolve
    scene bg pinpad
    with dissolve
    "You see a ominous person walking up to the door. He does not look like any univerity employee you know."
    "You watch as he puts his hand on the pinboard and inputs: \n '4' '7' '1' '9' '6' '5'."
    "While you observe you whisper to your friends what you see."
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
    PC "You can follow him if you want, but dont expect us to follow."
    show alex happy at alex_right
    with dissolve
    A "Nah im good. Just kidding."
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
    scene bg uni hallway # could be changed to uni backside instead if we have the image
    with dissolve
    "You get into position and start waiting."
    "After a short while you get a message from alex telling you to get to the lab."
    "When you approach the lab you see your friends infront of the open door."
    scene bg medievil lab front
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
    "Upon entering the lab the three of you start to investigate" 
    scene bg medievil lab
    with dissolve
    L "Let's take a look around this lab"

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
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water a some obstacels for the animal to walk around"
    $ show_textbox = False
    $ rat_seen = True
    jump inside_lab
label left_pc_stats:
    call hide_lab_screens
    scene bg left pc zoom
    with dissolve 
    $ show_textbox = True
    "you look at the pc and see suspicious stats. You see percentages, probabilites and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab
label left_wall_obj:
    call hide_lab_screens
    scene bg left wall zoom
    with dissolve
    $ show_textbox = True
    "Searching on the left coubard you find some chemicals and medical tools alongside what looks like a few of medievils implants but way smaller"
    $ show_textbox = False
    $ left_wall_seen = True 
    jump inside_lab
label symbols_on_screen:
    call hide_lab_screens
    scene bg monitor zoom
    with dissolve
    $ show_textbox = True
    "You see a screen with three symbols. A arrow pointing left another pointing right and a circle between them. They seem to be lighting up on random. When observing them a bit more you notice that only one of the is active at a time"
    $ show_textbox = False
    $ symbols_seen = True
    jump inside_lab
label rat_in_cage_right:
    call hide_lab_screens
    scene bg right cage zoom
    with dissolve
    $ show_textbox = True
    "When observing the cage you see a rat inside with a small scar on its head. Other than that the cage contains only food, water a some obstacels for the animal to walk around"
    $ show_textbox = False
    jump inside_lab
label right_pc_stats:
    call hide_lab_screens
    scene bg right pc zoom
    with dissolve
    $ show_textbox = True
    "you look at the pc and see suspicious stats. You see percentages, probabilites and results."
    $ show_textbox = False
    $ left_pc_seen = True
    jump inside_lab
label empty_trash:
    call hide_lab_screens
    scene bg trash zoom
    with dissolve
    $ show_textbox = True
    " you look in and realise the bin is empty"
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

    show leonie serious at leftR
    with dissolve
    L "It looks like it. But its a bit offset. Like the screen knows what the rat will do in befor it does it"

    PC "Why would medievil develop something like that?"

    show alex serious1 at alex_right
    with dissolve
    A "From what i know that is nothing that they're advertising so its probaply not for the world to know."

    show leonie sad at left
    with dissolve
    L "That can't be good. Looks like felix was onto something for real."

    PC "In any case i think we should'nt stick around in here any longer than we need to."

    show alex serious2 at alex_right
    with dissolve
    A "Agreed."
    "As you leave the lab you make sure that everything is left like you found it when you entered. After that you head out the back entrance and venture on home."
    $ lab_seen = True
    with dissolve
    jump research

label empty_label:
    ""
    $ renpy.notify("all good")
    jump empty_label
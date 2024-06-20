define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define new_objectives_not_heard = True

label level_2_start:
    play music main_music1 volume 0.1
    scene bg new kitchen 
    "you gather around the kitchen table while opening up your laptop"
    "You walk over and gather around a table while opening up your laptop."
    scene bg laptop
    A "I think it's best if we start by looking up what exactly Medievil is."
    show screen laptop_screen
    $ show_textbox = False
    ""
    jump empty_label

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
label website3_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_3_not_seen = False
    show screen website3_screen
    PC "Our good friend Mr Anderson had a meeting today."
    A "With whom."
    PC "Someone called Gill Cameron."
    L "Never heard of him."
    A "But maybe worth a look. We could try finding him on brainrot."
    $ show_image_buttons = True
    call websearch_done
    show screen website3_screen
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
label websearch_done:
    if not website_2_not_seen and not website_3_not_seen:
        PC ""
        $ renpy.notify("you have new objectives on your map")
    return
label new_objectives:
    $ show_textbox = True
    $ new_objectives_not_heard = False
    L "It's good that we were able to learn a lot about Mr. Anderson. How are we going to proceed, though?"
    PC "I believe Anderson should be our priority since he is the link between Medievil and Felix."
    L "How about we use the information we've gathered to infiltrate them?"
    A "Isn't that a bit too hasty? We don't know much about the building or Bob Anderson."
    PC "Going in without a proper plan could be very risky. They'd be onto us quickly. Let's weigh all the options first."
    L "We could also write a phishing email to gather more intel on Bob Anderson and his building. We could stay and dig deeper into Bob Anderson's background.Maybe check his social media?"
    A "Alternatively, we could go dumpster diving near his facility.how about we look into the university's partnered lab?What do you think we should do first?"
     
    show screen laptop_screen
    $ show_textbox = False
    jump empty_label

label dumpsterdive:
    $ show_textbox = True
    scene bg new kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    
    PC "Lets head to Bob Andersons office. I wonder what we can find there."
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
    A "Nice one, now what does it say?"
    PC "It's a receipt from the (name)."
    L "Isnt that the super fancy expensive restaurant where only celebreties and rich people go?"
    A "Yup ive heard alot of wild things about that restaurant. Youre right, only the higher classes can afford it"
    PC "Seems like Bob Anderson went there with someone"
    L "I wonder who he went there with. The food and drinks definetly look like for 2 people"


    jump game_over #this is just a placholder
    

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

    scene bg university hall
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

    "you head to the door of the lab, and see that theres a pin needed to unlock the door "

    show leonie thinking at left
    with dissolve
    show alex neutral at alex_right 
    with dissolve

    L "What should we do now?"

    menu: 
        "wait for someone to enter the lab in disguise":
            jump game_over
        "ask around to get access":
            jump game_over







label empty_label:
    ""
    $ renpy.notify("all good")
    jump empty_label
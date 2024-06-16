define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define new_objectives_not_heard = True

label level_2_start:
    play music main_music1 volume 0.1
    scene bg new kitchen 
    "you gather around the kitchen table while opening up your laptop"
    "You walk over and gather around a table while opening up your laptop."
    scene laptop
    A "I think it's best if we start by looking up what exactly Medievil is."
    call screen web_screen
    ""

label website1_button:
    $ website_1_not_seen = False
    show screen website1_screen
    PC "Apparently Medievil is getting funds from our city."
    A "Is there a reason?"
    L "Not really. Just for stronger industry and more workplaces"
    call websearch_done
    call screen website1_screen
    ""
label website2_button:
    $ website_2_not_seen = False
    show screen website2_screen
    PC "Here is something about a lab at our university. According to these news it was offered to Medievil for research."
    L "Maybe we should check it out."
    A "You think we have access?"
    L "I think we can get it if we really want."
    call websearch_done
    call screen website2_screen
    ""
label website3_button:
    $ website_3_not_seen = False
    show screen website3_screen
    PC "Our good friend Mr Anderson had a meeting today."
    A "With whom."
    PC "Someone called Gill Cameron."
    L "Never heard of him."
    A "But maybe worth a look. We could try finding him on brainrot."
    call websearch_done
    call screen website3_screen
    ""

label website1_call:
    call screen website1_screen
    ""
label website2_call:
    call screen website2_screen
    ""
label website3_call:
    call screen website3_screen
    ""
label websearch_done:
    if not website_2_not_seen and not website_3_not_seen:
        PC ""
        $ renpy.notify("you have new objectives on your map")
    return
label new_objectives:
    $ new_objectives_not_heard = False
    L "It's good that we were able to learn a lot about Mr. Anderson. How are we going to proceed, though?"
    PC "I believe Anderson should be our priority since he is the link between Medievil and Felix."
    L "How about we use the information we've gathered to infiltrate them?"
    A "Isn't that a bit too hasty? We don't know much about the building or Bob Anderson."
    PC "Going in without a proper plan could be very risky. They'd be onto us quickly. Let's weigh all the options first."
    L "We could also write a phishing email to gather more intel on Bob Anderson and his building. We could stay and dig deeper into Bob Anderson's background.Maybe check his social media?"
    A "Alternatively, we could go dumpster diving near his facility.how about we look into the university's partnered lab?What do you think we should do first?"
     
    call screen laptop_screen

label dumpsterdive:
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

    scene bg officeoutside #its dark outside

    show leonie neutral at left
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
    jump game_over #this is just a placholder
    



label visitlab:
   

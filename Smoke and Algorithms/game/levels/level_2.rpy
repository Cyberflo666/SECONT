#define website
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
    "You settle in at the kitchen table and open your laptop."
    scene bg laptop full
    $ gallery.add_data(["gallery_meme"])
    A "I think our best bet is to start by researching what Medievil is all about."
    jump research

label research:
    scene bg laptop full
    show screen phone_icon
    show screen laptop_screen
    with dissolve
    $ show_textbox = False
    jump empty_label

label warning:
    $ show_image_buttons = False
    $ player_warned = True
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    with dissolve
    L "Whoa, are you sure we have enough information to start crafting a phishing email?"
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
    PC "Looks like Medievil is receiving funding from our city."
    A "Any particular reason?"
    L "Not that I can see. Just the usual buzzwords about 'stronger industry' and 'more jobs'."
    $ show_image_buttons = True
    call websearch_done
    show screen website1_screen
    $ show_textbox = False
    jump empty_label

label website2_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_2_not_seen = False
    show screen website2_screen
    PC "Interesting. This article mentions a lab at our university being offered to Medievil for research."
    L "We should definitely check that out."
    A "Do you think we can even get access?"
    L "I'm sure we can find a way if we're determined enough."
    $ show_image_buttons = True
    call websearch_done
    show screen website2_screen
    $ show_textbox = False
    jump empty_label

label website4_button:
    $ show_image_buttons = False
    $ show_textbox = True
    $ website_3_not_seen = False
    show screen website4_screen
    PC "Hey, check this out!"
    A "What is it?"
    PC "It's the address of Mr. Anderson's office."
    L "Maybe it's time for a little field trip."
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
    L "We could also write a phishing email to gather more intel on Bob Anderson and his building. We could stay and dig deeper into Bob Anderson's background. Maybe check his social media?"
    A "Alternatively, we could go dumpster diving near his facility. How about we look into the university's partnered lab? What do you think we should do first?"
    $ show_textbox = False
    $ show_image_buttons = True
    jump research

label dumpsterdive:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    
    PC "Let's head to Bob Anderson's office. I wonder what we can find there."

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We don't have to step in. We can stay outside and do some dumpster diving to find out more information."
        show leonie surprised at left
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right
        with dissolve
        A "People often throw away sensitive information without disposing of it correctly. If we look at the trash, we could find something compromising that could give us a lead."
        "You, Alex, and Leoni head to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg officebehind
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright

    PC "Hm, the building seems smaller than described on the internet."
    show leonie happy at left
    with dissolve

    L "Well, that means we don't have to search for too much. Look, the garbage bins are right over there."
    show alex angry at alex_right
    with dissolve

    A "I think someone has to look out for anyone incoming. We don't want to be seen searching through the trash, as that's pretty suspicious. I'll take on the role and whistle loudly to warn you."
    PC "Thank you, bro. Let's get going then."

    scene bg wastepaper 

    jump dumpster_diving_minigame_start

label after_dumpsterdive:
    $ show_textbox = True
    scene bg officebehind
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright
    A "Nice one, that's more like what we're looking for. Now, what does it say?"
    PC "It's a receipt from the (name)."
    L "Isn't that the super fancy expensive restaurant where only celebrities and rich people go?"
    A "Yup, I've heard a lot of wild things about that restaurant. You're right, only the higher classes can afford it."
    PC "Seems like Bob Anderson went there with someone."
    L "I wonder who he went there with. The food and drinks definitely look like for two people."
    $ gloss_dumpster_seen = True
    $ dumpster_doven = True

    jump research 

label dumpsterdive2:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Well then, I suggest we head out to Gil's place and investigate there."

    if dumpster_explained == False:
        show leonie thinking at left 
        with dissolve
        L "What are we going to do there though? It's not like we can just step in."
        show alex neutral at alex_right
        with dissolve
        A "We don't have to step in. We can stay outside and do some dumpster diving to find out more information."
        show leonie surprised at left
        with dissolve
        L "How is there going to be information in trash?"
        show alex serious2 at alex_right
        with dissolve
        A "People often throw away sensitive information without disposing of it correctly. If we look at the trash, we could find something compromising that could give us a lead."
        "You, Alex, and Leoni head to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg facility_1
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright

    PC "Wow, what a beautiful looking house."
    show leonie happy at left
    with dissolve

    L "Are we sure Gil is a bad guy? No way an evil person has such a wonderful house."
    show alex neutral at alex_right
    with dissolve
    A "Well, in movies, the bad guys tend to own more expensive houses since they earn more money through illegal ways than the average person does."

    PC "I suggest we start quickly. The more time we spend here, the more suspicion we raise."

    show alex happy at alex_right 
    with dissolve 

    A "Alright, let's get digging then."

    show leonie sad at left
    with dissolve
    L "Digging into trash... yippie."

    show alex angry at alex_right
    with dissolve
    A "Well, if you're not enthusiastic about it, then I suggest you look out and warn us in case anyone comes by. Me and [PN] will go on. Don't worry."

    show leonie happy at left 
    with dissolve
    L "Mhm."

    scene bg wastepaper 
    jump dumpster_diving_minigame2_start

label after_dumpsterdive2:
    $ show_textbox = True
    scene bg officebehind
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright
    A "Nice one, that's more like what we're looking for. Now, what does it say?"
    PC "It's a note from Gil."
    L "It says something about a handover."
    A "Interesting."
    PC "I wonder if this can be of any use to us."
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
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Fine, I'll suggest that we head to the university lab then. The lab is in a part of the campus that practically never gets used, so that's quite shady."
    show leonie thinking at left 
    with dissolve

    L "Good point, but maybe they just don't want to disturb others with their noises or get distracted?"
    show alex neutral at alex_right
    with dissolve

    A "Or maybe they want to hide whatever they're doing?"
    "You, Alex, and Leoni head to the lab."

    hide alex with moveoutright
    hide leonie with moveoutleft

    scene bg labfront 
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright

    PC "Alright, here we are."

    show leonie happy at left
    with dissolve

    L "It's kinda far from everything else. I see why you call it shady."

    show alex angry at alex_right
    with dissolve

    A "They sure didn't want to be discovered. How are we going to get in?"
    PC "I'll find a way to sneak in."

    hide leonie with moveoutleft
    hide alex with moveoutright
    with dissolve

    scene bg labin1 
    with dissolve

    $ sneak_attempt += 1
    if sneak_attempt >= 2:
        jump lab_access_denied

    show alex neutral at left 
    with dissolve

    PC "Alright, let's search around. Anything useful we find will help us a lot."

    show leonie surprised at left 
    with dissolve
    show alex neutral at alex_right
    with dissolve

    A "What a lovely looking lab."
    L "Doesn't look as shady inside as it does from the outside."
    $ sneak_attempt += 1
    if sneak_attempt >= 2:
        jump lab_access_denied

    jump lab_search_minigame_start

label after_labsearch:
    $ show_textbox = True
    scene bg labfront
    with dissolve
    show leonie happy at left
    with moveinleft
    show alex neutral at alex_right
    with moveinright
    A "Nice one, that's more like what we're looking for. Now, what does it say?"
    PC "It's a logbook of some sort. It has names and details of people who entered the lab."
    L "Interesting. Let's make a copy of this."
    A "Yup, this will be useful for our investigation."
    PC "Good job, team."
    $ gloss_lab_seen = True
    $ lab_done = True
    jump research 

label research:
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label phishing:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "Let's craft a phishing email to gather more intel on Bob Anderson and his building."
    show leonie thinking at left 
    with dissolve
    L "Sounds good. We need to make it convincing enough for him to fall for it."
    show alex neutral at alex_right
    with dissolve
    A "Agreed. Let's use the information we already have to make it believable."
    PC "I'll start drafting the email."
    "You and your team work together to create a convincing phishing email targeting Bob Anderson."

    $ show_textbox = False
    $ show_image_buttons = True
    jump email_drafting

label email_drafting:
    $ show_textbox = True
    scene bg office
    with dissolve
    PC "Alright, let's see what we have here. We need to make sure this email looks authentic."
    show leonie happy at left
    with dissolve
    L "Make sure to include details that only someone close to him would know."
    show alex neutral at alex_right
    with dissolve
    A "And don't forget to create a sense of urgency. People are more likely to respond to urgent emails."
    PC "Got it. Let's get to work."
    "You and your team carefully craft the phishing email, making sure to include relevant details and an urgent tone."
    PC "All done. Now, we just have to wait and see if he takes the bait."
    L "Great job, everyone. Let's hope this works."
    A "Fingers crossed."
    $ email_sent = True
    $ phishing_done = True
    jump research

label wait_email:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "We'll have to wait for a response to our phishing email. In the meantime, let's explore other options."
    show leonie thinking at left 
    with dissolve
    L "Agreed. We shouldn't waste any time."
    show alex neutral at alex_right
    with dissolve
    A "Let's keep looking for more leads while we wait."
    PC "Good idea. Let's get back to work."
    $ wait_email_done = True
    jump research

label lab_done:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "We have the logbook from the lab. This could be very useful."
    show leonie thinking at left 
    with dissolve
    L "Let's analyze the names and details in the logbook. Maybe we'll find a connection."
    show alex neutral at alex_right
    with dissolve
    A "Good idea. Let's get to it."
    PC "We'll split up the work to make it faster."
    "You and your team analyze the logbook, looking for any useful information."
    PC "Look at this, there's a name that keeps appearing. This could be a lead."
    L "Interesting. Let's dig deeper into this person's background."
    A "On it. Let's see what we can find."
    $ logbook_analyzed = True
    $ lab_info_used = True
    jump research

label dumpster_doven:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "The dumpster diving was worth it. We found some useful information."
    show leonie thinking at left 
    with dissolve
    L "Let's go through what we found and see if there's anything that stands out."
    show alex neutral at alex_right
    with dissolve
    A "Agreed. We need to analyze everything carefully."
    PC "Let's start with the receipts and notes we found."
    "You and your team carefully analyze the items found during the dumpster dive, looking for any useful information."
    PC "This receipt from the expensive restaurant is interesting. Maybe we can use this to our advantage."
    L "Let's see if we can find out who Anderson was meeting with."
    A "I'll start looking into it right away."
    $ dumpster_info_analyzed = True
    $ dumpster_doven_done = True
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

label apartment_visited:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You've already been to the apartment. There's nothing more to find here."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

label email_responded:
    $ show_textbox = True
    scene bg office
    with dissolve
    PC "We got a response to our phishing email!"
    show leonie happy at left
    with dissolve
    L "Excellent! What does it say?"
    show alex excited at alex_right
    with dissolve
    A "This could be the breakthrough we need."
    PC "Let's see... he's scheduled a meeting at a new location. This might be our chance to gather more intel."
    L "Great work, team. Let's prepare for the meeting."
    $ email_responded = True
    jump plan_meeting

label plan_meeting:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "We need to be strategic about this meeting. It's our chance to gather crucial information."
    show leonie thinking at left 
    with dissolve
    L "We should blend in and observe without drawing attention."
    show alex neutral at alex_right
    with dissolve
    A "I'll handle the technical aspects. Maybe we can plant a device to listen in."
    PC "Good plan. Let's gather our gear and get ready."
    "You and your team prepare for the meeting, making sure you have all the necessary equipment."
    $ meeting_prepared = True
    jump attend_meeting

label attend_meeting:
    $ show_textbox = True
    scene bg cafe
    with dissolve
    "You and your team arrive at the meeting location and discreetly take your positions."
    show leonie casual at left
    with dissolve
    L "There he is. Let's keep a low profile and observe."
    show alex casual at alex_right
    with dissolve
    A "I'll plant the listening device."
    "Alex discreetly plants a listening device near Bob Anderson's table."
    PC "Now, we wait and listen."
    "You and your team listen in on the conversation, gathering valuable information."
    PC "This is it. We have enough evidence to take action."
    L "Great job, everyone. Let's regroup and plan our next move."
    $ meeting_attended = True
    jump regroup

label regroup:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "We've gathered a lot of information. Now we need to decide our next move."
    show leonie thinking at left 
    with dissolve
    L "We should compile everything we have and create a solid plan of action."
    show alex neutral at alex_right
    with dissolve
    A "Agreed. Let's make sure we cover all our bases."
    PC "I'll start organizing our findings."
    "You and your team compile all the information you've gathered and create a detailed plan of action."
    PC "This is it. We're ready to take the next step."
    L "Let's do this."
    A "For the mission."
    $ mission_ready = True
    jump execute_mission

label execute_mission:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "We've reached the final stage of our mission. Everything we've done so far has led to this moment."
    show leonie determined at left 
    with dissolve
    L "We need to stay focused and execute the plan perfectly."
    show alex determined at alex_right
    with dissolve
    A "No room for mistakes. Let's do this."
    PC "Team, let's move out."
    "You and your team move out to execute your carefully crafted plan. The success of your mission depends on your preparation and teamwork."
    PC "This is it. For everything we've worked for."
    $ mission_executed = True
    jump mission_outcome

label mission_outcome:
    $ show_textbox = True
    scene bg office
    with dissolve
    "After a tense and carefully executed operation, you and your team successfully complete your mission."
    show leonie happy at left
    with dissolve
    L "We did it! The mission was a success."
    show alex happy at alex_right
    with dissolve
    A "Great work, everyone. This was a team effort."
    PC "I'm proud of all of us. Let's celebrate this victory."
    "You and your team celebrate your successful mission, knowing that your hard work and dedication have paid off."
    PC "Here's to many more successful missions together."
    L "Cheers!"
    A "To the team!"
    "You and your team enjoy a well-deserved celebration, ready to take on whatever challenges come next."
    return

label check_email:
    if email_responded:
        jump email_responded
    else:
        $ show_textbox = True
        scene bg office
        with dissolve
        PC "Let's check our email to see if we got a response to the phishing attempt."
        show leonie thinking at left
        with dissolve
        L "We need to be patient, these things take time."
        show alex neutral at alex_right
        with dissolve
        A "I'll monitor the inbox closely."
        PC "Alright, let's keep our fingers crossed."
        $ show_textbox = False
        return

label mission_outcome:
    $ show_textbox = True
    scene bg office
    with dissolve
    "After a tense and carefully executed operation, you and your team successfully complete your mission."
    show leonie happy at left
    with dissolve
    L "We did it! The mission was a success."
    show alex happy at alex_right
    with dissolve
    A "Great work, everyone. This was a team effort."
    PC "I'm proud of all of us. Let's celebrate this victory."
    "You and your team celebrate your successful mission, knowing that your hard work and dedication have paid off."
    PC "Here's to many more successful missions together."
    L "Cheers!"
    A "To the team!"
    "You and your team enjoy a well-deserved celebration, ready to take on whatever challenges come next."
    return

label unknown_location:
    $ show_image_buttons = False
    if show_textbox == False:
        $ show_textbox = True
        $ hide_textbox = True
    hide screen phone_hand_map 
    "You can't proceed to an unknown location. You need to gather more information first."
    if hide_textbox == True:
        $ show_textbox = False
        $ hide_textbox = False
    $ show_image_buttons = True
    show screen phone_hand_map
    return

screen phone_hand_map:
    tag map
    imagemap:
        ground "bg/phone_hand_map.png"

        hotspot (60, 350, 240, 180) action Jump("apartment") # Apartment location
        hotspot (300, 350, 240, 180) action Jump("office") # Office location
        hotspot (540, 350, 240, 180) action Jump("cafe") # Cafe location
        hotspot (780, 350, 240, 180) action Jump("unknown_location") # Unknown location
   
    imagebutton:
        idle "phone_icon.png"
        hover "phone_icon_hover.png"
        action Jump("check_email")
        xpos 0.9 ypos 0.1
        xanchor 0.5 yanchor 0.5

# Backgrounds
image bg apartment = "bg/apartment.jpg"
image bg office = "bg/office.jpg"
image bg new_kitchen = "bg/new_kitchen.jpg"
image bg cafe = "bg/cafe.jpg"

# Characters
define PC = Character("[pc_name]", color="#a9dcff")
define L = Character("Leonie", color="#ffcc66")
define A = Character("Alex", color="#ff6b6b")

# Character Images
image leonie happy = "leonie_happy.png"
image leonie serious = "leonie_serious.png"
image leonie thinking = "leonie_thinking.png"
image leonie casual = "leonie_casual.png"
image leonie determined = "leonie_determined.png"
image alex excited = "alex_excited.png"
image alex serious1 = "alex_serious1.png"
image alex neutral = "alex_neutral.png"
image alex casual = "alex_casual.png"
image alex happy = "alex_happy.png"
image alex determined = "alex_determined.png"

init python:
    show_textbox = True
    hide_textbox = False
    show_image_buttons = True
    apartment_visited = False
    email_responded = False
    meeting_prepared = False
    meeting_attended = False
    mission_ready = False
    mission_executed = False
 
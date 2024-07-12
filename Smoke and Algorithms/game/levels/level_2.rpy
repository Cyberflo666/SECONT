```
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
    show leonie happy at left with moveinleft
    show alex neutral at alex_right with moveinright
    A "Jackpot! This is the kind of dirt we're after. Whatcha got there?"
    PC "Looks like a receipt from [name]." 
    L "[Name]? Isn't that that super swanky joint where the rich and famous rub elbows?"
    A "You betcha. Heard it's where the champagne flows like water and the caviar dreams come true. Definitely not for us mere mortals."
    PC "Looks like Bob Anderson had a little rendezvous there with someone."
    L "Hmm, the bill's definitely big enough for two. Wonder who the lucky guest was..."
    $ gloss_dumpster_seen = True
    $ dumpster_doven = True
    
    jump research 

label dumpsterdive2:
$ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve

    PC "Alright, team, next stop: Gil's place. Let's see what we can dig up."

    if dumpster_explained == False:
        show leonie thinking at left with dissolve
        L "Wait, what exactly are we planning to do there? We can't just waltz in."
        show alex neutral at alex_right with dissolve
        A "Who said anything about waltzing? We're going dumpster diving, baby! Think of it as urban archaeology, but with a side of stinky secrets."
        show leonie surprised at left with dissolve
        L "Garbage? Seriously? What are we hoping to find, last week's leftovers?"
        show alex serious2 at alex_right with dissolve
        A "Trust me, people toss out all sorts of incriminating evidence without thinking twice.  We might find a smoking gun in that trashcan."
        "You, Alex, and Leoni head to the building."
        $ dumpster_explained = True 

    hide alex with moveoutright
    hide leonie with moveoutleft
    scene bg facility_1 with dissolve
    show leonie happy at left with moveinleft
    show alex neutral at alex_right with moveinright

    PC "Whoa, this place is a palace!"
    show leonie happy at left with dissolve
    L "Seriously? Are we sure this guy is a baddie? This house screams 'luxury lifestyle,' not 'evil villain.'"
    show alex neutral at alex_right with dissolve
    A "Yeah, well, in the movies, the bad guys always have the best real estate. Gotta fund those nefarious schemes somehow."
    PC "Alright, team, let's not get distracted. Time to roll up our sleeves and get down and dirty."
    show alex happy at alex_right with dissolve 
    A "Let's do it! Who's ready for a treasure hunt in the trash?"
    show leonie sad at left with dissolve
    L "Ugh, digging through garbage... not exactly my idea of a good time."
    show alex angry at alex_right with dissolve
    A "Hey, no one's forcing you. You can play lookout while [PN] and I get our hands dirty. Don't worry, we'll save all the juicy gossip for you."
    show leonie happy at left with dissolve
    L "Deal. Just try not to get too smelly."
    scene bg wastepaper 
    jump dumpster_diving_minigame2_start

label after_dumpsterdive2:
    $ show_textbox = True
    scene bg officebehind
    with dissolve
    show leonie happy at left with moveinleft
    show alex neutral at alex_right with moveinright
    A "Bingo! This looks promising. Spill the beans, what's it say?"
    PC "It's a note from Gil."
    L "Hmm, something about a 'handover'...  This could be interesting."
    A "Definitely piques my curiosity. Let's see how this fits into the puzzle."
    PC "We'll figure it out. Every little clue brings us closer to the truth."
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

    PC "Alright, team, how about we check out that university lab? Tucked away in a forgotten corner of campus... definitely raises some eyebrows."
    show leonie thinking at left with dissolve
    L "True, but maybe they're just trying to avoid distractions, you know? Focus on their super-secret science stuff."
    show alex neutral at alex_right with dissolve
    A "Or maybe they're hiding something shady. Let's go snoop around and find out!"

     
    "The trio sets off, adrenaline pumping as they venture towards the mysterious lab."

    hide alex with moveoutright
    hide leonie with moveoutleft
    scene bg labfront with dissolve
    show leonie happy at left with moveinleft
    show alex neutral at alex_right with moveinright

    PC "Well, this is the place."
    show leonie happy at left with dissolve
    L "Creepy... just like you said. Gives me the heebie-jeebies."
    show alex angry at alex_right with dissolve
    A "They sure didn't want visitors. So, how do we crack this nut?"

     
    "Alex fiddles with his lockpick kit, a mischievous grin spreading across his face."

    PC "Leave that to me. I've got a few tricks up my sleeve."

    hide leonie with moveoutleft
    hide alex with moveoutright with dissolve
    scene bg labin1 with dissolve

    $ sneak_attempt += 1
    if sneak_attempt >= 2:
        jump lab_access_denied

    show alex neutral at left with dissolve
    PC "Okay, team, let's get to work. Keep your eyes peeled for anything out of the ordinary."
    show leonie surprised at left with dissolve
    show alex neutral at alex_right with dissolve
    A "Wow, this place is decked out! Top-notch equipment everywhere."
    L "Doesn't look so spooky on the inside. Maybe they're just science nerds, after all?"

      (if sneak_attempt < 2)
    "As the team begins their search, a sense of anticipation hangs in the air. What secrets will this lab reveal?"

    $ sneak_attempt += 1
    if sneak_attempt >= 2:
        jump lab_access_denied

    jump lab_search_minigame_start

label after_labsearch:
    $ show_textbox = True
    scene bg labfront
    with dissolve
    show leonie happy at left with moveinleft
    show alex neutral at alex_right with moveinright
    A "Booyah! That's more like it! Now, what's the scoop?"
    PC "Looks like some kind of logbook. Names, details... people who entered the lab."
    L "Ooh, juicy! Let's make a copy of this, stat."
    A "Roger that. This baby's gonna be a goldmine for our investigation."
    PC "Great work, team. You guys rock!"
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
    PC "Alright, team, time to get our phish on! Let's cook up an email that'll reel in Bob Anderson."
    show leonie thinking at left with dissolve
    L "We gotta make it irresistible bait. Think we can hook him?"
    show alex neutral at alex_right with dissolve
    A "No sweat. We've got the intel to make this email sing. Just watch him bite."
    PC "I'll get started on the draft. You guys brainstorm the juiciest details."
    "You and your team work together to create a convincing phishing email targeting Bob Anderson."

    $ show_textbox = False
    $ show_image_buttons = True
    jump email_drafting

label email_drafting:
    $ show_textbox = True
    scene bg office
    with dissolve
    PC "Okay, let's see what we've got. This email needs to be pure clickbait, folks."
    show leonie happy at left with dissolve
    L "Sprinkle in some inside info, something only his inner circle would know."
    show alex neutral at alex_right with dissolve
    A "And don't forget the urgency factor. Gotta make him sweat a little."
    PC "You got it. Let's craft this masterpiece."
    "You and your team carefully craft the phishing email, making sure to include relevant details and an urgent tone."
    PC "Boom! It's done. Now let's sit back and watch the magic happen."
    L "Nice work, everyone. Here's hoping he takes the bait."
    A "Fingers crossed, toes too!"
    $ email_sent = True
    $ phishing_done = True
    jump research

label wait_email:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "While we wait for that phishing line to tug, let's not twiddle our thumbs. What else can we dig up?"
    show leonie thinking at left with dissolve
    L "Agreed. Time is of the essence."
    show alex neutral at alex_right with dissolve
    A "Let's keep those leads flowing. We're on a roll!"
    PC "Sounds like a plan. Back to the grind, team!"
    $ wait_email_done = True
    jump research

label lab_done:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "That logbook we snagged from the lab is a real treasure trove."
    show leonie thinking at left with dissolve
    L "Let's crack it open and see what secrets it spills. Maybe we'll find a connection."
    show alex neutral at alex_right with dissolve
    A "Sounds good to me. Let's get to work, Sherlock."
    PC "We'll divide and conquer to speed things up."
    "You and your team analyze the logbook, looking for any useful information."
    PC "Whoa, check this out! This name keeps popping up. Could be a hot lead."
    L "Intriguing. Let's dig a little deeper into this character's past."
    A "I'm on it. Let's see what skeletons we can unearth."
    $ logbook_analyzed = True
    $ lab_info_used = True
    jump research

label dumpster_doven:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left
    show alex serious1 at alex_right
    with dissolve
    PC "Dumpster diving pays off, guys! We found some goodies in the trash."
    show leonie thinking at left with dissolve
    L "Let's sift through the loot and see if anything sparkles."
    show alex neutral at alex_right with dissolve
    A "Definitely. We need to examine every scrap."
    PC "Starting with these receipts and notes. Who knows what secrets they hold?"
    "You and your team carefully analyze the items found during the dumpster dive, looking for any useful information."
    PC "Hmm, this fancy restaurant receipt is interesting. Maybe we can squeeze some lemonade out of this lemon."
    L "Let's figure out who Anderson was dining with. Could be a key player."
    A "I'm on the case. Let's get this show on the road!"
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
    PC "We got a hit! The phishing email worked."
    show leonie happy at left with dissolve
    L "Yes! What's the response?"
    show alex excited at alex_right with dissolve
    A "This could be our big break."
    PC "It looks like... a meeting at a new location.  This could be our chance to get the intel we need."

     
    "A wave of excitement washes over the team. The long-awaited response brings them one step closer to their goal."

    L "Great work, team. Let's prepare."
    $ email_responded = True
    jump plan_meeting

label plan_meeting:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left with dissolve
    show alex serious1 at alex_right with dissolve

     
    "The mood shifts to focused determination. The team gathers in their makeshift headquarters, ready to strategize."

    PC "We need to approach this meeting strategically. It's our opportunity to gather crucial intel."
    show leonie thinking at left with dissolve
    L "We should blend in, observe, avoid drawing attention."
    show alex neutral at alex_right with dissolve
    A "I'll handle the tech. Maybe we can plant a bug to listen in."
    PC "Good idea. Let's get our gear together."

     
    "With a plan in place, the team sets about preparing for the meeting, ensuring they have everything they need to succeed."

    "You and your team prepare for the meeting, making sure you have all the necessary equipment."
    $ meeting_prepared = True
    jump attend_meeting

label attend_meeting:
    $ show_textbox = True
    scene bg cafe
    with dissolve

     
    "The day of the meeting arrives. The team takes their positions, nerves taut but resolve unwavering."

    "You and your team arrive at the meeting location and discreetly take your positions."
    show leonie casual at left with dissolve
    L "There he is. Stay casual, just observe for now."
    show alex casual at alex_right with dissolve
    A "I'm on it. Planting the bug now."

     
    "Alex, ever the tech expert, makes his move, slipping the tiny device into place undetected."

    "Alex discreetly plants a listening device near Bob Anderson's table."
    PC "Now, we wait and listen."

     
    "The minutes tick by as the team strains to hear every word, every nuance of the conversation."

    "You and your team listen in on the conversation, gathering valuable information."
    PC "This is it. We have the evidence we need."
    L "Excellent work, everyone. Let's regroup and plan our next steps."
    $ meeting_attended = True
    jump regroup

label regroup:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left with dissolve
    show alex serious1 at alex_right with dissolve

     
    "Back at their base, the weight of the gathered information settles on the team."

    PC "We've got a lot to work with here. Now we need to decide our next move."
    show leonie thinking at left with dissolve
    L "Let's compile everything and formulate a solid plan."
    show alex neutral at alex_right with dissolve
    A "Agreed. We need to be thorough."

     
    "The team spends hours poring over the data, connecting dots and uncovering hidden patterns."

    PC "I'll start organizing our findings."
    "You and your team compile all the information you've gathered and create a detailed plan of action."
    PC "This is it. We're ready for the next phase."
    L "Let's do this."
    A "For the mission."
    $ mission_ready = True
    jump execute_mission

label execute_mission:
    $ show_textbox = True
    scene bg new_kitchen
    show leonie serious at left with dissolve
    show alex serious1 at alex_right with dissolve

     
    "The final stage of the mission is upon them. The tension in the room is palpable."

    PC "This is the final stretch. Everything we've done has led to this."
    show leonie determined at left with dissolve
    L "We need to stay focused and execute flawlessly."
    show alex determined at alex_right with dissolve
    A "No room for error. Let's move."
    PC "Team, it's go time."

     
    "The team moves out, each member playing their part in the carefully orchestrated plan."

    "You and your team move out to execute your carefully crafted plan. The success of your mission depends on your preparation and teamwork."
    PC "This is it. For everything we've worked for."
    $ mission_executed = True
    jump mission_outcome

label mission_outcome:
    $ show_textbox = True
    scene bg office
    with dissolve

     
    "The aftermath of the operation. The team reconvenes, their faces etched with exhaustion and triumph."

    "After a tense and carefully executed operation, you and your team successfully complete your mission."
    show leonie happy at left with dissolve
    L "We did it! Mission accomplished."
    show alex happy at alex_right with dissolve
    A "Great work, everyone. This was a true team effort."
    PC "I couldn't be prouder. Let's celebrate!"

     
    "The team raises a toast to their victory, a hard-won triumph against the odds."

    "You and your team celebrate your successful mission, knowing that your hard work and dedication have paid off."
    PC "To many more successful missions together."
    L "Cheers!"
    A "To the team!"

     
    "As the celebration winds down, the team basks in the glow of their accomplishment, ready to face the next challenge."

    "You and your team enjoy a well-deserved celebration, ready to take on whatever comes next."
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
 
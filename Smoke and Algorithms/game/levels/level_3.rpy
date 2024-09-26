label level_3_start:
    $ in_dorms = False
    define level_3_s = False
    $ level_3_s = True
    define fire_alarm = False
    define door_state = False
    define leonie_away = True
    define a = "t"
    define b = "f"
    define have_USB = True
    define security_aware = False
    define detected = False
    define cameras_off = True
    define visability_list = [False,False,False,False]
    define visability_list1 = [False,False,False,False]
    define visability_list2 = [False,False]
    define number_found = False
    define phone_seen = False
    define first_time_in = True
    define game_matrix= [
                        [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                        [0,["c",b,0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                        [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                        [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                        [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                        [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                        [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                        [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                        [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                        [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                        [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                        [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                        [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                        [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                        [0,[0,a,0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                        ]
    define orange_path = [[14,3,1],[13,3,1],[12,3,1],[11,3,2],[11,4,2],[11,5,1],[10,5,1],[9,5,2],[9,6,2],[9,7,2],[9,8,1],[8,8,1],[7,8,1],[6,8,4],[5,8,4],[5,7,4],[5,6,4],[5,5,3],[6,5,3],[-1,-1]]
    define green_path = [[14,5,1],[13,5,1],[12,5,1],[11,5,1],[10,5,1],[9,5,4],[9,4,4],[9,3,4],[9,2,1],[8,2,1],[7,2,4],[7,1,4],[7,0,4],[-1,-1]]
    define purple_path = [[7,0,2],[7,1,2],[7,2,1],[6,2,1],[5,2,2],[5,3,2],[5,4,2],[5,5,1],[4,5,1],[3,5,1],[2,5,2],[2,6,2],[2,7,2],[2,8,2],[-1,-1]]
    define blue_path = [[2,0,2],[2,1,2],[2,2,2],[2,3,2],[2,4,2],[2,5,3],[3,5,3],[4,5,3],[5,5,4],[5,4,4],[5,3,4],[5,2,3],[6,2,3],[7,2,4],[7,1,4],[7,0,4],[-1,-1]]
    define sec_path_1 = [[2,8,4],[2,7,4],[2,6,4],[2,5,4],[2,4,4],[2,3,4],[2,2,4],[2,1,4],[2,0,4],[2,0,2],[2,1,2],[2,2,2],[2,3,2],[2,4,2],[2,5,2],[2,6,2],[2,7,2],[2,8,2],[-1,-1]]
    define sec_path_2 = [[11,8,4],[11,7,4],[11,6,4],[11,5,4],[11,4,4],[11,3,4],[11,2,4],[11,1,4],[11,0,4],[11,0,2],[11,1,2],[11,2,2],[11,3,2],[11,4,2],[11,5,2],[11,6,2],[11,7,2],[11,8,2],[-1,-1]]
    define sec_path_3 = [[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[-1,-1]]
    define sec_path_4 = [[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[-1,-1]]
    define sec_index_1 = 11
    define sec_index_2 = 0
    define sec_index_3 = 0
    define sec_index_4 = 0
    define sec_list = [[sec_path_1,sec_index_1],[sec_path_2,sec_index_2],[sec_path_3,sec_index_3],[sec_path_4,sec_index_4]]
    define orange_index = 2
    define green_index = 5
    define purple_index = 10
    define blue_index = 8
    define tailgate_list = [[orange_path,orange_index],[green_path,green_index],[purple_path,purple_index],[blue_path,blue_index]]
    define valid_inputs = [1,1,0,0,0]
    define player_pos = [14,1]
    define door_timer = 0
    define door_timer1 = 0
    define door_state1 = False
    define optional_flag = True
    define bobs_flag = True
    define courtyard_flag = True
    define painting_seen = False
    define sofa_seen = False
    define computer_seen = False
    define books_seen = False
    define hospital_bed_seen = False
    define operation_table_seen = False 
    define skull_anatomy_seen = False
    scene bg back office far 
    #show leonie neutral at left
    #show alex neutral at alex_right
    #with dissolve

    play music mystery_music1 volume loudness

    "As the sun starts to set, your team arrives at the facility where {color=[medievilColor]}Medievil{/color} probably conducts tons of unethical experiments and also where Bob Anderson works."

    #show leonie serious at left
    #with dissolve
    L "With the access code Bob unknowingly gave us, we should be able to enter via the back entrance."

    #show alex serious1 at alex_right
    #with dissolve
    A "Although it's probably emptier than at day, there are still a few people going in and out of the building. We have to be careful."

    "While staying at a save distance from the facility, Leonie examines the building."

    #show leonie sad at left
    #with dissolve
    L "It's no use. From here I can't really make out their methods of security."

    PC "Ok, let's go in then and take a closer look. That's what we have the codes for."

    show bg back office
    show leonie thinking at left
    show alex neutral at alex_right
    with dissolve
    "With Leonie leading, the three of you go towards the back entrance and towards the pin pad. None of the few people here seem to pay attention to you."

    show leonie thinking at left
    with dissolve
    L "..."

    show leonie happy at left
    with dissolve
    L "Yes, the code worked."

    show bg hallway night 3
    "With the door open, you sneakily follow the hallways towards the office areas. The hallways are almost completely void of any employees."

    show leonie serious at left
    with dissolve
    "Leonie whispers:"
    L "Wait, here it says that Bobs office and all the other important spaces are all in this area."

    show alex happy at alex_right
    with dissolve
    A "Sweet, let's go..."

    show leonie surprised at left
    with dissolve
    L "Wait!"
    "Leonie grabs Alex by his shirt and pulls him back behind the corner."

    show leonie serious at left
    with dissolve
    L "The following area seems to be secured by cameras and guards and you almost walked right into their field of view."

    show alex surprised at alex_right
    with dissolve
    A "Oh crap, thanks Leonie."

    show leonie neutral at left
    with dissolve
    L "Additionally, it seems as if we can't really get any further anyways. Do you see that door up ahead. It requires a key card to get through that we don't have."

    PC "I'm not sure how we are supposed to get our hands on one of these."

    show alex smile at alex_right
    with dissolve
    A "I don't think we have to."

    show leonie thinking at left
    with dissolve
    L "What do you mean."

    show alex neutral at alex_right
    with dissolve
    A "\'Tailgaiting\'. We follow one of the employees through the door and pretend we belong here. I think most people would believe us and just hold the door open for us like we were other employees."

    $ gloss_tailgating_seen = True

    show leonie serious at left
    with dissolve
    L "Great idea. So we have to come back during day for this to work."

    PC "Yup, let's do this."

    scene black
    with dissolve

    play music main_music1 volume loudness

    "Your group returns the way you came in and goes home without any incidents."

    "The next day during breakfast, you talk about your approach."
    scene bg new kitchen
    show alex neutral at alex_right
    show leonie thinking at left
    with dissolve
    L "I think I'm going to stay here. There were cameras all over the office spaces and if I stay here, I could give you support from afar."

    show leonie serious at left
    with dissolve
    L "Take this USB-Drive. If you manage to plug it into their security network, I get access to the cameras and can give you directions."

    PC "Hmm, this seems useful. Alright, everything set for todays infiltration?"

    show alex smile at alex_right
    with dissolve
    A "Yes."

    show leonie happy at left
    with dissolve
    L "Yup."

    scene black
    with dissolve
    "With Leonie staying home, only Alex and you go towards the facility."

    play music mystery_music1 volume loudness

    scene bg front office 2 
    with dissolve
    "You find yourself at the spot you were yesterday."
    #hide alex with dissolve

define main_entrace_flag = False
define observe_entrance_flag = False
define infront_facility = True
label menu_outside:
scene bg front office 2 
hide alex
with dissolve
show screen phone_icon

menu:
    "Take the main entrance." if main_entrace_flag == False:
        hide screen phone_icon
        "You and Alex decide to go through the main entrance"
        "Upon entering you are greeted by ... no one. Every employee seems to be heavily invested in their work and there is a lot of security roaming around."
        jump main_entrance
    "Observe the people entering the facility." if observe_entrance_flag == False:
        hide screen phone_icon
        "All the people you see look like they have buisness at this place. You can't spot anyone who looks like a visitor in your eyes."
        "Through the opening main entrance door you can make out that there is heavy security guarding this place, but they don't seem to check the people entering."
        $ observe_entrance_flag = True
        jump menu_outside
    "Go through the back door with the pin you got from Bob.":
        hide screen phone_icon
        scene bg back office day
        with dissolve
        "The two of you sneakily enter the building with the same method from yesterday."
        jump back_entrance

define stairs_went = False
define receptionist_talked = False
define USB_placed_0 = False
define main_entrance_entered = False
label main_entrance:
    hide phone_icon
    scene bg front lobby
    show alex serious2 at alex_right
    with dissolve
    if main_entrance_entered == False:
        A "(whispering){size=23}Is it just me or are they not expecting visitors.{/size}"
        PC "(whispering){size=23}Thats you, they are probaply just really busy.{/size}"
        A "(whispering){size=23}Yeah sure. Anyways, what's the plan now.{/size}"
label main_entrance_menu:
    menu:
        "Go back outside":
            "Alex and you leave through the entrance you came in attracting a few weird looks but nothing more."
            $ main_entrace_flag = True
            $ main_entrance_entered = True
            jump menu_outside
        "Talk to the receptionist" if receptionist_talked == False:
            scene bg receptionist
            with dissolve
            "Alex goes up to what looks like the guest reception. The Lady at the desk doesn't notice you at first."
            show alex neutralleft at alex_left
            show receptionist neutral at receptionist_right
            with dissolve
            A "Excuse me"
            show receptionist annoyed at right
            "He looks up slightly annoyed."
            R "Can i help you?"
            show alex smileleft at alex_left
            with dissolve
            A "My name is Gill Cameron and i need to deliver some packages to Bob Anderson."
            show receptionist suspicious at right
            R "Let me see your ID please."
            "Knowing that this will probaply not work out you signal alex with a look that its time to bale."
            show alex happyleft at alex_left
            with dissolve
            A "Yeah sure, its in my van outside. I'll be back in a minute."
            "Alex and you leave the building through the main entrance not daring to go back this way."
            $ receptionist_talked = True
            $ main_entrace_flag = True
            jump menu_outside
        "Try to go into the restricted office area" if stairs_went == False:
            "As you approach the stairs to the office area the security stops and questions you. By letting Alex talk you get out rather easy but the security now keeps an eye out for you."
            $ stairs_went = True
            $ security_aware = True
            jump main_entrance_menu
        "Place the USB-Drive with a deciving note on a nearby desk" if USB_placed_0 == False:
            "You try to sneakily place leonies drive on the desk. As you leave you notice a security guard inspecting your trap. Shortly after he looks up with a determined suspicious face."
            show alex serious1 at alex_right
            with dissolve
            A "(Whispering) {size=23}I dont think he fell for it.{/size}"
            PC "(Whispering) {size=23}We should probaply leave before finds what he is looking for.{/size}"
            "With your ninja-like agility you are able to avoid the guards gaze while leaving through the entrance."
            $ USB_placed_0 = True
            $ have_USB = False
            $ main_entrace_flag = True
            jump menu_outside

label back_entrance:
    scene bg secretary office
    "As you try to go the same way as before, you get noticed by what looks like a secretary."
    show secretary suspicious at center
    S1 "Excuse me, who are you. I have not seen you here before."
    menu:
        "Tell her that you are the new interns of Aob Anderson and you need to go to his office.":
            show secretary suspicious at secretary_right
            show alex smileleft at alex_left
            with dissolve
            A "We are Bob Andersons new interns and it's our first day. He said we should wait for him in his office for further instructions."
            show secretary angry at secretary_right
            with dissolve
            S1 "Bob didn't mention any new interns."
            show alex neutralleft at alex_left 
            with dissolve
            A "How else would we have gotten access."
            show secretary thinking at secretary_right
            with dissolve
            S1 "Well thats a good point. Sorry for being so mistrustful but our higher ups want us to take security rather serious"
            show alex happyleft at alex_left
            with dissolve
            A "Yeah we know. Bob also said to us we shouldnt speak of what we do here outside of work."
            show secretary neutral at secretary_right
            with dissolve
            S1 "Sounds like him. Anyways his office is in the area with the others just down this corridor."
            show alex smileleft at alex_left
            with dissolve
            A "Okay great, thank you."
            show secretary friendly at secretary_right_smile
            with dissolve
            S1 "No problem."
        "Tell her you need to go to the bathroom and make a run for it":
            #show secretary thinking at secretary_right
            scene bg hallway 2
            with dissolve
            "After you tell her your reason she looks like she wants to say something but you just start running in the direction of the bathroom."
            "The secretary will remember that."
            $ security_aware = True
        "Pretend to be technicians":
            show secretary suspicious at secretary_right
            show alex neutralleft at alex_left
            with dissolve
            A "We are technicians and here for problems with the internet connection in the west wing. We where called by Mr. Anderson you know where he is? We need some information before we start."
            show secretary thinking at secretary_right
            with dissolve
            S1 "Well i don't know where he is but just wait here a minute, i will call him right now."
            show alex happyleft at alex_left
            with dissolve
            A "Thats not gonna be necessary, we will just look for him ourselfs thank you."
            show secretary friendly at secretary_right_smile
            with dissolve
            S1 "No no, its nothing really. Just one second."
            show secretary neutral at secretary_right
            show alex serious2left at alex_left
            with dissolve
            "The secretary starts to type something on her phone and then proceeds to wait for a call."
            "You decide its best if you bale out while she is distracted before your lie falls apart right infront of you."
            scene bg hallway 2
            with dissolve
            "With that in mind you make a run for the office area before she can stop you."
            scene bg hallway 1
            show guard_angry at security
            with dissolve
            "After only a few minutes you find security waiting for you around the corner."
            jump game_over

define USB_placed_1 = False

label way_to_the_office:
    scene bg hallway 1
    hide alex
    hide secretary
    with dissolve
    "Going furhter into the facility you find the begining of the office area you were looking for."
    A "Well what do we do now? We still don't have control of the cameras."

define before_office = False

label before_the_office:
    scene bg hallway 1
    $ infront_facility = False
    show screen phone_icon
    $ before_office = True
    menu:
        "Infiltrate bobs office":
            hide screen phone_icon
            "You decide that now is the time to infiltrate bobs office."
            play music security_music volume loudness
            $ reset()
            if have_USB == False:
                $ cameras_off = True
            show screen minigame_screen()
            hide screen minigame_screen
            jump security_minigame_start
            
        "Place the USB-Drive as a bait for employees" if USB_placed_1 == False and have_USB == True:
            hide screen phone_icon
            "You put the USB-Drive on a nearby desk with a note saying \"Observation team, please have a look at this\"."
            "To avoid further confrontation you hide in the bathroom until you get a call from leonie telling you that she is now in control of the cameras."
            $ cameras_off = False
            $ USB_placed_1 = True
            jump before_the_office

        "Activate the fire alarm":
            hide screen phone_icon
            "After activate the fire alarm you heard sirens going off and speakers talking. While everyone is leaving the building you hide in the bathroom and wait a bit."
            "With noone in the building you can just strole into the office of bob anderson."
            $ fire_alarm = True
            jump bobs_office

label courtyard:
    scene bg courtyard
    play music main_music1 volume loudness
    hide screen minigame_screen
    with dissolve
    $ show_textbox = True
    "You see beautiful flowers and a nice garden."
    "Upon staring at the delightful scenary, a group of butterflies comes across your sight."
    "You feel like you could maybe try to catch them."
    show screen butterfly_mini_game
    with dissolve

label optional:
    scene bg secret lab
    hide screen minigame_screen
    with dissolve
    $ show_textbox = True
    "you sneakingly open the door, somewhat afraid that an employee might be here and walk in slowly"
    show alex serious2left at alex_left
    with dissolve
    A "since were already in this weird room we might aswell take a look around"
    jump optional_clicking
    #clicking through room + stories begin.
label optional_clicking: #need to add images
    if hospital_bed_seen and operation_table_seen and skull_anatomy_seen:
        jump optional_clicking_done
    $ show_textbox = False
    scene bg secret lab 
    show screen optional_room
    with dissolve
    show screen phone_icon
    with moveinright
    jump empty_label
label hospital_bed:
    call hide_optional_room_screen
    scene bg secret lab beds
    with dissolve
    $ show_textbox = True
    "You see a blood stained operational seat that gives you the creeps"
    A "wow this looks quite frightening. I wonder what they did here"
    $ show_textbox = False
    $ hospital_bed_seen = True
    show screen phone_icon
    jump optional_clicking
label operation_table:
    call hide_optional_room_screen
    scene bg secret lab equipment
    with dissolve
    $ show_textbox = True
    "You see messy operational equipment.Looks like they have been used lately"
    $ show_textbox = False
    $ operation_table_seen = True
    show screen phone_icon
    jump optional_clicking
label skull_anatomy:
    call hide_optional_room_screen
    scene bg secret lab skull
    with dissolve
    $ show_textbox = True
    "you see an anatomy picture of a skull with marks on it."
    $ show_textbox = False
    $ skull_anatomy_seen = True
    show screen phone_icon
    jump optional_clicking


label optional_clicking_done:
    $ show_textbox = True
    hide screen phone_icon
    "upon inspecting the room you decide to go back into the hallway"
    jump security_minigame_start


label bobs_office:
    scene bg bob office
    hide screen minigame_screen
    with dissolve
    $ show_textbox = True
    show alex serious2left at alex_left
    with dissolve
    A "Now this is what were talking about. We finally made it."
    PC "I cant believe this place has that many security guards and employees hording around"
    show alex angryleft at alex_left
    with dissolve
    A "You know theres probably a good reason why there are so many security guards here around the clock right? "
    PC "Well lets try to find clues about Felix now though"
    jump bob_clicking
    #bobs office clicking through room begins
label bob_clicking: #need to add images
    $ show_textbox = False
    scene bg bob office
    show screen bob_laptop
    show screen bob_book_shelf
    show screen bob_sofa
    show screen bob_painting
    show screen bob_phone
    with dissolve

    show screen phone_icon
    with moveinleft
    jump empty_label


label laptop:
    call hide_bob_screens 
    scene bg bob office computer
    with dissolve 
    $ show_textbox = True
    "When observing the laptop you see that the laptop is locked"
    $ show_textbox = False
    $ computer_seen = True
    show screen phone_icon
    jump bob_clicking
label book_shelf:
    call hide_bob_screens 
    scene bg bob office books
    with dissolve 
    $ show_textbox = True
    "You see interesting books and look for a secret doorway behind unsucessfully"
    $ show_textbox = False
    $ books_seen = True
    show screen phone_icon
    jump bob_clicking
label phone:
    call hide_bob_screens
    scene bg bob office phone
    with dissolve
    $ show_textbox = True
    "This must be bobs phone. It looks pretty fancy and expensive."
    $ show_textbox = False
    $ phone_seen = True
    show screen phone_icon
    jump bob_clicking
label phone_2:
    call hide_bob_screens
    scene bg bob office phone
    with dissolve
    $ show_textbox = True
    $ trust = 50
    "You call the number from the notes you found."
    $ show_textbox = False
    show screen phone_icon
    jump voice_phishing
label sofa:
    call hide_bob_screens
    scene bg bob office sofa
    with dissolve
    $ show_textbox = True
    "The Sofa seems quite comfy however theres nothing of interest here."
    $ show_textbox = False
    $ sofa_seen = True
    show screen phone_icon
    jump bob_clicking
label painting:
    call hide_bob_screens 
    scene bg bob office painting
    with dissolve
    $ show_textbox = True
    "You look at the painting and wonder why its placed so low and in the middle. You realise that you can take off the painting and theres a hidden little space with letters and a note with what seems to be a phone number."
    scene bg bob office
    "The Letters are from someone called Joe Arnold. They talk about how he was supposed to look out for felix because bob anderson found his latest behavior suspicious."
    "They even mention the day you last saw felix and that the problem was taken care of."
    A "Is this about felix? What does taken care of mean? Do you think he's ... dead?"
    "I dont know but we shouldnt think of that. We need to think of what to do next if he is still alive."
    A "The number from the notes! I think there is a good chance its from this Joe Arnold. If we call him and pretend to be bob anderson he might tell us what happened to felix."
    $ show_textbox = False
    $ painting_seen = True
    $ number_found = True
    $ phone_seen = False
    show screen phone_icon
    jump bob_clicking

define trust_delta_2 = 25
define called_from_smartphone = False
define joe_called = 0

label voice_phishing:
    scene bg bob office
    hide screen phone_icon
    $ show_textbox = True
    $ joe_called = 1
    show screen round_rect(trust)
    with dissolve
    "Biep ... Biep ...."
    if called_from_smartphone == False:
        JA "Hey Bob what is it? Im kinda busy."
        menu:
            "Hi Joe. Im not Mr. Anderson only his assistant, but I have a question from him.":
                jump voice_phishing_1
            "Im bobs assistant and I have a question":
                $ trust -= trust_delta_2
                jump voice_phishing_1
            "Hello Mr. Arnold. Im Mr. Andersons assistant and he wanted me to ask you something.":
                $ trust += trust_delta_2

    else:
        JA "Hello who is there? Im kinda busy."
        menu:
            "Hi Joe. Im Mr. Andersons assistant and I have a question from him.":
                jump voice_phishing_1
            "Im bobs assistant and I have a question":
                $ trust -= trust_delta_2
                jump voice_phishing_1
            "Hello Mr. Arnold. Im Mr. Andersons assistant and he wanted me to ask you something.":
                $ trust += trust_delta_2

label voice_phishing_1:
    show screen round_rect(trust)     
    JA "Ok just make it quick."
    menu:
        "Do you remember his former intern Felix whom he needed help with? The small and anxious one who looks kinda like shaggy from scooby doo. Where you told Mr. Anderson he was taken care of.":
            $ trust -= trust_delta_2
            jump voice_phishing_2
        "Do you recall when Mr. Anderson asked you to have an eye on someone.":
            jump voice_phishing_2
        "Its about this intern Felix you took care of.":
            $ trust += trust_delta_2
            jump voice_phishing_2

label voice_phishing_2:
    show screen round_rect(trust)
    JA "Yeah I can remember Felix. Now what about him."
    menu:
        "I need you to tell me where he is. I have a question for him.":
            $ trust -= trust_delta_2
            jump voice_phishing_3
        "Can you give me his location. Mr. Anderson has something to ask him.":
            $ trust += trust_delta_2
            jump voice_phishing_3
        "I need his whereabouts to ask him something.":
            jump voice_phishing_3

label voice_phishing_3:
    show screen round_rect(trust)
    JA "If you want an answer from him why not let me ask the question."
    menu:
        "No need for you to get involved again. We will take over from here.":
            $ trust -= trust_delta_2
            jump voice_phishing_done
        "Mr. Anderson wants to handle this more privately.":
            jump voice_phishing_done
        "Well Mr. Anderson trusted me with this task and since you're busy i think its best if I talk to him.":
            $ trust += trust_delta_2
            jump voice_phishing_done


label voice_phishing_done:
    show screen round_rect(trust)
    if trust < 75:
        JA "No way Bob sent you. Who are you really?"
        "You try to explain that you are actually bobs assistant but he does'nt fall for it and hangs up."
        "This was your best chance to find your friend and you ruined it."
        jump game_over
    JA "Alright we took him to the experimental department in the facility at cityville street 12345. We locked him in laboratory 2 in the cellar."
    hide screen round_rect
    PC "Ok great and how can i get in."
    JA "Oh rihgt, the pin to the door is 385529."
    PC "Perfect, thank you for your time"
    JA "Sure"
    A "He is here in this facility. C'mon we have to help him."

    menu:
        "Activate the fire alarm" if fire_alarm == False:
            "After activate the fire alarm you heard sirens going off and speakers talking. While everyone is leaving the building you wait in Bob's office."
            "With noone in the building you can just strole out of the office area again."
            jump find_felix
        "Sneak out of the security area":
            if fire_alarm:
                "You head out to find Felix but by now the entire building is full of people again and the doors you got past for free last time are now keycard locked again."
            $ fire_alarm = True
            play music security_music volume loudness
            $ reset()
            $ player_pos = [1,1]
            $ valid_inputs = [1,0,0,1,0]
            $ game_matrix= [
                [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                [0,["c","t",0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                [0,[0,"f",0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                ]
            show screen minigame_screen()
            hide screen minigame_screen
            jump security_minigame_start

label leave_facility:
    $ show_textbox = True
    hide screen minigame_screen
    "you see grass for the first time"
    "you get scared and accidentally run into traffic and die"
    jump security_minigame_start

label game_lost:
    #scene bg game_over
    hide screen minigame_screen
    show screen minigame_screen()
    $ show_image_buttons = False
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    "{color=[red_game_over_color]}{size=120}You got arrested{/size}{/color}{fast}{nw=0.5}"
    $ show_image_buttons = True
    $ detected = False
    $ reset()
    hide screen minigame_screen
    show screen minigame_screen()
    hide screen minigame_screen
    jump security_minigame_start

label get_another_USB:
    scene black
    with dissolve
    "You return to leonie and she gives you another USB_Drive after lecturing you to not loose it again."
    jump menu_outside

label install_malware:
    scene black
    with dissolve
    "After receiving a file from Leonie you install the content on a spare Drive you have in your pockets."
    jump before_the_office

init python:
    """
    # Not needed anymore?
    menu:
        "Take the main entrance.":
            play music security_music volume loudness
            $ reset()
            $ fire_alarm = True
            $ player_pos = [1,1]
            $ a = "f"
            $ b = "t"
            $ valid_inputs = [1,0,0,1,0]
            $ game_matrix= [
                [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                [0,["c",b,0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                [0,[0,a,0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                ]
            show screen minigame_screen()
            hide screen minigame_screen
            jump security_minigame_start
        "Take the back entrance.":
            play music security_music volume loudness
            $ reset()
            show screen minigame_screen()
            hide screen minigame_screen
            jump security_minigame_start
        "Observe the people entering the building.":
            play music security_music volume loudness
            $ reset()
            $ cameras_off = True
            show screen minigame_screen()
            hide screen minigame_screen
            jump security_minigame_start
    """

default temp_cps = 0
label find_felix:
    scene bg hallway 1
    $ renpy.hide_screen("minigame_screen")
    $ show_textbox = True
    with dissolve
    "As you are both stepping out of the office area, you both let out a sigh of relieve."
    show alex serious1 at alex_right
    with dissolve
    A "Ok, now that we are finally away from this high security we can start looking for Felix."
    PC "This Joe said they hold him captive in the basement so let's just follow the staircase downwards."
    scene black
    with dissolve
    "You and Alex go after the signs indicating the way to the basements. Along the way there are no people aside from you."
    "After reaching the bottom of the stairs, you follow the hallways."
    scene bg basement hallways
    with dissolve
    "There are no windows down here and the light emanating from the halogen lights fills the hallways in a constant dazzling brightness. Together with the walls just smelling like freshly pouren concrete, it creates an unnerving ambience."
    "You hear two women from afar, their voices echoing in the barren hallways. They appear to be office workers and you avoid them by staying out of sight until they've passed you."
    "Keeping the communication to simple hand signs as not to raise attention, the two of you push forward, coming along a series of heavy metal doors, labelled with cryptic number and letter combinations."
    "You check each one of the labels until you find the door that Felix is supposed to be kept behind."
    "The PIN Joe gave you seems to work just fine and Alex opens the door with a loud creak reflecting along the drawn out hallways."
    scene bg file room
    show felix neutral1 at felix_right
    with dissolve
    F "[PN]? Alex?"
    "Before you sits Felix on a simple metal chair. The room you are entering seems to be a small file storage space with metal racks filled with file boxes. Felix seems exhausted, his hair still a tangled mess and his clothes visibly not changed in a while."
    show alex happy at alex_left
    with dissolve
    A "Oh man, I was so worried about you."
    "The three of you give each other a big hug before Felix's energetic spirit comes back."

    # The following few texts from Felix are supposed to be cut off and the sentences are supposed to be that long!
    $ temp_cps = preferences.text_cps
    $ preferences.text_cps = 60
    show felix thinking at felix_right
    with dissolve
    F "I knew it. I fricking knew it. From the start when I got the internship here, it was clear that they had some hidden secrets. When I was asked with sorting out their databank I stumbled across this project \"Omicron Cerebrum\" and when I asked about it, my supervisor didn't tell my anything about it and made excuses that it was non of my business and that I should keep my mouth shut about it{nw}"
    show felix serious at felix_right
    with dissolve
    F "but then I feared that they might catch on to me snooping around so I reverted to accessing over the dark net solely to cover my tracks but the problem was that I had to get into their internal network to get access to the secured files they keep in their server rooms and so I planned to get access to their system via infiltrating it with a USB drive I would stick into one of their internal computers{nw}"
    $ preferences.text_cps = temp_cps
    show alex surprised at alex_left
    with dissolve
    A "Felix wai...{nw}"
    $ preferences.text_cps = 60
    show felix thinking at felix_right
    with dissolve
    F "but of course they caught on to me just as I had feared I contacted Bob Anderson, my supervisor to try to talk my ways out of this situation but they wouldn't listen so I ran to you guys to gave you the informations in hope that you would understand what what happening to me and ...{nw}"
    $ preferences.text_cps = temp_cps

    PC "Felix stop!"
    PC "The flash drive you gave us helped us to get to you but right now we have to get out of here first. Leonie helped too, but she stayed home to give technical support."
    show alex serious1 at alex_left
    with dissolve
    A "Right. They will probably notice your abscence so we should get away as fast as possible."
    show felix serious at felix_right
    with dissolve
    F "Of course, of course. Wait a minute I found something interesting in these documents"
    "Felix scoops up a pile of opened documents and loose paper lying next to a couple of opened file boxes and tries to fit most of it under his shirt and in his pockets."
    show felix neutral1 at felix_right
    with dissolve
    F "Alright, I'm ready. Do you know how to get out of here?"
    show alex serious2 at alex_left
    with dissolve
    A "Yes, follow us. We'll take the back entrace to get out again. There shouldn't really be anyone there."
    scene black
    with dissolve
    "The three of you leave the facility without further occurences and head home where Leonie waits."
    play music main_music1 volume loudness
    scene bg new kitchen
    show alex neutral at alex_left
    show leonie happy at left
    show felix smile at felix_right
    with dissolve
    L "Felix! We were worried sick. You have to tell us what happened."
    show alex happy at alex_left
    with dissolve
    A "Not so fast. I believe Felix should get some rest first after what happened to him."
    show felix neutral2 at felix_right
    with dissolve
    "Alex pours Felix a glass of water and rumbles through the fridge in an attempt to find something edible."

    play music end_music volume loudness
    scene bg party
    show felix smile at felix_right
    with dissolve
    F "Thank you guys for believing me. I knew I could put my trust in you."
    show alex smile at alex_left
    with dissolve
    A "Always Felix."
    show leonie thinking at left
    with dissolve
    L "Phew, this was quite the adventure. I can't believe {color=[medievilColor]}Medievil{/color} really held you captive."
    show alex happy at alex_left
    with dissolve
    A "Yes, I'm glad we got you out of there. However we can't let them continue with this. Felix is quite possible still in great danger and so might we be."
    PC "Correct. We shouldn't let our guard down now. We have to investigate further into this company and bring them down once and for all."
    show leonie happy at left
    with dissolve
    L "I agree, but why don't we enjoy at least this evening together without worrying about evil coorporations huting us."
    show alex smile at alex_left
    with dissolve
    A "Good Idea."
    $ show_textbox = False
    show screen end_screen
    jump empty_label

screen end_screen:
    image "images/backgrounds/bg new kitchen.png"
    image "images/characters/felix/felix smile.png":
        zoom 0.8
        xpos 550
        ypos -100
    image "images/characters/player/male/pcm smile.png":
        zoom 1.6
        xpos -600
        ypos 200
    image "images/characters/leonie/leonie happy.png":
        zoom 0.3
        xpos 1150
        ypos 200
    # Exit to main menu button
    imagebutton:
        idle "images/objects/main menu button idle.png"
        hover "images/objects/main menu button hover.png"
        focus_mask True
        action Jump("game_finished")

label game_finished:
    return
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
 
    scene bg back office far 
    #show leonie neutral at left
    #show alex neutral at alex_right
    #with dissolve

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

    show facility hallway bg
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
        scene bobs office backside
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
            scene bg receptionist desk
            with dissolve
            "Alex goes up to what looks like the guest reception. The Lady at the desk doesn't notice you at first."
            show alex neutralleft at alex_left
            with dissolve
            A "Excuse me"
            "She looks up slightly annoyed."
            R "Can i help you?"
            show alex smileleft at alex_left
            with dissolve
            A "My name is Gill Cameron and i need to deliver some packages to Bob Anderson."
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
    scene bg back entrance hallway
    "As you try to go the same way as before, you get noticed by what looks like a secretary."
    show secretary suspicious at center
    S1 "Excuse me, who are you. I have not seen you here before."
    menu:
        "Tell her that you are the new interns of Aob Anderson and you need to go to his office.":
            show secretary suspicious at right
            show alex smileleft at alex_left
            with dissolve
            A "We are Bob Andersons new interns and it's our first day. He said we should wait for him in his office for further instructions."
            show secretary angry at right
            with dissolve
            S1 "Bob didn't mention any new interns."
            show alex neutralleft at alex_left 
            with dissolve
            A "How else would we have gotten access."
            show secretary thinking at right
            with dissolve
            S1 "Well thats a good point. Sorry for being so mistrustful but our higher ups want us to take security rather serious"
            show alex happyleft at alex_left
            with dissolve
            A "Yeah we know. Bob also said to us we shouldnt speak of what we do here outside of work."
            show secretary neutral at right
            with dissolve
            S1 "Sounds like him. Anyways his office is in the area with the others just down this corridor."
            show alex smileleft at alex_left
            with dissolve
            A "Okay great, thank you."
            show secretary smile at right
            with dissolve
            S1 "No problem."
        "Tell her you need to go to the bathroom and make a run for it":
            show secretary thinking at right
            with dissolve
            "After you tell her your reason she looks like she wants to say something but you just start running in the direction of the bathroom."
            "The secretary will remember that."
            $ security_aware = True
        "Pretend to be technicians":
            show secretary suspicious at right
            show alex neutralleft at alex_left
            with dissolve
            A "We are technicians and here for problems with the internet connection in the west wing. We where called by Mr. Anderson you know where he is? We need some information before we start."
            show secretary thinking at right
            with dissolve
            S1 "Well i don't know where he is but just wait here a minute, i will call him right now."
            show alex happyleft at alex_left
            with dissolve
            A "Thats not gonna be necessary, we will just look for him ourselfs thank you."
            show secretary smile at right
            with dissolve
            S1 "No no, its nothing really. Just one second."
            show secretary neutral at right
            show alex serious2left at alex_left
            with dissolve
            "The secretary starts to type something on her phone and then proceeds to wait for a call."
            "You decide its best if you bale out while she is distracted before your lie falls apart right infront of you."
            scene bg facility hallway
            with dissolve
            "With that in mind you make a run for the office area before she can stop you."
            scene bg fcility hallway 2
            show security guard at center
            with dissolve
            "After only a few minutes you find security waiting for you around the corner."
            jump game_over

define USB_placed_1 = False

label way_to_the_office:
    scene bg facility
    hide alex
    hide secretary
    with dissolve
    "Going furhter into the facility you find the beginnig of the office area you were looking for."
    A "Well what do we do now? We still dont have control of the cameras."

define before_office = False

label before_the_office:
    scene bg facility
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
            "To avoid further confrontation you hide in the bathroom until you get a call from leonie telling you that she is now in controll of the cameras."
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
    $ show_textbox = True
    hide screen minigame_screen
    "you see beautiful flowers and a nice garden"
    "upon staring at the delightful scenary a butterfly comes across your sight."
    "you feel like you have to catch the butterfly"
    #butterfly chasing minigame starts
    "you decide to go back into the building"
    jump security_minigame_start

label optional:
    $ show_textbox = True
    hide screen minigame_screen
    "you sneakingly open the door, somewhat afraid that an employee might be here and walk in slowly"
    show alex smileleft at alex_left
    with dissolve
    A "since were already in this weird room we might aswell take a look around"
    #clicking through room + stories begin.
    "upon inspecting the room you decide to go back into the hallway"
    jump security_minigame_start


label bobs_office:
    $ show_textbox = True
    hide screen minigame_screen
    scene bg bob office
    show alex smileleft at alex_left
    with dissolve
    A "Now this is what were talking about. We finally made it."
    PC "I cant believe this place has that many security guards and employees hording around"
    show alex serious2left at alex_left
    with dissolve 
    A "You know theres probably a good reason why there are so many security guards here around the clock right? "
    PC "Well lets try to find clues about Felix now thoiugh"
    #bobs office clicking through room begins
    #voice phshing game begins
    "you go to where Felix is"
    play music security_music volume loudness
    if fire_alarm == True:
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
    
label finding_felix: 

    

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
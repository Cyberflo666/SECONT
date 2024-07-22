$ renpy.include("screens.rpy")
default current_index = 0

image phone_icon_hover :
    "images/objects/phone/phone hover.png"
    zoom 0.15
   

image phone_icon_idle :
    "images/objects/phone/phone idle.png"
    zoom 0.15

transform icon_pos:
    zoom 1.3
    xalign 0.7

transform phone_pos:
    xalign 0
    yalign 1.28

transform arrow_pos:
    zoom 0.7
    xalign 0.07
    yalign 0.1

transform change_arrow:
    zoom 0.35



# Variables
define phone_usable_area = (675, 140, 470, 730)
define phone_normal_text_color = "#000000"
define gil_social_media_seen = False
# Notification variables
default phone_not_glossary = False
default phone_not_gallery = False
default phone_not_notes = False
default phone_not_map = False

init python:
    def reset_notification(id):
        global phone_not_glossary
        global phone_not_gallery
        global phone_not_notes
        global phone_not_map
        
        if id == 0:
            phone_not_glossary = False
        elif id == 1:
            phone_not_gallery = False
        elif id == 2:
            phone_not_notes = False
        elif id == 3:
            phone_not_map = False


screen phone_hand():
    zorder 2
    modal True
    add Solid("#000c")
    if password_icon == True:
        image "images/objects/phone/phone hand with pw.png":
            zoom 1.3
            xalign 0.7
    else:
        image "images/objects/phone/phone hand.png":
            zoom 1.3
            xalign 0.7
    
    # Return arrow (closes phone)
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow_pos
        xpos 200
        ypos 0
        xsize 500
        ysize 300
        action Hide("phone_hand"), Show("phone_icon")
    
    # Phone icons
    imagebutton:
        hover "camera hover" at icon_pos
        idle "camera idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_camera")
    if phone_not_gallery:
        image "images/objects/phone/phone notify circ.png":
                zoom 0.2
                xpos 1085
                ypos 850
    
    imagebutton:
        hover "contacts hover" at icon_pos
        idle "contacts idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_contact")
    
    imagebutton:
        hover "map hover" at icon_pos
        idle "map idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_map")
    if phone_not_map:
        image "images/objects/phone/phone notify circ.png":
                zoom 0.2
                xpos 840
                ypos 380

    imagebutton:
        hover "notes hover" at icon_pos
        idle "notes idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_notes")
    if phone_not_notes:
        image "images/objects/phone/phone notify circ.png":
                zoom 0.2
                xpos 1060
                ypos 160

    imagebutton:
        hover "glossary hover" at icon_pos
        idle "glossary idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_glossary")
    if phone_not_glossary:
        image "images/objects/phone/phone notify circ.png":
                zoom 0.2
                xpos 1060
                ypos 380

    if password_icon == True:
        imagebutton:
            hover "password hover" at icon_pos
            idle "password idle"
            focus_mask True
            action Hide("phone_hand"), Show("phone_hand_password"),

################################### Password ##########################################

default password =""
default password_check_text = ""
default first_guess = ""
default password_check_color = "00000000"
default password_guessed = False
default password_guessed_correct = False
default password_fail_counter = 0

screen phone_hand_password():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    image "images/objects/phone/phone hand password box.png":
        zoom 1.3
        xalign 0.7

    # Return arrow
    if show_image_buttons:
        imagebutton:
            hover "return hover" at icon_pos
            idle "return idle" 
            focus_mask True
            action Hide("phone_hand_password"), Show("phone_hand")
    else:
        image "return idle" at icon_pos
    frame:
        background "#00000000"
        area(675, 150, 460, 50)
        text "{color=[search_result]}{size=50}{b}Access USB{/b}{/size}{/color}" at center
    
    frame:
        background "#00000000"
        area(675, 200, 460, 50)
        text "{color=[search_result]}{size=50}{b}Drive{/b}{/size}{/color}" at center
    frame:
        background "#00000000"
        area(675, 300, 460, 50)
        text "{color=[search_result]}Enter password:{/color}" at center
    frame:
        area (675, 360, 460, 100)
        background "#00000000"
        input:
            copypaste True
            default""
            size 30
            pixel_width(440)
            color "#000000"
            value VariableInputValue('password')
    imagebutton:
        hover "phone hand password confirm hover" at icon_pos
        idle "phone hand password confirm idle"
        focus_mask True
        action Function(password_input,password), Show("reset_password_text_timer")
    frame:
        background "#58585800"
        area(675, 700, 460, 50)
        text "{size=30}{color=[password_check_color]}{b}[password_check_text]{/b}{/color}{/size}" at center:
            outlines [(3, "#000000ff", 0, 0)]


screen reset_password_text_timer():
    #image "images/characters/alex/alex laughing.png"
    timer 1.7 action Function(reset_password_text), Function(after_password_action), Hide("reset_password_text_timer")


define correct_password =[ 
                        ["9/11", "911", "9.11", "9-11"],
                        ["cake"],
                        ["4/17", "417", "4.17", "4/17"],
                        ]

init python:
    def password_input(password_guess):
        global password_check_color
        global password_guessed
        global password_check_text
        global first_guess
        global password_guessed_correct
        global show_image_buttons
        global password_fail_counter

        if password_guessed == False or first_guess == password_guess:
            first_guess = password_guess
            password_guessed = True
            password_check_color = "#970000ff"
            password_check_text = "Incorrect password"
            return

        for i in range(0,len(correct_password)):
            part_found = False
            for j in range(0,len(correct_password[i])):
                if correct_password[i][j] in password_guess.lower():
                    part_found = True
            if part_found == False:
                password_check_color = "#970000ff"
                password_check_text = "Incorrect password"
                password_fail_counter += 1
                return
        password_check_color = "#288f00ff"
        password_check_text = "Correct password"
            
        password_guessed_correct = True
        show_image_buttons = False


        renpy.notify(password_fail_counter)
        # Correct Password: thecakeisalie0417911
    
    def reset_password_text():
        global password_check_text
        password_check_text = ""
        return

    def after_password_action():
        global password_guessed_correct
        global password_fail_counter
        if password_guessed_correct:
            renpy.jump("password_cracked")
        
        # Gives the player help after some failed attempts
        elif password_fail_counter >= 5:
            password_fail_counter = 0
            renpy.jump("password_help")
        return


#################################### Gallery ##########################################
transform change_arrow1:
        xpos 0.035
        ypos 0.40
        zoom 1.0
transform change_arrow2:
        xpos 0.75
        ypos 0.40
        zoom 1.0
transform index_gallery_pos:
        xpos 11.9
        ypos 22.9
default gallery_length = 1
$ gallery_length = len(gallery.items) 
screen phone_hand_camera():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 1)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_camera"), Show("phone_hand")
    imagebutton:
       
        idle "left arrow white idle" at change_arrow1
        hover "left arrow white hover"
        focus_mask True
        action Function(change_index,1), Hide("phone_hand_camera"), Show("phone_hand_camera")
        
    imagebutton:
        idle "right arrow white idle" at change_arrow2
        hover "right arrow white hover"
        focus_mask True
        action Function(change_index,-1), Hide("phone_hand_camera"), Show("phone_hand_camera")
    frame:
        area(670, 140, 467, 730)
        background "#00000000"
        image gallery.get_picture(current_index) at center
    frame: 
        text "[current_index +1 ] / [gallery_length]" at index_gallery_pos
        background "#00000000"

        
        

init python:
    def change_index(x):
        global gallery
        global current_index 
        global gallery_length
        gallery_length = len(gallery.items)
        if x < 0:
            current_index += 1 
            current_index = current_index % gallery_length 
        else:
            current_index-= 1  
            current_index = current_index % gallery_length 


# Screen for displaying the contacts of the player
define contacts_font_size = 45
screen phone_hand_contact():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_contact"), Show("phone_hand")
    
    viewport:
        area phone_usable_area
        draggable False
        mousewheel False

        # Content of the contacts
        vbox:
            spacing 90
            frame:
                area(0, 0 , 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box alex idle"
                    hover "contact box alex hover"
                    focus_mask True
                    action Call("call_alex")

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box leonie idle"
                    hover "contact box leonie hover"
                    focus_mask True
                    action Call("call_leonie")

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box felix idle"
                    hover "contact box felix hover"
                    focus_mask True
                    action Call("call_felix")

###################################### Map ############################################

init python:
    def already_here_notify():
        renpy.notify("You are already here.")

screen phone_hand_map():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 3)

    image "images/objects/phone/map/bg map blank.png"
    
    # Dorms
    imagebutton:
        idle "map dorms idle"
        hover "map dorms hover"  
        focus_mask True
        if hide_map:
            action Call("map_disabled")
        else:
            action Function(already_here_notify)

    # University
    if website_2_not_seen == False:
        imagebutton:
            idle "map university idle"
            hover "map university hover"
            focus_mask True
            if current_location == 1:
                action Function(already_here_notify)
            elif hide_map:
                action Call("map_disabled")
            elif uni_access_denied:
                action Call("lab_access_denied")
            elif lab_seen:
                action Call("lab_visited")
            else:
                # action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"),  Hide("website4_screen"), Hide("laptop_screen"), Jump("visitlab")
                action Function(hide_all_screens), Jump("visitlab")

    # Medievil
    if website_3_not_seen == False:
        imagebutton:
            idle "map medievil idle"
            hover "map medievil hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif dumpster_doven:
                action Call("dumpster_empty")
            else:
                # action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"), Hide("website4_screen"), Hide("laptop_screen"), Jump("dumpsterdive")
                action Function(hide_all_screens), Jump("dumpsterdive")

    # Gills Place
    if gil_visited == True and (gill_house_seen_bob or gill_house_seen_gill):
        imagebutton:
            idle "map gill house idle"
            hover "map gill house hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif dumpster2_doven:
                action Call("dumpster_empty")
            else:
                # action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"), Hide("website4_screen"), Hide("laptop_screen"), Hide("social_screen"), Jump("dumpsterdive2")
                action Function(hide_all_screens), Jump("dumpsterdive2")
    
    # Return arrow (closes phone)
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow_pos
        xpos 200
        ypos 0
        xsize 500
        ysize 300
        action Hide("phone_hand_map"), Show("phone_hand")

init python:
    def hide_all_screens():
        renpy.hide_screen("phone_hand_map")
        renpy.hide_screen("web_screen")
        renpy.hide_screen("website1_screen")
        renpy.hide_screen("website2_screen")
        renpy.hide_screen("website3_screen")
        renpy.hide_screen("website4_screen")
        renpy.hide_screen("laptop_screen")
        renpy.hide_screen("social_screen_explore")
        renpy.hide_screen("social_screen_search")
        renpy.hide_screen("social_screen_bob")
        renpy.hide_screen("social_screen_gill")
        renpy.hide_screen("social_screen_bob_tag")
        return

##################################### Notes ###########################################
define notes_font_size = 25
screen phone_hand_notes():
    zorder 2
    modal True
    add Solid("#000c")
    
    on "show" action Function(reset_notification, 2)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_notes"), Show("phone_hand")
    
    viewport:
        area phone_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0

        # Content of the notes
        vbox:
            spacing 20
            $ temp_items = notes.get_items_list()
            if len(temp_items) == 0:
                text "{size=[notes_font_size]}{color=[phone_normal_text_color]}There is no information in your notebook{/color}{/size}"
            else:
                for entry in notes.get_items_list():
                    text "{size=[notes_font_size]}{color=[phone_normal_text_color]}[entry.text]{/color}{/size}"



################################### Glossary ##########################################
define gloss_font_size_big = 40
define gloss_font_size_normal = 25

default gloss_bribery_seen = False
default gloss_impersonation_seen = False
default gloss_dumpster_seen = False
default gloss_tailgating_seen = False
default gloss_phishing_seen = False

define gloss_bribery_text = """{b}{size=[gloss_font_size_big]}Bribery{/size}{/b}\n\nAlso known as “Quid pro quo”, Latin for “something for something”. Involves an exchange of information or services for a compensation. Subjects of bribery are usually aware of their wrongdoings although the true scale of the consequences may not be comprehensible to them at first."""
define gloss_impersonation_text = """{b}{size=[gloss_font_size_big]}Impersonation{/size}{/b}\n\nExplains the act of posing as someone you are not in an attempt to deceive anyone. Impersonation can come in different styles: over the phone, where the voice is enough to pretend to be someone else, or even in person if the one being tricked doesn't know the impersonated one. Appearance, equipment and even other people can help strengthen the deception for example when wearing a warning vest and holding a clipboard."""
define gloss_dumpster_text = """{b}{size=[gloss_font_size_big]}Dumpster Diving{/size}{/b}\n\nMost people don't dispose of their trash properly, leaving a lot of sensitive information in the form of letters, notes or invoices free to access for anyone willing to rummage through the garbage. If hardware is being disposed of, the data can also often still be accessed if the contents of the drives haven't been overwritten properly. Usually people forget their stuff once it's in the trash. “Out of sight out of mind”, but with enough patience, adversaries can get a lot of compromising data through dumpster diving."""
define gloss_tailgatin_text = """{b}{size=[gloss_font_size_big]}Tailgating{/size}{/b}\n\nAlso known as “piggybacking”. Describes the act of gaining access to a restricted area by following other people who have access. A perpetrator could, for example, disguise himself as a delivery person or a repair man and wait for someone holding up the door for him in a nice gesture."""
define gloss_phishing_text = """{b}{size=[gloss_font_size_big]}Phishing Mail{/size}{/b}\n\nIs  an attack via a message which is used to bait the target into handing out sensitive information or installing malware. In these messages, the attacker pretends to be a legitimate source to gain the trust of the target so they will follow the instructions given. Another variant of this approach is Spear Phishing where the content of the message is directed towards a single individual. In this case, the attacker uses personal information to get to the targeted person."""

default gloss_entry_text = ""

style gloss_buttons:
    color "#000000"
    hover_color "#9c0000"
    underline False
    hover_underline True
    size gloss_font_size_big

style gloss_text:
    color "#000000"
    size gloss_font_size_normal

style gloss_text_header:
    color "#000000"
    bold True
    size gloss_font_size_big


# General overview Screen
screen phone_hand_glossary():
    zorder 2
    modal True
    add Solid("#000c")

    on "show" action Function(reset_notification, 0)

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_glossary"), Show("phone_hand")
    
    viewport:
        area phone_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0

        # List of buttons for the social engineering techniques
        vbox:
            spacing 20
            text "         Glossary" style "gloss_text_header"
            text "Read more about various social engineering techniques" style "gloss_text"
            if gloss_bribery_seen:
                textbutton "Bribery":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, gloss_bribery_text), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_impersonation_seen:
                textbutton "Impersonation":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, gloss_impersonation_text), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_dumpster_seen:
                textbutton "Dumpster Diving":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, gloss_dumpster_text), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_tailgating_seen:
                textbutton "Tailgating":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, gloss_tailgatin_text), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")
            if gloss_phishing_seen:
                textbutton "Phishing":
                    text_style "gloss_buttons"
                    action Function(set_gloss_text, gloss_phishing_text), Hide("phone_hand_glossary"), Show("phone_hand_glossary_entry")

# Seperate glossary entry screens
screen phone_hand_glossary_entry():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        idle "return idle" 
        hover "return hover" at icon_pos
        focus_mask True
        action Hide("phone_hand_glossary_entry"), Show("phone_hand_glossary")
    
    viewport:
        area phone_usable_area
        draggable True
        mousewheel True
        yinitial 1.0

        # List of buttons for the social engineering techniques
        text [gloss_entry_text] style "gloss_text"

init python:
    def set_gloss_text(input_text):
        global gloss_entry_text
        gloss_entry_text = input_text

################################## Phone Icon #########################################

screen phone_icon():
    zorder 2
    modal False
    if show_image_buttons:
        imagebutton:
            idle "phone_icon_idle" 
            hover "phone_icon_hover" at phone_pos
            
            focus_mask True
            action Show("phone_hand"), Hide("phone_icon")
        
        # Displays notification circ if there's any new notification
        if phone_not_glossary or phone_not_gallery or phone_not_notes or phone_not_map:
            image "images/objects/phone/phone notify circ.png":
                zoom 0.2
                xpos 225
                ypos 800

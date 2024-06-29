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
    
    imagebutton:
        hover "contacts hover" at icon_pos
        idle "contacts idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_contact")
    
    if map_active == True:
        imagebutton:
            hover "map hover" at icon_pos
            idle "map idle"
            focus_mask True
            action Hide("phone_hand"), Show("phone_hand_map")

    imagebutton:
        hover "notes hover" at icon_pos
        idle "notes idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_notes")

    imagebutton:
        hover "glossary hover" at icon_pos
        idle "glossary idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_glossary")

    if password_icon == True:
        imagebutton:
            hover "password hover" at icon_pos
            idle "password idle"
            focus_mask True
            action Hide("phone_hand"), Jump("password_cracked")


screen phone_hand_camera():
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
        action Hide("phone_hand_camera"), Show("phone_hand")
    imagebutton:
        xpos 0.345
        ypos 0.06
        idle "left arrow black idle" at change_arrow
        hover "left arrow black hover"
        focus_mask True
        action Function(change_index,1), Hide("phone_hand_camera"), Show("phone_hand_camera")
    imagebutton:
        xpos 0.54
        ypos 0.06
        idle "right arrow black idle" at change_arrow
        hover "right arrow black hover"
        focus_mask True
        action Function(change_index,-1), Hide("phone_hand_camera"), Show("phone_hand_camera")
    frame:
        area(670, 140, 467, 730)
        background "#00000000"
        image gallery.get_picture(current_index % len(gallery.items)) at center
        
        

init python:
    def change_index(x):
        global current_index
        if x < 0:
            current_index += 1
        else:
            current_index -= 1


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


init python:
    def notify_function():
        renpy.notify("You are already here")

screen phone_hand_map():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/map/map.png"
    
    imagebutton:
        idle "map dorms idle"
        hover "map dorms hover"  
        focus_mask True
        action Function(notify_function)
    if gil_social_media_seen == True: # need to add flag when implementing social media site.
        imagebutton: 
            idle "map gils house idle" # needs to get added
            hover "map gils house hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif dumpster2_doven:
                action Call("dumpster_empty")
            else:
                action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"), Hide("website4_screen"), Hide("laptop_screen"), Jump("dumpsterdive2")


    if website_2_not_seen == False:
        imagebutton:
            idle "map university idle"
            hover "map university hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif uni_access_denied:
                action Call("lab_access_denied")
            elif lab_seen:
                action Call("lab_visited")
            else:
                action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"),  Hide("website4_screen"), Hide("laptop_screen"), Jump("visitlab")

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
                action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"), Hide("website4_screen"), Hide("laptop_screen"), Jump("dumpsterdive")

    if False == False:
        imagebutton:
            idle "map gill idle"
            hover "map gill hover"
            focus_mask True
            if hide_map:
                action Call("map_disabled")
            elif dumpster2_doven:
                action Call("dumpster_empty")
            else:
                action Hide("phone_hand_map"), Hide("web_screen"), Hide("website1_screen"), Hide("website2_screen"), Hide("website3_screen"), Hide("website4_screen"), Hide("laptop_screen"), Jump("dumpsterdive2")
    
    # Return arrow (closes phone)
    imagebutton:
        idle "return arrow idle"
        hover "return arrow hover" at arrow_pos
        xpos 200
        ypos 0
        xsize 500
        ysize 300
        action Hide("phone_hand_map"), Show("phone_hand")


# Screen for displaying the notes the player collects throughout the game
define notes_font_size = 25
screen phone_hand_notes():
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

define gloss_bribery_text = """{b}{size=[gloss_font_size_big]}Bribery{/size}{/b}\nAlso known as “Quid pro quo”, Latin for “something for something”. Involves an exchange of information or services for a compensation. Subjects of bribery are usually aware of their wrongdoings although the true scale of the consequences may not be comprehensible to them at first."""
define gloss_impersonation_text = """{b}{size=[gloss_font_size_big]}Impersonation{/size}{/b}\nExplains the act of posing as someone you are not in an attempt to deceive someone. Impersonation can come in different styles: over the phone, where the voice is enough to pretend to be someone else, or even in person if the one being tricked doesn't know the impersonated one. Appearance, equipment and even other people can help strengthen the deception for example when wearing a warning vest and holding a clipboard."""
define gloss_dumpster_text = """{b}{size=[gloss_font_size_big]}Dumpster Diving{/size}{/b}\nMost people don't dispose of their trash properly, leaving a lot of sensitive information in the form of letters, notes or invoices free to access for anyone willing to rummage through the garbage. If hardware is being disposed of, the data can also often still be accessed if the contents of drives haven't been overwritten properly. Usually people forget their stuff once it's in the trash. “Out of sight out of mind”, but with enough patience, adversaries can get a lot of compromising data through dumpster diving."""
define gloss_tailgatin_text = """{b}{size=[gloss_font_size_big]}Tailgating{/size}{/b}\nAlso known as “piggybacking”. Describes the act of gaining access to a restricted area by following other people who have access. A perpetrator could, for example, disguise himself as a delivery person or a repair man and wait for someone holding up the door for him in a nice gesture."""
define gloss_phishing_text = """{b}{size=[gloss_font_size_big]}Phishing Mail{/size}{/b}\nIs  an attack via a message which is used to bait the target into handing out sensitive information or installing malware. In these messages the attacker pretends to be a legitimate source to gain the trust of the target so they will follow the instructions given. Another variant of this approach is Spear Phishing where the content of the message is directed towards a single individual. In this case the attacker uses personal information to get to the targeted person."""

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

# General overview Screen
screen phone_hand_glossary():
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

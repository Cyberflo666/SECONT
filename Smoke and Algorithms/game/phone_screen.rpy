$ renpy.include("screens.rpy")

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


# Variables
define phone_usable_area = (675, 140, 470, 730)
define phone_normal_text_color = "#000000"


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
                    idle "contact box idle"
                    hover "contact box hover"
                    focus_mask True
                    action Call("call_alex")
                text "{size=[contacts_font_size]}{color=[phone_normal_text_color]}Alex{/color}{/size}" at center 

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box idle"
                    hover "contact box hover"
                    focus_mask True
                    action Call("call_leonie")
                text "{size=[contacts_font_size]}{color=[phone_normal_text_color]}Leonie{/color}{/size}" at center

            frame:
                area(0, 0, 500, 122)
                background "#00000000"
                imagebutton:
                    xpos 0.08
                    idle "contact box idle"
                    hover "contact box hover"
                    focus_mask True
                    action Call("call_felix")
                text "{size=[contacts_font_size]}{color=[phone_normal_text_color]}Felix{/color}{/size}" at center

label map_done:
    $ renpy.notify("you have new objectives on your map")
    return

screen phone_hand_map():
    zorder 2
    modal True
    add Solid("#000c")

    image "images/objects/phone/map/map.png"
    
    imagebutton:
        idle "map dorms idle"
        hover "map dorms hover"  
        focus_mask True
        action Call("map_done")

    if website_2_not_seen == False:
        imagebutton:
            idle "map university idle"
            hover "map university hover"
            focus_mask True
            action Call("map_done")

    if website_3_not_seen == False:
        imagebutton:
            idle "map medievil idle"
            hover "map medievil hover"
            focus_mask True
            action Hide("phone_hand_map"), Hide("web_screen"), Jump("dumpsterdive")

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


screen phone_icon():
    
    zorder 2
    modal False

    imagebutton:
        idle "phone_icon_idle" 
        hover "phone_icon_hover" at phone_pos
        
        focus_mask True
        action Show("phone_hand"), Hide("phone_icon")

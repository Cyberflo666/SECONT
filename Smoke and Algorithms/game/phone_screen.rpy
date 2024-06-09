$ renpy.include("screens.rpy")

image phone_icon_hover :
    "images/objects/phone/phone hover.png"
    zoom 0.15
   

image phone_icon_idle :
    "images/objects/phone/phone idle.png"
    zoom 0.15
    

image return_arrow_hover :
    "images/objects/phone/return_arrow_hover.png"
    zoom 0.3
    

image return_arrow_idle :
    "images/objects/phone/return_arrow_idle.png"
    zoom 0.3
   
image camera_idle:
    "images/objects/phone/camera idle.png"
    zoom 2


image camera_hover:
    "images/objects/phone/camera hover.png"
    zoom 2

image contact_idle:
    "images/objects/phone/camera idle.png"
    zoom 1.3
    xalign 0.7

image contact_hover:
    "images/objects/phone/camera hover.png"
    zoom 1.3
    xalign 0.7

image glossary_idle:
    "images/objects/phone/glossary idle.png"
    zoom 1.3
    xalign 0.7

image glossary_hover:
    "images/objects/phone/glossary hover.png"
    zoom 1.3
    xalign 0.7

image map_idle:
    "images/objects/phone/map idle.png"
    zoom 1.3
    xalign 0.7

image map_hover:
    "images/objects/phone/map hover.png"
    zoom 1.3
    xalign 0.7

image notes_idle:
    "images/objects/phone/notes idle.png"
    zoom 1.3
    xalign 0.7

image notes_hover:
    "images/objects/phone/notes hover.png"
    zoom 1.3
    xalign 0.7

image return_idle:
    "images/objects/phone/return idle.png"
    zoom 1.3
    xalign 0.7

image return_hover:
    "images/objects/phone/return hover.png"
    zoom 1.3
    xalign 0.7

image password_idle:
    "images/objects/phone/password idle.png"
    zoom 1.3
    xalign 0.7

image password_hover:
    "images/objects/phone/password hover.png"
    zoom 1.3
    xalign 0.7

transform icon_pos:
    zoom 1.3
    xalign 0.7

transform phone_pos:
    xalign 0
    yalign 1.28

transform arrow_pos:
    zoom 0.7
    xalign 0.07
    yalign 0


screen phone_hand():
    zorder 2
    modal True

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
        
    
    # Return arrow
    imagebutton:
        hover "return arrow hover" at arrow_pos
        idle "return arrow idle" 
        focus_mask True
        action Hide("phone_hand"), Show("phone_icon")
    
    # Phone icons
    imagebutton:
        hover "camera hover" at icon_pos
        idle "camera idle"
        focus_mask True
        action Hide("phone_hand"), Show("phone_hand_camera")
    
    imagebutton:
        hover "contact hover" at icon_pos
        idle "contact idle"
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

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_camera"), Show("phone_hand")


screen phone_hand_contact():
    zorder 2
    modal True

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_contact"), Show("phone_hand")

screen phone_hand_map():
    zorder 2
    modal True

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_map"), Show("phone_hand")


# Screen for displaying the notes the player collects throughout the game
define notes_font_size = 25
screen phone_hand_notes():
    zorder 2
    modal True

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_notes"), Show("phone_hand")
    
    viewport:
        # xStartOffset, yStartOffset, xWidth, yHeight
        area(675, 140, 470, 730)
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0

        # Content of the notes
        vbox:
            spacing 20
            $ temp_items = notes.get_items_list()
            if len(temp_items) == 0:
                text "{size=[notes_font_size]}no information in your notebook{/size}"
            else:
                for entry in notes.get_items_list():
                    text "{size=[notes_font_size]}[entry.text]{/size}"


screen phone_hand_glossary():
    zorder 2
    modal True

    image "images/objects/phone/phone hand empty.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton:
        hover "return hover" at icon_pos
        idle "return idle" 
        focus_mask True
        action Hide("phone_hand_glossary"), Show("phone_hand")


screen phone_icon():
    
    zorder 2
    modal False

    imagebutton:
        hover "phone_icon_hover" at phone_pos
        idle "phone_icon_idle" 
        
        focus_mask True
        action Show("phone_hand"), Hide("phone_icon")

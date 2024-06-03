$ renpy.include("screens.rpy")

image phone_icon_hover :
    "images/objects/phone/phone_hover.png"
    zoom 0.15
   

image phone_icon_idle :
    "images/objects/phone/phone_idle.png"
    zoom 0.15
    

image return_arrow_hover :
    "images/objects/phone/return_arrow_hover.png"
    zoom 0.3
    

image return_arrow_idle :
    "images/objects/phone/return_arrow_idle.png"
    zoom 0.3
   

transform phone_pos:
    xalign 0
    yalign 1.28

transform arrow_pos:
    xalign 3
    yalign 0

screen phone_hand():
    zorder 2
    modal True

    image "images/objects/phone/phone hand.png":
        zoom 1.3
        xalign 0.7
    
    # Return arrow
    imagebutton auto "images/objects/phone/return_arrow_%s.png":
        hover "return_arrow_hover" at arrow_pos
        idle "return_arrow_idle" 
        focus_mask True
        action Hide("phone_hand"), Show("phone_icon")
    
    # Enter Password
    imagebutton auto "images/objects/phone/enter password %s.png":
        focus_mask True
        action Jump("password_cracked")

    

screen phone_icon():
    
    zorder 2
    modal False

    imagebutton :
        hover "phone_icon_hover" at phone_pos
        idle "phone_icon_idle" 
        
        focus_mask True
        action Show("phone_hand"), Hide("phone_icon")
define laptop_usable_area = (240, 110, 1441, 793)
define website_area = (0, 0, 1441, 4323)
define website_1_not_seen = True
define website_2_not_seen = True
define website_3_not_seen = True
define website_1_scrollbar_pos = 0
init python:
    def viewport_change(value):
        global website_1_scrollbar_pos
        website_1_scrollbar_pos = value
        renpy.notify(website_1_scrollbar_pos)

transform website1_icon:
    xalign 0.3
    yalign 0.5
transform website2_icon:
    xalign 0.3
    yalign 0.6
transform website3_icon:
    xalign 0.3
    yalign 0.7
screen laptop_screen():
    zorder 2
    modal False
        
    
    # Return arrow (closes phone)
    imagebutton:
        idle "mail idle"
        hover "mail hover"
        focus_mask True
        action Hide("laptop_screen"), Show("mail_screen")

    imagebutton:
        idle "power idle"
        hover "power hover"
        focus_mask True
        action Hide("laptop_screen"), Show("power_screen")

    imagebutton:
        idle "social idle"
        hover "social hover"
        focus_mask True
        action Hide("laptop_screen"), Show("social_screen")

    imagebutton:
        idle "web idle"
        hover "web hover"
        focus_mask True
        action Hide("laptop_screen"), Show("web_screen")

screen mail_screen():
    zorder 2
    modal True
    image "bg mail"
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        image "alex laughing"

screen power_screen():
    zorder 2
    modal True
    image "blank laptop"
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        image "alex laughing"

screen social_screen():
    zorder 2
    modal True
    image "blank laptop"
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        image "alex laughing"

screen web_screen():
    zorder 2
    modal True
    image "bg browser"
    imagebutton:
        focus_mask True
        idle "website1 icon idle" at website1_icon
        hover "website1 icon hover"
        action Hide("web_screen"), Show("website1_screen")
    imagebutton:
        focus_mask True
        idle "website2 icon idle" at website2_icon
        hover "website2 icon hover"
        action Hide("web_screen"), Show("website2_screen")
    imagebutton:
        focus_mask True
        idle "website3 icon idle" at website3_icon
        hover "website3 icon hover"
        action Hide("web_screen"), Show("website3_screen")

screen website1_screen():
    zorder 0
    modal False
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"

        yadjustment ui.adjustment(1, website_1_scrollbar_pos, changed=viewport_change)


        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 1"
                if True:
                    imagebutton:
                        idle "website 1 button idle"
                        hover "website 1 button hover"
                        focus_mask True
                        action Jump("website1_button")

screen website2_screen():
    zorder 0
    modal False
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 2"
                imagebutton:
                    idle "website 2 button idle"
                    hover "website 2 button hover"
                    focus_mask True
                    action Jump("website2_button")

screen website3_screen():
    zorder 0
    modal False
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 3"
                imagebutton:
                    idle "website 3 button idle"
                    hover "website 3 button hover"
                    focus_mask True
                    action Jump("website3_button")

screen website1_button_text:
    window:
        text "something useless"
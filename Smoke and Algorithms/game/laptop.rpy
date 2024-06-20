define laptop_usable_area = (240, 186, 1441, 702)
define website_area = (0, 0, 1441, 4323)
define website_1_scrollbar_pos = 0
define website_2_scrollbar_pos = 0
define website_3_scrollbar_pos = 0
define search_result = "#000000FF"

init python:
    def viewport_change1(value):
        global website_1_scrollbar_pos
        website_1_scrollbar_pos = value
        #renpy.notify(website_1_scrollbar_pos)
init python:
    def viewport_change2(value):
        global website_2_scrollbar_pos
        website_2_scrollbar_pos = value
        #renpy.notify(website_2_scrollbar_pos)
init python:
    def viewport_change3(value):
        global website_3_scrollbar_pos
        website_3_scrollbar_pos = value
        #renpy.notify(website_3_scrollbar_pos)

transform website1_icon:
    xalign 0.15
    yalign 0.2
transform website2_icon:
    xalign 0.15
    yalign 0.25
transform website3_icon:
    xalign 0.15
    yalign 0.3
transform return_arrow_black_pos:
    zoom 0.2
    xalign 0.14
    yalign 0.1

screen laptop_screen():
    zorder 1
    modal False
        
    
# Return arrow (closes phone)
    if show_image_buttons == True:
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
    modal False
    image "bg mail"
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        image "alex laughing"
    if show_image_buttons == True:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            action Hide("mail_screen"), Show("laptop_screen")
        
screen power_screen():
    zorder 2
    modal False
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
    modal False
    image "blank laptop"
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yinitial 1.0
        image "alex laughing"
    if show_image_buttons == True:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            action Hide("social_screen"), Show("laptop_screen")

screen web_screen():
    zorder 0
    modal False
    image "bg browser"
    frame: 
        xalign 0.30
        yalign 0.138
        background "#00000000"
        text "{color=[search_result]}Search: Medievil{/color}" at center
    if not website_2_not_seen and not website_3_not_seen and show_image_buttons:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            if new_objectives_not_heard:
                action Hide("web_screen"), Show("laptop_screen"), Jump("new_objectives")
            else:
                action Hide("web_screen"), Show("laptop_screen")
    if show_image_buttons == True:
        imagebutton:
            focus_mask True
            idle "website 1 icon idle" at website1_icon
            hover "website 1 icon hover"
            action Hide("web_screen"), Jump("website1_call")
        imagebutton:
            focus_mask True
            idle "website 2 icon idle" at website2_icon
            hover "website 2 icon hover"
            action Hide("web_screen"), Jump("website2_call")
        imagebutton:
            focus_mask True
            idle "website 3 icon idle" at website3_icon
            hover "website 3 icon hover"
            action Hide("web_screen"), Jump("website3_call")

screen website1_screen():
    zorder 0
    modal False
    image "bg browser"
    frame: 
        xalign 0.37
        yalign 0.138
        background "#00000000"
        text "{color=[search_result]}WestNews.com/456487568/Medievil {/color}" at center
    if show_image_buttons == True:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            action Hide("website1_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_1_scrollbar_pos, changed=viewport_change1)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 1"
                if website_1_not_seen:
                    imagebutton:
                        idle "website 1 button idle"
                        hover "website 1 button hover"
                        focus_mask True
                        action Hide("website1_screen"), Function(set_function, website_1_not_seen), Jump("website1_button")

screen website2_screen():
    zorder 0
    modal False
    image "bg browser"
    frame: 
        xalign 0.46
        yalign 0.138
        background "#00000000"
        text "{color=[search_result]}WesterosUniversityNews.com/80909783456/Medievil{/color}" at center
    if show_image_buttons == True:    
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            action Hide("website2_screen"), Show("web_screen")
        viewport:
            area laptop_usable_area
            draggable True
            mousewheel True
            scrollbars "vertical"
            yadjustment ui.adjustment(1, website_2_scrollbar_pos, changed=viewport_change2)
            #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 2"
                if website_2_not_seen and show_image_buttons:
                    imagebutton:
                        idle "website 2 button idle"
                        hover "website 2 button hover"
                        focus_mask True
                        action Hide("website2_screen"), Function(set_function, website_2_not_seen), Jump("website2_button")

screen website3_screen():
    zorder 0
    modal False
    image "bg browser"
    frame: 
        xalign 0.4
        yalign 0.138
        background "#00000000"
        text "{color=[search_result]}LinkedOut.com/765433907644358/Medievil{/color}" at center
    if show_image_buttons == True:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            xpos 200
            ypos 600
            xsize 500
            ysize 400
            #focus_mask True
            action Hide("website3_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        draggable True
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_3_scrollbar_pos, changed=viewport_change3)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "website 3"
                if website_3_not_seen and show_image_buttons:
                    imagebutton:
                        idle "website 3 button idle"
                        hover "website 3 button hover"
                        focus_mask True
                        action Hide("website3_screen"), Function(set_function, website_3_not_seen), Jump("website3_button")



screen website1_button_text:
    window:
        text "something useless"

# only known way to make it work (no idea why)
init python:
    def set_function(value):
        value = False
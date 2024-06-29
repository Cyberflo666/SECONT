define laptop_usable_area = (240, 186, 1441, 702)
define website_area = (0, 0, 1441, 2400)
define website_1_scrollbar_pos = 0
define website_2_scrollbar_pos = 0
define website_3_scrollbar_pos = 0
define website_4_scrollbar_pos = 0
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
init python:
    def viewport_change4(value):
        global website_4_scrollbar_pos
        website_4_scrollbar_pos = value
        #renpy.notify(website_1_scrollbar_pos)
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
transform website_button_pos:
    zoom 1

screen laptop_screen():
    zorder 1
    modal False
        
    
# Return arrow (closes phone)
    if show_image_buttons == True:
        imagebutton:
            idle "mail idle"
            hover "mail hover"
            focus_mask True
            if player_warned == False:
                action Call("warning")
            else:
                action Hide("laptop_screen"), Show("mail_screen")

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
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
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
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
            action Hide("social_screen"), Show("laptop_screen")

screen web_screen():
    zorder 0
    modal False
    image "web result all"
    image"return arrow black idle" at return_arrow_black_pos
    frame: 
        xalign 0.41
        yalign 0.138
        background "#00000000"
        text "{color=[search_result]}DingDing.com\search:7jh349rzdw23fzg2970{/color}" at center
    frame: 
        xalign 0.237
        yalign 0.200
        background "#00000000"
        text "{color=[search_result]}Medievil{/color}" at center
    if not website_2_not_seen and not website_3_not_seen and show_image_buttons:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
            if new_objectives_not_heard:
                action Hide("web_screen"), Show("laptop_screen"), Jump("new_objectives")
            else:
                action Hide("web_screen"), Show("laptop_screen")
    if show_image_buttons == True:
        imagebutton:
            focus_mask True
            idle "web result1 idle" #at website1_icon
            hover "web result1 hover"
            action Hide("web_screen"), Jump("website1_call")
        imagebutton:
            focus_mask True
            idle "web result2 idle" #at website2_icon
            hover "web result2 hover"
            action Hide("web_screen"), Jump("website2_call")
        imagebutton:
            focus_mask True
            idle "web result3 idle" #at website3_icon
            hover "web result3 hover"
            action Hide("web_screen"), Jump("website3_call")
        imagebutton:
            focus_mask True
            idle "web result4 idle" #at website3_icon
            hover "web result4 hover"
            action Hide("web_screen"), Jump("website4_call")

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
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
            action Hide("website1_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_1_scrollbar_pos, changed=viewport_change1)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "bg website 1"
                if website_1_not_seen:
                    imagebutton:
                        idle "website 1 idle" #at website_button_pos
                        hover "website 1 hover" 
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
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
            action Hide("website2_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_2_scrollbar_pos, changed=viewport_change2)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "bg website 2"
                if website_2_not_seen and show_image_buttons:
                    imagebutton:
                        idle "website 2 idle"
                        hover "website 2 hover"
                        focus_mask True
                        action Hide("website2_screen"), Function(set_function, website_2_not_seen), Jump("website2_button")

screen website4_screen():
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
            #xpos 200
            #ypos 600
            #xsize 500
            ##ysize 400
            #focus_mask True
            action Hide("website4_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_4_scrollbar_pos, changed=viewport_change4)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "bg website 4"
                if website_3_not_seen and show_image_buttons:
                    imagebutton:
                        idle "website 4 idle"
                        hover "website 4 hover"
                        focus_mask True
                        action Hide("website4_screen"), Function(set_function, website_3_not_seen), Jump("website4_button")

screen website3_screen():
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
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
            action Hide("website3_screen"), Show("web_screen")
    viewport:
        area laptop_usable_area
        mousewheel True
        scrollbars "vertical"
        yadjustment ui.adjustment(1, website_3_scrollbar_pos, changed=viewport_change3)
        #define laptop_usable_area = (240, 110, 1441, 830)
        vbox:
            frame:
                area website_area
                background "#00000000"
                image "bg website 3"
                
screen website1_button_text:
    window:
        text "something useless"

# only known way to make it work (no idea why)
init python:
    def set_function(value):
        value = False
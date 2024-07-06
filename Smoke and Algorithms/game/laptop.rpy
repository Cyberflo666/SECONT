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
            if player_warned == False and mail_1_text_unlocked[0] == 1 and mail_1_text_unlocked[1] == 1 and mail_1_text_unlocked[2] == 1:
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

################################### Mail ##########################################
# Variables
default offset = 0
default mail_1_text_unlocked = [0, 0, 0, 0] # 1 means the i-th text is unlocked
define mail_1_placement_sens = 100 # How sensitive the pieces must be aligned with their assigned spot (lower is more sensitive)
define mail_1_pieces_total = 10
define mail_1_piece_pos_goal = [(566, 301), (566, 449), (566, 599)]
define mail_1_piece_pos_initial = [(1000, 220), (1000, 280), (1000, 340), (1000, 400), (1000, 460), (1000, 520), (1000, 580), (1000, 640), (1000, 700), (1000, 760)]
define mail_1_piece_pos_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
define mail_1_correct_order = [1, 2, 3]
default mail_1_current_order = [0, 0, 0]
default mail_1_current_piece_count = 0
default mail_1_previous_piece_count = 0
default count_offset = 0
default count_changed = 0
define j = 0

screen mail_screen():
    zorder 2
    modal False
    image "bg mail"
    image "phishing mail screen"
        
    # Draggable pieces to assemble the correct mail
    draggroup:
        # Draggable mail pieces
        $ j = 0
        for i in range(mail_1_pieces_total):
            # Skips the pieces that need to be unlocked if they are still locked
            if mail_1_piece_pos_index[i] < len(mail_1_text_unlocked):
                if mail_1_text_unlocked[mail_1_piece_pos_index[i]] != 1:
                    continue
            drag:
                drag_name mail_1_piece_pos_index[i]
                pos mail_1_piece_pos_initial[j]

                focus_mask True
                draggable True
                drag_raise True
                dragged dragged_mail

                image "images/objects/laptop/phishing mail/phishing mail text %s.png" %(mail_1_piece_pos_index[i] + 1)
            $ j += 1

        # Spots where the pieces should snap onto
        for i in range(3):
            drag:
                drag_name i
                pos mail_1_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True              # Other drags can be dropped onto this drag
                dropped dropped_onto_mail   # Function beeing called when dropped onto

                image "images/objects/laptop/phishing mail/phishing mail slot.png"

    imagebutton:
        idle "phishing mail send idle"
        hover "phishing mail send hover"
        focus_mask True
        action Function(send_mail)

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

init python:
    import math
    
    # Randomizes indices so as to create a permutation for the indices of the mail pieces
    def randomize_indices():
        global mail_1_piece_pos_index
        for i in range (0,100):
            renpy.notify("something")
            x = renpy.random.randint(0,9)
            y = renpy.random.randint(0,9)
            temp = mail_1_piece_pos_index[x]
            mail_1_piece_pos_index[x] = mail_1_piece_pos_index[y]
            mail_1_piece_pos_index[y] = temp

    # Function called when one of the dragged_pieces is being dropped onto on of the snap_spots
    def dropped_onto_mail(snap_spot, dragged_piece):
        global mail_1_pieces_total

        # Snap piece
        distance = math.sqrt((snap_spot.x - dragged_piece[0].x)**2 + (snap_spot.y - dragged_piece[0].y)**2)
        if distance < mail_1_placement_sens:
            dragged_piece[0].snap(snap_spot.x, snap_spot.y, 0.1)
            mail_1_current_order[snap_spot.drag_name] = dragged_piece[0].drag_name + 1
            renpy.notify(mail_1_current_order)

    # Function called when one of the dragged_pieces is being lifted
    def dragged_mail(dragged_piece, dropped_onto):
        if (dragged_piece[0].drag_name + 1) in mail_1_current_order:
            indx = mail_1_current_order.index(dragged_piece[0].drag_name + 1)
            mail_1_current_order[indx] = 0
        renpy.notify(mail_1_current_order)

    # Function called when player wants to send the mail
    def send_mail():
        if mail_1_current_order == mail_1_correct_order:
            renpy.notify("correct mail")
        else:
            renpy.notify("not the correct mail")

###################################################################################

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
    if show_image_buttons == True:
        imagebutton:
            idle "return arrow black idle" 
            hover "return arrow black hover" at return_arrow_black_pos
            #xpos 200
            #ypos 600
            #xsize 500
            #ysize 400
            #focus_mask True
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
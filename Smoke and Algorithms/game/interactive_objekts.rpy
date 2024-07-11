label hide_felix_room_interactables():
    hide screen felixes_bin
    hide screen felixes_bed
    hide screen felixes_pc
    hide screen felixes_notebook
    hide screen felixes_map
    hide screen felixes_wall1
    hide screen felixes_wall2
    hide screen felixes_wall3
    return

label show_felix_room_interactables():
    show screen felixes_bin
    show screen felixes_bed
    show screen felixes_pc
    show screen felixes_notebook
    show screen felixes_map
    show screen felixes_wall1
    show screen felixes_wall2
    show screen felixes_wall3
    return

screen felixes_notebook():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f notebooks.png" 
            idle "images/backgrounds/felix room/fb notebooks.png" 
            focus_mask True
            action Hide("felixes_notebook"),Jump("notebooks")

screen felixes_bin():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f bin.png" 
            idle "images/backgrounds/felix room/fb bin.png" 
            focus_mask True
            action Hide("felixes_bin"),Jump("bin")


screen felixes_bed():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f bed.png" 
            idle "images/backgrounds/felix room/fb bed.png" 
            focus_mask True
            action Hide("felixes_bed"),Jump("bed")


screen felixes_map():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f map.png" 
            idle "images/backgrounds/felix room/fb map.png" 
            focus_mask True
            action Hide("felixes_map"),Jump("map")


screen felixes_pc():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f pc.png" 
            idle "images/backgrounds/felix room/fb pc.png" 
            focus_mask True
            action Hide("felixes_pc"),Jump("pc")

screen felixes_wall1():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall1.png" 
            idle "images/backgrounds/felix room/fb wall1.png" 
            focus_mask True
            action Hide("felixes_wall1"),Jump("wall1")

screen felixes_wall2():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall2.png" 
            idle "images/backgrounds/felix room/fb wall2.png" 
            focus_mask True
            action Hide("felixes_wall2"),Jump("wall2")

screen felixes_wall3():
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/felix room/f wall3.png" 
            idle "images/backgrounds/felix room/fb wall3.png" 
            focus_mask True
            action Hide("felixes_wall3"),Jump("wall3")

################################ Janitor mini game ####################################

screen round_rect(trust):
    image "gui/bar/bottom back.png":
        xalign 0.976 ypos 297
        ysize 506
        
    vbar:
        xalign 0.974 ypos 300
        ysize 500
        value AnimatedValue(trust,100,0.5)

        if (trust > 75 ):
            bottom_bar "gui/bar/bottomgreen.png"
        elif (trust > 40):
            bottom_bar "gui/bar/bottomyellow.png"
        else:
            bottom_bar "gui/bar/bottomred.png"

    
    text "{size=50}{b}TRUST{/b}{/size}":
        xalign 0.99 ypos 210
        size 50
        outlines [(3, "#000000ff", 0, 0)]
        color "#AA4473FF"

############################# Lab room point and click ################################

label hide_lab_screens:
    hide screen left_cage
    hide screen left_pc
    #hide screen medical_tools
    hide screen left_wall
    hide screen symbol_screen
    hide screen right_cage
    hide screen right_pc
    hide screen trash
    return

screen left_cage:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left cage hover.png" 
            idle "images/backgrounds/lab/left cage idle.png" 
            focus_mask True
            action Hide("left_cage"),Jump("rat_in_cage_left")

screen left_pc:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left pc hover.png" 
            idle "images/backgrounds/lab/left pc idle.png" 
            focus_mask True
            action Hide("left_pc"),Jump("left_pc_stats")

screen left_wall:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/left wall hover.png" 
            idle "images/backgrounds/lab/left wall idle.png" 
            focus_mask True
            action Hide("left_wall"),Jump("left_wall_obj")

screen symbol_screen:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/monitor hover.png" 
            idle "images/backgrounds/lab/monitor idle.png" 
            focus_mask True
            action Hide("symbol_screen"),Jump("symbols_on_screen")

screen right_cage:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/right cage hover.png" 
            idle "images/backgrounds/lab/right cage idle.png" 
            focus_mask True
            action Hide("right_cage"),Jump("rat_in_cage_right")

screen right_pc:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/right pc hover.png" 
            idle "images/backgrounds/lab/right pc idle.png" 
            focus_mask True
            action Hide("right_pc"),Jump("right_pc_stats")
screen trash:
    zorder 0
    modal False
    if show_image_buttons == True:
        imagebutton :
            hover "images/backgrounds/lab/trash hover.png" 
            idle "images/backgrounds/lab/trash idle.png" 
            focus_mask True
            action Hide("trash"),Jump("empty_trash")

#screen medical_tools:
    #zorder 0
    #modal False
    #if show_image_buttons == True:
        #imagebutton :
            #hover "images/backgrounds/felix room/f wall3.png" 
            #idle "images/backgrounds/felix room/fb wall3.png" 
            #focus_mask True
            #action Hide("medical_tools"),Jump("used_medical_tools")

            
                
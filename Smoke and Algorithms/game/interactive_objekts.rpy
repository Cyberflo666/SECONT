screen felixes_notebook():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f notebooks.png" 
        idle "images/backgrounds/felix room/fb notebooks.png" 
        focus_mask True
        action Hide("felixes_notebook"),Jump("notebooks")

screen felixes_bin():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f bin.png" 
        idle "images/backgrounds/felix room/fb bin.png" 
        focus_mask True
        action Hide("felixes_bin"),Jump("bin")


screen felixes_bed():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f bed.png" 
        idle "images/backgrounds/felix room/fb bed.png" 
        focus_mask True
        action Hide("felixes_bed"),Jump("bed")


screen felixes_map():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f map.png" 
        idle "images/backgrounds/felix room/fb map.png" 
        focus_mask True
        action Hide("felixes_map"),Jump("map")


screen felixes_pc():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f pc.png" 
        idle "images/backgrounds/felix room/fb pc.png" 
        focus_mask True
        action Hide("felixes_pc"),Jump("pc")

screen felixes_wall1():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f wall1.png" 
        idle "images/backgrounds/felix room/fb wall1.png" 
        focus_mask True
        action Hide("felixes_wall1"),Jump("wall1")

screen felixes_wall2():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f wall2.png" 
        idle "images/backgrounds/felix room/fb wall2.png" 
        focus_mask True
        action Hide("felixes_wall2"),Jump("wall2")

screen felixes_wall3():
    zorder 0
    modal False
    
    imagebutton :
        hover "images/backgrounds/felix room/f wall3.png" 
        idle "images/backgrounds/felix room/fb wall3.png" 
        focus_mask True
        action Hide("felixes_wall3"),Jump("wall3")

screen round_rect(trust):

        

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

    
    text "TRUST":
        xalign 0.995 ypos 250
        size 40
        color "00bdff"


            
                
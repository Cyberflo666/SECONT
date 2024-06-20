# This file contains the dumpster diving mini game
# 1 is the receipt 2 is the random trash
define diving1completed = False

label dumpster_diving_minigame_start:
    hide screen phone_icon
    call screen dumpster_diving_minigame_1 # Calling a screen hides the dialogue box

label dumpster_diving_minigame_completed_1:
    $ diving1completed = True
    scene bg dumpster diving 1 finished
    pause 1.5
    scene bg new kitchen

    $ renpy.notify("A picture has been added to your notes")
    pause 1.5
    call screen dumpster_diving_minigame_2

label dumpster_diving_minigame_completed_2:
    $ diving1completed = True
    scene bg dumpster diving 1 finished
    pause 1.5
    scene bg new kitchen

    $ renpy.notify("A picture has been added to your notes")
    pause 1.5
    jump after_dumpsterdive
    
# Variables
define placement_sens = 20 # How sensitive the pieces must be aligned with their assigned spot (lower is more sensitive)
define dd1_pieces_total = 7
default dd1_pieces_completed = 0
define dd1_piece_pos_goal = [(92, 28), (92, 137), (299, 28), (338, 216), (92, 345), (92, 553), (335, 654)]
define dd1_piece_pos_initial = [(1050, 140), (1020, 160), (1010, 130), (1100, 250), (1030, 180), (960, 150), (1000, 150)]

screen dumpster_diving_minigame_1:
    image "images/objects/dumpster diving/bg dumpster diving 1.png"

    draggroup:
        # Draggable image pieces
        for i in range(dd1_pieces_total):
            drag:
                drag_name i
                pos dd1_piece_pos_initial[i]

                focus_mask True
                draggable True
                drag_raise True

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1)

        # Spots where the pieces should snap onto
        for i in range(dd1_pieces_total):
            drag:
                drag_name i
                pos dd1_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True          # Other drags can be dropped onto this drag
                dropped dropped_onto    # Function beeing called when dropped onto

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1) alpha 0.0

define dd2_pieces_total = 7
default dd2_pieces_completed = 0
define dd2_piece_pos_goal = [(92, 28), (92, 137), (299, 28), (338, 216), (92, 345), (92, 553), (335, 654)]
define dd2_piece_pos_initial = [(1050, 140), (1020, 160), (1010, 130), (1100, 250), (1030, 180), (960, 150), (1000, 150)]

screen dumpster_diving_minigame_2:
    image "images/objects/dumpster diving/bg dumpster diving 1.png"

    draggroup:
        # Draggable image pieces
        for i in range(dd2_pieces_total):
            drag:
                drag_name i
                pos dd2_piece_pos_initial[i]

                focus_mask True
                draggable True
                drag_raise True

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1)

        # Spots where the pieces should snap onto
        for i in range(dd2_pieces_total):
            drag:
                drag_name i
                pos dd2_piece_pos_goal[i]

                focus_mask True
                draggable False
                droppable True          # Other drags can be dropped onto this drag
                dropped dropped_onto    # Function beeing called when dropped onto

                image "images/objects/dumpster diving/pieces 1/piece %s.png" %(i + 1) alpha 0.0


init python:
    import math
    
    # Function called when one of the dragged_pieces is being dropped onto on of the snap_spots
    def dropped_onto(snap_spot, dragged_piece):
        global dd1_pieces_completed
        global dd2_pieces_completed

        # Snap piece if piece is on correct spot and distance is close enough
        if snap_spot.drag_name == dragged_piece[0].drag_name:
            distance = math.sqrt((snap_spot.x - dragged_piece[0].x)**2 + (snap_spot.y - dragged_piece[0].y)**2)
            if distance < placement_sens:
                dragged_piece[0].snap(snap_spot.x, snap_spot.y, 0.1)
                dragged_piece[0].draggable = False
                if diving1completed == True:
                    dd2_pieces_completed +=1
                    if dd2_pieces_completed == dd2_pieces_total:
                        renpy.jump("dumpster_diving_minigame_completed_2")
                else:
                    dd1_pieces_completed += 1
                    if dd1_pieces_completed == dd1_pieces_total:
                        renpy.jump("dumpster_diving_minigame_completed_1")
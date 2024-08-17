label security_minigame_start:
    $ show_textbox = False
    show screen minigame_screen()
    jump empty_label
    #outside of tuple:
    #0s are no field 
    #1s are field 
    #2s are rooms 
    #3 bobs room
    #in tuple:
    #0 is notailgate person in 
    #1s are orange tailgate people
    #2s are green tailgate people
    #3s are purple tailgate people
    #4s are blue tailgate people
    #[field,security on field,is player on field,tailgate people] (t for true f for false) extra: door open : O door closed : C
    # 120, 60
default x = 0
default y = 0

screen minigame_screen():
    zorder 0
    modal False
    image "bg security minigame"
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "mid idle" 
            hover "mid hover"
            action Function(turn,0),Hide("minigame_screen"),Jump("security_minigame_start")
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "up idle" 
            hover "up hover"
            if valid_inputs[4] == 1:
                action Function(turn,4),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "right idle" 
            hover "right hover"
            if valid_inputs[1] == 1:
                action Function(turn,1),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "down idle" 
            hover "down hover"
            if valid_inputs[2] == 1:
                action Function(turn,2),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    if show_image_buttons == True:    
        imagebutton:
            focus_mask True
            idle "left idle" 
            hover "left hover"
            if valid_inputs[3] == 1:
                action Function(turn,3),Hide("minigame_screen"),Jump("security_minigame_start")
            else:
                action Function(real_notify,"Invalid input")
    
    if door_state == False:
        image "door closed"
    else:
        image "door open"

    for i in range(0,4):
        $ x = sec_list[i][0][sec_list[i][1]][1]
        $ y = sec_list[i][0][sec_list[i][1]][0]
        if i == 0:
            image "guard cone":
                alpha 0.5
                anchor (0.5,0.5)
                ypos  120 * x + 60 
                xpos 1800 - (60 + 120 * y) + 60
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        elif i == 1:
            image "guard cone":
                alpha 0.5
                anchor (0.5,0.5)
                ypos  120 * x + 60
                xpos 1800 - (60 + 120 * y) + 60
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        elif i == 2:
            image "guard cone":
                alpha 0.5
                anchor (0.5,0.5)
                ypos  120 * x + 60
                xpos 1800 - (60 + 120 * y) + 60
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        else:
            image "guard cone":
                alpha 0.5
                anchor (0.5,0.5)
                ypos  120 * x + 60
                xpos 1800 - (60 + 120 * y) + 60
                rotate 90 * (sec_list[i][0][sec_list[i][1]][2] - 1)
            image "guard" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        $ x = tailgate_list[i][0][tailgate_list[i][1]][1]
        $ y = tailgate_list[i][0][tailgate_list[i][1]][0]
        if i == 0:
            image "orange" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        elif i == 1:
            image "green" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        elif i == 2:
            image "purple" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
        else:
            image "blue" :
                ypos  120 * x + 16
                xpos 1800 - (60 + 120 * y) + 16
    $ x = player_pos[1]
    $ y = player_pos[0]
    image "player" :
        ypos  120 * x + 16
        xpos  1800 - (60 + 120 * y) + 16

define door_state = False
define game_matrix= [
                    [0,0,0,0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                    [0,["c","f",0],0,0,[0,"f",0,0,0,0],0,0,[0,"f",0,0,0,0],0],
                    [[0,"f",0,0,0,1],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                    [0,0,0,0,0,[0,"f",0,0,0,0,door_state],0,0,0],
                    [0,0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                    [0,0,[3,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0]],
                    [0,0,[0,"f",0,0,0,0],0,0,["b","f",0,0,],0,0,[0,"f",0,0,0,0]],
                    [[0,"f",0,0,1,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                    [0,0,[0,"f",0,0,0,0],0,0,0,0,0,[0,"f",0,0,0,0]],
                    [["a","f",0],0,[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[1,"f",0,0,0,0]],
                    [[0,"f",0,0,0,0],0,0,0,0,[0,"f",0,0,0,0],0,0,0],
                    [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[4,0,0,0,0,0]],
                    [0,0,0,[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                    [[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],[0,"f",0,0,0,0],0,[0,"f",0,0,0,0],0,0,0],
                    [0,[0,"t",0,0,0,0],0,[0,"f",1,0,0,0],0,[0,"f",0,2,0,0],0,0,0]
                    ]
define orange_path = [[14,3],[13,3],[12,3],[11,3],[11,4],[11,5],[10,5],[9,5],[9,6],[9,7],[9,8],[8,8],[7,8],[6,8],[5,8],[5,7],[5,6],[5,5],[6,5],[-1,-1]]
define green_path = [[14,5],[13,5],[12,5],[11,5],[10,5],[9,5],[9,4],[9,3],[9,2],[8,2],[7,2],[7,1],[7,0],[-1,-1]]
define purple_path = [[7,0],[7,1],[7,2],[6,2],[5,2],[5,3],[5,4],[5,5],[4,5],[3,5],[2,5],[2,6],[2,7],[2,8],[-1,-1]]
define blue_path = [[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,5],[4,5],[5,5],[5,4],[5,3],[5,2],[6,2],[7,2],[7,1],[7,0],[-1,-1]]
define sec_path_1 = [[2,8,4],[2,7,4],[2,6,4],[2,5,4],[2,4,4],[2,3,4],[2,2,4],[2,1,4],[2,0,4],[2,1,2],[2,2,2],[2,3,2],[2,4,2],[2,5,2],[2,6,2],[2,7,2],[-1,-1]]
define sec_path_2 = [[11,8,4],[11,7,4],[11,6,4],[11,5,4],[11,4,4],[11,3,4],[11,2,4],[11,1,4],[11,0,4],[11,1,2],[11,2,2],[11,3,2],[11,4,2],[11,5,2],[11,6,2],[11,7,2],[-1,-1]]
define sec_path_3 = [[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[-1,-1]]
define sec_path_4 = [[9,8,1],[8,8,1],[7,8,1],[6,8,1],[5,8,4],[5,7,4],[5,6,4],[5,5,4],[5,4,4],[5,3,4],[5,2,3],[6,2,3],[7,2,3],[8,2,3],[9,2,2],[9,3,2],[9,4,2],[9,5,2],[9,6,2],[9,7,2],[-1,-1]]
define sec_index_1 = 0
define sec_index_2 = 0
define sec_index_3 = 0
define sec_index_4 = 0
define sec_list = [[sec_path_1,sec_index_1],[sec_path_2,sec_index_2],[sec_path_3,sec_index_3],[sec_path_4,sec_index_4]]
define orange_index = 0
define green_index = 0
define purple_index = 0
define blue_index = 0
define tailgate_list = [[orange_path,orange_index],[green_path,green_index],[purple_path,purple_index],[blue_path,blue_index]]
define valid_inputs = [1,1,0,0,0]
define player_pos = [14,1]
define door_timer = 0
define optional_flag = True
define bobs_flag = True
define courtyard_flag = True

init python:
    def real_notify(string):
        renpy.notify(string)
    def turn(input):
        global game_matrix
        global sec_list
        global tailgate_list
        global valid_inputs
        global player_pos
        global door_timer
        global door_state
        global optional_flag
        global courtyard_flag
        global bobs_flag
        
        turn_personal(game_matrix,tailgate_list)
        turn_player(input,game_matrix)
        turn_security(game_matrix,sec_list)
        for i in range(0,4):
            if see(sec_list[i][0][sec_list[i][1]][1],sec_list[i][0][sec_list[i][1]][0],sec_list[i][0][sec_list[i][1]][2],game_matrix) == 1:
                renpy.notify("u lost")
        if door_timer < 0:
            door_state = False
        door_timer -= 1
        if player_pos == [6,5] and courtyard_flag:
            courtyard_flag = False
            renpy.jump("courtyard")
        elif player_pos == [1,1] and bobs_flag:
            bobs_flag = False
            renpy.jump("bobs_office")
        elif player_pos == [9,0] and optional_flag:
            optional_flag = False
            renpy.jump("optional")
        #renpy.notify(door_timer)
        renpy.restart_interaction()
        #renpy.show("minigame_screen")
    def turn_player(input,matrix):
        
        global player_pos
        global valid_inputs
        if input == 1:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[0] -= 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 2:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[1] += 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 3:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[0] += 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"
        elif input == 4:
            matrix[player_pos[0]][player_pos[1]][1] = "f"
            player_pos[1] -= 1 
            matrix[player_pos[0]][player_pos[1]][1] = "t"

        if player_pos[0] == 0:
            valid_inputs[1] = 0
        elif matrix[player_pos[0]-1][player_pos[1]] == 0:
            valid_inputs[1] = 0
        else:
            valid_inputs[1] = 1
        if player_pos[1] == 8:
            valid_inputs[2] = 0
        elif matrix[player_pos[0]][player_pos[1]+1] == 0:
            valid_inputs[2] = 0
        else:
            valid_inputs[2] = 1
        if player_pos[0] == 14:
            valid_inputs[3] = 0
        elif matrix[player_pos[0]+1][player_pos[1]] == 0:
            valid_inputs[3] = 0
        else:
            valid_inputs[3] = 1
        if player_pos[1] == 0:
            valid_inputs[4] = 0
        elif matrix[player_pos[0]][player_pos[1]-1] == 0:
            valid_inputs[4] = 0
        else:
            valid_inputs[4] = 1
    
        if player_pos == [4,5]:
            if door_state == False:
                valid_inputs[1] = 0
                renpy.notify(valid_inputs[1])
        if player_pos == [3,5]:
            if door_state == False:
                valid_inputs[3] = 0
            
    
    def turn_personal(matrix,path_list):
        global door_state
        global door_timer
        for i in range(0,4):
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = 0
            path_list[i][1] +=1
            path_list[i][1] = path_list[i][1] % (len(path_list[i][0]) - 1)
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = 1
            if i == 3:
                if path_list[3][0][path_list[3][1]][0] == 3 and path_list[3][0][path_list[3][1]][1] == 5:
                    door_state = True
                    door_timer = 2
                    #renpy.notify(door_state)
            if i == 2:
                if path_list[2][0][path_list[2][1]][0] == 4 and path_list[2][0][path_list[2][1]][1] == 5:
                    door_state = True
                    door_timer = 2
                    #renpy.notify(door_state)
    def turn_security(matrix,path_list):
        for i in range(0,4):
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][0] = 0
            path_list[i][1] +=1
            path_list[i][1] = path_list[i][1] % (len(path_list[i][0]) - 1)
            matrix[path_list[i][0][path_list[i][1]][0]][path_list[i][0][path_list[i][1]][1]][i+2] = path_list[i][0][path_list[i][1]][2]
    
    def see(x,y,d,matrix):
        if matrix[y][x][1] == "t":
            return 1
        if d == 4:
            if (x - 1) < 0:
                pass
            else:
                #print(str(x) + "," + str(y))
                if matrix[y][x - 1] == 0:
                    return 0
                elif matrix[y][x - 1][1] == "t":
                    return 1
            if x - (1 * 2) < 0:
                pass
            else:
                if matrix[y][x - (1 * 2)] == 0:
                    pass
                elif matrix[y][x-2][1] == "t":
                    return 1
            if (y-1) < 0:
                pass
            else:
                if matrix[y-1][x] == 0:
                    pass
                elif matrix[y-1][x][1] == "t":
                    return 1
            
            if (y+1) > 14:
                pass
            else:
                if matrix[y+1][x] == 0:
                    pass
                elif matrix[y+1][x][1] == "t":
                    return 1

        if d == 2:
            if x + 1 > 8:
                pass
            else:
                if matrix[y][x + 1] == 0:
                    pass
                elif matrix[y][x + 1][1] == "t":
                    return 1
            if x + (1 * 2) > 8 :
                pass
            else:
                if matrix[y][x + (1 * 2)] == 0:
                    pass
                elif matrix[y][x+2][1] == "t":
                    return 1
            
            if (y-1) < 0:
                pass
            else:
                if matrix[y-1][x] == 0:
                    pass
                elif matrix[y-1][x][1] == "t":
                    return 1
            
            if (y+1) > 14:
                pass
            else:
                if matrix[y+1][x] == 0:
                    pass
                elif matrix[y+1][x][1] == "t":
                    return 1
            
        if d == 1:
            if y - 1 < 0:
                pass
            else:
                if matrix[y - 1][x] == 0:
                    pass
                elif matrix[y - 1][x][1] == "t":
                    return 1
            if y - (1 * 2) < 0:
                pass
            else:
                if matrix[y - (1 * 2)][x] == 0:
                    pass
                elif matrix[y-2][x][1] == "t":
                    return 1

            if (x-1) < 0:
                pass
            else:
                if matrix[y][x-1] == 0:
                    pass
                elif matrix[y][x-1][1] == "t":
                    return 1
            
            if (x+1) > 8:
                pass
            else:
                if matrix[y][1+x] == 0:
                    pass
                elif matrix[y][1+x][1] == "t":
                    return 1

        if d == 3:
            if y + 1 > 14:
                pass
            else:
                if matrix[y + 1][x] == 0:
                    pass
                elif matrix[y + 1][x][1] == "t":
                    return 1
            if y + (1 * 2) > 14:
                pass
            else:
                if matrix[y + (1 * 2)][x] == 0:
                    pass
                elif matrix[y+2][x][1] == "t":
                    return 1

            if (x-1) < 0:
                pass
            else:
                if matrix[y][x-1] == 0:
                    pass
                elif matrix[y][x-1][1] == "t":
                    return 1
            
            if (x+1) > 8:
                pass
            else:
                if matrix[y][1+x] == 0:
                    pass
                elif matrix[y][1+x][1] == "t":
                    return 1
        return 0
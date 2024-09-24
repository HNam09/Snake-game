'''Goal: making a simple snake game'''

import turtle #graphical module 
import time
import random



#some variables
score = 0
high_score = 0
Width=800 
Height=800
Border_horz = int(Width/2)   
Border_vert = int(Height/2)
#refresh rate of the main loop, determine speed of the game
delay=0.1 
#list of different colors used to randomize food
food_color =['blue', 'chartreuse', 'purple', 'red'] 

#Define functions




#Functions for snake auto-movement
def move() :
    if head.direction == 'up' :
        y = head.ycor()  # define variable for current y co-ordinate
        head.sety(y+20)  #increamenting y co-ordinate automatically
        gd.clear()
    if head.direction == 'down' :
        y = head.ycor() 
        head.sety(y-20)
        gd.clear()
    if head.direction == 'left' :
        x = head.xcor() 
        head.setx(x-20)
        gd.clear()
    if head.direction == 'right' :
        x = head.xcor() 
        head.setx(x+20)
        gd.clear()




#Functions for player controlling the head 
def move_up():
    if head.direction != "down": #prevent going in reversed(180 deg) direction
        head.direction = "up" #function return to change direction if called
      
def move_down():
    if head.direction != "up":
        head.direction = "down"
       
def move_left():
    if head.direction != "right":
        head.direction = "left"
       
def move_right():
    if head.direction != "left":
        head.direction = "right"
        

#function for resetting score when game over
def reset_score() :
    sc.clear()
    sc.write(f'Score: {score}   High Score: {high_score}', align = 'center', font = ('Courier', 24, 'normal'))
    return score

#function for showing the guide at the start of each game
def pop_up() :
    gd.write(' Use arrow keys for movement\n There are no walls, you will go to the other side instead\n Effects of the foods:\n Red: detach and leave behind a piece of the tail\n Purple: add +5% to speed of the snake\n Blue: Snake turns around opposite direction from it\'s tail\n Green: no special effects, normal food   ', align = 'center', font = ('Courier', 14, 'normal'))


#function for adding parts to a list of snake's body parts
def add_parts() :
    more_part = turtle.Turtle()
    more_part.speed(0)
    more_part.shape('circle')
    more_part.color('DarkGrey')
    more_part.penup()
    body.append(more_part)



#Functions to randomize the position and color of new food
def food_pos():
    x_fd = random.randint((-Border_horz +10),( Border_horz -10))
    y_fd = random.randint((-Border_vert +10),(Border_vert -10))
    return x_fd , y_fd
def get_color() :
    color_fd = random.choice(food_color)
    return color_fd

#function to prevent new food overlap with body parts
def new_food(food):
    i = 1
    while i == 1:
        i = 0 #exit the loop if food and and parts not overlap
        food.goto(food_pos()) 
        food.color(get_color())
        #check if food overlap with body  
        for part in body: 
            if part.distance(food) <= 20 :
                i = 1 #overlap so repeat the while loop
                break
        #same check but for the detached parts
        for block in block_list:
            if block.distance(food) <= 20 :
                i = 1 
                break
        



#function for game over when collide with body parts
def game_over(body,block_list) :
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop" 
    for part in body:
        part.hideturtle()
    for block in block_list:
        block.hideturtle()
    block_list.clear()  
    body.clear()
    pop_up() # make the tutorial reappear until snake moves
    new_food(food1) #re-randomize food position and color
    new_food(food2)


#function for special event for each different colored food 
def special_food(food):
    if food.color()[0] == 'red':
        #create new turtle object then move it to the end of tail
        block = turtle.Turtle()
        block.speed(0)
        block.shape('circle')
        block.color('goldenrod4')
        block.penup()
        if len(body) > 0:
            x, y = body[-1].xcor() , body[-1].ycor()
        elif len(body) == 0:
            x, y = head.xcor(), head.ycor()
        block.goto(x,y)
        block_list.append(block)


    elif food.color()[0] == 'blue':
        #only works if 2 or more parts are added to body
        if len(body) > 1:
            #using last 2 parts of the tail for direction
            x1, y1 = body[-1].xcor(), body[-1].ycor()
            x2, y2 = body[-2].xcor(), body[-2].ycor()
            #warp then flip direction of the head depending on direction of the tail
            if (x2-x1) == 0 :
                if (y2-y1) > 0 :
                    head.goto(x1, y1)
                    head.direction = "down"
                elif (y2-y1) < 0 :
                    head.goto(x1, y1)
                    head.direction = "up"
            if (y2-y1) == 0 :
                if (x2-x1) > 0 :
                    head.goto(x1, y1)
                    head.direction = "left"
                elif (x2-x1) < 0 :
                    head.goto(x1, y1)
                    head.direction = "right"

 
        


   




#Creating various objects before game loop start

#launch the screen
wd=turtle.Screen() #create screen object
wd.title('Alternate version of Snake Game')  
wd.bgcolor('grey')  #background color
#variable for width and height
wd.setup(width=Width+10, height=Height+10)
#variable for the borders based on width and height
wd.tracer(0)    #turn off animation updates


#Create the head
head = turtle.Turtle() #main object in this module, default size = 20 pixels
head.speed(0)   #animation speed of the object
head.shape('circle')   
head.color('black')     
head.penup()    #turn off drawing lines when object moves
head.goto(0,0)  #set location for object, center by default
head.direction = "stop" #set direction for object, stop by default

#list of body parts
body=[]
block_list = []

#Create food object 
food1 = turtle.Turtle() 
food1.shape('square')   
food1.color(get_color()) 
food1.penup()      
food1.goto(food_pos()) # food starting position(randomized)

#Create food object 
food2 = turtle.Turtle() 
food2.shape('square')   
food2.color(get_color()) 
food2.penup()      
food2.goto(food_pos()) # food starting position(randomized)

#Writing the score
sc = turtle.Turtle()
sc.speed(0)
sc.shape('square')
sc.color('white')
sc.penup()
sc.hideturtle()
sc.goto(0,Border_vert - 30) 
sc.write('Score: 0    High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))

#Writing the tutorial/guide
gd = turtle.Turtle()
gd.speed(0)
gd.shape('square')
gd.color('white')
gd.penup()
gd.hideturtle()
gd.goto(0,-Border_vert)
pop_up()

#keyboard bindings
wd.listen() #function to register input
#pairing a function to be called once a key is pressed
wd.onkeypress(move_up, "Up") 
wd.onkeypress(move_down, "Down")
wd.onkeypress(move_left, "Left")
wd.onkeypress(move_right, "Right")
#wd.onkeypress(guide_popup, 'h')




#Game loop

while True: 
    wd.update() #refresh all objects each loop, since animation is turned off
    
    #check for collision with border
    if head.xcor() >= ( Border_horz -5) or head.xcor() <= (-Border_horz +5) or head.ycor() >= (Border_vert -5) or head.ycor() <= (-Border_vert +5) :
        #Get position of the head
        x_h = head.xcor()
        y_h = head.ycor()
        #Determine which of the 4 quadrants the head is in, warp it to the opposite side accordingly
        if y_h > 0 and abs(y_h) > abs(x_h) :
            head.goto(x_h,-y_h +10)  # add an extra 10 pixel after the warp to prevent weird behavior at border lines
        elif y_h < 0 and abs(y_h) > abs(x_h) :
            head.goto(x_h,-y_h -10) 
        elif  x_h > 0 and abs(x_h) > abs(y_h) :
            head.goto(-x_h +10,y_h) 
        elif  x_h < 0 and abs(x_h) > abs(y_h) :
            head.goto(-x_h -10,y_h) 

    #check collision with its own body parts
    for part in body:
        if part.distance(head) < 20 :
            game_over(body,block_list)
            #Reset things when game over
            score = 0
            reset_score()  
            delay = 0.1 #back to default speed
            
    #Check collision with the detached parts
    for block in block_list:
        if block.distance(head) < 20:
            game_over(body,block_list)
            #Reset things when game over
            score = 0
            reset_score()  
            delay = 0.1
            
        

    #Check for collision with food
    if head.distance(food1)  < 20 or head.distance(food2)  < 20: 
        #check which of the 2 foods are eaten, then call their special trait
        if head.distance(food1)  < 20:
            special_food(food1)
            if food1.color()[0] == 'purple' :
                delay -= (0.05 * delay) #add 5% speed each time
            #reset both foods
            new_food(food1)
            new_food(food2)

            
        elif head.distance(food2)  < 20 :
            special_food(food2)
            if food1.color()[0] == 'purple' :
                delay -= (0.05 * delay)

            new_food(food2)
            new_food(food1)
        
        #Add length to Snake's body
        add_parts()
        

        #Add score whenver body part is added
        score += 10
        if score > high_score :
            high_score = score
        sc.clear() #clear old score text
        sc.write(f'Score: {score}    High Score: {high_score}', align = 'center', font = ('Courier', 24, 'normal'))
   


    #stacking the body parts 
    #moving each body part to the previous position of the part ahead of it
    for i in range(len(body)-1,0,-1) : 
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)

    #move the first part to the head
    if len(body) > 0 :
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move() #automate movement of snake

    time.sleep(delay) #set speed of the refresh(game speed)
wd.mainloop()
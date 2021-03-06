


import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(1000,1000) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
border=turtle.clone()
border.penup()
border.goto(0,270)
border.pendown()
border.goto(410,270)
border.goto(-410,270)
border.left(90)
border.goto(-410,-270)
border.left(90)
border.goto(410,-270)
border.left(90)
border.goto(410,270)
border.penup()
border.goto(-50,400)
border.pendown()
border.write('snake game!!!',font=('Arial',32,'normal'))
border.hideturtle()
border.penup()
border.goto(-50,-450)
border.pendown()








             

#Initialize listsbor
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for START_LENGTH in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos=x_pos+SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################

UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN=1
LEFT=2
RIGHT=3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400



def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
def down():
    global direction
    direction = DOWN
    print('you pressed the down key!')

def left():
    global direction
    direction = LEFT
    
    print("you pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("you pressed the right key!")
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the DOWN edge! Game over!")
        quit()

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')

    
    
    global food_stamps,food_pos
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        
        
        

    
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        print("You have eaten the food!")
        
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)


    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
   
    #if new_pos
    if len(food_stamps) <= 6 :
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
    if my_pos in pos_list[0:len(pos_list)-1]:
        quit()


turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()

food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    stamp_ID = food.stamp()
    food_stamps.append(stamp_ID)


    
            



def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    food_x = random.randint(min_x,max_y)*SQUARE_SIZE
    food_y = random.randint(min_x,max_y)*SQUARE_SIZE
    
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

  
        
        
     
     
    
           

    
print('moving snake')
move_snake()


#min_x,max_y
#min_x,max_y

   

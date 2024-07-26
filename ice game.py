import turtle, random, time

sc = turtle.Screen()
sc.bgcolor("#251963")
sc.setup(500,500)
sc.tracer(0)

sc.addshape("cat.gif")
penguin = turtle.Turtle()
penguin.shape("cat.gif")
penguin.goto(-10, 50)

ice = turtle.Turtle()
ice.up()
ice.speed(0)
ice.shape("square")
ice.color("#dad5f5")
ice.goto(-30, 70)
ice_size = 5
ice.turtlesize(20, 30)

top_line = 175
bottom_line = -125
directions = [ 90, 270, 180, 0]
columns = [-125, -50, 25, 100 ]
speed = 5

def square(sam):
    sam.begin_fill()
    sam.down()
    for x in range (4):
        sam.fd(50)
        sam.lt(180)
    sam.end_fill() 

def boxes():
    sam = turtle.Turtle()
    sam.shape("triangle")
    sam.speed(0)
    sam.ht()
    sam.fillcolor("#db1218")
    sam.pencolor("#1f1f6b")

    for s in range (4):
        sam.up()
        sam.goto(columns[s] , bottom_line -25)
        sam.seth(directions[s])         
        sam.stamp()

        sam.seth(0)
        sam.goto(columns[s] - 25,bottom_line)
        square(sam)

def resetArrow(a):
    red = 0
    green = random.random()
    blue = random.random()
    a.color(red, green, blue)
    randPos = random.randint(0, 3)
    a.seth(directions[randPos])
    offset = 0
    for ar in arrows:
        if ar.ycor() > top_line-20 and ar.xcor() == columns[randPos]:
            offset = 75

    a.sety(top_line + offset)
    a.setx(columns[randPos])


arrows = []
for m in range(0,6):
    arrows.append(turtle.Turtle())
    arrows[m].shape("triangle")
    arrows[m].speed(0)
    arrows[m].up()
    resetArrow(arrows[m])


def arrowsFall():
    global score, ice_size
    for a in arrows:
        if a.ycor() > bottom_line-25:
            a.sety(a.ycor()-speed)
        else:
            resetArrow(a)
            score -=1
            ice_size+=1
            updateScore("red")


#key presses

# Check if there are any arrows in the box of the key that was pressed:
def checkBox(c):
  # Our lists have info about the arrows in this order: Up, Down, Left, Right
  # C is the index number of the arrow key that was pressed (Up = 0, Down = 1, Left = 2, Right = 3 )
  global score, ice_size, speed
  correct = False
  # We have to go through all the arrows to check if any were in the box when their key was pressed
  for a in arrows:
    if a.ycor() < bottom_line+50:#if the arrow is in the box
      # columns is the list with the x-coordinates of each column
      if a.xcor() == columns[c]: #if the arrow is in the column we are looking for
        resetArrow(a)#reset the arrow
        score = score + 10 #score points
        ice_size -= 1 #the ice gets chiselled away
        # If all the ice is gone:
        if ice_size == 0:
          ice_size = 1
          ice.ht() #hide turtle
          ice.goto(-210,top_line) #send to the top to write some text
          ice.color("hotpink")
          ice.write("YOU FREED ME!!! Now let's play on SUPER SPEED!!!", font=("Arial", 12, "bold"))
          speed = 20 #super speed mode

        correct = True #they pressed the right key!
        updateScore("yellowgreen") #score is green when they get a point
  if not correct: #if there were now arrows of the key they pressed in the box...
    score = score - 2 #lose points
    ice_size += 2 #ice grows
    updateScore("maroon") #update score in maroon


# Connect the check function to each arrow key
sc.onkey(lambda:checkBox(0), 'Up')
sc.onkey(lambda:checkBox(1), 'Down')
sc.onkey(lambda:checkBox(2), 'Left')
sc.onkey(lambda:checkBox(3), 'Right')
# Lambda lets us send arguments to the function.


#score code
sk = turtle.Turtle()
sk.speed(0)
sk.up()
sk.ht()
sk.goto(columns[1]-25,bottom_line-100)

score = 0

def updateScore(color):
    sk.clear()
    sk.color(color)
    sk.write("Score: "+str(score), font =("Arial",24,"bold"))

updateScore("green")
        
boxes()

sc.listen()
while True:
    time.sleep(0.1)
    arrowsFall()
    ice.turtlesize(ice_size)
    sc.update()

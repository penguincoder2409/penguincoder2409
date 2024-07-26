import turtle, random, time

sc = turtle.Screen()
size = 250
sc.setup(size*2,size*2)

backgrounds = ["image1.gif","image2.gif","image3.gif"]
items = ["Darth Vader LE.gif","catfish.gif","star wars cat.gif"]
itemNames = ["Darth Vader LE","catfish","star wars cat"]
itemSizes = [30,30,30]

images = backgrounds + items


for image in images:
    sc.addshape(image)

hidden=turtle.Turtle()
hidden.speed(0)
hidden.up()

hidden.x=0
hidden.y=0
level=0
def start_round():
    sc.bgpic(backgrounds[level])
    hidden.shape(items[level])
    hidden.x=random.randint(-150,150)
    hidden.y=random.randint(-150,150)
    hidden.goto(hidden.x,hidden.y)
    print(f"Find the {itemNames[level]}!")
    countdown()

    
def click(mouseX, mouseY):
    global passedRound, level
    hitbox=itemSizes[level]
    
    if mouseX <= hidden.x + hitbox and mouseX >=hidden.x - hitbox and  (mouseY <= hidden.y + hitbox and mouseY >= hidden.y-hitbox):
        print("you found it")
        passedRound=True
        level += 1
        level = level%len(items)
        if not end:
            start_round()
    else:
        print("Nope. that's not it buddy. you suck!")

sc.onclick(click)
found = turtle.Turtle()
found.ht()
found.speed(0)
found.color("red")
found.pensize(5)

end=False

def gameover():
    global end
    end=True
    found.up()
    found.goto(hidden.x, hidden.y-itemSizes[level])
    found.down()
    found.circle(itemSizes[level])

timer=turtle.Turtle()
timer.ht()
timer.up()
timer.goto(0, size-50)

timerBG=turtle.Turtle()
timerBG.up()
timerBG.color("white")
timerBG.speed(0)
timerBG.goto(0, size-35)
timerBG.shape("square")
timerBG.turtlesize(2)

limit = 15

def countdown():
    global passedRound
    passedRound=False
    timerBG.stamp()
    start=time.time()
    while(time.time()-start)<limit:
        timePassed=(time.time()-start)
        secondsLeft=int(limit-timePassed)
        timer.write(secondsLeft, align="center",font=("courier",15,"normal"))
        newSecondsLeft=limit-(time.time()-start)
        if secondsLeft>newSecondsLeft:
            timer.clear()
    if not passedRound:
          gameover()

start_round()



















    


    
















































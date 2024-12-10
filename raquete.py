import turtle as t
name1=input(" P1-> entre your name :")
name2=input(" P2-> entre your name :")
my_scren=t.Screen()
my_scren.title("jmlahiti gaming:")
my_scren.setup(800,600)
my_scren.tracer(0)
my_scren.colormode(255)
my_scren.bgcolor((33, 47, 60))

##########
bale=t.Turtle()
bale.color("white")
bale.speed(0)
bale.shape("circle")
bale.shapesize(1,1)
bale.penup()
bale.goto(0,0)
bal_x,bal_y=1,-1
#######################
line=t.Turtle()
line.color((179, 182, 183 ))
line.shape("square")
line.shapesize(25,0.1)
line.goto(0,0)


################
#player one
player1=t.Turtle()
player1.shape("square")
player1.speed(0)
player1.shapesize(6.2,1.1)
player1.color("red")
player1.penup()
player1.goto(-355,0)
################
#player two
player2=t.Turtle()
player2.shape("square")
player2.speed(0)
player2.shapesize(6.2,1.1)
player2.color("blue")
player2.penup()
player2.goto(355,0)
##################
#score
score=t.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.goto(0,270)
score.write(f"{name1}: 0 | {name2}: 0" , align="center", font=("courier" ,14, "normal"))
score.hideturtle()
p1,p2=0,0
##########direction
step=30
def up_player1():
    if player1.ycor()<300 :
        player1.sety(player1.ycor()+step)
def down_player1():
    if player1.ycor()>-300:
        player1.sety(player1.ycor()-step)
  

##p2
def up_player2():
    if player2.ycor()<300 :
        player2.sety(player2.ycor()+step)
def down_player2():
    if player2.ycor()>-300 :
        player2.sety(player2.ycor()-step)
##get user input
my_scren.listen()
my_scren.onkeypress(up_player1,"w")
my_scren.onkeypress(down_player1,"s")
my_scren.onkeypress(up_player2,"Up")
my_scren.onkeypress(down_player2,"Down")


#####gaime logic loop#######

while True:

    my_scren.update()
    bale.setx(bale.xcor()+bal_x)
    bale.sety(bale.ycor()+bal_y)

    if (bale.ycor() > 290 or bale.ycor() < -290):
        bal_y *= -1
##########
    if bale.xcor() > -355 and bale.xcor() < -350 and  bale.ycor() < (player1.ycor()+75) and bale.ycor()>(player1.ycor()-75):
       
        bal_x *= -1

    if bale.xcor() > 350 and bale.xcor() < 355 and  bale.ycor() < (player2.ycor()+75) and bale.ycor()>(player2.ycor()-75):
        
        bal_x *= -1
    
    if bale.xcor()>385 :
        bale.goto(0,0)
        bal_x *= -1
        score.clear()
        p1 += 1
        score.write(f"{name1}: {p1} | {name2}: {p2}", align="center", font=("courier",14,"normal"))
    
    if bale.xcor()<-385 :
        bale.goto(0,0)
        bal_x *= -1
        score.clear()
        p2 += 1
        score.write(f"{name1}: {p1} | {name2}: {p2}", align="center", font=("courier",14,"normal"))
    
### pour savoir le gagnant  par la couleur####
    if p1>p2:
        bale.color("red")
    elif p1<p2:
        bale.color("blue")
    else:
        bale.color("white")


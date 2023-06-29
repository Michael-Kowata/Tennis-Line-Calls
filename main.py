#About the program
'''
In tennis, line calls are used to determine if a ball is in or out. Tennis can either be played singles or doubles. This program will help the user understand when to call a ball in or out based on the location and the type of tennis match, by playing a game with the user.

The inner line is the singles sideline, while the outer line is the doubles sideline. When the ball is on the line it is considered in. 
'''

#import statements
import turtle as trtl
import random as rand 
import time

#Game configuration
colors=["red", "yellow", "orange", "green", "blue"]
times=[0.25, 0.50, 0.75, 1, 1.25, 1.50, 1.75, 2]
pts=0

#Initailize turtles 
tennis_ball=trtl.Turtle()
tennis_ball.pensize(5)
tennis_ball.shape("circle")

court_drawer=trtl.Turtle()
court_drawer.pensize(10)

#Functions 
def doubles_line():
  court_drawer.penup()
  court_drawer.goto(-75,-200)
  court_drawer.pendown()
  for i in range (2):
    court_drawer.penup()
    court_drawer.forward(200)
    court_drawer.pendown()
    court_drawer.left(90)
    court_drawer.forward(400)
    court_drawer.left(90)
    
def singles_line():
  court_drawer.penup()
  court_drawer.goto(-30,-200)
  court_drawer.pendown()
  for i in range (2):
    court_drawer.penup()
    court_drawer.forward(200)
    court_drawer.pendown()
    court_drawer.left(90)
    court_drawer.forward(400)
    court_drawer.left(90)

def move_ball():
  tennis_ball.penup()
  x=rand.randint(-100,100)
  y=rand.randint(-100,100)
  tennis_ball.goto(x,y)

#s is the parameter for whether the game is singles or doubles
def game_on(s):
  global pts
  global question
  #function will ask 3 questions regarding the ball's location 
  for i in range(3):
    move_ball()
    tennis_ball.fillcolor(rand.choice(colors))
    if (s==1): 
      time.sleep(rand.choice(times))
      tennis_ball.hideturtle()
      print("Game is singles")
      question=input("Is the ball in or out? ")
      if (question=="in"):
        if (tennis_ball.xcor()>=-25 or tennis_ball.xcor()<=120):
          pts=pts+1
        else:
          pts=pts-1
      elif(question=="out"):
        if (tennis_ball.xcor()<=-25 or tennis_ball.xcor()>=120):
          pts=pts+1
        else:
          pts=pts-1
      tennis_ball.showturtle()
    elif (s==2):
      time.sleep(rand.choice(times))
      tennis_ball.hideturtle()
      print("Game is doubles")
      question=input("Is the ball in or out? ")
      if (question=="in"):
        if (tennis_ball.xcor()>=-65 or tennis_ball.xcor()<=160):
          pts=pts+1
        else:
          pts=pts-1
      elif (question=="out"):
        if (tennis_ball.xcor()<=-65 or tennis_ball.xcor()>=160):
          pts=pts+1
        else:
          pts=pts-1
      tennis_ball.showturtle()

#Events 
start=input("Enter 1 to start the game: ")
singles_line()
doubles_line()
if start=="1":
  game_on(1)
  game_on(2)
  print("total correctly called:",pts)

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)
snek=Snake()
food=Food()
Score=Scoreboard()
screen.listen()
screen.onkey(snek.up,"Up")
screen.onkey(snek.up,"w")
screen.onkey(snek.down,"Down")
screen.onkey(snek.down,"s")
screen.onkey(snek.left,"Left")
screen.onkey(snek.left,"a")
screen.onkey(snek.right,"Right")
screen.onkey(snek.right,"d")
gameOver=Turtle()
gameOver.color("white")
gameOver.hideturtle()
gameOn=True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snek.move()
    if snek.segs[0].distance(food)<15:
        food.refresh()
        Score.plus()
        snek.extend()
    if snek.segs[0].xcor()>285 or snek.segs[0].xcor()<-285 or snek.segs[0].ycor()>285 or snek.segs[0].ycor()<-285:
        gameOver.write("GAME OVER",align="center",font=("Arial",25,"normal"))
        gameOn=False
    for seg in snek.segs:
        if seg==snek.segs[0]:
            pass
        elif snek.segs[0].distance(seg)<5:
            gameOver.write("GAME OVER",align="center",font=("Arial",25,"normal"))
            gameOn=False
            
screen.exitonclick()
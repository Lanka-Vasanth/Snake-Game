from turtle import Turtle
startpos=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segs=[]
        self.create_snake()

    def create_snake(self):
        for pos in startpos:
            newseg=Turtle()
            newseg.penup()
            newseg.shape("square")
            newseg.color("white")
            newseg.setpos(pos)
            self.segs.append(newseg)    

    def move(self):
        for i in range(len(self.segs)-1,0,-1):
            new_x=self.segs[i-1].xcor()
            new_y=self.segs[i-1].ycor()
            self.segs[i].goto(new_x,new_y)
        self.segs[0].forward(20)      
    
    def extend(self):
        newseg=Turtle()
        newseg.penup()
        newseg.shape("square")
        newseg.color("white")
        newseg.setpos(self.segs[-1].xcor(),self.segs[-1].ycor())
        self.segs.append(newseg)
    def up(self):
        if self.segs[0].heading()!=DOWN:
            self.segs[0].setheading(UP)
    def down(self):
        if self.segs[0].heading()!=UP:
            self.segs[0].setheading(DOWN)
    def left(self):
        if self.segs[0].heading()!=RIGHT:
            self.segs[0].setheading(LEFT)
    def right(self):
        if self.segs[0].heading()!=LEFT:
            self.segs[0].setheading(RIGHT)
    # while gameOn:
    #     screen.update()
    #     time.sleep(0.166)
    #     for i in range(len(segs)-1,0,-1):
    #         segs[i].goto(segs[i-1].pos())

    #     segs[0].forward(20)
    #     segs[0].left(90)
    # screen.exitonclick()
    # def move():
    #     snake.forward(10)
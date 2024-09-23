import turtle

wn = turtle.Screen()
wn.title('uler')
wn.bgcolor('green')
wn.setup(widht=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'up'

def go_up():
    head.direction = 'up'
def go_down():
    head.direcion = 'down'
def go_right():
    head.direction = 'right'
def go_left():
    head.direction = 'left'
    
def move():
    wn.listen()
    wn.onkeypress(go_up,'w')
    wn.onkeypress(go_down,'s')
    wn.onkeypress(go_right,'d')
    wn.onkeypress(go_left,'a')


    









while True:
    wn.update()


wn.mainloop()
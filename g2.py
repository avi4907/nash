import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 1000

C=Actor('chick',(100,100))
W=Actor('bear',(400,400))
def draw():
    screen.blit('bg', pos=(0,0))
    screen.fill('white')
    C.draw()
    W.draw()
    #screen.draw.text('A chicken story', (10,WIDTH//2), 'red')
def update():
    if keyboard.W:
        C.y -=3
    elif keyboard.S:
        C.y +=3
    elif keyboard.A:
        C.x -=3
    elif keyboard.D:
        C.x +=3
pgzrun.go()
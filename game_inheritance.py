from random import randint as ri
from turtle import speed
import pgzrun

WIDTH=600
HEIGHT=400

class Player(Actor):

    def __init__(self, image, speed = 5):
        pos = ri(0, WIDTH), ri(0, HEIGHT)
        super().__init__(image, pos)
        self.speed = speed

    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.angle = +10
            self.x -= self.speed
        elif keyboard.D:
            self.x += self.speed
            self.angle = -10
        elif keyboard.E:
            self.x += self.speed
            self.y -= self.speedb   
        else:
            self.angle = 0

    def check_boundary(self):
        pass
p=Player('ironman')  

def draw():
    screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundary()

pgzrun.go()
import turtle

WIDTH = 500
HEIGHT = 500
playground = turtle.Screen()
playground.setup(WIDTH, HEIGHT)
player = turtle.Turtle()
step = 50
angle = 30

player.forward(step)

player.right(angle)
player.forward(step * 0.8)

import turtle
import random

COLORS = ["black", "red", "yellow", "green", "cyan", "brown", "blue", "pink", "orange", "violet"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric. Try again !")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range: 2 - 10. Try again !")

def game_init(colors, racers):
    WIDTH, HEIGHT = 500, 500
    playground = turtle.Screen()
    playground.title("Window")
    playground.setup(WIDTH, HEIGHT)
    
    print(colors)
    random.shuffle(colors)
    player_colors = colors[:racers]
    print(f"Debug: {player_colors}")
    print(player_colors)

def game_loop():
    player = turtle.Turtle()
    player.forward(100)

def program(colors):
    racers = get_number_of_racers()
    print(racers)
    game_init(colors, racers)
    # game_loop()

if __name__ == "__main__":
    program(COLORS)
    print("GAME OVER")


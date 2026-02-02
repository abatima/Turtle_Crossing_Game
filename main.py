import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
all_cars = []
game_is_on = True
car_speed = 0.1

screen.listen()
screen.onkey(player.go_forward,"Up")

while game_is_on:
    time.sleep(car_speed)
    screen.update()
    if random.randint(1, 5) == 1:
        car = CarManager()
        all_cars.append(car)

    for car in all_cars:
        car.move()
        if car.xcor() < -420:
            car.hideturtle()
            all_cars.remove(car)
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 300:
        scoreboard.increase_score()
        car_speed *= 0.9
        player.reset_position()

screen.exitonclick()


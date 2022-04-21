from turtle import Turtle
import matplotlib.pyplot as plt
import numpy as np

ACOEF = 1.1                         # Coefficient for accelerating and decelerating of the hunter

def init_hunter(x=-400, y=300):
    """ Initializes the hunter object """
    hunter = Turtle()
    hunter.penup()
    hunter.setposition(x, y)
    hunter.color("green")
    hunter.speed(0)
    hunter.pendown()

    hunter.setheading(0)

    return hunter

def init_dog(x=-400, y=-300):
    """ Initializes the dog object """
    dog = Turtle()
    dog.penup()
    dog.setposition(x, y)
    dog.color("red")
    dog.speed(0)
    dog.pendown()

    return dog

def chasing_curve_straight(hunter_velocity=2, dog_velocity=5, dt=1):
    """ Straight motion of the hunter """
    hunter = init_hunter()
    dog = init_dog()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

def chasing_curve_circle(hunter_velocity=2, dog_velocity=5, hunter_turn_velocity=1, dt=1):
    """ Circular motion of the hunter """
    hunter = init_hunter(x=0)
    dog = init_dog()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        hunter.right(hunter_turn_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

def chasing_curve_events(hunter_velocity=2, dog_velocity=5, dt=1):
    """ Chasing curve with interactive hunter 
        (left key - turn left, right key - turn right, up key - accelerate, down key - decelerate)
    """
    hunter = init_hunter()
    dog = init_dog()

    def right_event():
        hunter.right(3)

    def left_event():
        hunter.left(3)

    def up_event():
        nonlocal hunter_velocity
        hunter_velocity *= ACOEF

    def down_event():
        nonlocal hunter_velocity
        hunter_velocity /= ACOEF

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)                          # This speeds up the animation
    hunter_screen.onkeypress(right_event, "Right")
    hunter_screen.onkeypress(left_event, "Left")
    hunter_screen.onkeypress(up_event, "Up")
    hunter_screen.onkeypress(down_event, "Down")
    hunter_screen.listen()                          # Necessary for the screen to listen to the events

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)
        dog.setheading(dog.towards(hunter))
        dog.forward(dog_velocity * dt)

    input()

def chasing_curve_acceleration(hunter_velocity=2, dog_velocity=5, dt=1):
    """ Chasing curve with interactive hunter 
        (left key - turn left, right key - turn right, up key - accelerate, down key - decelerate)
    """
    hunter = init_hunter()
    dog = init_dog()

    def right_event():
        hunter.right(3)

    def left_event():
        hunter.left(3)

    def up_event():
        nonlocal hunter_velocity
        hunter_velocity *= ACOEF

    def down_event():
        nonlocal hunter_velocity
        hunter_velocity /= ACOEF

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(0)
    hunter_screen.onkeypress(right_event, "Right")
    hunter_screen.onkeypress(left_event, "Left")
    hunter_screen.onkeypress(up_event, "Up")
    hunter_screen.onkeypress(down_event, "Down")
    hunter_screen.listen()
   
    dog.setheading(dog.towards(hunter))

    A = []
    T = []
    t = 0

    plt.ion()

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(hunter_velocity * dt)

        phi1 = dog.heading()
        phi2 = dog.towards(hunter)

        dphi = phi2 - phi1    
        if dphi > 180:
            dphi -= 360    
        if dphi <- 180:
            dphi += 360

        dphi *= np.pi / 180             # Convert degrees to radians
        a = dog_velocity * dphi / dt 

        dog.setheading(phi2)
        dog.forward(dog_velocity * dt)

        A.append(a)
        T.append(t)

        plt.clf()
        plt.plot(T, A, color="black")
        plt.xlabel("$t\ [s]$")
        plt.ylabel("$a\ [ms^{-2}]$")    
        plt.scatter(t, a, color="black")

        t += dt

    input()

#chasing_curve_straight()
#chasing_curve_circle(hunter_velocity=8, hunter_turn_velocity=2)

chasing_curve_acceleration()

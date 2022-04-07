from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_up(60)
tello.move_left(60)
tello.move_right(60)
tello.rotate_counter_clockwise(360)
tello.flip_forward()
tello.move_forward(60)
tello.move_back(60)
sleep(10)


tello.land()
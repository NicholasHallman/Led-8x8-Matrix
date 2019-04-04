from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image
from copy import deepcopy

from kbhit import KBHit

import time
import random
import sys

INTERVAL = 1/10

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)  

kb = KBHit()

snake = [(4,4)]
direction = 0 # 0 up, 1 right, 2 down, 3 left
apple = (0,0)
released = True


def draw():
    with canvas(device) as draw:
        draw.point(snake,fill=128)
        draw.point(apple,fill=128)

def moveSnake():
    kb.kbhit()
    direction = kb.getarrow()

    last = (-1,-1)    
    if direction == 0:
        for point in snake:
            if point != last:
                last = point
                point[1] += 1
            else:
                last = point

    elif direction == 1:
        for point in snake:
            if point != last:
                last = point
                point[0] += 1
            else:
                last = point
    elif direction == 2:
        for point in snake:
            if point != last:
                last = point
                point[1] -= 1
            else:
                last = point
    elif direction == 3:
        for point in snake:
            if point != last:
                last = point
                point[0] -= 1
            else:
                last = point



def placeApple():
    apple = (random.randint(0,8), random.randint(0,8))
    collide = True
    while collide:
        collide = False
        for point in snake:
            if apple == point:
                collide = True
                apple = (random.randint(0,8), random.randint(0,8))

def checkRules():
    if snake[0][0] < 0 or snake[0][0] > 7 or snake[0][1] < 0 or snake[0][1] > 7:
        #snake out of bounds
        sys.exit()
    if snake[0] == apple:
        placeApple()
        snake.append(deepcopy(snake[-1]))

def gameLoop():
    while True:
        moveSnake()
        checkRules()
        draw()
        time.sleep(INTERVAL)

gameLoop()
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image

import pygame
from pygame.locals import *
from copy import deepcopy

import time
import random
import sys

INTERVAL = 1/10

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)    

snake = []
direction = 0 # 0 up, 1 right, 2 down, 3 left
apple = (0,0)

pygame.init()


def draw():
    with canvas(device) as draw:
        draw.point(snake,fill=128)
        draw.point(apple,fill=128)

def moveSnake():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 0
            elif event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_DOWN:
                direction = 2
            elif event.key == pygame.K_LEFT:
                direction = 3

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
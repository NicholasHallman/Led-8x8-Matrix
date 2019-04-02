from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image

import time

INTERVAL = 1000/60

row = 0

while True:
    with canvas(max7219) as draw:
        draw.line([(row,0),(row,7)],None)
        row += 1
        if(row == 8):
            row = 0
        time.sleep(INTERVAL)

    
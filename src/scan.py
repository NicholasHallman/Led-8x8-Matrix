from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image

import time

INTERVAL = 1/10

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

row = 0

while True:
    with canvas(device) as draw:
        draw.line([(row,0),(row,7)],fill=128, width=1,joint=None )
        row += 1
        if(row == 8):
            row = 0
        time.sleep(INTERVAL)

    
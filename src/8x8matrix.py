from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

def set_matrix(char):

    with canvas(device) as draw:
        legacy.text(draw, (0,0), char, fill="white", 
        font=proportional(CP437_FONT) )
    
    return None

try:
    while True:
        input = input("Input a char or number: ")
        set_matrix(input)
except KeyboardInterrupt:
    pass
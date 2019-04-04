# Led 8x8 Matrix

## Resources

How can you install Luma for the 8x8 LED Matrix?
https://luma-led-matrix.readthedocs.io/en/latest/install.html

How can you use luma with the 8x8? And is there a good reference?
https://luma-led-matrix.readthedocs.io/en/latest/python-usage.html#x8-led-matrices

Is there a datasheet for the MAX7219 used y the matrix?
https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf

This project is for RaspberryPi but is there Arduino code available?
https://gist.github.com/nrdobie/8193350

Is Luma open source? Where can I find more exmaples?
https://github.com/rm-hull/luma.led_matrix

## Instructions

Install Pip
```bash
sudo apt-get install pip
```

Install Luma
```bash
pip install luma.core
pip install luma.led_matrix
```

Using Luma

```python
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

with canvas(device) as draw:
        legacy.text(draw, (0,0), "Your string here", fill="white", 
        font=proportional(CP437_FONT) )
    
    return None
```
## Diagram

![Block Diagram](https://raw.githubusercontent.com/NicholasHallman/Led-8x8-Matrix/master/exploration%20diagram.png)

## Video Demonstration

[![Exploration Demo](http://img.youtube.com/vi/l2-7ydX_DR0/0.jpg)](http://www.youtube.com/watch?v=l2-7ydX_DR0)

## Challenges

    Familiarity with pip and other package managers was required to do this project. To add, Luma and its device packages abstract away the complications of controling the MAX7219. However, it prevents the programmer from fully understanding what the library is doing, which is usefull in many cases. Pillow is also a large component of the Luma library. People who are not already familliar with pillow will have difficulty understanding how to control the 8x8 matrix.

## Issues
    The 8x8 matrix on its own is small which limits the scope of any project. This limitation makes drawing multiple characters and numbers impossible and only allows for primitive praphics of a single color.
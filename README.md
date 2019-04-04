# Led 8x8 Matrix

# Resources

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

[![Block Diagram]()]
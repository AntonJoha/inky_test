import os
from PIL import Image
from inky import auto
from get_inky import get_inky



def _take_screenshot():
    os.system("chromium \
    --headless \
    --disable-gpu \
    -window-size=1000,1500 \
    --screenshot  \
    https://www.smhi.se/vader/prognoser/ortsprognoser/q/Kristinehamn/2699282 \
    ")


def _open_image():
    return Image.open("screenshot.png")

def _get_crop_dimensions():
    return (60, 611, 806, 1161)

def _get_image():
    _take_screenshot()
    image = _open_image()
    copy = image.crop(_get_crop_dimensions())
    image.close()
    os.system("rm screenshot.png")
    return copy

def get_weather_image():
    inky = get_inky()
    image = _get_image()
    image_resized = image.resize(inky.resolution)
    return image_resized

   

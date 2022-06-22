from extract import set_texttv
import time
from test import image_yo
from try_inky import set_screen
from raspcheck import on_pi


while True:
    try:
        set_screen(image_yo)
        if on_pi():
            time.sleep(60*2)
        else:
            time.sleep(1)
    except:
        print("Error")
        time.sleep(1)
        pass

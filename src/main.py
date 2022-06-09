from extract import set_texttv
import time
from try_inky import set_screen
import os
from raspcheck import on_pi


while True:
    try:
        set_screen(set_texttv)
        if on_pi():
            time.sleep(60*2)
    except:
        print("Failed")

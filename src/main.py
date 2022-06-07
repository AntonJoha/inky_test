from extract import set_texttv
import time
from try_inky import set_screen

while True:
    try:
        set_screen(set_texttv)
        time.sleep(60*2)
    except:
        print("Failed")

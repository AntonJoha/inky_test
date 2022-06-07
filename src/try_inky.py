import hitherdither
from inky import auto
from PIL import Image



def set_screen(fun):
    
    inky = auto(ask_user=True, verbose=True)
    inky.set_image(fun())
    inky.show()


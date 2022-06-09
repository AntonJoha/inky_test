import hitherdither
from inky import auto
from PIL import Image
from get_inky import get_inky,new_inky
from raspcheck import on_pi

def _dither_image(img):
    inky = get_inky()
    thresholds = [64, 64, 64]  # Threshold for snapping colours, I guess?
    palette = hitherdither.palette.Palette(inky._palette_blend(0.8, dtype='uint24'))
    return hitherdither.ordered.bayer.bayer_dithering(image_resized, palette, thresholds, order=8)


def set_screen(fun):
    
    inky = get_inky()
    
    image = fun()
    
    if on_pi():
        image = _dither_image(image)

    inky.set_image(image)
    inky.show()
    
    #If it's a Mock
    if on_pi() == False:
        inky.wait_for_window_close()
        new_inky()

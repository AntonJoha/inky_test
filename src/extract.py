import urllib.request
import io
import urllib.parse
import base64
import sys

import hitherdither
from inky import auto
from PIL import Image



def _get_image(page):
    url = "https://www.svt.se/text-tv/" + str(page)
    f = urllib.request.urlopen(url)
    site = f.read().decode('ISO-8859-1')


    pos = site.index("data:image/gif;base64,", 0 , len(site)) + 22
    newpos = site.index("\"", pos, len(site))

    to_decode = site[pos:newpos + 1]

    to_decode = site[pos:newpos + 1]
    fh = io.BytesIO()
    fh.write(base64.b64decode(to_decode))
    return fh

def set_page(page):

    if (page < 100) or( page > 999):
        page = 100

    inky = auto(ask_user=True, verbose=True)
    thresholds = [64, 64, 64]  # Threshold for snapping colours, I guess?

    palette = hitherdither.palette.Palette(inky._palette_blend(0.8, dtype='uint24'))

    image = Image.open(_get_image(page)).convert("RGB")
    image_resized = image.resize(inky.resolution)

    image_dithered = hitherdither.ordered.bayer.bayer_dithering(image_resized, palette, thresholds, order=8)

    inky.set_image(image_resized)
    inky.show()

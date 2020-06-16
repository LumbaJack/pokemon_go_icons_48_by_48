#!/usr/bin/python
import os

from PIL import Image

path = "./pokemon_icons/"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        location = path + item

        if os.path.isfile(location):
            im = Image.open(location)
            imResize = im.resize((72, 72), Image.ANTIALIAS)
            imResize.save(location, 'PNG', quality=90)


resize()

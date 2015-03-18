#!/usr/bin/env python3
# -*- coding: utf8 -*-


# http://www.pythonchallenge.com/pc/return/5808.html
# odd even

from PIL import Image


def solve_it():
    img = Image.open('11.jpg')
    sub = Image.new('RGB', (img.size[0]//2, img.size[1]))
    for i in range(sub.size[0]):
        for j in range(sub.size[1]):
            sub.putpixel( (i,j), img.getpixel( (i*2+j%2, j) ) )
    sub.show()
    return input('Your answer: ')
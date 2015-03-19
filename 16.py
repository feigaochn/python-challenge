#!/usr/bin/env python3
# -*- coding: utf8 -*-

url = 'http://www.pythonchallenge.com/pc/return/mozart.html'

# title: let me get this straight

from PIL import Image


def solve_it():
    img = Image.open('16.gif')
    w, h = img.size

    ip = img.getpixel

    # notice some pink colored bars of length 5

    color = [ip((c, 0)) for c in range(w - 5) if len(set(ip((c + i, 0)) for i in range(5))) == 1][0]
    # color = 195

    bars = []
    for r in range(h):
        for c in range(w - 5):
            if ip((c, r)) == ip((c + 4, r)) == color:
                bars.append((c, r))
    # print(bars)
    # note that each line has only one bar

    # title suggest put this straight
    out = Image.new(img.mode, img.size)
    for r in range(h):
        for c in range(w):
            out.putpixel((c, r), ip(((c + bars[r][0]) % w, r)))
    out.show()

    return input('what you see? ')
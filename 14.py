#!/usr/bin/env python3
# -*- coding: utf8 -*-

url = 'http://www.pythonchallenge.com/pc/return/italy.html'


def solve_it():
    # from solver import get_bytes
    # data = get_bytes('return/wire.png')
    # with open('14.png', 'wb') as f:
    #   f.write(data)

    from PIL import Image

    img = Image.open('14.png')
    sq = Image.new(img.mode, (100, 100))

    w, h, idx = 0, 0, 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for side in range(99, 0, -2):
        for n, d in enumerate(dirs):
            for i in range(side):
                try:
                    sq.putpixel((w, h), img.getpixel((idx, 0)))
                except IndexError:
                    print(w, h, idx)
                w, h, idx = w + d[0], h + d[1], idx + 1
            print(w, h, idx)
        w, h = w + 1, h + 1
    sq.show()
    # the image is a 'cat'
    # Open 'cat.html', you know the name of cat is 'uzi'

    return 'uzi'
#!/usr/bin/env python3
# -*- coding: utf8 -*-

from PIL import Image


def solve_it():
    img = Image.open('7.png')
    region = img.crop((0, 45, 625, 50))
    data = list(region.getdata())[:region.size[0]]
    pixels = [data[i][0] for i in range(len(data)-1) if data[i] != data[i+1] and data[i][0] == data[i][1]]

    hint = ''.join(chr(i) for i in pixels)
    # print(hint)
    # 'smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]'

    question = [105, 10, 16, 101, 103, 14, 105, 16, 121]
    answer = ''.join(chr(i) if i > 100 else chr(i+100) for i in question)
    return answer
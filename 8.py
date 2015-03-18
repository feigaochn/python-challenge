#!/usr/bin/env python3
# -*- coding: utf8 -*-

# http://www.pythonchallenge.com/pc/def/integrity.html


def solve_it():
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    import bz2

    print('username :' + bz2.decompress(un).decode())
    print('password :' + bz2.decompress(pw).decode())

    # click the insect to go to
    # http://www.pythonchallenge.com/pc/return/good.html
    # with above username and password
    return None
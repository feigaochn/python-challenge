#!/usr/bin/env python3
# -*- coding: utf8 -*-

# http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request
import pickle

def solve_it():
    # title: peak hell
    # content: pronounce it
    # hint: <!-- peak hell sounds familiar ? -->

    peakhell = '5.txt' # 'http://www.pythonchallenge.com/pc/def/banner.p'

    data = pickle.load(open(peakhell, 'rb'))
    lines = [''.join(ch * num for ch, num in line) for line in data]
    print('\n'.join(lines))

    return 'channel'

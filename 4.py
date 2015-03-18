#!/usr/bin/env python3
# -*- coding: utf8 -*-

# http://www.pythonchallenge.com/pc/def/linkedlist.php


def solve_it():
    URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
    values = [
        # 12345,
        # 16044/2,
        63579]
    import urllib.request

    while False:
        try:
            line = urllib.request.urlopen(URL.format(values[-1])).readline().decode().split()
            print(' '.join(line))
            values.append(int(line[-1]))
        except Exception as e:
            line[-1] = int(input('start with '))
            values.append(int(line[-1]))
        print(values[-1])

    return 'peak'


if __name__ == '__main__':
    solve_it()
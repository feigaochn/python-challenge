#!/usr/bin/env python3
# -*- coding: utf8 -*-


url = 'http://www.pythonchallenge.com/pc/return/uzi.html'


def solve_it():
    # title: whom?
    # hint in comment:
    # <!-- he ain't the youngest, he is the second -->
    # <!-- buy flowers for tomorrow -->

    # 1??6 Jan 26 is Monday
    # Jan 27 is important day
    # this is a leap year
    import datetime
    for y in range(99, 0, -1):
        yy = int('1{}6'.format(y))
        if 0 == datetime.date(yy, 1, 26).weekday() and yy % 4 == 0:
            print(yy)
    # 1976, 1756, ...

    # wiki Jan 27 tells this is birthday "Wolfgang Amadeus Mozart, Austrian pianist and composer"

    return 'mozart'
#!/usr/bin/env python3
# -*- coding: utf8 -*-

# http://www.pythonchallenge.com/pc/return/bull.html

def solve_it():
    a = [1, 11, 21, 1211, 111221]
    # len(a[30])

    a = [str(x) for x in a]

    a = ['1']

    while len(a) < 31:
        last = a[-1]
        answer = ''
        while last:
            remain = last.lstrip(last[0])
            answer += str(len(last) - len(remain)) + last[0]
            last = remain
        a.append(answer)

    print(a)
    return len(a[30])
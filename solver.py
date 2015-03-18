#!/usr/bin/env python3
# -*- coding: utf8 -*-

__author__ = 'feigao'

target = "http://www.pythonchallenge.com/pc/def/{}.html"

import sys

def main():
    if len(sys.argv) > 1:
        pid = sys.argv[1]
    else:
        pid = input('Input Problem ID: ')

    try:
        pkg = __import__(pid)
        if not hasattr(pkg, 'solve_it'):
            print('the solve_it() function was not found in "{}.py."'.format(pid))
            quit()
    except ImportError:
        print('"{}.py" was not found in the path.'.format(pid))
        quit()

    answer = pkg.solve_it()
    print('Answer: {}\nURL: {}\n'.format(answer, target.format(answer)))

if __name__ == '__main__':
    main()
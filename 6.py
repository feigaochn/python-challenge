#!/usr/bin/env python3
# -*- coding: utf8 -*-

import zipfile


def solve_it():
    zip = zipfile.ZipFile(open('6.zip', 'rb'))
    val = 90052
    commets = []

    while True:
        fn = str(val) + '.txt'
        row = zip.read(fn).decode()
        print(fn + row)
        commets.append(zip.getinfo(fn).comment.decode())
        try:
            val = int(row.split()[-1])
        except ValueError:
            break

    print(''.join(commets))
    # 'HOCKEY' in ascii-art

    # http://www.pythonchallenge.com/pc/def/hockey.html
    # it's in the air. look at the letters

    return 'oxygen'


def main():
    pass


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf8 -*-

__author__ = 'feigao'

url_prefix = 'http://www.pythonchallenge.com/pc/{}'

import sys
import urllib.request
import urllib.parse
import base64


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

    if int(pid) <= 7:
        # p0 to p7: "http://www.pythonchallenge.com/pc/def/{}.html"
        url = url_prefix.format('def/' + answer + '.html')
    else:
        # p8 to ?: "http://www.pythonchallenge.com/pc/return/{}.html"
        url = url_prefix.format('return/' + answer + '.html')

    print('Answer: {}\nURL: {}\n'.format(answer, url))


def get_bytes(suffix):
    """
    :type suffix: str
    :rtype: bytes
    """
    url = url_prefix.format(suffix)
    req = urllib.request.Request(url)

    try:
        resp = urllib.request.urlopen(req)
    except urllib.request.HTTPError as e:
        print(e.reason)
        print(e.headers)
        if e.code == 401 and e.headers['WWW-Authenticate'].find('inflate') != -1:
            unpw = '{}:{}'.format('huge', 'file')
            print('Try as "{}"'.format(unpw))
            b64unpw = base64.encodebytes(unpw.encode()).decode().strip()
            req.add_header('Authorization', 'Basic {}'.format(b64unpw))
            resp = urllib.request.urlopen(req)
        else:
            print('Quit.')
            quit()

    return resp.read()


if __name__ == '__main__':
    main()
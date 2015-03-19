# http://www.pythonchallenge.com/pc/return/evil.html

def solve_it():
    # the image is "evil1.jpg"
    # open "evil2.jpg" show to change "jpg" to "gfx"
    # download "evil2.gfx"

    evil = open('12.gfx', 'rb').read()
    for i in range(5):
        img = open('12-%d.jpg' % i, 'wb')
        img.write(evil[i::5])
        img.close()
    # dis, pro, port, ional, ~ity~
    return 'disproportional'

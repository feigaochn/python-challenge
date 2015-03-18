# http://www.pythonchallenge.com/pc/def/map.html

clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
perm = "abcdefghijklmnopqrstuvwxyz"


def shift(s, offset=2):
    ret = ''
    for key in s:
        if key.isalpha() is False:
            ret += key
        else:
            ret += perm[(perm.find(key) + offset) % len(perm)]
    return ret


def solve_it():
    print(shift(clue, 2))
    # i hope you didnt translate it by hand. that's what computers are for.
    # doing it in by hand is inefficient and that's why this text is so long.
    # using string.maketrans() is recommended. now apply on the url."

    url = 'map'
    return shift(url)


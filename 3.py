# http://www.pythonchallenge.com/pc/def/equality.html


def solve_it():
    data = open("3.txt").read()
    lines = data.splitlines()

    import re
    answer = ''
    for line in lines:
        answer += ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', line))
    return answer

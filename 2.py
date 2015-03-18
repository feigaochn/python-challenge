# http://www.pythonchallenge.com/pc/def/ocr.html

# find rare characters in the mess below:


def solve_it():
    clue = open("2.txt").read()
    answer = ''
    for i in clue:
        if i.isalpha():
            answer += i
    return answer
    # equality

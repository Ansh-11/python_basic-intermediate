import random


def game():
    return random.randrange(10, 400)


score = game()
with open("sample.txt") as f:
    data = f.read()
    if data == "":
        hiscore = 0
    else:
        hiscore = int(data)
if hiscore < score or hiscore == "":
    with open("sample.txt", "w") as f:
        f.write(str(score))

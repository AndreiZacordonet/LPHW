
def getScript(room_name):
    file = open("ex36_dialogue.txt", encoding='UTF-8')
    data = file.read()
    file.close()
    chapters = data[data.find(room_name):]
    chapters = chapters[:chapters.find('\n#')]
    # creating a list with lines of dialogue
    return list(map(lambda l: l.split('\n'), chapters.split('\n>')[1:]))

def sleep(nr):
    i = 0
    while i < nr * 10**7 * 5:
        i += 1

def lineDisplay(line, time=1):
    for l in line:
        print(l)
    sleep(time)

def show_room():
    """Returns 'leave' if the player is done
    and 'Long Corridor' if the player advanced to the next room"""

    script = getScript('Show Room')

    lineDisplay(script[0], 1.5)
    lineDisplay(script[1], 3)
    lineDisplay(script[2], 0.7)
    lineDisplay(script[3], 0.7)
    lineDisplay(script[4])
    lineDisplay(script[5])
    lineDisplay(script[6])
    lineDisplay(script[7])

    choice = input('>')

    wrong_number = True
    while wrong_number:
        if choice in [1, "one", "One", "ONE"]:
            lineDisplay(script[8])
            lineDisplay(script[9])
            lineDisplay(script[10])
            wrong_number = False
            return 'leave'
        elif choice in [2, "two", "Two", "TWO"]:
            wrong_number = False
            return 'Long Corridor'
        else:
            print("A proper number bitte...")
            choice = input('>')


def long_corridor():
    """Return 'left' or 'right'"""

    script = getScript('Long Corridor')

    while True:
        lineDisplay(script[0], 1.5)
        lineDisplay(script[1])
        lineDisplay(script[2])
        lineDisplay(script[3], 1.5)
        lineDisplay(script[4])
        lineDisplay(script[5])

        choice = input('>')

        if choice in ['left', 'Left', 'LEFT']:
            return 'left'
        elif choice in ['right', 'Right', 'RIGHT']:
            return 'right'
        else:
            lineDisplay(script[6], 1.5)


def poneys_factory():
    """Returns 'Gandalf'"""
    script = getScript('Poneys Factory')
    lineDisplay(script[0])
    lineDisplay(script[1])
    lineDisplay(script[2], 3)

    while True:
        lineDisplay(script[3])
        choice = int(input('>'))

        if choice == 3:
            lineDisplay(script[4])
            choice = int(input('>'))

            if choice == 1:
                lineDisplay(script[5])
                choice = int(input('>'))

                if choice == 3:
                    lineDisplay(script[6])
                    choice = int(input('>'))

                    if choice == 3:
                        lineDisplay(script[8], 2)
                        return 'Gandalf'
        lineDisplay(script[7], 1.5)


def gandalf():
    """Returns 'Blosom Field'"""
    script = getScript('Gandalf')

    lineDisplay(script[0], 2)
    lineDisplay(script[1])
    lineDisplay(script[2], 1.5)

    while True:
        lineDisplay(script[3])
        choice = input('>')

        if choice == 'egg':

            while True:
                lineDisplay(script[4])
                choice = input('>')

                if 'all' in choice:

                    while True:
                        lineDisplay(script[5])
                        choice = input('>')

                        if choice == 'sponge':
                            lineDisplay(script[6])
                            return 'Blosom Field'
                        else:
                            lineDisplay(script[8])
                else:
                    lineDisplay(script[9])
        else:
            lineDisplay(script[7])


def blosom_field():
    script = getScript('Blosom Field')

    lineDisplay(script[0])
    lineDisplay(script[1])
    lineDisplay(script[2])
    lineDisplay(script[3], 2)
    lineDisplay(script[4])
    lineDisplay(script[5])

    while True:
        lineDisplay(script[6])
        choice = input('>')

        if choice == '🌻':
            lineDisplay(script[7])
            choice = input('>')

            if choice == '🌷':
                lineDisplay(script[8])
                choice = input('>')

                if choice == '🌷':
                    lineDisplay(script[9])
                    choice = input('>')

                    if choice == '🌹':
                        lineDisplay(script[10])
                        choice = input('>')

                        if choice == '💮':
                            lineDisplay(script[11])
                            return 'Fontain of Life'
        lineDisplay(script[12])


def fontain_of_life(path):
    """End of the game"""
    script = getScript('Fontain of Life')

    lineDisplay(script[0], 2)
    lineDisplay(script[1])
    lineDisplay(script[2], 2)
    if path != 'right':
        lineDisplay(script[3], 4)


def maze():
    """Returns 'Basement'"""
    script = getScript('Maze')

    lineDisplay(script[0])
    lineDisplay(script[1])
    lineDisplay(script[2])
    lineDisplay(script[3], 0.7)
    lineDisplay(script[4], 1.5)
    lineDisplay(script[5])
    lineDisplay(script[6], 6)
    lineDisplay(script[7])
    lineDisplay(script[8])
    lineDisplay(script[9])

    while True:
        choice = input('>')

        if choice == 'right, left, right, right, left, left, left, left, left, left, right, right, right, left, right':
            lineDisplay(script[10])
            return 'Basement'
        lineDisplay(script[11])


def basement():
    """Returns 'Meeting Hall'"""
    script = getScript('Basement')

    lineDisplay(script[0], 2)
    lineDisplay(script[1])
    lineDisplay(script[2], 2)
    lineDisplay(script[3])
    lineDisplay(script[4], 3)
    lineDisplay(script[5])
    lineDisplay(script[6])
    lineDisplay(script[7])

    i = 1
    while i <= 16:
        try:
            number = int(input('>'))
            if i == number:
                i += 1
            else:
                lineDisplay(script[8])
                i = 1
        except ValueError:
            lineDisplay(script[8])
            i = 1

    lineDisplay(script[9])
    return 'Meeting Hall'


def meeting_hall():
    """Returns 'Living Room'"""
    script = getScript('Meeting Hall')

    lineDisplay(script[0])
    lineDisplay(script[1])
    lineDisplay(script[2], 2)
    lineDisplay(script[3])

    strange_words = ['Trumpet', 'Symphony', 'Bass', 'Pig', 'Your', 'BS']
    while len(strange_words):
        answer = input('>')
        if answer in strange_words:
            strange_words.remove(answer)
        else:
            lineDisplay(script[4])

    lineDisplay(script[5])
    return 'Living Room'


def living_room():
    script = getScript('Living Room')

    lineDisplay(script[0])
    lineDisplay(script[1])
    lineDisplay(script[2])
    lineDisplay(script[3])
    lineDisplay(script[4], 2)
    lineDisplay(script[5])

    lineDisplay(script[6])
    answer = input('>')

    if 'all' in answer:
        lineDisplay(script[7])
        answer = input('>')

        if answer == 'sponge':
            lineDisplay(script[8])
            answer = input('>')

            if answer == 'towel':
                lineDisplay(script[11])
                return 'Fontain of Life'

    lineDisplay(script[9])
    lineDisplay(script[10])
    return 'death'

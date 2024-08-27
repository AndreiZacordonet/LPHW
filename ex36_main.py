import ex36_rooms as rooms

def main():
    next = rooms.show_room()

    if next == 'Long Corridor':
        next = rooms.long_corridor()

        if next == 'right':
            next = rooms.poneys_factory()

            if next == 'Gandalf':
                next = rooms.gandalf()

                if next == 'Blosom Field':
                    next = rooms.blosom_field()

                    if next == 'Fontain of Life':
                        rooms.fontain_of_life('right')
        elif next == 'left':
            next = rooms.maze()

            if next == 'Basement':
                next = rooms.basement()

                if next == 'Meeting Hall':
                    next = rooms.meeting_hall()

                    if next == 'Living Room':
                        next = rooms.living_room()

                        if next == 'Fontain of Life':
                            rooms.fontain_of_life('left')

main()

# print("""You enter a dark room with two doors.
# Do you go through door #1 or door #2?""")
#
# door = input("> ")
#
# if door == "1":
#     print("There's a giant bear here eating a cheese cake.")
#     print("What do you do?")
#     print("1. Take the cake.")
#     print("2. Scream at the bear.")
#
#     bear = input("> ")
#
#     if bear == "1":
#         print("The bear eats your face off. Good job!")
#     elif bear == "2":
#         print("The bear eats your legs off. Good job!")
#     else:
#         print(f"Well, doing {bear} is probably better.")
#         print("Bear runs away.")
#
# elif door == "2":
#     print("You stare into the endless abyss at Cthulhu's retina.")
#     print("1. Blueberries.")
#     print("2. Yellow jacket clothespins.")
#     print("3. Understanding revolves yelling melodies.")
#
#     insanity = input("> ")
#
#     if insanity == "1" or insanity == "2":
#         print("Your body survives powered by  a mind of jello.")
#         print("Good job!")
#     else:
#         print("The insanity rots your eyes into a pool of muck.")
#         print("Good job!")
# else:
#     print("You stumbled arount and fell on to a knife and die. Good job!")


##################
# My game ------->

print("The bear is in the chamber. Where is the bear?")

bear_location = input("(ALL CAPS)> ")

if bear_location == "IN THE CHAMBER" or bear_location == "THE CHAMBER" or bear_location == "CHAMBER":
    print("Very bag things will happen. Bye!")
else:
    print("You dind't got fooled by the bear. Huray!")
    print("There a rail splits in other 2 tracks. \nO one track to the rail is chianed 1 person.")
    print("On the other are chained 5 persons.")
    print("How old are you?")

    age = input("> ")

    if age == "18":
        print("Your are 18 years old.")
        print("Are you a boy or a girl?")

        gender = input("(ALL CAPS)> ")

        if gender == "BOY":
            print("Well done!")
        elif gender == "GIRL":
            print("Well done!")
        else:
            print("Are you an alien?")

            alien = input("(ALL CAPS)> ")

            if alien == "YES":
                print("Damn...")
            elif alien == "NO":
                print("...")
            else:
                print("I'm done...")
    else:
        print("You are not 18!")

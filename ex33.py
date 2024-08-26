

def list_builder(len, step):
    numbers = []
    for i in range(0, len, step):
        print(f"At the tip i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

list_builder(0, 1)
list_builder(2, 2)
list_builder(8, 2)
list_builder(7, 3)

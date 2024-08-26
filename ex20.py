from sys import argv

script, input_file = argv

def print_all(f):
    show_pointer(f)
    print(f.read())
    show_pointer(f)

def rewind(f):
    show_pointer(f)
    f.seek(0)
    show_pointer(f)

def show_pointer(f):
    print(f"File pointer position: {f.tell()}")

def print_a_line(line_count, f):
    show_pointer(f)
    print(line_count, f.readline())
    show_pointer(f)

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind,  kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

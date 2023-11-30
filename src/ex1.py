from ValidationException import ValidationException

def validate_file():
    lines = []

    # Reading
    with open("input.txt", "r") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            lines.append(line)
    print(lines)

    ### for i in lines:
    ###    if lines == float(i):
    ###      print(lines)
    ###  */

def ex1():
    try:
        validate_file()
    except ValidationException as ve:
        print(ve)

ex1()
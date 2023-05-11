import sys

filename = "valid_numbers.csv"

def generate_ser(numbers: bool, letters: bool, length: int) -> str:
    import random
    res = ""
    for i in range(length):
        if numbers and letters:
            res += random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif numbers:
            res += random.choice("0123456789")
        elif letters:
            res += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return res

def set_ser(ser: str, valid: bool = True) -> None:
    import os
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.close()
    with open(filename, "r") as file:
        lines = file.readlines()
        file.close()
        
    done = False
    for i, line in enumerate(lines):
        if line.strip().split(",") == ser:
            lines[i] = f"{ser},{valid}"
            done = True
            break
    if not done:
        lines.append(f"{ser},{valid}")
    with open(filename, "w") as file:
        file.writelines(lines)
        file.close()

def check_ser(ser: str) -> bool:
    import os
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.close()
        return False
    with open(filename, "r") as file:
        for line in file:
            if f"{ser},{True}" == line.strip():
                file.close()
                return True
        file.close()
        return False


options = [option.lower() for option in sys.argv[1:]]

if "generate" in options:
    # get length
    length = -1
    for option in options:
        if option.isdigit():
            length = int(option)
            break
    if length < 0:
        print("Error: no length specified")
        exit(1)
    if "numbers" not in options and "letters" not in options:
        print("Error: no type specified")
        exit(1)
    new_ser = generate_ser("numbers" in options, "letters" in options, length)
    print(f"Generated serial: {new_ser}")
    set_ser(new_ser)
elif "check" in options:
    ser = ""
    for i, option in enumerate(options):
        if option != "check":
            ser = sys.argv[i+1]
            break
    if check_ser(ser):
        print("Valid serial")
        set_ser(ser, False)
    else:
        print("Invalid serial")
elif "help" in options:
    print("Usage: python3 main.py [generate [length] [numbers] [letters]] [check [<ur-serial-number>]] [help]")
else:
    print("Error: no valid option specified, use 'help' for help")
    exit(1)

# Path: main.py


FILENAME = "money.txt"


def write_money(money):
    try:
        with open(FILENAME, "w") as file:
            file.write((str(money)))
    except FileNotFoundError:
        print("Data file missing, resetting starting amount to 1000.")
        write_money(1000)
        return 1000
    else:
        return money


def read_money():
    try:
        with open(FILENAME, "r") as file:
            line = file.readline()
            money = float(line)
            return money
    except FileNotFoundError:
        print("Data file missing, resetting starting amount to 1000.")
        write_money(1000)
        return 1000

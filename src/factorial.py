import sys


class Factorial:

    @staticmethod
    def calc(value):
        if not isinstance(value, int):
            raise TypeError("Value provided must be an integer : {}".format(str(value)))

        if value < 0:
            raise ValueError("Value provided must not be less than zero : {}".format(value))

        # 0! is 1
        if value == 0:
            return 1

        # Base case
        if value == 1:
            return value
        else:
            return value * Factorial.calc(value - 1)


if __name__ == "__main__":
    try:
        Factorial.calc("Bob")
    except TypeError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    try:
        Factorial.calc(-16)
    except ValueError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    print("0 factorial = {}".format(Factorial.calc(0)))
    print("1 factorial = {}".format(Factorial.calc(1)))
    print("2 factorial = {}".format(Factorial.calc(2)))
    print("3 factorial = {}".format(Factorial.calc(3)))
    print("4 factorial = {}".format(Factorial.calc(4)))
    print("5 factorial = {}".format(Factorial.calc(5)))

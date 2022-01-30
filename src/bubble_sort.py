from numbers import Number
import sys


class BubbleSort:

    @staticmethod
    def sort(values):
        if not isinstance(values, list):
            raise TypeError("Only a list can be sorted")

        if not all(isinstance(val, Number) for val in values):
            raise ValueError("All list values must be numeric : {}".format(values))

        for i in range(len(values) - 1):
            for j in range(len(values) - i - 1):
                if values[j] > values[j + 1]:
                    tmp = values[j]
                    values[j] = values[j + 1]
                    values[j + 1] = tmp

        return values


if __name__ == "__main__":
    try:
        BubbleSort.sort("Bob")
    except TypeError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    try:
        BubbleSort.sort([1, 15.3, -17, 0, 0.00065])
        BubbleSort.sort([1, 15.3, "Bob"])
    except ValueError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    values = []
    print("Bubble sort of {} = {}".format(values, BubbleSort.sort(values.copy())))

    values = [3]
    print("Bubble sort of {} = {}".format(values, BubbleSort.sort(values.copy())))

    values = [2, 6, 3, 1, 5, 4]
    print("Bubble sort of {} = {}".format(values, BubbleSort.sort(values.copy())))

    values = [201, 26, 3, 0.01, 0.55, 4.456]
    print("Bubble sort of {} = {}".format(values, BubbleSort.sort(values.copy())))
from numbers import Number
import sys


# Big O for list that is already sorted (or nearly sorted) is O(n)
#   - this is due to while loop not running in this scenario
class InsertionSort:

    @staticmethod
    def sort(values):
        if not isinstance(values, list):
            raise TypeError("Only a list can be sorted")

        if not all(isinstance(val, Number) for val in values):
            raise ValueError("All list values must be numeric : {}".format(values))

        vals_len = len(values)

        if vals_len < 2:
            return values

        # Starting from the 2nd item in the list
        for i in range(1, vals_len):
            # Copy current item value to temp variable
            tmp = values[i]
            # Get the index of the previous item
            j = i - 1
            # Swap values if current item value is smaller than previous
            while j >= 0 and tmp < values[j]:
                values[j + 1] = values[j]
                values[j] = tmp
                j -= 1

        return values


if __name__ == "__main__":
    try:
        InsertionSort.sort("Bob")
    except TypeError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    try:
        InsertionSort.sort([1, 15.3, -17, 0, 0.00065])
        InsertionSort.sort([1, 15.3, "Bob"])
    except ValueError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    values = []
    print("Insertion sort of {} = {}".format(values, InsertionSort.sort(values.copy())))

    values = [3]
    print("Insertion sort of {} = {}".format(values, InsertionSort.sort(values.copy())))

    values = [2, 6, 3, 1, 5, 4]
    print("Insertion sort of {} = {}".format(values, InsertionSort.sort(values.copy())))

    values = [201, 26, 3, 0.01, 0.55, 4.456]
    print("Insertion sort of {} = {}".format(values, InsertionSort.sort(values.copy())))
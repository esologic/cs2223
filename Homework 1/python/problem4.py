"""
problem4.py
Written By: Devon Bray for CS2223

Does a binary-type search on a list using 1/3 rather than 1/2 for the divisor.
Prints the location of the key in the list and the number of searches conducted
If the key isn't found in the list, it prints an error

The search list is even numbers between 2 and 400

arg = the value you want to search for
To run: python problem4.py arg
"""

from sys import argv


def search(search_array, key):
    min_index = 0
    max_index = len(search_array)
    number_of_searches = 0

    while min_index < max_index:
        check_index = int(round(min_index + (max_index - min_index) / 3))
        check_value = search_array[check_index]
        number_of_searches += 1

        if key == check_value:
            print("Key [" + str(key) + "] found at location [" + str(check_index) + "] after [" + str(number_of_searches) + "] searches.")
            return True
        elif key > check_value:
            if min_index == check_index:
                break
            min_index = check_index
        elif key < check_value:
            max_index = check_index

    print("Key [" + str(key) + "] not found")
    return False

if __name__ == "__main__":

    if len(argv) != 2:
        print("Bad number of arguments")
        exit()

    users_key = None

    try:
        users_key = int(argv[1])
    except ValueError:
        print("Bad argument")
        exit()

    array = []
    for x in range(1, 401):
        if (x % 2) == 0:
            array.append(x)

    search(array, users_key)
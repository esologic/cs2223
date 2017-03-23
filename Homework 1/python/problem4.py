import sys


def search(search_me, key):

    original = search_me
    number_of_comparisons = 0
    location = 0

    while True:

        if len(search_me) > 1:

            number_of_items = len(search_me)
            check_index = int(round(number_of_items / 3))
            check_value = search_me[check_index]

            good_slice = []
            bad_slice = []

            number_of_comparisons += 1

            location += check_index

            if key > check_value:
                search_me = search_me[check_index:]

            elif key < check_value:
                search_me = search_me[:check_index]

            else:
                print("Found K")
                print(str(number_of_comparisons) + " Comparisons")
                print("Location: " + str(original.index(key)))
                break
        else:
            print("K not in list")
            break


if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("Bad input, too many args")
        exit()

    user_in = sys.argv[1]

    k = None

    try:
        k = int(user_in)
    except ValueError:
        print("Bad input, bad value")
        exit()

    test_list = []

    for x in range(1, 401):
        if x % 2 == 0:
            test_list.append(x)

    search(test_list, k)



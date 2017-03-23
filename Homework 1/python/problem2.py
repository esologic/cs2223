from random import sample

def order_n_sort(items):

    d = {}

    for item in items:
        while True:  # will re-try if the item isn't found
            try:
                d[item].append(item)
                break
            except KeyError:
                d[item] = []

    sorted_list = []

    for x in range(1000):
        try:
            sorted_list += d[x]
        except KeyError:
            pass  # ignore the items that don't show up

    return sorted_list

if __name__ == "__main__":
    unsorted_randoms = sample(range(1000), 100)
    print("Unsorted: " + str(unsorted_randoms))

    sorted_randoms = order_n_sort(unsorted_randoms)
    print("Sorted: " + str(sorted_randoms))

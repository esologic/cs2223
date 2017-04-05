"""
problem1.py
Written By: Devon Bray for CS2223

sorts a given list with quicksort

to run: python3 problem1.py
"""

from statistics import median


def get_random_list(min_value, max_value, num_items):
    """
    Creates a random list
    """
    from random import randint
    output_list = []

    for x in range(num_items):
        output_list.append(randint(min_value, max_value))

    return output_list


def write_line_to_file(line, mode):
    """
     Write a line to the global file
    """
    global filename
    with open(filename, mode) as the_file:
        the_file.write(line + '\n')


def partition(sort_me, begin_location, end_location):
    center_location = int((begin_location + end_location) / 2)
    right_most_element = sort_me[end_location]
    left_most_element = sort_me[begin_location]
    center_element = sort_me[center_location]
    median_value = median([right_most_element, left_most_element, center_element])

    if median_value == right_most_element:
        pivot_location = end_location
    elif median_value == left_most_element:
        pivot_location = begin_location
    else:
        pivot_location = center_location

    pivot_location = begin_location

    for i in range(begin_location+1, end_location+1):
        if sort_me[i] <= sort_me[begin_location]:
            pivot_location += 1
            swap_values_at_index(sort_me, pivot_location, i)
    swap_values_at_index(sort_me, pivot_location, begin_location)

    return pivot_location


def swap_values_at_index(swap_me, x, y):
    """
    Since python passes by reference, we don't have to return the array.
    """
    temp_value = swap_me[x]
    swap_me[x] = swap_me[y]
    swap_me[y] = temp_value


def quick_sort(sort_me, begin=0, end=None):
    if end is None:
        end = len(sort_me) - 1
    if begin >= end:
        return

    pivot_location = partition(sort_me, begin, end)
    write_line_to_file(str(sort_me), 'a')  # append to file
    quick_sort(sort_me, begin, pivot_location - 1)
    quick_sort(sort_me, pivot_location + 1, end)

if __name__ == "__main__":

    random_list = get_random_list(0, 1000, 100)

    filename = 'output.txt'
    write_line_to_file(str("Quicksort or Array:"), 'w')  # create file

    quick_sort(random_list)
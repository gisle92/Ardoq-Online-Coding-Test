import numpy as np
import heapq


def highest_product(input_list, n_highest):

    if not all(isinstance(i, int) for i in input_list):
        raise ValueError("The list must contain only integers")
    elif not isinstance(n_highest, int):
        raise ValueError("The n_highest must be an integer")
    elif len(input_list) < n_highest:
        raise ValueError("The number of units in the list cannot be smaller than the n highest number in list ")
    elif n_highest<1:
        raise ValueError("You must choose the n largest number larger or equal to 1")

    n_largest = heapq.nlargest(n_highest, input_list)

    return np.prod(n_largest)
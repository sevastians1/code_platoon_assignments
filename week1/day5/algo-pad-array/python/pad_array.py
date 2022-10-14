#REMEMBER TO PSEUDOCODE
from unittest import result


def pad(array, min_size, value = None):
    

    if len(array) >= min_size:
        return array[:min_size]

    num_to_add = min_size - len(array)

    for i in range(num_to_add):
        array.append(value)

    return array
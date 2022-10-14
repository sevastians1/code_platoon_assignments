array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    count = 0

    for value in array_to_search_through:

        if value == value_to_find:
            return count

        count += 1

def linear_search_global(value_to_find, array_to_search_through):
    count = 0
    result = []

    for value in array_to_search_through:

        if value == value_to_find:
            result.append(count)

        count += 1

    return result
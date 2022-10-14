from itertools import count


def calculate_mode(list):
    count_dict = {}

    result = []

    for char in list:
        if char in count_dict:
            count_dict[char] += 1

        else:
            count_dict[char] = 1

    top_count = 0

    # print(count_dict)

    for value in count_dict:
        if count_dict[value] > top_count:
            top_count = count_dict[value]

    for value in count_dict:
        if count_dict[value] == top_count:
            result.append(value)

    return result
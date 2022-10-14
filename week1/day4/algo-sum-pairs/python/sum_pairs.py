def sum_pairs(numbers, target):
    # 2 loops
    # go through array using a reference index, add to the subsequent index, if == target then append array index values to new list.

    sum_pairs = []

    for index in range(len(numbers)):
        for next_index in range(1, len(numbers)):
            sum = numbers[index] + numbers[next_index]

            if sum == target and index < next_index:
                sum_pairs.append([numbers[index], numbers[next_index]])

    if len(sum_pairs) == 0:
        return 'unable to find pairs'

    return sum_pairs
    # print(sum_pairs)
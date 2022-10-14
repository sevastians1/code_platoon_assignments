def picker(prices):
    best_profit = 0
    index = []

    count = 1

    for i in range(len(prices)):
        for j in range(count, len(prices)):
            if prices[j] - prices[i] > best_profit:
                best_profit = prices[j] - prices[i]
                index.append([i, j])
        count += 1

    return index[len(index) - 1]
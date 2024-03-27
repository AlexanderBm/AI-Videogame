def weighted_avg(data):
    n = len(data)
    weights = [2**i for i in range(n)]
    weighted_sum = sum(val * weight for val, weight in zip(data, weights))
    sum_of_weights = sum(weights)
    return weighted_sum / sum_of_weights
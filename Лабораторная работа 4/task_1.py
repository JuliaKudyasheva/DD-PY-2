def task() -> float:
    dict_list = [
        {'a': 2, 'b': 3},
        {'a': 4, 'b': 5},
        {'a': 1, 'b': 6}
    ]

    total_sum = 0

    for d in dict_list:
        total_sum += d['a'] * d['b']

    return total_sum


print(task())


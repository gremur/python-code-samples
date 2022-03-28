# flatten list - convert list of lists or tuples like [(1, 2)] to flat list of items like [1, 2]
lst = [(1, 2)]
result1 = [item for subitem in lst for item in subitem]


# split list on chunks where
# n - chunk size
# lst - list of items
lst = [1, 2, 2, 4, 5, 6]
n = 2
result2 = [lst[i:i + n] for i in range(0, len(lst), n)]
# print(result2) returns [[1, 2], [2, 4], [5, 6]]


# sort dict by value
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result3 = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# or
result4 = dict(sorted(x.items(), key=lambda item: item[1]))

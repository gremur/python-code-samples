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



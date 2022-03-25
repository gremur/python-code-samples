# flatten list - convert list of lists or tuples like [(1, 2)] to flat list of items like [1, 2]
lst = [(1, 2)]
result = [item for subitem in lst for item in subitem]



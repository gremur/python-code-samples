a[start:stop]       # items start through stop-1
a[start:]           # items start through the rest of the array
a[:stop]            # items from the beginning through stop-1
a[:]                # a copy of the whole array

a[start:stop:step]  # start through not past stop, by step

a[-1]               # last item in the array
a[-2:]              # last two items in the array
a[:-2]              # everything except the last two items

a[::-1]             # all items in the array, reversed
a[1::-1]            # the first two items, reversed
a[:-3:-1]           # the last two items, reversed
a[-3::-1]           # everything except the last two items, reversed
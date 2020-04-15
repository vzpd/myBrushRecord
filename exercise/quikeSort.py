from typing import List


def quikeSort(data: List):
    if len(data) < 2:
        return data
    else:
        base = data[0]
        left = [x for x in data[1:] if x <= base]
        right = [x for x in data[1:] if x > base]
        l1 = quikeSort(left)
        l2 = quikeSort(right)
        return l1 + [base] + l2


print(quikeSort([4, 2, 3, 4, 2, 4, 5]))

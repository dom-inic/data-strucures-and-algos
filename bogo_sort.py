import random

def is_sorted(list):
    for index  in range(len(list) -1):
        if list[index] > list[index -1 ]:
            return False
        return True

def bogo_sort(list):
    attempts = 0
    # while not is_sorted(list):
    random.shuffle(list)
    attempts += 1
    return list

alist = [17, 12, 15, 13, 19, 50]
print(bogo_sort(alist))

# terrible sorting algorithm
# randomizes values to reach the correct sort 
import random 

def selection_sort(list):
    
    """
    compares each element in the list whether its smaller than the previous one
    if true it moves the element to a new list and the process continues recursively
    has time complexity of O(log n)
    """
    sorted_list = []
    for i in range(0, len(list)):
        index_to_move = index_of_min(list)
        sorted_list.append(list.pop(index_to_move))

    return sorted_list

def index_of_min(list):
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i 
    return min_index


alist = [17, 12, 15, 13, 19, 50]
print(selection_sort(alist))



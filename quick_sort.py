import random 

def quick_sort(list):
    
    """
    creates a pivot by taking the first element on the list
    using the pivot it combares if there are element lesser or greater than the pivot
    the process continues recursively until there is a sorted list
    """

    # check if list is equal to 1
    if len(list) <= 1:
        return list

    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]

    for i in list[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

alist = [17, 12, 15, 13, 19, 50]

print(quick_sort(alist))

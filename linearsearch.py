def lin_search(ourlist, key):
    
    for index in range(0, len(ourlist)):
        if (ourlist[index] == key):
            return  index
    else:
        return "not fund"
    
ourlist = [15, 1, 9, 3]

lin_search(ourlist, 27)

def linear_search(list, target):
    """ Return the index position of the target if founde and returns None"""

    for i in range(0, len(list)):
        if list[i] == target:
            return i 
    return None

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 1)
verify(result)
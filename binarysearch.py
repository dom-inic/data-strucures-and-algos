# def bin_search(ourlist, key):
#     left = 0 # I assign left position to zero
#     right = len(ourlist)-1 # I assign right position by defining the length of ourlist minus one 
#     matched = False
#     while(left<=right and not matched): # the loop will continue untill the left element is less or equal to the right element and the matched is True
#         mid = (left+right)//2 # I find the position of the middle element
#         if ourlist[mid] == key: # if the middle element correponds to the key element
#              matched = True
#         else: #otherwise 
#             if key < ourlist[mid]: # if key element is less than the middle element
#                 right = mid - 1 #I assign the position of the right element as mid - 1
#             else: #otherwise
#                 left = mid + 1 #left position will become the middle position plus 1
#     return matched

# print(bin_search([1, 3, 9, 15], 17))
# print(bin_search([1, 3, 9, 15], 3))

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +2
        else:
            last = midpoint-1
    return None

from linearsearch import verify

numbers = [1,2,3,4,5,6,7,8,9,10]
# result = binary_search(numbers, 7)
# verify(result)

#  recursive binary search 

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target) # new list to work with created
            else:
                return recursive_binary_search(list[:midpoint], target)# another list from index 0 to midpoint

def verifyer(result):
    print("Target found: ", result)

result = recursive_binary_search(numbers, 6)
verifyer(result)




# def merge_sort(ourlist, left, right): #left and right corresponds to starting and ending element of ourlist
#     if right -left > 1: # check if the length of ourlist is greater than 1
#         middle = (left + right) // 2 # we divide the length in two parts
#         merge_sort(ourlist, left, middle) # recursevely I call the merge_sort function from left to middle
#         merge_sort(ourlist, middle, right) # then from middle to right
#         merge_list(ourlist, left, middle, right) # finally I create ourlist in complete form(left, middle and right) 
        
# def merge_list(ourlist, left, middle, right):# I create the function merged_list
#     leftlist = ourlist[left:middle] # I define the leftlist
#     rightlist = ourlist[middle:right] # I define the right list
#     k = left # it is the the temporary variable
#     i = 0 # this variable that corespond to the index of the first group help me to iterate from left to right
#     j = 0 # this variable that corespond to the index of the second group help me to iterate from left to right
#     while (left + i < middle and middle+ j < right): # the condition that I want to achive before to stop my iteration
#         if (leftlist[i] <= rightlist[j]): #if the element in the leftlist is less or equal to the element in the rightlist
#             ourlist[k] = leftlist[i] # In this case I fill the value of the leftlist in ourlist with index k
#             i = i + 1 #now I have to increment the value by 1
#         else: # if the above codition is not match
#             ourlist[k] = rightlist[j] # I fill the rightlist element in ourlist with index k
#             j = j + 1 # I increment index j by 1
#         k = k+1 # now I increment the value of k by 1
#     if left + i < middle: # check if left + i is less than middle
#         ourlist[k] = leftlist[i] # I place all elements of my leftlist in ourlist
#         i = i + 1
#         k = k + 1
#     else: # otherwise if my leftlist is empty
#         while k < right: # untill k is less then right
#             ourlist[k] = rightlist[j] # I place all elements of rightlist in ourlist 
#             j = j + 1
#             k = k + 1
            
# ourlist = input('input - unordered elements: ').split() # insert the input and split
# ourlist = [int(x) for x in ourlist]
# merge_sort(ourlist, 0, len(ourlist))
# print('output - ordered elements: ')
# print(ourlist)


# implementation of merge sort. new approach
# has linear space complexity
def merge_sort(list):
    """sorts a list in ascending order
    returns a new sorted list
    Divide: find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists created in previous steps
    combine: merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    divide the unsorted list at midpoint into sublists
    returns two sublists i.e left and right 
    takes overall o(log n ) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    merges two lists, sorting them in the process
    returns a new merged list
    runs in overall linear time O(n log n)
    """

    l = []
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l

alist = [38, 83, 56, 78, 17, 33, 10, 60]
s = merge_sort(alist)
print(s)



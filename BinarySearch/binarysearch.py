import random
import time
#Implementation of Binary search algorithm

#We are actually comparing Linear search and Binary Search

#LinearSearch
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#BinarySearch
def binary_search(arr, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if high < low:
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid+1, high)

#Main

if __name__=='__main__':
    #Creating a list of random sorted elements
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list)) # sorting the random list
     
 
    start_time = time.time()#time taken for linear search
    for target in sorted_list:
        linear_search(sorted_list, target)
    end_time = time.time()
    print(f"linear Search took: {(end_time - start_time)/2} seconds")
            

    start_time = time.time()#time taken for binary search
    for target in sorted_list:
        binary_search(sorted_list, target)
    end_time = time.time()
    print(f"Binary Search took: {(end_time - start_time)/2} seconds")
            

    




        
"""
Problem: Linear Search
Topic: Searching

Approach:

Time Complexity: O(n) // In the worst case, we may have to traverse the entire array to find the target element. In average case, we may find the target element in the middle of the array, resulting in a time complexity of O(n/2) which simplifies to O(n).
Space Complexity: O(1) // Only a constant amount of extra space is used. No recursion or additional data structures are used.

Notes:
"""


def linear_search(arr, target):
    
    l = len(arr)
    
    # indexes = []
    
    for i in range(l):
        if arr[i] == target:
            return i
    return -1


    # for i in range(l):
    #     if arr[i] == target:
    #         indexes.append(i)
    # return indexes


r = list(map(int, input("Enter array elements separated by spaces: ").split()))
t = int(input("Enter the target element to search: "))

res = linear_search(r, t)
if res != -1:
    print(f"Element found at index: {res}") 
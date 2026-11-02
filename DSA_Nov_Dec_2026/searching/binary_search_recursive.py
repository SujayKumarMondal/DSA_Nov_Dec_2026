"""
Problem: Binary Search Recursive
Topic: Searching

Approach:

Time Complexity:
Space Complexity:

Notes:
"""


def recursive_binar_search(arr, target, low, high):
    
    if arr is not sorted:
        arr.sort()  # Sort the array if it's not sorted
        
    if low > high:
        return -1  # Target not found
    
    if arr[low] == target:
        return low  # Target found at the low index
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return recursive_binar_search(arr, target, mid + 1, high)
    
    else:
        return recursive_binar_search(arr, target, low, mid - 1)
    
    
o = list(map(int, input("Enter the elements of the array: ").split()))
target = int(input("Enter the target element to search: "))

res = recursive_binar_search(o, target, 0, len(o) - 1)
if res == -1:
    print("Element not found in the array.")
else:
    print(f"Element found at index: {res}")
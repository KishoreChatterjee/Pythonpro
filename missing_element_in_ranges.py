# Python library for binary search
from bisect import bisect_left


# A sorting based python program to find missing
# elements from an array

# Print all elements of range [low, high] that
# are not present in arr[0..n-1]

def printMissing(arr, n, low, high):
    # Sort the array
    arr = sorted(arr)

    # Do binary search for 'low' in sorted
    # array and find index of first element
    # which either equal to or greater than
    # low.
    ptr = bisect_left(arr, low)
    index = ptr

    # Start from the found index and linearly
    # search every range element x after this
    # index in arr[]
    i = index
    x = low
    while (i < n and x <= high):
        # If x doesn't match with current element
        # print it
        if (arr[i] != x):
            print(x, end=" ")

        # If x matches, move to next element in arr[]
        else:
            i = i + 1
        # Move to next element in range [low, high]
        x = x + 1

    # Print range elements that are greater than the
    # last element of sorted array.
    while (x <= high):
        print(x, end=" ")
        x = x + 1


# Driver code

arr = set(list(map(int,input("Enter the list of numbers: ").split(' '))))

n = len(arr)
low = int(input("Enter low limit: "))
high = int(input("Enter high limit: "))
print("The missing elements are:")
printMissing(arr, n, low, high);


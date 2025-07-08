# Count subarrays where x is the maximum element

arr = [7,1, 2, 3, 4, 5, 6]
l, r = 2, 6
def countSubarrays(arr,left,right):
    sarr = sorted(arr)
    subarr =[]
    subarrlst=[]
    # left=0
    # right=len(arr)
    if (left not in sarr) or (right not in sarr):
        return False
    else:
       while left < right:
                print(sarr[left:right])

                print(sarr[left:right-1])
                print(sarr[left])
                left = left +1
                countSubarrays(sarr[left:right], left, right)






# Python3 code to print all possible subarrays
# for given array using recursion

# Recursive function to print all possible subarrays
# for given array
def printSubArrays(arr, start, end):
    # Stop if we have reached the end of the array
    if end == len(arr):
        return

    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)


# Driver code
# arr = [1, 2, 3]
countSubarrays(arr, 2, 5)



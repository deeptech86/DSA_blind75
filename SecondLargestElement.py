def secondlargestelement(arr):
    # maxi = max(arr)
    # secondmax= arr[0]
    # for i in arr:
    #     if (i > secondmax and i<= maxi):
    #         secondmax = i
    # return secondmax
    n = len(arr)

    # Sort the array in non-decreasing order
    arr.sort()

    # start from second last element as last element is the largest
    for i in range(n - 2, -1, -1):

        # return the first element which is not equal to the
        # largest element
        if arr[i] != arr[n - 1]:
            return arr[i]

    # If no second largest element was found, return -1
    return -1


arr= [10, 5, 10]
# print(arr[-2])
print(secondlargestelement(arr))


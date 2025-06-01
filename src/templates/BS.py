# arr = [200,200, 200,200,200,200,500,500,500]
num=500

def bs(arr, num):
    low=0
    high= len(arr)-1
    mid=0

    while (low<=high) :
        mid = (low+ high)//2
        if arr[mid]<num:
            low= mid+1
        elif arr[mid]>num :
            high = mid-1
        else:
            return mid
    return -1

# print(bs(arr, num))

arr= [8, 9, 10, 2, 5, 6]

def circularArr(nums):
    # low=0
    # high = len(arr) - 1
    # mid = 0
    # count = 0
    #
    #
    #
    # if (arr[low] <= arr[high]):
    #     return low
    # else:
    #
    #     while (low<= high):
    #         mid = (low + high) // 2
    #
    #          # Find the next and prev element from Mid
    #         prev = (mid-1+ len(arr)) % len(arr)
    #         next = (mid + 1) %  len(arr)
    #
    #         if (arr[mid] <= arr[prev] and arr[mid] <= arr[next]):
    #             return mid
    #         elif (arr[mid] >= arr[low]):
    #             low = mid+1
    #         elif (arr[mid] <= arr[high]):
    #             high = mid-1
    #     return -1

    (left, right) = (0, len(nums) - 1)

    # loop till the search space is exhausted
    while left <= right:

        # if the search space is already sorted, we have
        # found the minimum element (at index `left`)
        if nums[left] <= nums[right]:
            return left

        mid = (left + right) // 2

        # find the next and previous element of the `mid` element (in circular manner)
        next = (mid + 1) % len(nums)
        prev = (mid - 1 + len(nums)) % len(nums)

        # if the `mid` element is less than both its next and previous
        # neighbor, it is the list's minimum element

        if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
            return mid

        # if nums[mid…right] is sorted, and `mid` is not the minimum element,
        # then the pivot element cannot be present in nums[mid…right],
        # discard nums[mid…right] and search in the left half

        elif nums[mid] <= nums[right]:
            right = mid - 1

        # if nums[left…mid] is sorted, then the pivot element cannot be present in it;
        # discard nums[left…mid] and search in the right half

        elif nums[mid] >= nums[left]:
            left = mid + 1

    # invalid input
    return -1



print(circularArr(arr))
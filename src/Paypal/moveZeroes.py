# Move all zeros to end of array
# arr = [1, 2, 0, 4, 3, 0, 5, 0]
from collections import deque


def moveZeroes(nums):
    # queue= deque([arr])
    # for i in queue:
    #     if i==0:
    # left =0
    # right = len(arr)
    #
    # while left < right:
    #     if arr[left]==0:
    #         arr.remove(arr[left])
    #         arr.append(0)
    #     left = left + 1
    # return arr
    snowball = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            snowball += 1
        elif snowball > 0:
            t = nums[i]
            nums[i] = 0
            nums[i - snowball] = t
    return nums







arr = [1, 2, 0, 0, 4,0, 3, 0, 5, 0]

print(moveZeroes(arr))
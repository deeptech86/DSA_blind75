"""
Problem: Product of Array Except Self
Technique: Prefix Sum
"""

def product_of_array_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        List[int] - Product of all elements except self
    """
    # TODO: Implement solution
    n = len(nums)
    # pref = [1] * n

    # total=1
    #
    # for i in range(len(nums)):
    #     if nums[i]!=0:
    #         total *= nums[i]
    #     else:
    #         total = 0
    #
    # for i in range(len(nums)):
    #         if nums[i] != 0:
    #             pref[i] = total//nums[i]
    #         else:
    #             pref[i] = total
    #
    #
    #
    # return pref
    # n = len(nums)
    # prefix=[1]* (n-1)
    #
    # prefix.append(nums[0])
    # for i in range(1,n):
    #     prefix[i] = prefix[i-1]*nums[i]
    # return prefix
    #
    # # for range of query_range(prefix,left,right)
    # for i in range(n):
    #     if nums[i]==0:

    n = len(nums)

    # Build prefix products: prefix[i] = nums[0] * nums[1] * ... * nums[i]
    prefix = [1] * n
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    print('prefix')
    print(prefix)
    print('-------')

    # Build suffix products: suffix[i] = nums[i] * nums[i+1] * ... * nums[n-1]
    suffix = [1] * n
    suffix[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i]
    print('suffix')
    print(suffix)
    print('-------[1, 2, 3, 4]')

    # Calculate result using prefix and suffix
    result = [1] * n
    for i in range(n):
        left_product = prefix[i - 1] if i > 0 else 1
        right_product = suffix[i + 1] if i < n - 1 else 1
        result[i] = left_product * right_product

    return result

def tryagain(arr):
    n= len(arr)
    prefix =[1]*n
    suffix = [1]*n
    result = [1]*n
    prefix[0]=arr[0]
    suffix[n-1]=arr[n-1]

    for i in range(1,len(arr)):
        prefix[i]= prefix[i-1] * arr[i]
    print(prefix)

    for i in range(n-2,-1,-1):
        suffix[i] =suffix[i+1] * arr[i]
    print(suffix)

    for i in range(n):
        left_product= prefix[i - 1] if i > 0 else 1
        right_product = suffix[i+1] if i < n-1else 1
        result[i] = left_product * right_product
    return result







'''
[2,3,-1,2,1,1,2]
Prefix sum technique: 
n=len(arr)
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]= prefix[i-1] + arr[i]
return prefix

# for range of query_range(prefix,left,right)
if left == 0
    return prefix[right]
return prefix[right] - prefix[left-1]

[2,5,4,6,7,8,10],2,5






'''




# Example 1
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Explanation: [1*2*3*4/1, 1*2*3*4/2, 1*2*3*4/3, 1*2*3*4/4]

# Example 2
# Input: nums = [-1, 1, 0, 3, -3]
# Output: [0, 0, 9, 0, 0]
# Explanation: Zero in the array causes most products to be zero

nums = [1, 2, 3, 4]
print(product_of_array_except_self(nums))

print('--------------')

print(tryagain
      (nums))
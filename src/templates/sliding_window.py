def sliding_window_fixed(arr,k):
    left,right= 0,k
    sum_arr = sum(arr[left:right])
    while right < len(arr):

        left+=1
        right += 1
        sum_arr=max(sum_arr,sum(arr[left:right]))
    return sum_arr #largestSum




#Return the array
def sliding_window_fixed_subarray(arr,k):
    left,right= 0,k
    sum_arr = sum(arr[left:right])
    subarray=arr[left:right]
    while right < len(arr):

        left+=1
        right += 1
        if sum(arr[left:right])>sum_arr:
            subarray = arr[left:right]
            sum_arr = sum(arr[left:right])

    return subarray #Print the array of largestSum


def sliding_longest_subarray(str):
    arr=list(str)
    left,right= 0,0
    longest_substr = [arr[left]]
    while right<len(arr)-1:
        right+=1
        if arr[right] not in longest_substr:
            longest_substr.append(arr[right])
        else:
            longest_substr.remove(arr[left])
            left +=1
    return longest_substr

def lengthOfLongestSubstring(s) -> int:
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


str="pwwkew"
k = 3
# print(sliding_window_fixed_subarray(str,k))
print(sliding_longest_subarray(str))
print(lengthOfLongestSubstring(str))
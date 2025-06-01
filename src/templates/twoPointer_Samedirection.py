# arr=[sortedarray]
# slow,fast=0,0
# while (fast < len(arr)):
    # Process here specifies the current iteration
    # current = process(arr[slow],arr[fast])
    #Specified Condition for sloa and fast
    # if condition(arr[slow],arr[fast]):
    # slow moves forward if conditoin is met
        # slow+=1
    #Fast moves irrespective
    # fast+=1


arr = [0,0,1,1,1,2,2,3,4,4]
def find_duplicates(arr):
    slow,fast=0,1
    dup =[]
    while (fast<len(arr)):
        if (arr[slow]==arr[fast]):
            if not dup or dup[-1]!=arr[slow]:
                dup.append(arr[slow])

        slow=fast
        fast +=1
    return dup

# print(find_duplicates(arr))


def remove_duplicates(arr) :
    slow, fast = 0, 1
    dup = []
    while (fast < len(arr)):
        current = arr[fast] != arr[slow]
        if current:
            slow +=1
            # if not dup or dup[-1]!=arr[slow]:
            #     dup.append(arr[fast])
            arr[slow]=arr[fast]
            # slow=fast

        fast +=1
    # return len(dup)
    return slow +1

print(remove_duplicates(arr))

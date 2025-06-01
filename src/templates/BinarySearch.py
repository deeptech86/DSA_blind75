arr = [200,200, 200,200,200,200,500,500,500]
num=500

# def binarySearchTemplate(arr,num):
#     left,right=0,len(arr)-1
#     first_index=-1
#     mid = (left +right) //2
#     if arr[mid]==num:
#         first_index = mid
#     if arr[mid]>num:
#         right= mid-1
#         binarySearchTemplate(arr[left:right], num)
#     else:
#         left=mid+1
#         binarySearchTemplate(arr[left:right], num)
#     return first_index

def binarySearchTemplate(arr, num) :

        low = 0
        high = len(arr) - 1
        mid = 0



        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if arr[mid] < num:
                low = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > num:
                high = mid - 1

            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1





print(binarySearchTemplate(arr,num))
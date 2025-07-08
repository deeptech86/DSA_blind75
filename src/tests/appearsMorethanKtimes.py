
arr = [ 1, 2, 2,2,2,2,6, 6, 6, 6, 6, 10 ]
K = 4

def NDivKWithFreq(arr, K):
    n= len(arr)
    dict={}
    res=[]


    for i in range(n):
        if arr[i] not in dict.keys():
            dict[arr[i]] = 1
        else:
            current= dict.get(arr[i])
            dict[arr[i]] = current+1
    for key,val in dict.items():
        if val > K:
            res.append(key)
    return res


print(NDivKWithFreq(arr, K))
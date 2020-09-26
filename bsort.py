def bsort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        for x in range(len(arr)):
            print(arr[x])
        print("iteration")
bsort([45,3,78,54,4])

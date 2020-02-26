def SelectionSort(arr):
    for i in range(len(arr)):
        print(f"-->{arr}")
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]):
                arr[i],arr[j] = arr[j],arr[i] 
  

l = [6,5,9,2,4,8,1,4,6,3]
SelectionSort(l)


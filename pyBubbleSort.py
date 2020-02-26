def bubble_sort(arr):
    swapped = True
    while swapped:  
        swapped = False  
        print(f"-->{arr}")
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                swapped = True
                arr[i],arr[i+1] = arr[i+1],arr[i]
                print(f"--sub iterations-->{arr}")


l = [6,5,9,2,4,8,1,4,6,3]
bubble_sort(l)
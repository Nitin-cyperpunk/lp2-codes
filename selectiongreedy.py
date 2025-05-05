def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = list(map(int, input("Enter the elements of the array separated by spaces:␣ ").split()))    
print("Original array:", arr)  
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)   
 # Get the length of the array
 
 # Traverse through all elements in the array
 
 # Assume the minimum element is at the current position

 # Find the minimum element in the unsorted portion of the array
 
 

 # Taking input from the user
 # Swap the found minimum element with the first element of the unsorted␣
 

 # Sorting the array using Selection Sort (Greedy approach)

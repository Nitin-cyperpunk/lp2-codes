def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("\nSORTED ARRAY IN ASCENDING ORDER:\n")
    print(" ".join(map(str, arr)))

    print("\nSORTED ARRAY IN DESCENDING ORDER:\n")
    print(" ".join(map(str, arr[::-1])))
def main():
    n = int(input("Enter The Size Of Array: "))
    arr = list(map(int, input("Enter The Elements Of Array: ").split()))
    if len(arr) != n:
        print(f"Error: You entered {len(arr)} elements but expected {n}.")
        return
    selection_sort(arr)
if __name__ == "__main__":
    main()

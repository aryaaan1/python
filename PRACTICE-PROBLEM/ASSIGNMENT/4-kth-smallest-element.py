arr = [7, 10, 4, 3, 20, 15]

k = int(input("Enter the value of k: "))

arr.sort()

if k >= 1 and k <= len(arr):
    print("Kth smallest element:", arr[k - 1])
else:
    print("Invalid value of k")
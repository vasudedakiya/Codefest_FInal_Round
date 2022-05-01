N = int(input("Enter Size Of Array : "))
arr = []
for k in range(0, N, 1):
    arr.append(int(input(f"Enter array element {k+1} : ")))

for i in range(0, len(arr) - 1):
    for j in range(0, len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

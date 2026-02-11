n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(input().strip())

total_swaps = 0
passes = 0

for i in range(n):
    if n - i - 1 <= 0:
        break  
    swapped = False
    passes += 1

    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            total_swaps += 1
            swapped = True

    if not swapped:
        break

print(f"Total Swaps: {total_swaps}")
print(f"Total Passes: {passes}")
print("Sorted Strings:")
for s in arr:
    print(s)
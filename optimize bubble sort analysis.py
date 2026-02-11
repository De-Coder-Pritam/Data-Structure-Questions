n = int(input().strip())
arr = list(map(int, input().split()))

total_swaps = 0
passes = 0

for i in range(n):
    swapped = False
    passes += 1

    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            total_swaps += 1
            swapped = True

    # Optimized stop condition
    if not swapped:
        break

print(total_swaps)
print(passes)
print(*arr)
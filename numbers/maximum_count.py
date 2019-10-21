num=int(input())
arr=list(map(int,input().split()))
arr.sort()

# find the max frequency using
# linear traversal
max_count = 1
res = arr[0]
curr_count = 1

for i in range(1, len(arr)):
    if (arr[i] == arr[i - 1]):
        curr_count += 1

    else:
        if (curr_count > max_count):
            max_count = curr_count
            res = arr[i - 1]

        curr_count = 1

# If last element is most frequent
if (curr_count > max_count):
    max_count = curr_count
    res = arr[n - 1]

print(res)
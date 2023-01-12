def binary_search(num, a):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == num:
            return 1
        elif a[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
compared = list(map(int, input().split()))
for num in compared:
    print(binary_search(num, a))
import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
dia = sorted(tuple(map(int, input().split())) for _ in range(n))
bag = sorted(int(input()) for _ in range(k))

arr = []
value = 0
i = 0
for c in bag:
    while i < n:
        m, v = dia[i]
        if m <= c:
            heapq.heappush(arr, -v)
            i += 1
        else:
            break
    if arr:
        value -= heapq.heappop(arr)
print(value)
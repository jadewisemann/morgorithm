from collections import deque
import sys
import heapq
input = sys.stdin.readline
numval = [] #보석리스트(무게,가치)
bag = [] #가방 무게 리스트

n,k = map(int,input().split())
for _ in range(n):
    a,b = map(int,input().split())
    numval.append((a,b)) #무게,가치
for _ in range(k):
    c = int(input())
    bag.append(c)

bag.sort()
numval.sort()

hq = [] #(음수로 가치를 넣을 예정)
ans = 0
idx = 0

for b in bag :
    # 이미 넣은 보석은 다시 안 넣기 위해 idx 사용
    while idx < n and numval[idx][0] <= b :
        # 힙큐는 가장 작은 값부터 빼주기에 음수 사용
        heapq.heappush(hq,-numval[idx][1])
        idx += 1
    
    if hq :
        ans += -heapq.heappop(hq)
print(ans)
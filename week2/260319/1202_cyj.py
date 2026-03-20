import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())    # 보석 개수 N, 가방 개수 K
dia = []
bag = []

for _ in range(N):
    M, V = map(int, input().split())    # 보석 무게 M, 가격 V
    dia.append((M, V))

for _ in range(K):
    C = int(input())    # 가방 적재 가능 무게 C
    bag.append(C)

dia.sort()
bag.sort()
ans = 0
heap = []
i = 0   # 보석 인덱스

for c in bag:
    while i < N and dia[i][0] <= c:
        heapq.heappush(heap, -dia[i][1])    # 가격을 음수로 넣어 최대 힙처럼 사용
        i += 1

    # 후보 중 가장 비싼 보석 선택
    if heap:
        ans += -heapq.heappop(heap)

print(ans)




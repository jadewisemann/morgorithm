import heapq, sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())    # N은 보석의 총 개수, K는 가방의 총 개수
    jewel = [list(map(int, input().split())) for _ in range(N)]     #무게, 가격
    bags = [int(input()) for _ in range(K)]
    jewel.sort()
    bags.sort()

    heap = []
    idx = 0
    ans = 0

    for bag in bags:
        while idx < N and bag >= jewel[idx][0]:
            heapq.heappush(heap, -jewel[idx][1]) #최댓값 찾을 예정이니까, -해서 저장하자.
            idx += 1
            
        if heap:    # 가방에 보석 있다면
            ans += -(heapq.heappop(heap))
            
    print(ans)

solve()
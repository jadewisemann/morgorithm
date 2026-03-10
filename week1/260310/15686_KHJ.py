from itertools import combinations

N, M = map(int, input().split())    # N은 격자 크기, M은 뽑을 치킨집
grid = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

# 집과 치킨집 좌표 따로 저장해두기
for y in range(N):
    for x in range(N):
        if grid[y][x] == 1:
            home.append((y, x))
        elif grid[y][x] == 2:
            chicken.append((y, x))
            
min_ans = 10000
# 치킨집 조합 생성
for chic in combinations(chicken, M):
    #chic = ( (1, 2), (2, 2), (4, 4) )
    total_dist = 0
    
    #집 좌표와 치킨 좌표 간 최소거리 찾기
    for hy, hx in home:
        min_dist = 10000
        for cy, cx in chic:
            curr_dist = abs(hy - cy) + abs(hx - cx)
            if min_dist > curr_dist:
                min_dist = curr_dist
        total_dist += min_dist
        
    if min_ans > total_dist:
        min_ans = total_dist

print(min_ans)
    

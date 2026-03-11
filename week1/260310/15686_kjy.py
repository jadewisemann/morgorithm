from itertools import combinations
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
food = []
ans = float('inf')
for i in range(n):
    for j in range(n):
        if board[i][j] == 2 :
            food.append((i,j))        
home = {}
while food :
    r,c = food.pop()
    key = (r,c)
    home[key] = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                value = (abs(r-i)+abs(c-j))
                home[key].append(value)

chicken = list(home.keys())

for comb in combinations(chicken,m) :

    total = 0

    for x in range(len(home[(4,4)])):
        min_dist = min(home[ch][x] for ch in comb)
        total += min_dist
    ans = min(ans,total)

print(ans)



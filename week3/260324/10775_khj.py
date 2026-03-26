import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA != rootB:
        parent[rootA] = rootB    

G = int(input())    # G는 게이트의 수
P = int(input())    # P는 비행기의 수
info = [int(input()) for _ in range(P)]
parent = list(range(G+1))
cnt = 0

for i in info:
    now_dock = find(i)
    if now_dock == 0:
        break
    
    cnt += 1
    union(now_dock, now_dock-1)

print(cnt)
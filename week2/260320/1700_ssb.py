n, k = map(int, input().split())
elec = list(map(int, input().split()))
order = [[] for _ in range(k+1)]
for i in range(k):
    order[elec[i]].append(i)

multitab = set()
multitab_order = [0] * (k+1)
counter = [0] * (k+1)

i = 0
while len(multitab) < n:
    if i >= k:
        print(0)
        exit()

    now = elec[i]
    multitab.add(now)
    counter[now] += 1
    multitab_order[now] = order[now][counter[now]] if counter[now] < len(order[now]) else float('inf')
    i += 1

cnt = 0
for j in range(i, k):
    now = elec[j]
    # now가 멀티탭에 있다면
    if now in multitab:
        counter[now] += 1
        multitab_order[now] = order[now][counter[now]] if counter[now] < len(order[now]) else float('inf')
        continue
    # now가 멀티탭에 없다면
    prev = multitab_order.index(max(multitab_order[m] for m in multitab))
    multitab.remove(prev)
    multitab_order[prev] = 0
    multitab.add(now)
    counter[now] += 1
    multitab_order[now] = order[now][counter[now]] if counter[now] < len(order[now]) else float('inf')
    cnt += 1
    
print(cnt)
n,k = map(int,input().split())
arr = list(map(int,input().split()))

base = []
ans = 0

for i in range(k):
    diff = []
    diffnum = []

    now = arr[i]
    
    # 안에 있으면 컨티뉴
    if now in base:
        continue
   
    # n 보다 작으면 어펜드
    if len(base) < n:
        base.append(now)
        continue  
    # 다르다? 안에 있는 애들 i+1 부터 끝까지 다 본다
    for b in base:
        if b in arr[i+1:]:
            idx = arr[i+1:].index(b)
            diff.append(b)
            diffnum.append(idx)
        # base 안에 있는 값들이 이제 안쓰이면 바로 제거 후 break
        else:
            base.remove(b)
            base.append(now)
            ans += 1
            break
    else:
        # 모든 값들이 뒤에도 나올 때는 가장 늦게 나오는 걸 제거해야 한다.
        max_idx = max(diffnum)
        for j in range(len(diffnum)):
            if diffnum[j] == max_idx:
                base.remove(diff[j])
                base.append(now)
                ans += 1
                break

print(ans)
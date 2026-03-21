N, K = map(int, input().split())
info = list(map(int, input().split()))

socket = set()
cnt = 0

# info 순회 돌기
for i in range(K):
    # 조건 1. 이미 해당 번호의 플러그가 꽂혀있는 경우
    curr = info[i]
    
    if curr in socket:
        continue
    
    # 조건 2. 콘센트에 빈 자리 있다면
    if len(socket) < N:
        socket.add(info[i])
    
    # 조건 3. 조건 1,2에 모두 해당 안되는 경우
    else:
        max_idx = -1
        target_val = -1
        
        # 이후 사용 여부 확인하기        
        next_usage = info[i+1:]
        for s in socket:
            # 만약 이후에 사용예정 이라면?
            if s in next_usage:
                idx = next_usage.index(s)   # 언제 사용할 예정인지에 대한 정보(인덱스) 저장
                if max_idx < idx:           # 인덱스가 최대값인 플러그 뽑을 예정이므로, 최댓값 업데이트
                    max_idx = idx
                    target_val = s          # set으로 콘센트 저장 중이므로 해당 value값을 저장해줘야 함.
            
            # 만약 사용 예정이 아니라면?
            else:
                max_idx = float('inf')      # 엄큰수로 저장해두어 무조건 뽑아내게 설정하기.
                target_val = s
                break

        # 모든 조건 충족 여부 확인 후 뽑고 꽂기 실행하기
        socket.remove(target_val)
        cnt += 1
        socket.add(curr)
        
print(cnt)
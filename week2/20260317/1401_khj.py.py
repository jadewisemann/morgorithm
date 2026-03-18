N = int(input())


A, B, C, D, E, F = map(int, input().split())

if N == 1:
    print(sum([A,B,C,D,E,F]) - max([A,B,C,D,E,F]))
else:

    min_ans = float('inf')

    for n1, n2, n3 in [(A, B, C), (A, B, D), (A, C, E), (A, D, E), (F, B, C), (F, B, D), (F, C, E), (F, D, E)]:
        num_list = sorted([n1, n2, n3])

        three = 4 
        
        one = (N-2) * (N-1) * 4 + (N-2) ** 2
        
        two = (N**2 * 5 - one - 3 * three) // 2
        
        
        
    
        res = (three * (num_list[0] + num_list[1] + num_list[2])) + two * (num_list[0] + num_list[1]) + one * num_list[0]
        
        if min_ans > res:
            min_ans = res

    print(min_ans)
    








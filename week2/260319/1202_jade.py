import heapq as hq

def solve():
    it = iter(open(0).read().split())

    n, k = int(next(it)), int(next(it))

    jewels = sorted(
        (int(next(it)), int(next(it)))
        for _ in range(n) 
    )

    bags = sorted(
        int(next(it))
        for _ in range(k)
    )
    
    result = 0
    avail_jewels = []
    jewel_idx = 0

    for bag in bags:
        while jewel_idx < n and jewels[jewel_idx][0] <= bag:
            hq.heappush(avail_jewels, -jewels[jewel_idx][1])
            jewel_idx += 1

        if avail_jewels:
            result += -hq.heappop(avail_jewels)

    print(result) 


if __name__ == "__main__":
    solve()
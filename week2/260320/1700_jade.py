def solve():
    n, k = map(int, input().split())
    items = list(map(int, input().split()))

    multitap = set()
    plug_out_count = 0

    for i, item in enumerate(items):
        if item in multitap: continue
        
        if len(multitap) < n:
            multitap.add(item)
            continue
        
        target_to_unplug = max(
            multitap, 
            key=lambda x:
                items[i+1:].index(x)
                if x in items[i+1:] 
                else k + 1
        )
        
        multitap.remove(target_to_unplug)
        multitap.add(item)
        plug_out_count += 1

    print(plug_out_count)

solve()
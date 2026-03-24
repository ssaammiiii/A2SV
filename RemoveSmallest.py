t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    ok = True
    for i in range(n - 1):
        if arr[i+1] - arr[i] > 1:
            ok = False
            break
    
    if ok:
        print("YES")
    else:
        print("NO")

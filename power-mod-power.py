a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

if m == None:
    print(a**b)
    
elif b >= 0:
    print(a**b)
    print(a**b % m)

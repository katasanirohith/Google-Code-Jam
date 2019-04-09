import math
go = 0
def fucn():
    n, l = input().split()
    val = 0
    x = 0
    n = int(n)
    l = int(l)
    a = list(map(int, input().split()))
    temp = 0
    for i in range(0,len(a)):
        if a[0]!= a[i]:
            temp = i
            break
    sim = int(math.gcd(a[0],a[temp]))
    ar = []
    tsmilar = sim
    for i in range(temp-1,-1,-1):
        sim = a[i] // sim
        ar.append(sim)
    ar.reverse()
    ar.append(tsmilar)
    sim = tsmilar
    for i in range(temp,len(a)):
        sim = a[i] // sim
        ar.append(sim)
    ars = set(ar)
    asor = []
    for s in sorted(ars, key=int):
        asor.append(s)
    dic = {}
    c = 65
    for i in range(0,26):
        dic[asor[i]] = chr(c)
        c += 1
    ans = []
    for i in ar:
        ans.append(dic[i])
    ans = "".join(ans)
    print("Case #" + str(go) + ":", end=" ")
    print(ans)
t = int(input())
for i in range(0, t):
    go = go + 1
    fucn()
t = int(input())
def fucn(n):
    l = list(n)
    u = []
    b = 0
    for i in range(len(l)):
        if int(l[i])  == 4:
            u.append(len(l)-i-1)
    for i in u:
        l[len(l)-i-1] = 3
        b = b + pow(10,i)
    str1 = ''.join(str(e) for e in l)
    print(str1,b)
a = []
for i in range(0,t):
    a.append(input())
    print("Case #"+str(i+1)+":", end=" ")
    fucn(a[i])
t = int(input())
for i in range(0,t):
    n = int(input())
    a = input()
    a = list(a)

    ans = []
    for k in a:
        if k == 'E':
            ans.append('S')
        else:
            ans.append('E')
    ans = "".join(ans)
    print("Case #"+str(i+1)+":",end=" ")
    print(ans)


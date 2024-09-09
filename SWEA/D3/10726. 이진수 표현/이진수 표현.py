def dex_to_bin(m):
    r=''
    while m!=0:
        r+=str(m%2)
        m//=2
    return r

for t in range(1, int(input())+1):
    N,M=map(int, input().split())
    M=dex_to_bin(M)
    c=0
    for m in M:
        if m=='0':break
        if c==N:break
        c+=1
    if c==N:print(f'#{t} ON')
    else:print(f'#{t} OFF')
def ss(a,b,c):
    s=0
    for i in range(a,b):
        if i%c==0:
            s+=1
    return s
a,b,c=map(int,input().split())
s=ss(a,b,c)
print(s)
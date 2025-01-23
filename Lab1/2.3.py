#2.1
n=int(input())
for i in range(n,0,-1):
    s = ''.join(str(k) for k in range(1, i + 1))
    print(s)

#2.2
'''
n=int(input())
lenprev=0
for i in range(n,0,-1):
    s = ''.join(str(k) for k in range(i,0,-1))
    s += ''.join(str(k) for k in range(2,i+1))
    if lenprev==0:
        k=0
    else:
        k+=(lenprev-len(s))//2
    lenprev=len(s)
    print(' '*k+s)
'''
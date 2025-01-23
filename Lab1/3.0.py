n=int(input())
sprev=[1]
s=[1]
print('строка ',1,': ',s)
for i in range(1,n):
    s=[1]
    for j in range(1,i):
        s.append(sprev[j-1]+sprev[j])
    s.append(1)
    sprev=s
    print('строка ',i+1,': ',s)
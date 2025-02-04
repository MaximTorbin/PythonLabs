s=str(input())
d={}
for i in s:
    if i!=" ":
        d[i]=s.count(i)
d=sorted(d.items(),key=lambda arg: arg[1],reverse=True)
if len(d)>2:
    for ch in d[:3]:
        print(f'{ch[0]}: {ch[1]}')
else:
    for ch in d[::]:
        print(f'{ch[0]}: {ch[1]}')
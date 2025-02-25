#0
'''
a=[]
for i in range(int(input())):
    a.append(int(input()))
b=[]
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        b.append(a[i])
print(b)
'''
#1 
'''
a=[]
for i in range(int(input())):
    a.append(int(input()))
ind_min=a.index(min(a))
ind_max=a.index(max(a))
a[ind_min],a[ind_max]=a[ind_max],a[ind_min]
print(a)
'''
#2
'''
a=[]
ans=0
for i in range(int(input())):
    a.append(int(input()))
for i in range(int(input())):
    if int(input()) in a:
        ans+=1;
print(ans)
'''
#3
'''
a=[]
for i in range(int(input())):
    a.append(str(input()))
ans={}
for el in a:
    if el in ans:
        ans[el]+=1
    else:
        ans[el]=1
for el in ans.values():
    print(el)
'''   
    

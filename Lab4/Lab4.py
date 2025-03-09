#1
'''
dic={'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
print(dic.get(input()))
'''
#2
'''
dic={'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
rev_dic={str(v):str(k) for k,v in dic.items()}
print(rev_dic.get(input()))
'''
#4
'''
s=input()
dic={i:s.count(str(i)) for i in range(10)}
dic=sorted(dic.items(),key=lambda item:item[1],reverse=True)[:3]
print(dic)
'''
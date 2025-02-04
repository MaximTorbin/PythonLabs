s=str(input())
newstring=""
i=0
while i<len(s):
    j=1
    num=""
    while (i+j)<(len(s)):
        if s[i+j].isdigit():
            num+=str(s[i+j])
            j+=1
        else: break
    if num=="" and not(s[i].isdigit()):
        newstring+=s[i]
    elif not(s[i].isdigit()):
        newstring+=s[i]*(int(num))
    i+=j
print(newstring)

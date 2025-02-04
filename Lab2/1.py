s=str(input())
newstring = ""
count = 1
prev = s[0]

for char in s[1::]:
    if char==prev:
        count+=1
    else:
        if count>1:
            newstring+=prev+str(count)
        else:
            newstring+=prev
        prev=char
        count=1
if count>1:
    newstring+=prev+str(count)
else:
    newstring+=prev
print(newstring)

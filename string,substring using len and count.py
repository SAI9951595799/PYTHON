s='ABCABCABCA'
s1='ABC'
i=s.find(s1)
while i!=-1:
    print('substring',s1,'present at index',i)
    i=s.find(s1,i+len(s1),len(s))
print('the count of substring is:',len(s1))

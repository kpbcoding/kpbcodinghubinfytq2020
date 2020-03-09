x=input()
d={}
for i in x:
	if i in d:
		d[i]=d[i]+1
	else:
		d[i]=1
print(d)
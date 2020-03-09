x=input()
y=[]
i=0
while i<=len(x):
	if i in (2,3,5,7):
		y.append(x[i])
	i=i+1
print(''.join(y))

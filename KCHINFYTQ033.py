x=list(input())
y=list(input())
z=[]
for i in x:
	if i in y:
		z.append(i)
print(''.join(z))

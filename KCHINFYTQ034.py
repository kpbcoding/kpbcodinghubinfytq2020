x=list(input())
z=[]
for i in x:
	if i not in z:
		z.append(i)
print(''.join(z))

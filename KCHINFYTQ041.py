a=int(input())
b=int(input())
x=[0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0]
i=7
while a!=0:
	x[i]=a%2
	a=a//2
	i=i-1
i=7
while b!=0:
	y[i]=b%2
	b=b//2
	i=i-1
i=0
c=0
while i<len(x) or i<len(y):
	if x[i]!=y[i]:
		c=c+1
	i=i+1
print(c)
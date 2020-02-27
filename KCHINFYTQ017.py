import math
n=int(input())
x=n
s=0
while n!=0:
	d = n % 10
	s = s + math.factorial(d)
	n = n // 10
if s==x:
	print('STRONG')
else:
	print('NOT')


n=int(input())
x=n
s=0
while n!=0:
	d = n % 10
	s = s + (d**3)
	n = n // 10
if s==x:
	print('ARMSTRONG')
else:
	print('NOT')
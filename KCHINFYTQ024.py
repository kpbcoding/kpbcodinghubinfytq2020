n=int(input())
s=0
while n!=0:
	d = n % 10
	if d in (2,3,5,7):
		s = s + d
	n = n // 10
print(s)
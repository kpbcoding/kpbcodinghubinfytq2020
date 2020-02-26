y=int(input())
if y%100==0:
	if y%400==0 and y%4==0:
		print('LEAPYEAR')
	else:
		print('NOT')
else:
	if y%4==0:
		print('LEAPYEAR')
	else:
		print('NOT')

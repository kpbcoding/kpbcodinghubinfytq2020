y=int(input())
if y%4==0:
    if y%100==0:
        if y%400==0:
            print('LEAP YEAR')
        else:
            print('NOT')
    else:
        print('LEAP YEAR')
else:
    print('NOT')
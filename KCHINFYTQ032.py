s=input()
x = [i for i in s if int(i)%5!=0 and int(i)%7!=0]
print(''.join(x))

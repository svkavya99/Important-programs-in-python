n=int(input('ENTER A NUMBER'))
num1=n;result=0
while num1!=0:
    reminder=num1%10
    result+=reminder**3
    num1//=10
if result==n:
    print('given number is armstrong')
else:
    print('given number is not armstrong')

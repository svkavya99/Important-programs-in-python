'''n=int(input('enternum of ur choice'))
n1=n
temp=0;rev =0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(n1==rev):
    print('the number is a palindrome')
else:
    pirnt("not a palindrome!")'''
def palin(str):
    return str[::-1]
n=input('enter a string')
k=palin(n)
if(n==k):
    print('palin')
else:
    print('not a palin')

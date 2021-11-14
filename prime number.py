'''
n=int(input('enter the number'))
if n <2:
    print('not a prime number')
else:
    for i in range(2,n):
        if n%i==0:
            print('not a prime number')
            break
    else:
        print('prime number')

# BY USing while loop
n=int(input('enter the number:'))
count=0
i=1
while (i<=n):
    if n%i==0:
        count= count +1
    i=i+1
if (count==2):
    print('prime number')
else:
    print('not a prime number')

s = 'india is my country'
q = ''
for i in s.split():
    q = q +  i[0].upper()+i[1:-1]+i[-1].upper()+' '
print(q)
'''

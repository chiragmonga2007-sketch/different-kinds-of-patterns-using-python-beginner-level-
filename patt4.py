n=int(input('enter the no. of lines'))
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(0,i):
        print('*',end=' ')
    for j in range(0,i-1):
        print('*',end=' ')
    print()
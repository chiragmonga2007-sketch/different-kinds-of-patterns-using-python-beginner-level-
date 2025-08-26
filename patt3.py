n=int(input('enter the no. of lines'))
for i in range(n):
    for j in range(i+1):
        print('_',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
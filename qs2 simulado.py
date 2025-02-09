n1, n2= map(int,input().split(','))

while n1>=n2:
    for i in range(n1, n2-1, -1):
        print(i, end=' ')
    print()
    for i in range(n2, n1):
        print(i, end=' ')
    print()
    n1 -= 1
    n2 += 1
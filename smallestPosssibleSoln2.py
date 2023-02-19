def solution(a):
    if len(a) == 1:
        return a[0]
    while 1:
        a.sort()
        if a[-1] == a[0]:
            return a[0]*len(a)
        if a[0] == 1:
            return len(a)
        for i,j in enumerate(a):
            y = j % a[0]
            if y != 0:
                a[i] = y
            else:
                a[i] = a[0]



array1 = [6, 9, 12]
solution(array1)
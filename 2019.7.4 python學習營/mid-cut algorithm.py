a = []
while True:
    b = int(input())
    if b == 0:
        break
    a.append(b)
a.sort()
find = int(input('find? :'))
low, high = 0, len(a)
turn = 0
while low < high:
    mid = int((low+high)/2)
    if a[mid] > find:
        high = mid
    elif a[mid] < find:
        low = mid
    else:
        break
    turn += 1
print(a)
print('第',turn+1,'turn 找到')
print(mid)
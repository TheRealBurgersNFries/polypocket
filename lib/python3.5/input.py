xcur = 0
xin = []
for i in range(5):
    xin.append(int(input('Please input a number: ')))
    xcur = xcur + xin[i]
print('Your numbers were: \n')
for i in range(5):
    print(xin[i])
print('Your sum was: \n')
print(xcur)

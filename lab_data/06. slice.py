import numpy as np

# a = [1, 2, 3, 4, 5]

# print(a[1:4]) # 2, 3, 4
# print(a[:-3]) # 1, 2
# print(a[2:]) # 3, 4, 5
# print(a[:]) # 전체

b = np.array(
    [
        ['00', '01', '02', '03'],
        ['10', '11', '12', '13'],
        ['20', '21', '22', '23'],
        ['30', '31', '32', '33'],
    ]
)

# b 변수에 담겨있는 2차원 배열 슬라이싱
print(b[1:3, 1:])
print(b[:2, :])
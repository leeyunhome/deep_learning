# 1.3.8 for 문
# for index in[1, 2, 3]:
#     print(index)

# 1.3.9 함수
# def hello(object):
#     print("Hello " + object + "!")

# hello("neuezeal!")

# print('# 1.4.2 클래스')

# 1.4.2 클래스

# class Man:
#     def __init__(self, name):
#         self.name = name
#         print("Initialized!")

#     def hello(self):
#         print("Hello " + self.name + "!")

#     def goodbye(self):
#         print("Good-bye " + self.name + "!")

# m = Man("Neuezeal")
# m.hello()
# m.goodbye()

# 1.5 넘파이
# print("# 1.5 넘파이")

# import numpy as np

# x = np.array([1.0, 2.0, 3.0])
# print(x)
# print(type(x))

# 1.5.3 넘파이의 산술연산
print(" ")
print("# 1.5.3 넘파이의 산술연산")

import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)  # 원소별 덧셈
print(x - y)  # 원소별 뺄셈
print(x * y)  # 원소별 곱셈
print(x / y)  # 원소별 나눗셈


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
# print(" ")
# print("# 1.5.3 넘파이의 산술연산")

# import numpy as np

# x = np.array([1.0, 2.0, 3.0])
# y = np.array([2.0, 4.0, 6.0])
# print(x + y)  # 원소별 덧셈
# print(x - y)  # 원소별 뺄셈
# print(x * y)  # 원소별 곱셈
# print(x / y)  # 원소별 나눗셈

# x = np.array([1.0, 2.0, 3.0])
# print(x / 2.0)

# 1.5.4 넘파이의 N차원 배열
# print(" ")
# print("# 1.5.4 넘파이의 N차원 배열")

# import numpy as np

# A = np.array([[1, 2], [3, 4]])
# print(A)
# print(A.shape)
# print(A.dtype)

# B = np.array([[3, 0], [0, 6]])
# print(A + B)
# print(A * B)

# print(A)
# print(A * 10)

# 1.5.5 브로드캐스트
# import numpy as np

# A = np.array([[1, 2], [3, 4]])
# B = np.array([10, 20])
# print(A * B)

# 1.5.6 원소 접근

# import numpy as np
# X = np.array([[51, 55], [14, 19], [0, 4]])
# print(X)
# print("X[0] : ", X[0])
# print("X[0][1] : ", X[0][1])

# for row in X:
#     print(row)

# X = X.flatten()
# print(X)
# print(X[np.array([0, 2, 4])])
# print(X>15)
# print(X[X>15])

# 1.6.1 단순한 그래프 그리기
# import numpy as np
# import matplotlib.pyplot as plt

# # 데이터 준비
# x = np.arange(0, 6, 0.1)  # 0에서 6까지 -.1 간격으로 생성
# y = np.sin(x)

# # 그래프 그리기
# plt.plot(x, y)
# plt.show()

# 1.6.2 pyplot의 기능
# import numpy as np
# import matplotlib.pyplot as plt

# # 데이터 준비
# x = np.arange(0, 6, 0.1)  # 0에서 6까지 0.1간격으로 생성
# y1 = np.sin(x)
# y2 = np.cos(x)

# # 그래프 그리기
# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos")  # cos 함수는 점선으로 그리기
# plt.xlabel("x")  # x축 이름
# plt.ylabel("y")  # y축 이름
# plt.title('sin & cos')  # 제목
# plt.legend()
# plt.show()

# 1.6.3 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('img/hodu3.png')
plt.show()

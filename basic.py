# 1.3.8 for 문
for index in[1, 2, 3]:
    print(index)

# 1.3.9 함수
def hello(object):
    print("Hello " + object + "!")

hello("neuezeal!")

print('# 1.4.2 클래스')
# 1.4.2 클래스

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("Neuezeal")
m.hello()
m.goodbye()
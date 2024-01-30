'''
Date: 2024-01-30 09:31:43
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-30 09:34:32
FilePath: \100days-of-python\day-21\main.py
'''
class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("moving in water")
    
    def breath(self):
        super().breath()
        print("doing under the water")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)
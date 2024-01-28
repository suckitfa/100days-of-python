'''
Date: 2024-01-28 12:54:52
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-28 13:51:50
FilePath: \100days-of-python\day-17\main.py
'''
class User:
    # called every time you create a class
    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1
    
    def __str__(self) -> str:
        return f'{self.username} has {self.followers} followers and {self.following} following'


user_1 = User('001','anlgela')
user_2 = User('002','Bob')

user_1.follow(user_2)

print(user_1)
print(user_2)
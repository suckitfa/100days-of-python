# file = open('test.txt')
# contents = file.read()
# print(contents)
# file.close()

with open('test.txt') as file:
    print(file.read())


with open('test.txt',mode='a+') as newFile:
    newFile.write('hello worldddd\n')
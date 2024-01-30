# 100days-of-coding
### day one
- print 
- input
- strings

### day 2
- data types: string,int,float,boolean
- len() func
```py
str()
int()
float()
bool()
```
- math operation order
```py
# PEMDAS
# Parenthese ()
# Exponents **
# Division /
# Addition +
# Subtraction -

8 // 3 # get an int
```
- round()
- f-strings: format strings
```py
print(f'Your age is {age}.')
```
### day 3
- if else
- nested if-else statement
- if elif else
- mulitiple if
```py
if condition:
    do1

if condition2:
    do2
```
- logic operator: and or not

### day 4 random and list
- random, random.ranint(start,end)
- list
- complete the paper rock scissors game
- learn about module system in Python

### day 5 
- for-loops: loop through a list
- new funs: len, sum, range
- PyPassword Generator

### day 06
- code blocks & indent(py prefer space,u can set your editor to support that)
- func: built in funcs and self-def funcs
- while-loop

### day 07
- for & while loop
- if-elif-else
- lists
- strings
- range
- module
- complete the hang man game

### day 08 more about funcs
- funcs with inputs: paramter => argumnet
- positional paramters
- Caesar Cipher

### day 09 DS: dicts,
- dict manipulate a dict, add
- loop the key of the dict
- list in dict
- auction program

### day 10 funcs with outputs
- single return
- multiple returns
- doc string in a func
- while-loops vs recursion

### day 11
- must call the func after it was declared

### day 12
- global scope
- func scope: only avabile inside the func.
- there is no block scope in python: if /for-loop...
```python
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside func: {enemies}")
```
- declare constants

### day 13
- debug
- reproduce the bug 重现BUG
- using a debugger in vscode
- most important: it is okay to get bugs when coding.

### day 16 OOP trying modeling real life objects
- what is has: attributes
- what it does: methods
- class: blue print of objects

### day 21
- class inheritance
```py
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
```
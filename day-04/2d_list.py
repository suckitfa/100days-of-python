emoj_map = [
    ['🪲','🪲','🪲','🪲'],
    ['🪲','🪲','🪲','🪲'],
    ['🪲','🪲','🪲','🪲'],
    ['🪲','🪲','🪲','🪲'],
    ['🪲','🪲','🪲','🪲'],
    ['🪲','🪲','🪲','🪲'],
]
position = input("enter position，serperated by comma: ")
[x_str,y_str] = position.split(',')
x = int(x_str)
y = int(y_str)
emoj_map[x-1][y-1] = "X"
print(emoj_map)
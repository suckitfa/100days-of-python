enemies = "Skeleton"
enemies_count = 1
def increate_enemies():
    global enemies_count
    enemies_count += 1
    enemies = "Zoombie"
    print(f"enemies inside funcs:{enemies}")
    print(f"global enemies count{enemies_count}")
increate_enemies()
print(f"enemies outside funcs:{enemies}")


# modifiy a global variable
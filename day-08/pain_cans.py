import math
test_h = int(input("Height of the wall:"))
test_w = int(input("Width of the wall:"))
coverage = 5

def paint_calc(height,width,cover):
    # round up the nums
    num_of_can = math.ceil((height * width) / cover)
    print(f"We need {num_of_can} cans of paint.")
paint_calc(height=test_h,width=test_w,cover=coverage)
def get_rectangle(length, width):
    if length < 0 or width < 0:
        return -1
    return length * width

length = 8
width = 6

area = get_rectangle(length, width)
print(area)
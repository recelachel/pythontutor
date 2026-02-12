def calculate_area(width, height = None):
    if height is None:
        height = width
    luas = width * height
    return luas

print (calculate_area(4))
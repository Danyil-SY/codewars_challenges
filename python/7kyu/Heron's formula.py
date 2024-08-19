https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

def heron(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)

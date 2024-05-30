def triangle(a, b, c):
    if a + b > c:
        print("Это треугольник")
    elif a + c > b:
        print("Это треугольник")
    elif b + c > a:
        print("Это треугольник")
    else: print("Это не треугольник")


a = input()
b = input()
c = input()
triangle(a,b,c)
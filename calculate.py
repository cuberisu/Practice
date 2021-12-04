# 7장 연습문제 8번
def add(a, b):
    print("(%d + %d)" % (a, b), end=" ")
    return a + b

def subtract(a, b):
    print("(%d - %d)" % (a, b), end=" ")
    return a - b

def multiply(a, b):
    print("(%d * %d)" % (a, b), end=" ")
    return a * b

def devide(a, b):
    print("(%d / %d)" % (a, b), end=" ")
    return a / b

what = add(20, 10)
print("= ", what)
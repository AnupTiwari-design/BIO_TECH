try:
    a = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Type error")

finally:
    print("always execute ")

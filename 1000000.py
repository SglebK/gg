a = int(input("Ведите первое чысло: "))

try:
    b = int(input("Ведите второе чысло: "))
    print(a / b)
except ZeroDivisionError:
    print("error zero")
except Exception as error:
    print(f"ff {error}")
else:
    print("ffffff")
finally:
    print("gffffgfffg")
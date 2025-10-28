try:
    m = 0
    res = 100/m
except ZeroDivisionError:
    print("You Can't Divided By Zero")
except ValueError:
    print("Enter a valid number")
else:
    print("Result is: ", res)
finally:
    print("Execution is Complete")

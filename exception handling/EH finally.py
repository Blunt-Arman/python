try:
    x = int(3)
    Inverse = 1/x
except ZeroDivisionError:
    print("Zero has no Inverse")
except ValueError:
    print("Please Enter an Valid Number")
else:
    print("Inverse of",x,"is",Inverse)
finally:
    print("Execution is Complete")

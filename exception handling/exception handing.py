a = ["10","twenty",30]

try:
    total = int(a[0]+a[2])
except(ValueError,TypeError) as e:
    print("Error",e)
except IndexError:
    print("Index out of range")
else:
    print("Total is:",total)
finally:
    print("Execution is complete")
    

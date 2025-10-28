import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print("--------------------------------")

a = np.array([1,2,6,7,8,9])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,4,5]]])
d = np.array(42)

print(a,"NUMBER OF DIMENTIONS",a.ndim)
print("--------------------------------")
print(b,"NUMBER OF DIMENTIONS",b.ndim)
print("--------------------------------")
print(c,"NUMBER OF DIMENTIONS",c.ndim)
print("--------------------------------")
print(d,"NUMBER OF DIMENTIONS",d.ndim)

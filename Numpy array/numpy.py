import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print('Given array is :','\n',arr,'\n')
print('using ndim() function  showing below output')
print(arr.ndim,'\n')

print('using size() function  showing below output')
print(arr.size,'\n')

print('using dtype() function  showing below output')
print(arr.dtype,'\n')

print('using shape() function  showing below output')
print(arr.shape,'\n')

print('using item size() function  showing below output')
print(arr.itemsize,'\n')

print('using zeros() function  showing below output:','\n')
arr2=np.zeros(5)
print('Given Output are array zeros :','\n',arr2,'\n')

print('using item full() function  showing below output')

a = np.full([2, 2],3)
print(a,'\n')

print('using data() function  showing below output')
print(arr.data,'\n')

import numpy as np
import matmul

A = matmul.readm('A.txt')
b = matmul.readn('b.txt')

def guass(A,b):
    a = np.array(A)
    n = len(a)
    b = np.array(b)
    
    for k in range(0, n-1):
      for i in range(k+1, n):
        if a[i,k] != 0.0:
            lam = a[i,k]/a[k,k]
            a[i,k+1:n] = a[i, k+1:n] - lam*a[k,k+1:n]
            b[i] = b[i] - lam*b[k]
    x=[0]*n
    for k in range(n-1, -1, -1):
      x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x

for i in guass(A,b):
    print(i)
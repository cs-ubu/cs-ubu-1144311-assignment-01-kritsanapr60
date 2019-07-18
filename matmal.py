# 1. read matrix A from 'A.csv'
# 2. read matrix b from 'b.csv'
# 3. find the result of C = A x b
# 4. print

import numpy.linalg as linalg
import numpy as np

import csv


def readm(fname='A.csv'):
    f = open(fname,'r')
    A = []
    for line in f.readlines():
        A.append([ float(x) for x in line.strip().split(',') ])
    f.close()
    return A

def readn(fname='b.csv'):
    f = open(fname,'r')
    b = []
    for line in f.readlines():
        b.append([ float(x) for x in line.strip().split(',') ])
    f.close()
    return b

def matmul(A,b):
    m,n = len(A),len(b[0])
    J = len(A[0])
    if len(A[0]) == len(b):
        C = [ [0]*n for i in range(m) ]
        #A[0][0]*b[0][0] + A[0][1]*b[1][0] + A[0][2]*b[2][0]
        for r in range (m):
            for c in range(n):
                 C[r][c] = sum([ A[r][j]*b[j][c] for j in range(J) ])
        return C




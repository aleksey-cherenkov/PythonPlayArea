import numpy as np
s = np.array([4,1,6])
t = np.array([2,3,5])
r = np.cross(s,t)
print (r)

A = np.array([[1,2,3],
              [4,5,6]])
print (A)
print (A.T)

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([[9,8],
              [7,6],
              [5,4]])
print(np.dot(A,B))
print(A @ B)

D = np.array([[6,1],
              [-2,3]])
E = np.array([[2,3],
              [7,4]])
print (D @ E)

C = np.matrix([[1,7],[-5,3]])
print(C.I)

F = np.matrix([[1,2],
              [2,6]])
G = np.matrix([[3,6],
              [7,1]])              
print(F.I * G)

S = np.matrix([[5,3],
              [6,4]])
T = np.matrix([[1,4],
              [2,6]])              
print(S.I)
print(S.I * T)

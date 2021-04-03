import numpy as np

e = 0.1

A = np.array([[0, 1/3, 0, 0],
              [0, 0, 0, 1/2],
              [0, 1/3, 0, 0],
              [0, 1/3, 0, 1/2]])

ans = np.array([1/4, 1/4, 1/4, 1/4])

for i in range (51):
    ans = (1 - e) * np.dot(A, ans) + e * np.array([1/4, 1/4, 1/4, 1/4])

print (ans)
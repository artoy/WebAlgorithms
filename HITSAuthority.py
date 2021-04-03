import numpy as np

A = np.array([[0, 0, 0, 0],
              [1, 0, 1, 1],
              [0, 0, 0, 0],
              [0, 1, 1, 0]])

matrix = np.dot(A.T, A)

ans = np.array([1, 1, 1, 1])

for i in range (51):
    ans = np.dot(matrix, ans)
    norm = np.linalg.norm(ans)
    ans = ans / norm

print (ans)
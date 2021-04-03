import math
import numpy as np

# Dは文書の集合
# qはクエリ
# wordsは単語の集合
D = ["ABCCCCCCCCCC", "DE", "A", "B", "C", "D", "E"]
q = "ABCDE"
words = ['A', 'B', 'C', 'D', 'E']

# 指定した範囲の文書Dの中の単語wordが含まれている数
def count(D, word):
    value = 0

    for i in range(len(D)):
        if(word in D[i]):
            value += 1

    return value

# d, qベクトルの計算
def dq_vector(d, words, idf):
    vector = []

    for i in range(len(words)):
        vector.append(idf[i] * d.count(words[i]))

    return vector

# ここから実質main関数
idf = []
q_idf = [1] * len(words)
d_vector = []
q_vector = []
sim = []

# idfの計算
for i in range(len(words)):
    idf.append(math.log2(len(D) / count(D, words[i])))

print("idfは%sの順に" %words)
print(idf)
print()

# 文書ベクトルの計算
for i in range(len(D)):
    d_origin = dq_vector(D[i], words, idf)
    d_vector.append(d_origin / np.linalg.norm(d_origin))

for i in range(len(D)):
    print("D%dの文書ベクトルは" %(i+1))
    print(d_vector[i])

print()

# クエリベクトルの計算
q_vector = dq_vector(q, words, q_idf)

print("クエリベクトルは")
print(q_vector)
print()

# simの計算
for i in range(len(D)):
    sim.append(np.dot(d_vector[i], q_vector))

print("simは%sの順に" %D)
print(sim)
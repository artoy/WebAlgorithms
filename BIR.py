# Dは文書の集合
# qはクエリ
# wordsは単語の集合
# nはsimが高い順にいくつ抜き出すか
# loopは何周simを計算するか
D = ["ABCCCCCCCC", "DE", "A", "B", "C", "D", "E"]
q = "ABCDE"
words = ['A', 'B', 'C', 'D', 'E']
n = 2
loop = 2

# 指定した範囲の文書Dの中の単語wordが含まれている数
def count(D, word):
    value = 0

    for i in range(len(D)):
        if(word in D[i]):
            value += 1

    return value

# P(k_i|R)の計算
def PR(A, D, word, n):
    probability = count(A, word) / n

    if (probability == 0 or probability == 1):
        print("注意!! P(%s|R)が%dになっています!!" %(word, probability))
        return (count(A, word) + (count(D, word) / len(D))) / (n + 1)
    else:
        return probability

# P(k_i|\overline{R})の計算
def PRbar(A, D, word, n):
    probability = (count(D, word) - count(A, word)) / (len(D) - n)

    if (probability == 0 or probability == 1):
        print("注意!! P(%s|Rbar)が%dになっています!!" %(word, probability))
        return (count(D, word) - count(A, word) + (count(D, word) / len(D))) / (len(D) - n + 1)
    else:
        return probability

# simの計算
def sim(PR_list, PRbar_list, words, d, q):
    simv = 1

    for i in range(len(words)):
        if(words[i] in d and words[i] in q):
            simv *= (PR_list[i] / (1 - PR_list[i])) / (PRbar_list[i] / (1 - PRbar_list[i]))

    return simv


# ここから実質main関数
sim_list = []
A = [0] * n
PR_list = [0] * len(words)
PRbar_list = [0] * len(words)

# simの初期値計算(スライドのp30に載ってる方法)
for i in range(len(D)):
    simv = 1

    for j in range(len(words)):
        if(words[j] in D[i] and words[j] in q):
            simv *= (len(D) - count(D, words[j])) / count(D, words[j])

    sim_list.append(simv)

print("simの初期値は")
print(sim_list)
print()

for i in range(loop):
    print("%dループ目" %(i+1))

    # simの上位n文書を取得
    sim_n = sorted(sim_list, reverse=True)[:n]

    for j in range(n):
        A[j] = D[sim_list.index(sim_n[j])]

    print("simの上位%d個は" %n)
    print(A)
    print()

    # P(k_i|R), P(k_i|\overline{R})の更新
    for j in range(len(words)):
        PR_list[j] = PR(A, D, words[j], n)
        PRbar_list[j] = PRbar(A, D, words[j], n)

    print("%sの順に" %words)
    print("P(k|R)は%s" %PR_list)
    print("P(k|Rbar)は%s" %PRbar_list)
    print()

    # simの更新
    for j in range(len(D)):
        sim_list[j] = sim(PR_list, PRbar_list, words, D[j], q)

    print("%sの順に" %D)
    print("simは%s" %sim_list)
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print()

print("最終的なsimは")
print(sim_list)
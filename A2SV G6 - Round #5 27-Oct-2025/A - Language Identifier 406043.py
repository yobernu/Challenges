# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t = int(input())
for _ in range(t):
    word = input()
    n = len(word)
    if word[n-2:] == "po":
        print("FILIPINO")
    elif word[n-4:] == "desu" or word[n-4:] == "masu":
        print("JAPANESE")
    elif word[n-5:] == "mnida":
        print("KOREAN")
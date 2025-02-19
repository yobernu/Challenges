# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
persons = []
for _ in range(n):
    p = input()
    persons.append(p)
# persons[::-1]
rev = persons[::-1]
s = set()
for person in rev:
    if person not in s:
        s.add(person)
        print(person)


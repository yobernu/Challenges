# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

n = int(input())
s = input()
ones = 0
zeros = 0
for i in s:
    if i == "n":
        ones += 1
    elif i == "z":
        zeros += 1
ans = []
if ones:
    for i in range(ones):
        ans.append(1)
if zeros:
    for i in range(zeros):
        ans.append(0)
print(*ans)
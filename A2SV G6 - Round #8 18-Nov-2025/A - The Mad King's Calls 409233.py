# Problem: A - The Mad King's Calls - https://codeforces.com/gym/599383/problem/A

t = int(input())
for _ in range(t):
    num = int(input())
    ans = []
    flag = False
    for i in range(1, 10):
        for j in range(1, 5):
            temp = str(i)*j
            ans.append(int(temp))
            if int(temp) == num:
                flag = True
                break
        if flag:
            break
    res = 0
    for i in ans:
        res += len(str(i))
    print(res)


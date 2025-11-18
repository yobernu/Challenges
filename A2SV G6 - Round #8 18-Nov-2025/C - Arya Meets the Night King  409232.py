# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C


s, b = map(int, input().split())
attacks = list(map(int, input().split()))

i_att = sorted(enumerate(attacks), key=lambda x: x[1])
ans = [0] * s
bon = [tuple(map(int, input().split())) for _ in range(b)]
bon.sort()
c_bon = []
tot = 0

for d, g in bon:
    tot += g
    c_bon.append((d, tot))
i = 0  
tot = 0
for index, attack in i_att:
    while i < b and c_bon[i][0] <= attack:
        tot = c_bon[i][1]
        i += 1
    ans[index] = tot  

print(*ans)

# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
stones = list(map(int, input().split()))
sorted_stones = sorted(stones)

stones_cumsum = [0]
for i in range(n):
    stones_cumsum.append(stones_cumsum[-1] + stones[i])

sorted_stones_cumsum = [0]
for i in range(n):
    sorted_stones_cumsum.append(sorted_stones_cumsum[-1] + sorted_stones[i])
m = int(input())
for _ in range(m):
    type, l, r = map(int, input().split())
    if type == 2:
        print(sorted_stones_cumsum[r] - sorted_stones_cumsum[l-1])
    else:
        print(stones_cumsum[r] - stones_cumsum[l-1])

    
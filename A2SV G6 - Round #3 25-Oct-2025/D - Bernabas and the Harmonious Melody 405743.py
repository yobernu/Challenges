# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def count_deletions(c):
    l, r = 0, n - 1
    deleted = 0
    while l < r:
        if melodies[l] != melodies[r]:
            if melodies[l] == c:
                deleted += 1
                l += 1
            elif melodies[r] == c:
                deleted += 1
                r -= 1
            else:
                return float('inf')
        else:
            l += 1
            r -= 1
    
    return deleted

t = int(input())
for _ in range(t):
    n = int(input())
    melodies = input()

    is_palindrome = True
    l, r = 0, n - 1
    while l < r:
        if melodies[l] != melodies[r]:
            is_palindrome = False
            break
        l += 1
        r -= 1
    
    if is_palindrome:
        print(0)
    else:
        deleted1 = count_deletions(melodies[l])
        deleted2 = count_deletions(melodies[r])

        ans = min(deleted1, deleted2)

        print(ans if ans != float('inf') else -1)
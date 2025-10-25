# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out_lines = []
    for _ in range(t):
        n = next(it); k = next(it); d = next(it)
        a = [next(it) for _ in range(n)]

        freq = {}
        distinct = 0
        
        # initiate [first window]
        for i in range(d):
            x = a[i]
            if freq.get(x, 0) == 0:
                distinct += 1
            freq[x] = freq.get(x, 0) + 1

        ans = distinct

        for i in range(d, n):
            out_elem = a[i - d]
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                distinct -= 1
                del freq[out_elem]

            in_elem = a[i]
            if freq.get(in_elem, 0) == 0:
                distinct += 1
            freq[in_elem] = freq.get(in_elem, 0) + 1

            if distinct < ans:
                ans = distinct
                if ans == 1: 
                    break
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))
if __name__ == "__main__":
    main()

# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    h = [0] + list(map(int, data[1:1+n]))  
    dp = [0] * (n + 1)
    dp[2] = abs(h[2] - h[1])
    
    for i in range(3, n + 1):
        dp[i] = min(
            dp[i-1] + abs(h[i] - h[i-1]),
            dp[i-2] + abs(h[i] - h[i-2])
        )
    
    print(dp[n])

if __name__ == "__main__":
    main()
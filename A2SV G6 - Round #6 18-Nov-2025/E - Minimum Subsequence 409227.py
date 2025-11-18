# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

import  sys
def solve():
    n = int(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().strip()]

    zero = []   
    one = []    
    ans = []    
    maxi = 0 
    for val in nums:
        if val == 1:  # If the current character is '1'
            if zero:
                # If there exists a subsequence ending in '0', use it
                temp = zero.pop()
            else:
                # Otherwise, create a new subsequence
                maxi += 1
                temp = maxi 
              
            # Mark that this subsequence now ends in '1'
            one.append(temp)
            ans.append(temp)

        else:  # If the current character is '0'
            if one:
                # If there exists a subsequence ending in '1', use it
                temp = one.pop()
            else:
                # Otherwise, create a new subsequence
                maxi += 1
                temp = maxi 

            # Mark that this subsequence now ends in '0'
            zero.append(temp)
            ans.append(temp)

    # Print the total number of subsequences used
    print(max(ans))
    
    # Print the assigned subsequence number for each character
    print(*ans)

q = int(sys.stdin.readline().strip())

for _ in range(q):
    solve()
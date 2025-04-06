# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())
for _ in range(t):
    left, right = map(str, input().split())
    cl, cr = 0, 0
    for i in left:
        if i == "X":
            cl += 1
    for i in right:
        if i == "X":
            cr += 1
    if left[-1] == right[-1]:
        if left[-1] == "S":
            if cl > cr:
                print("<")
            elif cl < cr:
                print(">")
            else:
                print("=")
        elif left[-1] == "M":
            print("=")
        elif left[-1] == "L":
            if cl > cr:
                print(">")
            elif cl < cr:
                print("<")
            else:
                print("=")
    else:
        order = {'S': 0, 'M': 1, 'L': 2}

        if order[left[-1]] > order[right[-1]]:
            print(">")
        elif order[left[-1]] < order[right[-1]]:
            print("<")
        else:
            print("=")


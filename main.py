def canGetSolution() -> bool:
    n = int(input())
    mountain_top = []
    branch = []
    for i in range(n):
        mountain_top.append(int(input()))

    i = 1

    while i <= n:
        if mountain_top and mountain_top[-1] == i:
            mountain_top.pop()
            i += 1
        elif branch and branch[-1] == i:
            branch.pop()
            i += 1
        elif mountain_top:
            temp = mountain_top.pop()
            branch.append(temp)
        elif branch:
            return False
        else:
            return True
    return True


n = int(input())
for i in range(n):
    if canGetSolution():
        print('Y')
    else:
        print('N')


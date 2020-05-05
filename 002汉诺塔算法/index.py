def hanoi(n, x, y, z):
    if n == 1:
        print(x, '----->', z)
    else: # 将前n-1的盘子移动从x到y上
        hanoi(n-1, x, z, y)
        print(x, '----->', z)
        hanoi(n-1, y, x, z)
hanoi(3,'X','Y','Z')
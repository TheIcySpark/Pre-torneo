if __name__ == '__main__':
    s = 0
    for i in range(int(input())):
        num = int(input().split('.')[1])
        s += num
    print(s)

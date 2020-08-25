def Function(b):
    count = 0
    for i in range(len(b) - 1):
        if b[i] == '1':
            b[i] = '0'
            if b[i + 1] == '0':
                b[i + 1] = '1'
            else:
                b[i + 1] = '0'

            count += 1
            print(b)
    print(b)
    print(count, " steps required")


if __name__ == '__main__':
    a = list("11111111111111111111")
    print(a)
    Function(a)

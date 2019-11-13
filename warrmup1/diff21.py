def diff21(n):
    difference = abs(n - 21)
    if difference < 22:
        return difference
    else:
        return difference * 2


if __name__ == '__main__':
    print(diff21(-1))

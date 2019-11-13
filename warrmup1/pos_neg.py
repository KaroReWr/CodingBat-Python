def pos_neg(a, b, negative):
    return ((a < 0 and b > 0) or (a > 0 and b < 0) and negative == False)  or ((a < 0 and b < 0) and negative == True)


if __name__ == '__main__':
    a = "no"
    if a[:3] != "not":
        print("not " + a)
    else:
        print(a)
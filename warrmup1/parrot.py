def parrot_trouble(talking, hour):
    if talking == True and (7 > hour or hour > 20):
        return True
    else:
        return False

if __name__ == '__main__':
    print(parrot_trouble(True,22))
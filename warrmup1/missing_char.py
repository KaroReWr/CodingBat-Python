def missing_char(str, n):
  if n >= len(str):
    return str
  else:
    return str[:n] + str[(n+1):]


if __name__ == '__main__':
    a = "kot"
    a.replace(a[1],"jk")
    print(a)
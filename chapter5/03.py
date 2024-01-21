for i in range(9):
  num=i+1
  for j in range(9):
    col=j+1
    print(num*col, end='')
    if j == 8:
      print()
    else:
      print(' ', end='')


## 解答例
# for i in range(1, 10):
#   for j in range(1, 10):
#     if j == 9:
#       print(i * j)
#     else:
#       print(i * j, end = ' ')
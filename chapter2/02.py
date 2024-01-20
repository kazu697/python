# 1 2 3 4 5 6 7 8 9 10 を出力する
# 末尾にスペースがある
str = ''
for i in range(1, 11):
  str += "{0} ".format(i)
print(str)
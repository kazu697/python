# 大きな数値 N を3 けたごとにカンマ区切りで出力
# pythonのテクニックを使う

# N=int(input())
# print(f"{N:,}")


## 回答例
## 長さを桁数で割ったあまりを求めて上から順に出力していく
N=input()
# N='12345'
keta=3
# 桁数を割ったあまりを出して3の倍数でない
x=len(N) % keta
for i in range(len(N)):
  if (i - x) % keta == 0 and i != 0:
    print(',', end='')
  print(N[i], end='')
print()
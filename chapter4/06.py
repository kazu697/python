# 大きな数値 N を3 けたごとにカンマ区切りで出力
# pythonのテクニックを使う

# N=int(input())
# print(f"{N:,}")


## 回答例
## これ3の倍数桁じゃないときうまく出力されない気がする。。
N=input()
keta=3
for i in range(len(N)):
  if i % keta == 0 and i != 0:
    print(',', end='')
  print(N[i], end='')
print()
# 10 個の数値が半角スペース区切りのものをカンマ区切りにしてください。

# line=input()
# str = ''
# for i in line.split(' '):
#   str += i + ','
# print(str)


## ベスト

nums = input().split()
for num in nums:
    print(num, end=',')

print()

## sepのテクニック
## 配列をある文字で結合するのであればjoinを使わないでも下記のようにするのもいいかも
## アンパックの方法 *[]
# L = [1, 2, 3, 4, 5]
# print(*L, sep=' ')
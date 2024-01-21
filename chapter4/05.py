# 10 個の数値が改行区切りの数値を半角スペース 2 つとバーティカルライン | 区切りで出力

N=10
L=[]
for i in range(N):
  L.append(input())
print(*L, sep=' | ')


## 参考例

# for i in range(10):
#     if i == 9:
#         print(input())
#     else:
#         print(input(), end=" | ")
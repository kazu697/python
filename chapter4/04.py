# 10 個の数値が半角スペース区切りのものをカンマ区切りにしてください。末尾は開業にすること

line=input().split()
print(*line, sep=',')

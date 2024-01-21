N=int(input())
M=list(map(int, input().split()))

for i in range(N):
  for j in range(1, M[i]+1):
    if j == M[i]:
      print(j)
    else:
      print(j, end=' ')
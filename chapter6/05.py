[N,M]=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

head=0
for i in B:
  for j in range(i):
    if j == i - 1:
      print(A[head])
    else:
      print(A[head], end=' ')
    head += 1
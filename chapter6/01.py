N=int(input())

for i in range(1, N+1):
  if i % (N//2) == 0:
    print(i)
  else:
    print(i, end=' ')
[N, M] = map(int, input().split())

for i in range(1, N+1):
  if i == N:
    print(i)
  else:
    print(i, end=' ')
for i in range(1, M+1):
  if i == M:
    print(i)
  else:
    print(i, end=' ')
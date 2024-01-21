nums=input().split()
col=3

for i in range(len(nums)):
  if (i+1) % col != 0:
    print(nums[i], end=' ')
  elif (i+1) % col == 0:
    print(nums[i])



## 回答例
    
nums=input().split()

for i in range(len(nums)):
  print(nums[i], end='')
  if i % 3 == 2:
    print()
  else:
    print(' ', end='')
n = int(input())
arr = map(int, input().split())


arr = list(arr)
maxnum= -100   
runner_up = -100

for x in arr:
    if x > maxnum:
        runner_up = maxnum
        maxnum = x
    elif x< maxnum and x > runner_up:
        runner_up = x    
print(runner_up) 

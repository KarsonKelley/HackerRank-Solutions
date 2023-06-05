n = 5
a, b, c, d, e = 5, 3, 6, 2, 2 #sample inputs
arr = [a,b,c,d,e]

arr.sort()
runner_up = arr[n-1]
while n > 0:
    if arr[n-1] < runner_up:
        runner_up = arr[n-1]
        break
    n = n-1
print(runner_up)
    




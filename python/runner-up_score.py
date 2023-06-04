n = 5
a, b, c, d, e = 5, 3, 6, 2, 2 #sample inputs
scores_ar = [a,b,c,d,e]

scores_ar.sort()
runner_up = scores_ar[n-1]
while n > 0:
    if scores_ar[n-1] < runner_up:
        runner_up = scores_ar[n-1]
        break
    n-=1
print(runner_up)





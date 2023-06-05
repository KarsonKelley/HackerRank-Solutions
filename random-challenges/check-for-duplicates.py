numbers = [2,2,4,6,3,4,6,1]
i = 0
while i < len(numbers):
    if numbers.count(numbers[i]) > 1:
        numbers.remove(numbers[i])
    i+=1
    

print(numbers)

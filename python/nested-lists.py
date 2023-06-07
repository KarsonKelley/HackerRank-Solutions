records = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score]) 
      
grades = []
names = []
for entry in records:
    grades.append(entry[1])
grades.sort()
for value in grades:
    if value != min(grades):
        min_grade = value
        break
for entry in records:
    if entry[1] == min_grade:
        names.append(entry[0])
names.sort()
i = 0
while i < len(names):
    print(names[i])
    i+=1
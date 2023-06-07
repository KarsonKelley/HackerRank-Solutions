if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
average = 0
selected_scores = student_marks[query_name]
for value in selected_scores:
    average+=value
average /= len(selected_scores)
formatted_average= f'{average:.2f}'
print(formatted_average)


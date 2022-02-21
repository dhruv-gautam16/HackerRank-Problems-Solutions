if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score]) 
    x = 99999
    for i in range(len(students)):
        if x > float(students[i][1]):
            x = float(students[i][1])
    y = 999999
    for i in range(len(students)):
        if float(students[i][1]) > float(x) and y > float(students[i][1]):
            y = float(students[i][1])
    runner = []
    for i in range(len(students)):
        if float(students[i][1]) == float(y):
            runner.append(students[i][0])
    runner = sorted(runner)

    for i in range(len(runner)):
        print(runner[i])

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
   
    scores = sorted(set([s[1] for s in students]))
    
  
    second_lowest_score = scores[1]
    
    names = []
    for student in students:
        if student[1] == second_lowest_score:
            names.append(student[0])
            
    names.sort()
    for name in names:
        print(name)
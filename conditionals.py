def check_grade(score):
    if score >= 90:
        if score == 100:
            grade = "A+"
        else:
            grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

score=int(input("Enter a score = "))
result = check_grade(score)
print(result)
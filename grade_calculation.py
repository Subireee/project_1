def calculate_grade(score):
    if score >= 80:
        return 'A+'
    elif 70 <= score < 80:
        return 'A'
    elif 65 <= score < 70:
        return 'A-'
    elif 60 <= score < 65:
        return 'B'
    elif 50 <= score < 60:
        return 'B-'
    elif 40 <= score < 50:
        return 'C'
    elif 33 <= score < 40:
        return 'D'
    else:
        return 'F'

try:
    score = float(input("Enter the student's score: "))

    if score < 0 or score > 100:
        print("Please enter a valid score between 0 and 100.")
    else:
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")

except ValueError:
    print("Please enter a valid numerical score.")
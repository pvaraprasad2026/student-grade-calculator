# Grade Calculation Modulegit add .
def calculate_grade(percentage):
    if marks1 < 0 or marks1 > 100:
         print("Invalid Marks")
    elif percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


name = input("Enter Student Name: ")

marks1 = float(input("Subject 1 Marks: "))
marks2 = float(input("Subject 2 Marks: "))
marks3 = float(input("Subject 3 Marks: "))

total = marks1 + marks2 + marks3
percentage = total / 3

grade = calculate_grade(percentage)

print("\nStudent Report")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
print("Grade:", grade)
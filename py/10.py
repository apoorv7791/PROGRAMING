# WAP to store students information like admission number, roll number, name and marks in a dictionary and display information on the basis of admission number.


admision = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    adm_no = int(input("Enter the admission number: "))
    roll_no = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    admision[adm_no] = [roll_no, name, marks]
print(admision)
adm_no = int(input("Enter the admission number to display information: "))
if adm_no in admision:
    print(admision[adm_no])
else:
    print("Admission number not found.")

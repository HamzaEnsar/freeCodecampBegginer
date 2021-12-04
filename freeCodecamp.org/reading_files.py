empolyee_file = open("employees.txt", "r")
for employee in empolyee_file.readlines():
    print(employee)
#print(empolyee_file.readlines()[0])

empolyee_file.close()

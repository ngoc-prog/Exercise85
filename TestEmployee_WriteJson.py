from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Employee import Employee

employees=[]
employees.append(Employee("E1","Tèo","teo","123"))
employees.append(Employee("E2","Tý","ty","789"))
employees.append(Employee("E3","Bin","bin","456"))
employees.append(Employee("E4","Bo","bo","abc1"))
employees.append(Employee("E5","Bủn","bun","x@123"))
employees.append(Employee("E6","Rủn","run","y1231"))
print("Danh sách Employee:")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename="../dataset/employees.json"
jff.write_data(employees,filename)
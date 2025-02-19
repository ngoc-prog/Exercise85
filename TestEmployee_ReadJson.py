from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Employee import Employee

jff=JsonFileFactory()
filename="../dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("Danh sách Employee sau khi đọc file:")
for e in employees:
    print(e)
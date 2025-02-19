from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Employee_Asset import Employee_Asset

eas=[]
eas.append(Employee_Asset("E1","AS1","MAIN"))
eas.append(Employee_Asset("E2","AS2","MAIN"))
eas.append(Employee_Asset("E3","AS3","MAIN"))
eas.append(Employee_Asset("E4","AS4","MAIN"))
eas.append(Employee_Asset("E5","AS5","MAIN"))
eas.append(Employee_Asset("E6","AS6","MAIN"))
eas.append(Employee_Asset("E1","AS3","MAIN"))
eas.append(Employee_Asset("E3","AS7","MAIN"))
eas.append(Employee_Asset("E5","AS2","MAIN"))
eas.append(Employee_Asset("E4","AS5","MAIN"))

print("Danh sách phân công quản lý tài sản:")
for ea in eas:
    print(ea)

jff=JsonFileFactory()
filename="../dataset/employee_assets.json"
jff.write_data(eas,filename)
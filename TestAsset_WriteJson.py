from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Asset import Asset

assets=[]
assets.append(Asset("AS1","Máy chiếu 1",2017,18))
assets.append(Asset("AS2","Máy chiếu 2",2017,17))
assets.append(Asset("AS3","Máy tính 1",2024,20))
assets.append(Asset("AS4","Máy tính 2",2019,20))
assets.append(Asset("AS5","Máy ảnh 1",2018,10))
assets.append(Asset("AS6","Máy ảnh 2",2018,5))
assets.append(Asset("AS7","Xe hơi ",2021,100))
print("Danh sách tài sản:")
for a in assets:
    print(a)
jff=JsonFileFactory()
filename="../dataset/assets.json"
jff.write_data(assets,filename)
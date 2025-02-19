from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Asset import Asset

jff=JsonFileFactory()
filename="../dataset/assets.json"
assets=jff.read_data(filename,Asset)
print("Tài sản sau khi đọc từ file:")
for a in assets:
    print(a)
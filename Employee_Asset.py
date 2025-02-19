class Employee_Asset:
    def __init__(self,EmployeeId, AssetId, Role):
        self.EmployeeId=EmployeeId
        self.AssetId=AssetId
        self.Role=Role
    def __str__(self):
        return f"{self.EmployeeId}\t{self.AssetId}\t{self.Role}"
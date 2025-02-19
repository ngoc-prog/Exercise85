class Asset:
    def __init__(self,AssetId, AssetName, ImportYear, Value):
        self.AssetId=AssetId
        self.AssetName=AssetName
        self.ImportYear=ImportYear
        self.Value=Value
    def __str__(self):
        return f"{self.AssetId}\t{self.AssetName}"
import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chapter4_oop.exercise85.libs.DataConnector import DataConnector
from chapter4_oop.exercise85.libs.JsonFileFactory import JsonFileFactory
from chapter4_oop.exercise85.models.Asset import Asset
from chapter4_oop.exercise85.ui.MainWindow85 import Ui_MainWindow


class MainWindow85Ext(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.assets=self.dc.get_all_assets()
        self.selected_asset=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.setupSignalAndSlot()

        self.hienthi_sanpham_len_giaodien()

    def showWindow(self):
        self.MainWindow.show()
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def hienthi_sanpham_len_giaodien(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.assets)):
            sp=self.assets[i]
            btn=QPushButton(text=str(sp))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet,sp))
    def xem_chi_tiet(self,sp):
        self.lineEditId.setText(sp.AssetId)
        self.lineEditName.setText(sp.AssetName)
        self.lineEditYear.setText(str(sp.ImportYear))
        self.lineEditValue.setText(str(sp.Value))
        self.selected_asset=sp

    def setupSignalAndSlot(self):
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonSave.clicked.connect(self.xuly_luu)
    def xuly_xoa(self):
        msp=self.lineEditId.text()

        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Ê, muốn xóa tài sản [{msp}] hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button=dlg.exec()
        if button==QMessageBox.StandardButton.No:
            return #ngừng hàm xóa, ko làm gì cả
        if self.selected_asset!=None:
            self.assets.remove(self.selected_asset)
            #cập nhật lại CSDL sau khi xóa:
            # cần lưu lại cơ sở dữ liệu:
            jff = JsonFileFactory()
            filename = "../dataset/assets.json"
            jff.write_data(self.assets, filename)

            self.hienthi_sanpham_len_giaodien()
    def xuly_luu(self):
        id=self.lineEditId.text()
        name=self.lineEditName.text()
        year=int(self.lineEditYear.text())
        value=int(self.lineEditValue.text())
        a=Asset(id,name,year,value)
        self.assets.append(a)
        #cần lưu lại cơ sở dữ liệu:
        jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        jff.write_data(self.assets, filename)
        self.hienthi_sanpham_len_giaodien()

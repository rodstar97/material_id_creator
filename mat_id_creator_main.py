from utils.convert_ui_files import convert
#from ui.qtd_main import Ui_sbrys_main_qw
#from sbrysMainWidget import *
import os, sys
from PySide import QtGui,QtCore
from ui.mc_main import Ui_MainWindow
from mc_material_widget import Material_widget

class ControlMainWindow(QtGui.QMainWindow):
    """
        MainWindow for Asset import, QWidget for docking
    """
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_ui_functions()

        for i in range(5):
            self.add_material_id_widget(locked=True)

        for item in self.iterAllMaterialIds():
            self.ui.materiIds_LW.update()
            if item.locked :
                item.lock()
            self.ui.materiIds_LW.update()
            self.update()

    def connect_ui_functions(self):

        self.ui.addMatPB.clicked.connect(self.add_material_id_widget)
        self.ui.saveFilePB.clicked.connect(self.test)


    def add_material_id_widget(self, locked=False):
        if locked:
            itemN = QtGui.QListWidgetItem()
            matWidget = Material_widget(locked=False)#Should be locked
            itemN.setSizeHint(matWidget.sizeHint())
            self.ui.materiIds_LW.addItem(itemN)
            self.ui.materiIds_LW.setItemWidget(itemN, matWidget)
            self.ui.materiIds_LW.update()
        else:
            itemN = QtGui.QListWidgetItem()
            matWidget = Material_widget()
            itemN.setSizeHint(matWidget.sizeHint())
            self.ui.materiIds_LW.addItem(itemN)
            self.ui.materiIds_LW.setItemWidget(itemN, matWidget)
            self.ui.materiIds_LW.update()

    def test(self):
        for item in self.iterAllMaterialIds():
            print item

    def iterAllMaterialIds(self):
        for i in range(self.ui.materiIds_LW.count()):
            yield self.ui.materiIds_LW.itemWidget(self.ui.materiIds_LW.item(i))














if __name__ == '__main__':
    import sys, os
    from utils.convert_ui_files import convert


    '''Convert UI Files'''
    pwd = os.path.dirname(os.path.realpath(__file__))
    ui_files = os.path.join(pwd, 'ui')
    print ui_files
    convert(ui_files)

    '''Show GUI'''
    app = QtGui.QApplication(sys.argv)
    app.setStyle('Plastique')
    myWidget =  ControlMainWindow()
    myWidget.show()
    app.exec_()




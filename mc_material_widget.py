from ui.mc_material_id import Ui_mc_material_wg
from PySide import QtCore, QtGui
from color_button import QColorButton





class Material_widget(QtGui.QWidget,Ui_mc_material_wg):
    """
        MainWindow for Asset import, QWidget for docking
    """
    def __init__(self, locked = False):
        super(Material_widget, self).__init__()
        self.setupUi(self)
        colorB = QColorButton()
        self.horizontalLayout.addWidget(QColorButton())
        self.locked = locked
        self.connect_ui_functions()

    def connect_ui_functions(self):
        pass
        #self.lockedCB.toggled.connect(self.toggle_lock)


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            pass
            #self.toggle_lock()
            #do what you want here
            #if self.dis

    def lock(self):
        for child in self.children():
            if child.objectName() != 'lockedCB':
                child.setEnabled(False)

    def toggle_lock(self):
        if not self.locked:
            for child in self.children():
                if child.objectName() != 'lockedCB':
                    child.setEnabled(False)
            self.locked = 1
        else:
            for child in self.children():
                if child.objectName() != 'lockedCB':
                    child.setEnabled(True)
            self.locked = 0
        self.window().update()

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
    myWidget =  Material_widget()
    myWidget.show()
    app.exec_()
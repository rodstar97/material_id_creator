from PySide import QtCore, QtGui


class QColorButton(QtGui.QPushButton):
    '''
    Custom Qt Widget to show a chosen color.

    Left-clicking the button shows the color-chooser, while
    right-clicking resets the color to None (no-color).
    '''

    colorChanged = QtCore.Signal() #.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        self._color = None
        self.setMaximumWidth(52)
        self.pressed.connect(self.onColorPicker)

    def setColor(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

        if self._color:
            self.setStyleSheet("background-color: %s;" % self._color)
        else:
            self.setStyleSheet("")

    def color(self):
        return self._color

    def onColorPicker(self):
        '''
        Show color-picker dialog to select color.

        Qt will use the native dialog by default.

        '''
        dlg = QtGui.QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QtGui.QColor(self._color))

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

    def mousePressEvent(self, e):
        #if e.button() == QtGui.Qt.RightButton:
            #self.setColor(None)

        return super(QColorButton, self).mousePressEvent(e)


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
    myWidget =  QColorButton()
    myWidget.show()
    app.exec_()
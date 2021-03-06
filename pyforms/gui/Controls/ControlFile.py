#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyforms.gui.Controls.ControlText import ControlText
import pyforms.utils.tools as tools
from PyQt4 import uic
from PyQt4.QtGui import QFileDialog

__author__ = "Ricardo Ribeiro"
__copyright__ = ""
__credits__ = "Ricardo Ribeiro"
__license__ = "MIT"
__version__ = "0.0"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mão de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"

from pysettings import conf

class ControlFile(ControlText):

    def init_form(self):
        control_path = tools.getFileInSameDirectory(__file__, "fileInput.ui")
        self._form = uic.loadUi(control_path)
        self._form.label.setText(self._label)        
        self._form.pushButton.clicked.connect(self.click)
        self.form.lineEdit.editingFinished.connect(self.finishEditing)
        self._form.pushButton.setIcon(conf.PYFORMS_ICON_FILE_OPEN)

    def finishEditing(self):
        """Function called when the lineEdit widget is edited"""
        self.changed_event()

    def click(self):
        value = str(QFileDialog.getOpenFileName(
            self._form, self._label, self.value))
        if value:
            self.value = value

    @property
    def parent(self): return ControlText.parent.fget(self, value)

    @parent.setter
    def parent(self, value):
        ControlText.parent.fset(self, value)

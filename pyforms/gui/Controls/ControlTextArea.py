#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyforms.utils.tools as tools
from PyQt4 import uic
from pyforms.gui.Controls.ControlBase import ControlBase

__author__ = "Ricardo Ribeiro"
__credits__ = ["Ricardo Ribeiro"]
__license__ = "MIT"
__version__ = "0.0"
__maintainer__ = "Ricardo Ribeiro"
__email__ = "ricardojvr@gmail.com"
__status__ = "Development"


class ControlTextArea(ControlBase):

    def init_form(self):
        control_path = tools.getFileInSameDirectory(__file__, "textArea.ui")
        self._form = uic.loadUi(control_path)
        self._form.label.setText(self._label)
        if self._value:
            self._form.plainTextEdit.setPlainText(str(self._value))

        if not self._label or len(self._label)==0: 
            self.form.label.hide()

        super(ControlTextArea, self).init_form()
        self.form.plainTextEdit.textChanged.connect(self.finishEditing)

    def __add__(self, other):
        self._form.plainTextEdit.appendPlainText(str(other))
        return self

    def finishEditing(self):
        """Function called when the lineEdit widget is edited"""
        self.changed_event()
        

    @property
    def value(self):
        return self._form.plainTextEdit.toPlainText()

    @value.setter
    def value(self, value):
        self._form.plainTextEdit.setPlainText(str(value))

    @property
    def readonly(self):
        return self._form.plainTextEdit.isReadOnly()

    @readonly.setter
    def readonly(self, value):
        self._form.plainTextEdit.setReadOnly(value)

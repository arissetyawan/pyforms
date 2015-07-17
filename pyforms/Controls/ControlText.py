#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Ricardo Ribeiro
@credits: Ricardo Ribeiro
@license: MIT
@version: 0.0
@maintainer: Ricardo Ribeiro
@email: ricardojvr@gmail.com
@status: Development
@lastEditedBy: Carlos Mão de Ferro (carlos.maodeferro@neuro.fchampalimaud.org)
'''

from pyforms.Controls.ControlBase import ControlBase


class ControlText(ControlBase):

    def initForm(self):
        super(ControlText, self).initForm()
        self.form.lineEdit.editingFinished.connect(self.finishEditing)

    def finishEditing(self):
        """Function called when the lineEdit widget is edited"""
        self.changed()

    ###################################################################
    ############ Properties ###########################################
    ###################################################################

    @property
    def value(self):
        self._value = str(self._form.lineEdit.text())
        return self._value

    @value.setter
    def value(self, value):
        self._form.lineEdit.setText(value)
        ControlBase.value.fset(self, value)

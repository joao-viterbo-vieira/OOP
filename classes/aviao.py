# -*- coding: utf-8 -*-
"""
Created on Sun May 29 22:26:25 2022

@author: costa
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Aviao(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # Attribute names list, identifier attribute must be the first one
    att = ['_modelo','_n_lugares','_codigo']
    # auto_number = 1      # Uncomment in case of auto number on
    # Constructor: Called when an object is instantiated
    def __init__(self, modelo, n_lugares, codigo):
        super().__init__()
        # Object attributes
        self._modelo = modelo
        self._n_lugares = n_lugares
        self._codigo = codigo
        # Add the new object to the dictionary of objects
        Aviao.obj[modelo] = self
        # Add the code to the list of object codes
        Aviao.lst.append(modelo)

    # modelo property getter method
    @property
    def modelo(self):
        return self._modelo
    # modelo property setter method
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    # n_lugares property getter method
    @property
    def n_lugares(self):
        return self._n_lugares
    # n_lugares property setter method
    @n_lugares.setter
    def name(self, n_lugares):
        self._n_lugares = n_lugares
    # codigo property getter method
    @property
    def codigo(self):
        return self._codigo
    # codigo property setter method
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo


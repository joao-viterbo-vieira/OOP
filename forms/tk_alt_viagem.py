# -*- coding: utf-8 -*-
"""
@author: costa
(2022)


"""""
#%% 
import datetime
# Import the generic class
from classes.gclass import Gclass

class viagens(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0

    # class attributes, identifier attribute must be the first one on the list
    att = ['_codigo','_data','_hora','_Destino','_preco']
    # Constructor: Called when an object is instantiated
    def __init__(self, codigo,data,hora,Destino,preco):
        super().__init__()
        # Object attributes
        self._Destino = Destino
        self._data = datetime.date.fromisoformat(data)
        self._hora = hora
        self._codigo = codigo
        self._preco = preco
        # Add the new object to the Customer_login list
        viagens.obj[codigo] = self
        viagens.lst.append(codigo)
        

    # Object properties
    # getter methodes
    # Destino property getter method
    @property
    def Destino(self):
        return self._Destino
    # data property getter method
    @property
    def data(self):
        return self._data
    # hora property getter method
    @property
    def hora(self):
        return self._hora
    # codigo property getter method
    @property
    def codigo(self):
        return self._codigo
    # preco property getter method
    @property
    def preco(self):
        return self._preco
    # login property getter method
    @data.setter
    def data(self, data):
        self._data = data
    # hora property setter method
    @hora.setter
    def hora(self, hora):
        self._hora = hora
    # codigo property setter method
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    # preco property setter method
    @preco.setter
    def preco(self, preco):
        self._preco = preco
    
    
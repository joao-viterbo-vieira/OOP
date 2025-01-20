# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:28:58 2022

@author: costa
"""
from classes.gclass import Gclass
#from classes.cliente import Cliente
import datetime

import datetime
class Passageiro(Gclass):
    list_cc=[]
    list_nome=[]
    list_data=[]
    list_telefone=[]
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # Attribute nomes list, identifier attribute must be the first one
    att = ['_numeroCC','_nome','_data','_telefone']
    
    desconto_menor= 0.2
    # auto_number = 1      # Uncomment in case of auto number on
    # Constructor: Called when an object is instantiated
    def __init__(self, numeroCC, nome, data, telefone):
        super().__init__()
        # Object attributes
        self._numeroCC = numeroCC
        self._nome = nome
        self._data = datetime.date.fromisoformat(data)
        self._telefone = telefone
        # Add the new object to the dictionary of objects
        Passageiro.obj[numeroCC] = self
        # Add the numeroCC to the list of object numeroCCs
        Passageiro.lst.append(numeroCC)

    # numeroCC property getter method
    @property
    def numeroCC(self):
        return self._numeroCC
    @numeroCC.setter
    def numeroCC(self, numeroCC):
        self._numeroCC = numeroCC
    # nome property getter method
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    # data property getter method
    @property
    def data(self):
        return self._data
    # data property setter method
    @data.setter
    def data(self, data):
        self._data = data
    # telefone property getter method
    @property
    def telefone(self):
        return self._telefone
    # telefone property setter method
    @telefone.setter
    def telefone(self, ntelefone):
        self._telefone = ntelefone

    @property
    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.data.year
        if tday.month < self.data.month or \
            (tday.month == self.data.month and tday.day < self.data.day):
            age -= 1
        return age
    
    @property
    def price_adolescente(self):
        if self.age<18:
            return "adolescente"
        
    def lugar(self, lugar):
        return self._lugar

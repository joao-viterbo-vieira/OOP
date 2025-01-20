# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:07:45 2022

@author: costa
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime
class Voo(Gclass):
    lugares_dict = {"A1" : "livre", "B1" : "livre", "C1" : "livre", "D1" : "livre", "E1" : "livre", "F1" : "livre", "A2" : "livre", "B2" : "livre", "C2" : "livre", "D2" : "livre", "E2" : "livre", "F2" : "livre", "A3" : "livre", "B3" : "livre", "C3" : "livre", "D3" : "livre", "E3" : "livre", "F3" : "livre", "A4" : "livre", "B4" : "livre", "C4" : "livre", "D4" : "livre", "E4" : "livre", "F4" : "livre", "A5" : "livre", "B5" : "livre", "C5" : "livre", "D5" : "livre", "E5" : "livre", "F5" : "livre"}
    lugares = []
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # Attribute hora_partidas list, identifier attribute must be the first one
    att = ['_data','_hora_partida','_hora_chegada','_lugares_ocupados']
    # auto_number = 1      # Uncomment in case of auto number on
    # Constructor: Called when an object is instantiated
    def __init__(self, data, hora_partida, hora_chegada, lugares_ocupados, lugares_disponiveis, codigo):
        super().__init__()
        # Object attributes
        self._data = data
        self._hora_partida = datetime.date.fromisoformat(hora_partida)
        self._hora_chegada = datetime.date.fromisoformat(hora_chegada)
        self._lugares_ocupados = lugares_ocupados
        self._lugares_disponiveis = lugares_disponiveis
        self._codigo = codigo
        # Add the new object to the dictionary of objects
        Voo.obj[data] = self
        # Add the data to the list of object datas
        Voo.lst.append(data)

    # data property getter method
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data
    # hora_partida property getter method
    @property
    def hora_partida(self):
        return self._hora_partida
    @hora_partida.setter
    def hora_partida(self, hora_partida):
        self._hora_partida = hora_partida
    # hora_chegada property getter method
    @property
    def hora_chegada(self):
        return self._hora_chegada
    # hora_chegada property setter method
    @hora_chegada.setter
    def hora_chegada(self, hora_chegada):
        self._hora_chegada = hora_chegada
    # lugares_ocupados property getter method
    @property
    def lugares_ocupados(self):
        return self._lugares_ocupados
    # lugares_ocupados property setter method
    @lugares_ocupados.setter
    def lugares_ocupados(self, lugares_ocupados):
        self._lugares_ocupados = lugares_ocupados
    # lugares_disponiveis property getter method
    @property
    def lugares_disponiveis(self):
        return self._lugares_disponiveis
    # lugares_disponiveis property setter method
    @lugares_disponiveis.setter
    def lugares_disponiveis(self, lugares_disponiveis):
        self._lugares_disponiveis = lugares_disponiveis
    # codigo property getter method
    @property
    def codigo(self):
        return self._codigo
    # codigo property setter method
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

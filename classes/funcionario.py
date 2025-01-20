# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:46:50 2022

@author: nmmr
"""
from classes.gclass import Gclass
import datetime
class Funcionario(Gclass):
    funcionarios={}
    def __init__(self, nome, ID, password):
        self._nome=nome
        self._ID = ID
        self._password = password
        self._viagensadicionadas=[]
        self._func = True
        Funcionario.funcionarios[ID] = password
        
    @property 
    def nome(self):
        return self._nome 
    @property 
    def ID(self):
        return self._ID
    @property 
    def password(self):
        return self._password
    
    # def adicionarviagens(self, destino, voo):
    #     self._viagensadicionadas.append(Viagem(destino,voo))
    #     Viagem.listaviagens.append(Viagem(destino,voo))
    #     return 
    
    # def retirarviagens(self, codigo):
    #     for viagem in Viagem.listaviagens:
    #         if viagem._codigo == codigo:
    #             Viagem.listaviagens.pop(Viagem.listaviagens.index(viagem))
    #     return
#%%      


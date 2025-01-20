# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:17:10 2022

@author: costa
"""


class Viagem:
    list_dest=[]
    list_data=[]
    list_hora=[]
    list_cod=[]
    list_prec=[]
    def init(self, dest, voo):
        self._dest=dest
        self._voo=voo

    @property
    def dest(self):
        return self._dest

    @property
    def voo(self):
        return self._voo

    

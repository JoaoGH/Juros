# -*- coding: utf-8 -*-
from math import *
class Calculos():
    def __init__(self, capital):
        self.conta1=0
        self.capital=capital

    def var(self,capital, taxa, periodo, montante):
        self.capital = capital
        self.taxa = taxa
        self.periodo = periodo
        self.montante = montante

    def simples(self, capital, taxa, periodo, montante):
        ##montante
        if(capital != "" and taxa != "" and periodo != ""):
            capital=float(capital)
            taxa=float(taxa)/100
            periodo=float(periodo)
            resultado=capital*(1+(taxa*periodo))
            resultado="Montante: "+str(resultado)
        ##capital
        elif(taxa != "" and periodo != "" and montante != ""):
            taxa=float(taxa)/100
            periodo = float(periodo)
            montante = float(montante)
            resultado=montante/(1+(taxa*periodo))
            resultado="Capital Inicial: "+str(resultado)
        ##taxa
        elif(periodo != "" and montante != "" and capital != ""):
            periodo = float(periodo)
            montante = float(montante)
            capital = float(capital)
            resultado=(montante-capital)/capital/periodo
            resultado="Taxa(ao mes): "+str(resultado)
        ##periodo
        elif(montante != "" and capital != "" and taxa != ""):
            montante = float(montante)
            capital = float(capital)
            taxa=float(taxa)/100
            resultado = (montante-capital)/capital/taxa
            resultado="Período (em meses): "+str(resultado)
        ##info
        else:
            resultado="Itens faltando."
        return (resultado)

    def composto(self, capital, taxa, periodo, montante):
        ##montante
        if (capital != "" and taxa != "" and periodo != ""):
            capital = float(capital)
            taxa=float(taxa)/100
            periodo = float(periodo)
            resultado = capital * ((1+taxa)** periodo)
            resultado="Montante: "+str(resultado)
        ##capital
        elif (taxa != "" and periodo != "" and montante != ""):
            taxa=float(taxa)/100
            periodo = float(periodo)
            montante = float(montante)
            perc=taxa/100
            resultado = montante / ((1+taxa) ** periodo)
            resultado="Capital inicial: "+str(resultado)
        ##taxa
        elif (periodo != "" and montante != "" and capital != ""):
            periodo = float(periodo)
            montante = float(montante)
            capital = float(capital)
            resultado = periodo//(montante/capital)-1
            resultado="Taxa(ao mes): "+str(resultado)
        ##periodo
        elif (montante != "" and capital != "" and taxa != ""):
            montante = float(montante)
            capital = float(capital)
            taxa=float(taxa)/100
            resultado = log10(montante/capital)/log10(1+taxa)
            resultado="Período (meses): "+str(resultado)
        ##info
        else:
            resultado = "Itens faltando."
        return (resultado)

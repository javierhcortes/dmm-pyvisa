
# -*- coding: utf-8 -*-
""" 
Aquí ejecutaremos el primer comando SCPI a el instrumento.
Comprobaremos que responda.
"""
# importamos los módulos
import visa

resources = visa.ResourceManager('@sim')
#resources = visa.ResourceManager('@py')

# Esto carga el multimetro Tektronix DMM 4050
dmm = resources.open_resource('USB0::1510::8464::8007816::0::INSTR')
#dmm = resources.open_resource('TCPIP0::localhost:4444::inst0::INSTR')

# Preguntemos el identification number por comando SCPI
idn = dmm.query('*IDN?')

#Imprimimos el IDN
print(idn)

#Close the connection
dmm.close()
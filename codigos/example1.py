# -*- coding: utf-8 -*-

""" 
Para ejecutar esta prueba, conecte los mutimetros
a su computador mediante el puerto USB y luego ejecute la linea con '@py'

Si usted no tiene instrumento compatible 
e instalo 'pyvisa-sim' ejecute la linea con '@sim'

Deberías obtener algo como esto
('USB0::1510::8464::8007816::0::INSTR'), donde la parte que
esta entre comillas empezando con USB0:: es el nombre del recurso
VISA de tu instrumento.
Esto es como lo identificaras en adelante.
"""

# Cargamos el modulo de VISA
import visa

# obtenemos el manejador de recursos visa
resources = visa.ResourceManager('@sim')
#resources = visa.ResourceManager('@py')

# cargamos la lista de dispositivos VISA conectados
list = resources.list_resources()

# imprimimos en pantalla la lista de recursos
print (list)
# Como instalar este repositorio

Se detalla las dependencias necesarias para instalar este repositorio.

## Sistema Operativo Linux

* Instalar python 2.7

> sudo apt get install python

* Instalar manejado de paquetes (pip)

> sudo apt-get install python-pip

* Instalar paquetes de py-visa

```bash
sudo pip install pyusb
sudo pip install pyvisa
sudo pip install pyvisa-py
```

Instrucciones comprobadas en Xubuntu 18.04

## Sistema operativo Windows

* Instalar python 2.7 desde su pagina [web](https://www.python.org/downloads/release/python-2715/) (Debería venir instalado pip)

* instalar los paquetes

        ????

El que sepa como hacerlo, enviar un merge request

## Ejecutar los códigos ejemplos sin Instrumentos (PyVisa-sim)

Si no tienes instrumento compatible con el protocolo IEEE.484
puedes instalar estos módulos desde pip para simular un instrumento

Requerimientos:

* Python (tested with 2.6 and 2.7, 3.2+)
* PyVISA 1.6+ ( para conocer tu version de pyvisa ejecutar el comando)

>$ pyvisa-info

Instalación:

>$ pip install -U pyvisa-sim

o instala la version en desarrollo

>$ pip install -U https://github.com/pyvisa/pyvisa-sim/zipball/master

PyVISA estará automáticamente instalado.

Para revisar la documentación de [pyVisa-sim](https://pyvisa-sim.readthedocs.io/en/latest/)
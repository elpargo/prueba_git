#!/bin/python

################################
# Autor: Junior Montilla       #
# Version: 0.1                 #
################################


import os 

os.system("clear")

print chr(27)+"[0;36m"+" ______ ______            ______"                       
print chr(27)+"[0;36m"+"___  /____  /_____ _________  /_______________________"
print chr(27)+"[0;36m"+"__  __ \_  /_  __ `/  ___/_  //_/  __ \__  __ \_  ___/"
print chr(27)+"[0;36m"+"_  /_/ /  / / /_/ // /__ _  ,<  / /_/ /_  /_/ /(__  ) "
print chr(27)+"[0;36m"+"/_.___//_/  \__,_/ \___/ /_/|_| \____/_  .___//____/  "
print chr(27)+"[0;36m"+"                                    /_/              "
print  "\n"

def  ver_contenido():
  e = os.environ
	variable =  raw_input("Ponga la variable de entorno a consultar\n>")
	variable.upper()
	
	for i in e :
   		 if i == variable:    	
			print "\n"
			print "el contenido de su variable es:\n %s" %  e[variable]
			print "\n\n\n\n\n"


def main():
	print "menu\n"
	print "1)ver el contenido de la variable"
	opcion  =  raw_input(">")
	if opcion ==  "1":
		ver_contenido() 

main()

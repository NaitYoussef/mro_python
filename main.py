#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *
from init import *
from algo import *

while num != 0:

	print intro

	num = input("Entrer le numéro correspondant: ")
	print '\n'

	def dyn():
		print "à faire"

	def floyd():
		
		print "Matrice de test :"
		print floyd_cours.affiche()

		res = floyd_algo(floyd_cours)

		print "Résultat Algortihme Floyd-Warshall"
		print res.affiche()
 

	def exit():
		print "fin"
	

	algo ={	0 : exit,
		1 : dyn,
		2 : floyd
		#3 : poten,
		#4 : johnson
		#5 : ford,
		#6 : branch,
		#7 : simplexe
		
	}

	algo[num]() 







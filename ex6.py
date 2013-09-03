# -*- coding: utf-8 -*-
x = "Hay %d tipos de personas." % 10
binario = "binario"
lqn="los que don't"
y= "Los que saben %s y %s." % (binario, lqn)

print x
print y


print "Dije: %r." % x
print "Y también dije: '%s'." % y

gracioso = False
evaluacion_de_chiste = "No es gracioso? %r"

print evaluacion_de_chiste % gracioso 

w = "Este es el lado izquierdo de..."
e = "una cadena con lado derecho"

print w + e



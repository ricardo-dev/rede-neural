# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 11:58:39 2021

@author: ricardo

basico: https://www.treinaweb.com.br/blog/principais-estruturas-de-dados-no-python

classes: https://algoritmosempython.com.br/cursos/programacao-python/classes-objetos/
"""

## básico
x = 3
print type(x);

y = raw_input('Entre com valor')
print type(y);

z = int(raw_input('Entre com valor'))
print type(z);

## condição
if x < y and x < z:
    print 'x e menor'

if x == 1:
    print '1'
elif x == 2:
    print '2'
else:
    print 'outro valor'


## foor e while loops
for i in range(0,10):
    print x

index = 0
while index <= 10:
    print index
    index += index

## funcoes
def f1():
    print 'f1'

def g1(x):
    print 'g1 ',x

def soma(a,b):
    """ espeficicacao da funcao """
    assert type(a) == int and type(b) == b
    x = a+b
    print 'soma: ',x
    return x

print soma(2,3);
x = soma(2,3)
print x


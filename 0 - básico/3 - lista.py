### Listas

lista = ["1", "2", "3", [1,2,3], 1, 2, 3]
##print lista

rg = range(1,5); # retorna uma lista
##print rg

### Acessando

##print lista[0]
i=0
while i < 6:
    ##print lista[i]
    i += 1

### Tamanho
x = len(lista)
##print x

i=0
while i < len(lista)-1:
    ##print lista[i]
    i += 1

### busca

##if "1" in lista:
##    print 'tem 1 str'
##if "10" not in lista:
##    print 'nao tem 10 str'

### listas e for loop

##for el in lista:
##    ##print el
##
##for f in ["banana", "orange", "apple"]:
##    if f == "orange":
##        ##print 'orange'
##    elif f == 'apple':
##        ##print 'apple'
##    else:
##        ##print 'None'

### operacao com lista
    
a = [1,2,3]
b = [4,5,6]
c = a + b
print 'a= ',a,' - b= ',b,' - c= ',c;

e = [0]
f = e * 4
print 'e= ',e,' - f= ',f;

### slice - retorna uma nova lista

lista = ['a', 'b', 'c', 'd', 'e']
print lista[1:3] #[initialIndex: finalIndex-1]
print lista[:] # copia toda a lista
print lista

### listas sao mutaveis (altera o valor do objeto"
lista[0] = 'A'
print lista

lista[1:3] = ['x','y']
print lista

lista[1:3] = [] # remove elementos
print lista

### apagar elementos

print lista
del lista[0]
print lista

### inserindo elementos
print lista
lista.append('z')
print lista
lista.append('b')
print lista

### aliasing - um objeto com varios nomes
l1 = [2]
l2 = [l1, l1]

print 'L1= ',l1, ' - L2= ',l2;

l1[0] = 3
print 'L1= ',l1, ' - L2= ',l2;

l2[0] = 'a'
print 'L1= ',l1, ' - L2= ',l2;

l1 = [2]
print 'L1= ',l1, ' - L2= ',l2;

a = [1,2,3]
b = a
print 'A= ',a,' - B= ',b
b[0] = 5;
print 'A= ',a,' - B= ',b

### clonando listas
a = [1,2,3]
b = a[:]
print 'A= ',a,' - B= ',b
b[0] = 5;
print 'A= ',a,' - B= ',b

### matriz
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print matriz
print matriz[1][1]
print matriz[2][1]

for x in matriz:
    for y in x:
        print y


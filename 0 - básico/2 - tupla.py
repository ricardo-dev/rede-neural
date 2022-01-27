### Tupla

tupla1 = 'a','b','c','d'
tupla2 = ('a','b','c','d')
print tupla1
print type(tupla1)
print tupla2
print type(tupla2)

t1 = ('a')
t2 = ('a',)

print t1
print type(t1)
print t2
print type(t2)

t3 = (1,2,3)
print t3
t3 += (4,)
print t3

print t3[0]
print t3[-1]

### slice

tx = tupla2[1:3]
print tx
print type(tx)

tx = ('A',)+tx
print tx

### assinatura de tupla
a,b = 1,2

print 'a= ',a,' b= ',b
print 'a= ',type(a),' b= ',type(b)

### tuplas e retorno de valores
def swap(x,y):
    return y,x

dois,tres = swap(2,3)
print dois, tres

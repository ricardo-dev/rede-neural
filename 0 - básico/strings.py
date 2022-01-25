## Strings
fruit = 'banana';

print fruit[1];
print fruit[0];

## Tamanho
x = len(fruit)
print x
print fruit[len(fruit)-1];

## Strings in loop
print 'while with string'
index = 0;
while index < len(fruit):
    letter = fruit[index]
    print '- ',letter
    index = index+1

print 'for with strings'
for letter in fruit:
    print '-- ',letter

prefixes = 'JKLMNOPQ'
suffix = 'ack'

print 'exercices'
for letter in prefixes:
    l = letter
    if l == 'Q':
        l = 'Qu'
    print l + suffix

## slice
s = "Peter, Paul and Mary"
print s[0:5] ##[indexInicial: indexFinal -1]

## comparando string - ordem alfabetica
word = "Zebra"
if word == "Banana":
    print 'yes! we have no bananas!'

if word < "Banana":
    print 'word is menor'

if word > "Banana":
    print 'word is bigger'

## Strings imutaveis
greeting = "Hello!"
#greeting[0] = 'J' # ERROR!
print greeting

## find
def find(word, ch):
    assert type(word) == str and type(ch) == str
    index = 0
    while index < len(word):
        if word[index] == ch:
            return index
        index = index + 1
    return -1

test = 'my name';
print find(test, 'e')
#print find(23, 'f') # ERROR!

print test.find('m');

## string module
import string

ii = string.find(test, "my");    #string, char
print ii

jj = string.find(test, "a", 3);  #string, char, indexStart
zz = string.find(test, "a", 3, 4)#string, char, indexStart, indexEnd

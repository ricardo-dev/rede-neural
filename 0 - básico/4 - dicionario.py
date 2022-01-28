### Dicionario

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'

print eng2sp
print eng2sp['one']

### operacoes

inventory = {"apple":430, "banana": 312, "oranges":525, "pears":217}
print inventory
inventory["apple"] = inventory["apple"]-30
print inventory

del inventory['pears']
print inventory

print len(inventory)

### metodos

for key in eng2sp.keys():
    print key

for value in eng2sp.values():
    print value

for item in eng2sp.items():
    print item

if eng2sp.has_key('one'):
    print 'achei'
    
### aliasing
opp = {"up":"down", "right":"wrong", "true":"false"}
alias = opp
copy = opp.copy()

print 'opp= ',opp
print 'alias= ',alias
print 'copy= ',copy

alias["right"] = 'left'
print 'opp= ',opp
print 'alias= ',alias
print 'copy= ',copy

copy['right'] = 'privilege'
print 'opp= ',opp
print 'alias= ',alias
print 'copy= ',copy


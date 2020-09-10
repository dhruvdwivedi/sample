from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for k,v in od.items():
	print(k,v)

print("\n After:\n")
od['c']=5
for k,v in od.items():
	print(k,v)


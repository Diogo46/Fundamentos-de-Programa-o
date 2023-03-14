shop = {'eggs':6, 'sugar':1.0}
print(shop)
{'sugar':1, "eggs":6} == shop
print(type(shop))
print(len(shop))
print(shop['eggs'])
print(6 in shop)
print(shop.get(6, 'nada'))
print(shop.keys())
print(shop.values())
print(shop.items())


d = {}
print(type(d))
print(len(d))
d[93542] = {'maria','P1'}
d[95612] = {'daniel', 'P2'}
d[76367] = {'john', 'P1'}
print(len(d))


for x in d:
	print(x, d[x])
	
for x,y in d.items():
	print(x, y, sep='->')
	
t = {'P1':[], 'P2':[]}

	
print(len(t['P1']))
print(t.pop('P2'))

tempo = int(input('Tempo em segundos: '))
s = tempo % 3600
m = s // 60
h = tempo //3600
print('{:02d} : {:02d} : {:02d} '.format(h, m, s))

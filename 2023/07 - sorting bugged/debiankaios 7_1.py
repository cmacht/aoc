import re

datei = open("input-training","r")
punkte = 0
summe = 0
liste = []

for i, zeile in enumerate(datei):
	liste.append(list(filter(None, zeile.split(" "))))
	liste[i][1] = int(liste[i][1].strip())

for n, i in enumerate(liste):
	a = liste[n][0].split("T")
	liste[n][0] = "B".join(a)
	liste[n][0] = "C".join(liste[n][0].split("J"))
	liste[n][0] = "D".join(liste[n][0].split("Q"))
	liste[n][0] = "E".join(liste[n][0].split("K"))
	liste[n][0] = "F".join(liste[n][0].split("A"))
	
for n, i in enumerate(liste):
	print(i[0])
	done = []
	laengen = [0, 0, 0, 0, 0]
	for o, j in enumerate(i[0]):
		if o in done:
			continue
		for p, k in enumerate(i[0]):
			if j == k:
				done.append(p)
				laengen[o] += 1
	print(laengen)
	if 5 in laengen:
		liste[n].append(7)
	elif 4 in laengen:
		liste[n].append(6)
	elif (3 in laengen) and (2 in laengen):
		liste[n].append(5)
	elif 3 in laengen:
		liste[n].append(4)
	elif laengen.count(2) == 2:
		liste[n].append(3)
	elif laengen.count(2) == 1:
		liste[n].append(2)
	else:
		liste[n].append(1)

liste.sort(key=lambda x: x[0], reverse = False)
liste.sort(key=lambda x: x[2], reverse = False)

for n, i in enumerate(liste):
	summe += (n+1)*i[1]
print(summe)

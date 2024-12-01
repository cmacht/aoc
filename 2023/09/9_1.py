datei = open("input","r")
summe = 0

for i, zeile in enumerate(datei):
	a = [list(map(int, filter(None, zeile.split(" "))))]
	
	
	while any(a[-1]):
		temp = []
		for n in range(len(a[-1])-1):
			temp.append(a[-1][n+1]-a[-1][n])
		a.append(temp)
	a[-1].append(0)
	for n in reversed(range(1, len(a))):
		a[n-1].append(a[n-1][-1]+a[n][-1])
	print(a)
	summe += a[0][-1]
	
# print(summe)

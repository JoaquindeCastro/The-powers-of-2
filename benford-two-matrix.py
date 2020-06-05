l = 1
matrix = []
row = []
for n in range(1,100):
	p = 2**n
	row.append(p)
	newl = int(len(str(p)))
	if newl > l:
		matrix.append(row)
		row = []
	l = newl

for n in matrix:
	print(n)

	
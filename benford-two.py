
sequence = []
for n in range(1,100):
	p = 2**n
	digit = int(str(p)[:1])
	sequence.append(digit)
	benford = {
	"one": sequence.count(1)*100/n,
	"two":sequence.count(2)*100/n,
	"three":sequence.count(3)*100/n,
	"four":sequence.count(4)*100/n,
	"five":sequence.count(5)*100/n,
	"six":sequence.count(6)*100/n,
	"seven":sequence.count(7)*100/n,
	"eight":sequence.count(8)*100/n,
	"nine":sequence.count(9)*100/n
	}
	relBenford = {
		"one":abs(benford['one'] - 30.1),
		"two":abs(benford['two'] - 17.6),
		"three":abs(benford['three'] - 12.5),
		"four":abs(benford['four'] - 9.7),
		"five":abs(benford['five'] - 7.9),
		"six":abs(benford['six'] - 6.7),
		"seven":abs(benford['seven'] - 5.8),
		"eight":abs(benford['eight'] - 5.1),
		"nine":abs(benford['nine'] - 4.6),
	}
	print(sum(relBenford.values())/9)
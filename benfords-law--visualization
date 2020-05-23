import matplotlib.pyplot as plt

numbers = []
prob = []
ones = 0
digit = int(input("choose a digit"))
for n in range(1,1000):
	m = int(str(n)[:1])
	numbers.append(m)
	ones = numbers.count(digit)
	p = ones / n
	prob.append(p)

total = sum(prob)
mean = total / 999

domain = range(1,1000)

plt.plot(domain, prob, label='Probability')
plt.ylim(0, 1)

plt.axhline(y=mean, color="red", linestyle='--', label='Mean')


plt.legend()
plt.show()

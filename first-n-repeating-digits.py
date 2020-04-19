def intersection(lst1, lst2):
	newLst = [value for value in lst1 if value in lst2]
	return newLst


digits = []
repeatedDigits = []
k = int(input('how many digits are to be considered?'))

#formula for period given k: 4*5^(n-1)

p = k - 1
q = 5**p
l = 4 * q

n = 1
for n in range(1, l * 10):
	m = int(2**n % 10**k)
	if m in digits:
		repeatedDigits.append(m)
	else:
		digits.append(m)

newLst = intersection(digits, repeatedDigits)

print(newLst)
print("This pattern has a period of " + str(len(newLst)))
print("The pattern periodically repeats at the number " + newLst[0])

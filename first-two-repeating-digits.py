digits = []
repeatedDigits = []
for n in range(1, 50):
	i = int(2**n % 100)
	if i in digits:
		repeatedDigits.append(i)
	else:
		digits.append(i)


def intersection(lst1, lst2):
	newLst = [value for value in lst1 if value in lst2]
	return newLst


newLst = intersection(digits, repeatedDigits)

print(newLst)
print("This pattern has a period of " + str(len(newLst)))
print("The pattern periodically repeats at the number " + newLst[0])

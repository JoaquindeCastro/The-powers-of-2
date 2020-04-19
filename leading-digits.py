powers = []
digits = []
N = int(input("give a very large N"))
for k in range(0,N):
  powers.append(2**k)
for number in powers:
  number = str(number)
  a = number[0]
  digits.append(a)
print(digits)

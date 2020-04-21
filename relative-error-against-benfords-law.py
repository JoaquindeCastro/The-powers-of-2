import math

powers = []
digits = []

N = int(input("give a very large N"))
for k in range(0,N):
  powers.append(2**k)
for number in powers:
  number = str(number)
  a = number[0]
  digits.append(a)

def digitCount(k):
  k = str(k)
  k = digits.count(k)/N
  return float(k)

def benford(k):
  return math.log10(1 + (1/k))

for k in range(1,10):
  relError = abs(100*(benford(k) - digitCount(k))/(benford(k)))
  print(str(relError) + '%')

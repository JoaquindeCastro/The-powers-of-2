digits = []
for n in range (1,50):
  i = int(2**n % 10)
  if i in digits:
    break
  else:
    digits.append(i)
print(digits)

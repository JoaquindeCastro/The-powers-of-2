digits = []
for n in range (1,50):
  i = int(2**n % 10)
  if i in digits:
    break
  else:
    digits.append(i)
print(digits)
print("This has a period of " + str(len(digits)))
print("This pattern starts at " + str(digits[0]))

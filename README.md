# The-powers-of-2
This repository illustrated properties and patterns present in the powers of two through simple python scripts

See my full article series on this on Medium: https://medium.com/all-is-number/the-powers-of-two-53d9ede72001

## Repeating digits
I used python scripts to illustrate how certain place values have an almost (or even completely) periodic repetition of digits. In general, these digits would be any given number of trailing digits (from the right) and the leading digit of each power of two.

## Repeating ones digit
The ones digits repeats every **4 terms** in the pattern 2, 4, 8, 6 starting at the **second term** (2^n = 2)

```
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
```
from https://github.com/JoaquindeCastro/The-powers-of-2/blob/master/repeating-ones-digit.py

More updates coming soon!

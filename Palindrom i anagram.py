a, b = input(), input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
if X == Y:
  print("Anagram")
else:
  print("Nie")


def palindrom(s):
  return s == s[::-1]


a = input()
if palindrom(a):
  print("palindrom")
else:
  print("nie")

p = 29
ints = [14, 6, 11]

for a in range(29):
  a2 = pow(a,2,29)
  if a2 in ints:
    print(a2,a)
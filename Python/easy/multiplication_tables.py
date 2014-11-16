line = ''
for factor in range(1,13):
  for num in range(1,13):
    if num < 12:
      line += str(num * factor) + ' '
    else: 
      line += str(num * factor) + '\n'

print line
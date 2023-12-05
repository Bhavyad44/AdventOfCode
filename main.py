f = open("values.txt", "r") 
f_lines = f.readlines()  
total = 0 
finalTotal = 0 



for line in f_lines:
  firstValue = None
  secondValue = None

  for char in line:
    if char.isdigit() and firstValue is None:
      firstValue = char
      secondValue = char
      
    elif char.isdigit():
      secondValue = char
      
  if firstValue is not None and secondValue is not None:
    joined = firstValue + secondValue
    total = int(joined)
    print(total)
    finalTotal += total
    
print(finalTotal)

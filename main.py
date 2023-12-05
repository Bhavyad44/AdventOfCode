f = open("values.txt", "r") # Opens the file
f_lines = f.readlines()  # Reads the file
total = 0 # Creates total variable
finalTotal = 0 # Creates finalTotal variable



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
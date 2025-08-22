import os 
os.system("cls")

n1 = int(input("digite um valor inteiro:"))
n2 = int (input("digite um segundo valor inteiro:"))

media = (n1 + n2) /2
soma = n1 + n2
produto = n1 * n2 

print(f"sua media:{media}")
print(f"sua soma: {soma}")
print(f"produto:{produto}")
  
if n1 < n2:
 print("o primeiro e o menor ")
else:
 print(" o segundo e o menor")

 if n1 == n2: 
  print ("sao iguais ")




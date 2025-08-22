import os
os.system("cls")

primeira_nota = float(input("digite sua primeira_nota:"))
segunda_nota = float(input("digite sua segunda_nota:"))
terceira_nota = float(input("digite sua terceira nota:"))

media = (primeira_nota + segunda_nota + terceira_nota) / 3
if media < 7:
     print("voce reprovou ")

else:
     print("voce foi aprovado ")

import os 
os.system("cls")

print(" olá , nosso cardapio logo  baixo :)")

print("""
codigo \t prato \t\t valor   
1 \t picanha \t R$ 25,00 
2 \t lasanha \t R$ 20,00 
3 \t strogonoff \t R$ 18,00
4 \t Bife acebolado  R$ 15,00  
5 \t pão com ovo \t R$ 5,00 
      

""") 
codigo= int (input ("qual o prato vc deseja ? "))

match codigo:
    case 1: 
        print("picanha / R$25,00 ")
    case 2: 
        print("lasanha / R$ 20,00")
    case 3: 
        print("strogonoff / R$ 18,00")
    case 4: 
        print("bife aacebolado / R$ 15,00")
    case 5: 
        print("paõ com ovo / R$ 5,00 ")                        

        print(" otimá escolha , agradeçemos sua compra ")
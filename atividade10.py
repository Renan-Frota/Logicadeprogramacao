#Crie uma função que recebe um número (N) como argumento e imprime os números de 0 até N que são múltiplos de 5 e ímpar
def exercicio():
  num = int(input("insira o número")) 
i = 0
while i <= num:
 if n 5% == 0 and n 2% !=0:
    print(i)
 i + 1
 
 #Crie uma função que recebe um numero (N) como argumento e retorna uma lista de tamanho N, que é preenchida por inputs do usuário
 def exercicio2():
  num_entradas: int(input("Digite o número de intens na sua lista"))
  lista = []
  i = 0
  while i < num_entrada:
    lista.append(input())
    i += 1
    
    
    #Crie uma função que dada uma lista de números, retorna o número de números maiores que 5
    lista = input("Insira uma lista de valores separados por um espaço: ")
lis = lista.split()
lis = []
def funcao_3():
  i = 0
  while i < len(list):
    if int(list[i]) > 5:
      lis.append(list[i])
      i += 1
    else:
      i += 1
  return lis
funcao_3()




#Crie uma função em que dentro dela tenha o seguinte menu: A opção 'a' imprime 'PSG' e a 'b' imprime 'BAYERN'. Se for 'd', finaliza o programa.
def exercicio4():

 menu = {
  'a' : "PSG",
  'b' :"BAYERN"
  }
 opcao = input()
 while opcao != 'd':
    if opcao in menu:
      print(menu[opcao])
    else:
      print("invalido")
    opcao = imput()

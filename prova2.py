#Exercicio 1
def exercicio_1():
    list = []
    soma = 0
    while len(list) < 3:
       list.append(int(input ("Isira nota: ") ))
    for number in list:
        soma += number
        media = soma/3
    return(f"A nédia do aluno sera: {media}")


#Exercicio 2

def exercicio_2(n):
  lista = []
  while len(lista) != n:
    entrada = input("digite qualquer tecla")
    list.append(entrada)
  return(lista)


#Exercicio 3
def exercicio_3():
 entrada = input("Digite a, b, 'z': ")
  if (entrada == 'z'):
    return
  elif (entrada == 'a'):
    print("globo")
  elif (entrada == 'b'):
    print('sbt')
  else:
    print('inválido')
    
    #Exercicio 4
    def exercicio_4(list):
   medias_que_são_inferiores_a_sete = 0
  for media in list:
    if (media < 7):
      medias_que_são_inferiores_a_sete += 1
  if ( medias_que_são_inferiores_a_sete < (len(list) * 0.25)):
    return "Professor Coxa"
  else:
    return "Professor Padrão"




   
  

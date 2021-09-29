####para exibir letras na palavra secreta
###ex _ _ _ _ palavra bala.Conforme
#vai acertando preenche a secreta
'''
Jogo da forca :Proposto pelo curso da DataScienceAcademy
'''
###Imprime a figura correspondente da forca
#3Vai aumentando até dar Game Over.
##GAME OVER == range(len(figura)) -- comprimento é o tamanho da palavra sorteada
def desenha(erro , comprimento):
  figura = ['''

>>>>>>>>>>Hangman<<<<<<<<<<z

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
  gameOver = False
  if figura == comprimento:
    print(figura[erro])
    gameOver = True
  else:
    print(figura[erro])
    gameOver = False
    
    
###Função para gerar um sorteio em uma lista de palavras.
###vai retornar uma lista de caracteres, que é o mesmo que uma string
###exemplo de utilização : print(palavraAleatoria([AQUI VAI UMA LISTA DE PALAVRAS]))
def palavraAleatoria(ListaPalavras):  
  a =random.randrange(0,len(ListaPalavras))
  sorteio = ListaPalavras[a]
  matriz= []
  letrasDigitadas = ['0']
  resultado = False

  for i in range(len(sorteio)):
    matriz.append(sorteio[i])
  return matriz
  
  
##FUNÇAO QUE CONSULTA SE ESTA CERTO A OPÇAO
def consulta(e,l):
  try:
    l.index(e)
    return True
  except:
    return False
    
    
import random
secreta = palavraAleatoria(['bala' , 'casa' , 'doce','rato']) ##chama a função para sortear uma palavra da listaa
pontos = 0
erro = 0 
letra = []
for i in range(len(secreta)):
  letra.append('_ ')

esc =''
resultado = False ##booleano que mostrara se o jogador ganhou ou perdeu

while esc != '0':
  esc = input('Adivinhe : ')
  
  if consulta(esc,secreta): ##chama a funcao consulta que retornra verdadeiro se achar esc na lista   
    pontos += secreta.count(esc) ###Aqui a jogada de contar quantas ocorrencias tem da letra na frase
## A PARTIR DAQUI É NOVO ######
    for k in range(len(secreta)):
      if secreta.count(esc) > 1:
###item = [i for i, item in enumerate(lista) if item == escolha] cria uma lista do index das ocorrencias
        item = [i for i, item in enumerate(secreta) if item == esc]
        for j in item:
          letra[j] = esc  ###a lista criada anteriormente , coloco o mesmo index em letra e atribuo o valor escolhido
      elif secreta.count(esc) == 1:
        numero = secreta.index(esc)
        letra[numero] = esc
                   
    for k in letra:
      print(k , end ='')


######ATÉ AQUI É NOVO ######
    print()
    print('Pontos :',pontos)
    #pass
    

  else:  ###se retornar falso fara a sequencia deste else
    #pass
    
    desenha(erro , len(secreta))
    erro +=1
    for k in letra:
      print(k , end ='')
    print()
    print('Pontos : ',pontos)
    if erro == 7:
      esc ='0'
      resultado = False
    

  #desenha(0 , len(secreta))
  if pontos == len(secreta):
    esc = '0'
    resultado = True
  else:
    pass

if resultado == False:
  print('GAME OVER!!!')
else:
  print('Parabens! Você Ganhou!')

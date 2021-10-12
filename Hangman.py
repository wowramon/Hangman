import os
import random
import re

def loadData(): # Cargamos las palabras del archivo Data
    
  with open('Data.txt','r', encoding = "utf-8") as Dp:  # Abrimos el archivo Data en modo solo lectura y le agregamos el formato de decodificacion utf-8
      Words = [i for i in Dp ] # Comprehension list para almacenar el texto en variable
  return Words
  
def getRamdonW(): # Funcion que devuelve una palabra aleatoria
  text = loadData() # cargamos la lista en la variable text
  word = text[random.randrange(len(text))] # Guardamos el texto en la variable indexando dentro de la lista con un numero aleatorio
  return word # devolvemos el resultado
    

def SplitList(word,hidden): #Funcion que nos ayuda a dividir la palabra en una lista letra por letra, Ademas nos ayuda a crear una lista que oculta dichas letras
  newlist = [char for char in word if char != '\n'] #Comprehension list que nos ayuda a separa la palabra en letras
  if hidden : #Condicional 
      hiddenList = ['_' for char in word if char != '\n' ] # añadimos el caracter especial a una nueva lista dependiendo de la cantidad de letras que tenga la palabra Validamos para no agregar el salto de linea
      return hiddenList # return
  else:
    return newlist # return
    
def Display(List): # Funcion que nos despliega los espacios 
   display = ''  #Inicializamos variable
   for i in range(len(List)):
      char = List[i]
      display = display + char #Cadena de caracteres
      
   return display

def Validate(listH,listW):  #Funcion que nos ayuda a validar la cadena de strings
    countH = 0  #Counts 
    countW = 0
    
    for i in range(len(listH)):
      if listH[i] != '_':  #Si el char es diferente al de _ suma 1 al contador
        countH = countH+1
        
    for i in range(len(listW)):
      countW = countW+1  #contador por cada char
      
      
    return countH == countW  #valida si la cantidad de char es correcta
    
def board(): # Indica el tablero de juego
    Trigger = True # Armamos variable trigger para salir del loop
    
    print('Welcom to the hangman game') # Header
    word = getRamdonW()  
    List = SplitList(word,False)
    HiddenList = SplitList(word,True)
    print(Display(HiddenList))  #Mostramos en pantalla los espacio a completar
    
    while Trigger:
        
        input_word =input('Introduce una letra:\n ') #Ingresamos una letra
     
        
        for item in input_word.split():
          for i in range(len(List)):           # Body
            if(item.lower() == List[i]): #Validamos la letra y la pasamos a minusculas con la funcion lower
              HiddenList[i] = item.lower() #Si coninciden agregamos dicho item en el index correspondiente
        
        
        if Validate(Display(HiddenList),Display(List)):
         print(Display(HiddenList)) #Mostramos en pantalla los espacio a completar
         Trigger = False # Salimos del Loop
        else:
         print(Display(HiddenList))
         
         
        
            
   

    
     
def run(): # Funcion principal
    # word = getRamdonW()  # Body
    # List = SplitList(word,False)
    # Display(List)
    board()

if __name__=='__main__':
    run()
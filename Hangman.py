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
  newlist = [char for char in word] #Comprehension list que nos ayuda a separa la palabra en letras
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


    
def board(): # Indica el tablero de juego
    Trigger = True # Armamos variable trigger para salir del loop
    
    print('Welcom to the hangman game') # Header
    word = getRamdonW()  
    List = SplitList(word,False)
    HiddenList = SplitList(word,True)
    print(Display(HiddenList))  #Mostramos en pantalla los espacio a completar
    
    while Trigger:
        
        print(Display(List))
        input_word =input('Introduce una letra:\n ') #Ingresamos una letra
     
        for item in input_word.split():
          for i in range(len(List)):           # Body
            if(item.lower() == List[i]): #Validamos la letra y la pasamos a minusculas con la funcion lower
              HiddenList[i] = item.lower() #Si coninciden agregamos dicho item en el index correspondiente
               
        h = str(Display(HiddenList))
        l= str(Display(List))
        print(h.lower() is l.lower())
        
        
        if sorted(h) is sorted(l):
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
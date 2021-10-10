import os
import random
import re

def loadData(): # Cargamos las palabras del archivo Data
    
  with open('Data.txt','r', encoding="utf-8") as Dp:  # Abrimos el archivo Data en modo solo lectura y le agregamos el formato de decodificacion utf-8
      Words = [i for i in Dp ] # Comprehension list para almacenar el texto en variable
  return Words
  
def getRamdonW(): # Funcion que devuelve una palabra aleatoria
  text = loadData() # cargamos la lista en la variable text
  word = text[random.randrange(len(text))] # Guardamos el texto en la variable indexando dentro de la lista con un numero aleatorio
  return word # devolvemos el resultado
    

def SplitList(word,hidden): #Funcion que nos ayuda a dividir la palabra en una lista letra por letra, Ademas nos ayuda a crear una lista que oculta dichas letras
  newlist = [char for char in word] #Comprehension list que nos ayuda a separa la palabra en letras
  if hidden : #Condicional 
      hiddenList = ['_' for char in word] # añadimos el caracter especial a una nueva lista dependiendo de la cantidad de letras que tenga la palabra
      return hiddenList # return
  else:
    return newlist # return
    
def Display(List): # Funcion que nos despliega los espacios 
   display = ' ' 
   for i in range(len(List)):
      char = List[i]
      display = display + char #Cadena de caracteres
      
   print(display)

    
def board(): # Indica el tablero de juego
    Trigger = False  # Armamos variable trigger para salir del loop
    while Trigger:
        print('Welcom to the hangman game') # Header
        word = getRamdonW()  # Body
        List = SplitList(word,False)
        HiddenList = SplitList(word,True)
        
       
        
        os.system('pause')
        Trigger = True # Salimos del Loop
        
            
   

    
     
def run(): # Funcion principal
    word = getRamdonW()  # Body
    List = SplitList(word,False)
    Display(List)

if __name__=='__main__':
    run()
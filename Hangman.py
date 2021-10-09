import os



def loadData(): # Cargamos las palabras del archivo Data
    
  with open('Data.txt','r', encoding='utf-8') as Dp:  # Abrimos el archivo Data en modo solo lectura y le agregamos el formato de decodificacion utf-8
      Words = [i for i in Dp ] # Comprehension list para almacenar el texto en variable
  return Words
  
def board(): # Indica el tablero de juego
    Trigger = False  # Armamos variable trigger para salir del loop
    while Trigger:
        print('Welcom to the hangman game') # Header
        
        Trigger = True # Salirmos del Loop
        
            
   

    
     
def run(): # Funcion principal
   loadData()


if __name__=='__main__':
    run()
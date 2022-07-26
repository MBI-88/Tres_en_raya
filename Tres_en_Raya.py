#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Juego de tres en raya
import numpy as np
from collections import deque

def jugador(tupla):
    tupla.rotate()
    return tupla[0]
def busqueda(jugador):
    empate = "empate"
    if table[0,0]==jugador and table[0,1]==jugador and table[0,2]==jugador:
        return jugador
    elif table[1,0]==jugador and table[1,1]==jugador and table[1,2]==jugador:
        return jugador
    elif table[2,0]==jugador and table[2,1]==jugador and table[2,2]==jugador:
        return jugador
    elif table[0,0]==jugador and table[1,0]==jugador and table[2,0]==jugador:
        return jugador
    elif table[0,1]==jugador and table[1,1]==jugador and table[2,1]==jugador:
        return jugador
    elif table[0,2]==jugador and table[1,2]==jugador and table[2,2]==jugador:
        return jugador
    elif table[0,0]==jugador and table[1,1]==jugador and table[2,2]==jugador:
        return jugador
    elif table[0,2]==jugador and table[1,1]==jugador and table[2,0]==jugador:
        return jugador
    else :
        return empate
#Main:    
table=np.array([ 
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]])
turno=deque(("X","O"))
comprueba=9
print("****Bienvenido al juego de tres en raya****")
while comprueba>0:
    player=jugador(turno)
    coordenadas=input("Introdusca coordenadas jugador {}\n para salir ponga salir:__".format(player))
    try:
        if coordenadas.lower()=="salir":
            print("saliendo del juego...")
            break
        elif coordenadas.isalpha():
            print("No se admiten letras ")
            break
        else:
            if  coordenadas[0]=="0" or  coordenadas[2]=="0" or coordenadas[1]!='.':
                print("Error caracteres no admitido ")
                break
            else:
                coordenada_X=int(coordenadas[0])-1
                coordenada_Y=int(coordenadas[2])-1
                table[coordenada_X,coordenada_Y]=player
                print(table)
                busqueda(player)
                if busqueda(player)==player:
                    print("Ganador es {}".format(player))
                    break
                else:
                    comprueba-=1
                    continue      
    except :
        print("Valor incorrecto fuera del rango")
        break
if comprueba==0:
    print("Empate")
    print("Fin del juego...")
    input()
else:
    print("Fin del juego...")
    input()
    
    
    
    


# In[ ]:







import socket
import pickle
import random

turno="0"
t1="0"
puntoscliente = 0
puntosservidor=0
cordenadaxp1 = 0
cordenadayp1 = 0
cordenadaxp2 = 0
cordenadayp2 = 0
puntajeganador = 0
dato=[]
datorec=[]
coordenadas=[]
palabrasfacil=["socket","socket","TCP","TCP","UDP","UDP","red","red","ipn","ipn","escom","escom","ip","ip","router","router"]
palabrasdificil=["socket","socket","TCP","TCP","UDP","UDP","red","red","ipn","ipn","escom","escom","ip","ip","router","router",
                 "switch","switch","OSI","OSI","linux","linux","python","python","server","server","pc","pc","host","host",
                 "puerto","puerto","IDE","IDE","admin","admin"
                 ]
memoramafacil = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]


memoramafacilprint = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]

memoramafacilbuffer = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]

memoramadificil =[[0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0]]

memoramadificilprint =[ [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]

memoramadificilbuffer =[ [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]
def validartablerodestapado(matriz):
    destapado=0
    i=0
    j=0
    for k in matriz:
        for n in k:
            
            aux=matriz[i][j]
            if aux==0:
                destapado=destapado+1
            j=j+1
        j=0    
        i=i+1
        if destapado>0:
            return True
        else:
            return False

def imprimirmatriz(matriz):
    #print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end="")
        print()

def generartablero(matriz,lista):
    aleatorio=[] 
    i=0
    j=0
   
    m=0
    aleatorio=[]
    while (len(lista)!=0):
        aux1=random.choice(lista)
        aleatorio.append(aux1)
        lista.remove(aux1)
        m=m+1
   
    index=0
    for k in matriz:
        for n in k:
            
            matriz[i][j]=aleatorio[index]
            index=1+index
            j=j+1
        j=0    
        i=i+1   



#HOST = "192.168.100.62"  # Hostname o  dirección IP del servidor
#PORT = 65433  # Puerto del servidor
#HOST="127.0.0.1"
buffer_size = 1024
HOST = input("digite la ip destino: ")
PORT = int(input("DIGITE EL PUERTO DESTINO: "))




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
  
    dificultad=input("ingresa la dificultad \n 1---facil \n2---dificil:\n")
   
    
    if dificultad=="1":
        print("elegiste  facil")
        generartablero(memoramafacil,palabrasfacil)
        print("el tablero es el siguiente: ")
        imprimirmatriz(memoramafacilprint)
        puntajeganador=0

        while (puntajeganador!=8):
            
            
            while turno=="0":
                if puntajeganador==8:
                    dato=[]
                    dato.append("0")
                    dato.append("0")
                    dato.append("0")
                    dato.append(puntoscliente)
                    dato.append(puntosservidor)
                    dato.append("termino")
                    bufferdato=pickle.dumps(dato)
                    TCPClientSocket.send(bufferdato)
                    break
                datoenv=[]
                datorec=[]
                datoenvbuffer=[]
                datorecbuffer=[]
                print("TURNO DEL CLIENTE")
                cordenadaxp1=input("digita la fila de la casilla que quieres destapar---(0-3): ")
                cordenadayp1=input("digita la columna de la casilla que quieres destapar---(0-3): ")
                xp1=int(cordenadaxp1)
                yp1=int(cordenadayp1)
                memoramafacilprint[xp1][yp1]=memoramafacil[xp1][yp1]
                memoramafacilbuffer[xp1][yp1]=memoramafacil[xp1][yp1]
                par1=memoramafacilprint[xp1][yp1]
                cordenadaxp2=input("digita la fila de la casilla que quieres destapar---(0-3): ")
                cordenadayp2=input("digita la columna de la casilla que quieres destapar---(0-3): ")
                xp2=int(cordenadaxp2)
                yp2=int(cordenadayp2)
                memoramafacilprint[xp2][yp2]=memoramafacil[xp2][yp2]
                memoramafacilbuffer[xp2][yp2]=memoramafacil[xp2][yp2]
                par2=memoramafacilprint[xp2][yp2]   
                print("destapaste las siguientes palabras")
                imprimirmatriz(memoramafacilprint)
                
                dato=[]
                #print(dato)
                t1="1"
                
                dato.append(t1)
                dato.append(par1)
                dato.append(par2)
                dato.append(puntoscliente)
                dato.append(puntosservidor)
                dato.append("no")
                
                #print(dato)
                bufferdato=pickle.dumps(dato)
                TCPClientSocket.send(bufferdato)

                datorecbuffer=TCPClientSocket.recv(buffer_size)
                datorec=pickle.loads(datorecbuffer)
                #print(datorec)
           
                if datorec[1]=="1":
                    print("obtuviste un punto!")
                    memoramafacilprint[xp1][yp1]="0"
                    memoramafacilprint[xp2][yp2]="0"
                    puntoscliente=puntoscliente+1
                    puntajeganador=puntajeganador+1
                else:
                    print("lo siento las casillas seleccionadas no son un par")
                    memoramafacilprint[xp1][yp1]="0"
                    memoramafacilprint[xp2][yp2]="0"
                    memoramafacilbuffer[xp1][yp1]=0
                    memoramafacilbuffer[xp2][yp2]=0

                    print("TURNO DEL SERVIDOR")
                    xs1=datorec[2][0]
                    ys1=datorec[2][1]
                    xs2=datorec[2][2]
                    ys2=datorec[2][3]
                    memoramafacilprint[xs1][ys1]=memoramafacil[xs1][ys1]
                    memoramafacilprint[xs2][ys2]=memoramafacil[xp1][ys2]
                    memoramafacilbuffer[xs1][ys1]=memoramafacil[xs1][ys1]
                    memoramafacilbuffer[xs2][ys2]=memoramafacil[xp1][ys2]
                    print("el servidor selecciono las siguientes casillas")
                    ps1=memoramafacilprint[xs1][ys1]
                    ps2=memoramafacilprint[xs2][ys2]
                    imprimirmatriz(memoramafacilprint)
                    if ps1==ps2:
                        print("el servidor obtuvo un punto")
                        memoramafacilprint[xs1][ys1]="0"
                        memoramafacilprint[xs2][ys2]="0" 
                        puntosservidor=puntosservidor+1
                        puntajeganador=puntajeganador+1
                    else:
                        print("el servidor se equivoco")
                        memoramafacilprint[xs1][ys1]="0"
                        memoramafacilprint[xs2][ys2]="0" 
                        memoramafacilbuffer[xs1][ys1]=0
                        memoramafacilbuffer[xs2][ys2]=0 
                        
                 
            

                turno=datorec[0]
                #print("SE HAN DESTAPADO LAS SIGUIENTES CASILLAS")
                #imprimirmatriz(memoramafacilbuffer)
             
            
            
                

             
            print("TERMINO EL JUEGO")
            print(dato)
            resultadofinal=TCPClientSocket.recv(buffer_size)
            print(resultadofinal)
                                                                                                                                                                                                                                                                                                                                                                                                 

    elif dificultad=="2":
        print("elegiste  dificil")
        generartablero(memoramadificil,palabrasdificil)
        print("el tablero es el siguiente: ")
        imprimirmatriz(memoramadificilprint)
        puntajeganador=0

        while (puntajeganador!=8):
            
            
            while turno=="0":
                if puntajeganador==8:
                    dato=[]
                    dato.append("0")
                    dato.append("0")
                    dato.append("0")
                    dato.append(puntoscliente)
                    dato.append(puntosservidor)
                    dato.append("termino")
                    bufferdato=pickle.dumps(dato)
                    TCPClientSocket.send(bufferdato)
                    break
                datoenv=[]
                datorec=[]
                datoenvbuffer=[]
                datorecbuffer=[]
                print("TURNO DEL CLIENTE")
                cordenadaxp1=input("digita la fila de la casilla que quieres destapar---(0-3): ")
                cordenadayp1=input("digita la columna de la casilla que quieres destapar---(0-3): ")
                xp1=int(cordenadaxp1)
                yp1=int(cordenadayp1)
                memoramadificilprint[xp1][yp1]=memoramadificil[xp1][yp1]
                memoramadificilbuffer[xp1][yp1]=memoramadificil[xp1][yp1]
                par1=memoramadificilprint[xp1][yp1]
                cordenadaxp2=input("digita la fila de la casilla que quieres destapar---(0-3): ")
                cordenadayp2=input("digita la columna de la casilla que quieres destapar---(0-3): ")
                xp2=int(cordenadaxp2)
                yp2=int(cordenadayp2)
                memoramadificilprint[xp2][yp2]=memoramadificil[xp2][yp2]
                memoramadificilbuffer[xp2][yp2]=memoramadificil[xp2][yp2]
                par2=memoramadificilprint[xp2][yp2]   
                print("destapaste las siguientes palabras")
                imprimirmatriz(memoramadificilprint)
                
                dato=[]
                #print(dato)
                t1="1"
                
                dato.append(t1)
                dato.append(par1)
                dato.append(par2)
                dato.append(puntoscliente)
                dato.append(puntosservidor)
                dato.append("no")
                
                #print(dato)
                bufferdato=pickle.dumps(dato)
                TCPClientSocket.send(bufferdato)

                datorecbuffer=TCPClientSocket.recv(buffer_size)
                datorec=pickle.loads(datorecbuffer)
                #print(datorec)
           
                if datorec[1]=="1":
                    print("obtuviste un punto!")
                    memoramadificilprint[xp1][yp1]="0"
                    memoramadificilprint[xp2][yp2]="0"
                    puntoscliente=puntoscliente+1
                    puntajeganador=puntajeganador+1
                else:
                    print("lo siento las casillas seleccionadas no son un par")
                    memoramadificilprint[xp1][yp1]="0"
                    memoramadificilprint[xp2][yp2]="0"
                    memoramadificilbuffer[xp1][yp1]=0
                    memoramadificilbuffer[xp2][yp2]=0

                    print("TURNO DEL SERVIDOR")
                    xs1=datorec[2][0]
                    ys1=datorec[2][1]
                    xs2=datorec[2][2]
                    ys2=datorec[2][3]
                    memoramadificilprint[xs1][ys1]=memoramadificil[xs1][ys1]
                    memoramadificilprint[xs2][ys2]=memoramadificil[xp1][ys2]
                    memoramadificilbuffer[xs1][ys1]=memoramadificil[xs1][ys1]
                    memoramadificilbuffer[xs2][ys2]=memoramadificil[xp1][ys2]
                    print("el servidor selecciono las siguientes casillas")
                    ps1=memoramadificilprint[xs1][ys1]
                    ps2=memoramadificilprint[xs2][ys2]
                    imprimirmatriz(memoramadificilprint)
                    if ps1==ps2:
                        print("el servidor obtuvo un punto")
                        memoramadificilprint[xs1][ys1]="0"
                        memoramadificilprint[xs2][ys2]="0" 
                        puntosservidor=puntosservidor+1
                        puntajeganador=puntajeganador+1
                    else:
                        print("el servidor se equivoco")
                        memoramadificilprint[xs1][ys1]="0"
                        memoramadificilprint[xs2][ys2]="0" 
                        memoramadificilbuffer[xs1][ys1]=0
                        memoramadificilbuffer[xs2][ys2]=0 
                        
                 
            

                turno=datorec[0]
                #print("SE HAN DESTAPADO LAS SIGUIENTES CASILLAS")
                #imprimirmatriz(memoramadificilbuffer)
             
            
            
                

             
            print("TERMINO EL JUEGO")
            print(dato)
            resultadofinal=TCPClientSocket.recv(buffer_size)
            print(resultadofinal)

    else:
        print("no seleccionaste una dificultad valida")
    

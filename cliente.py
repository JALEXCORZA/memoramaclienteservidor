
import socket
import pickle
import random

turno="0"
t1="0"
puntaje = 0
cordenadaxp1 = 0
cordenadayp1 = 0
cordenadaxp2 = 0
cordenadayp2 = 0
puntajeganador = 0
dato=[]
datorec=[]
coordenadas=[]


def imprimirmatriz(matriz):
    #print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end="")
        print()





#HOST = "192.168.100.62"  # Hostname o  dirección IP del servidor
#PORT = 65435  # Puerto del servidor
#HOST="127.0.0.1"
buffer_size = 1024
HOST = input("digite la ip destino: ")
PORT = int(input("DIGITE EL PUERTO DESTINO: "))




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
  
    dificultad=input("ingresa la dificultad \n 1---facil \n2---dificil:\n")
    #print(dificultad)
    TCPClientSocket.sendall(dificultad.encode())
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    
    
    databuffer=pickle.loads(data)
    
    
    #print(databuffer)
    print(databuffer[0])
    imprimirmatriz(databuffer[1])
    print("el puntaje necesario para ganar es :"+str(databuffer[2]))
    puntajeganadorn=databuffer[2]
        
    while (puntajeganador!=puntajeganadorn):
        
        while turno=="0":
            
            datoenv=[]
            datorec=[]
            datoenvbuffer=[]
            datorecbuffer=[]
            coordenadas=[]
            dato=[]
            print("-----------------TURNO DEL CLIENTE--------------")
            cordenadaxp1=input("digita la fila de la casilla que quieres destapar---(0-3): ")
            cordenadayp1=input("digita la columna de la casilla que quieres destapar---(0-3): ")
            xp1=int(cordenadaxp1)
            yp1=int(cordenadayp1)
            cordenadaxp2=input("digita la fila de la casilla que quieres destapar---(0-3): ")
            cordenadayp2=input("digita la columna de la casilla que quieres destapar---(0-3): ")
            xp2=int(cordenadaxp2)
            yp2=int(cordenadayp2)
            t1="1"
            coordenadas.append(xp1)
            coordenadas.append(yp1)
            coordenadas.append(xp2)
            coordenadas.append(yp2)
            #print(coordenadas)
            dato.append(t1)
            dato.append(coordenadas)
            #print(dato)
            bufferdato=pickle.dumps(dato)
            TCPClientSocket.send(bufferdato)
            datorec=[]
            datorecbuffer=TCPClientSocket.recv(buffer_size)
            datorec=pickle.loads(datorecbuffer)
            #print(datorec)
            
            print("seleccionaste las siguientes casillas")
            imprimirmatriz(datorec[1])
            #print(datorec[2])
            if datorec[2]=="1":
                print("obtuviste un punto!")
                
            else:
                print("lo siento las casillas seleccionadas no son un par")
                print("-----------------TURNO DEL SERVIDOR------------------------")
                print("el servidor selecciono estas casillas")
                
                imprimirmatriz(datorec[3])
                print(datorec[4])
                if datorec[4]=="1":
                    print("el servidor obtuvo un punto")
                else:
                    print("el servidor se equivoco")
            #print("se han obtenido "+str(datorec[5])+" puntos en total")
            puntajeganador=datorec[5]
            if(datorec[5]==puntajeganadorn):
                
                break
            
            print(puntajeganador)
            turno=datorec[0]
    print("TERMINO EL JUEGO")
    resultadofinal=TCPClientSocket.recv(buffer_size)
    print(resultadofinal)
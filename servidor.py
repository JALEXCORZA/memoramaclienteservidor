
#!/usr/bin python3
import socket
import random
import pickle
import time
HOST = "192.168.100.62"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65435  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024

datoenv=[]
dato=[]

turno="0"
t1="0"
puntaje = 0
cordenadaxp1 = 0
cordenadayp1 = 0
cordenadaxp2 = 0
cordenadayp2 = 0
puntajeganador = 0
puntoscliente=0
puntosservidor=0
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
memoramafacilprintserver = [[0,0,0,0],
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
memoramadificilprintserver =[ [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]

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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Esperando a recibir datos... ")
        inicio=time.time()
        dificultad = Client_conn.recv(buffer_size)
        print ("Recibido,",dificultad,"   de ", Client_addr)
        print("Conectado a", Client_addr)
        if dificultad.decode()=="1":
            generartablero(memoramafacil,palabrasfacil)
            datosiniciales=[]
            datosiniciales.append("elegiste facil")
            datosiniciales.append(memoramafacilprint)
            datosiniciales.append(8)
            print(datosiniciales)
            print(type(memoramafacil))
            datosinicialesbuffer=pickle.dumps(datosiniciales)
            Client_conn.send(datosinicialesbuffer)
            puntajeganador=0
            while puntajeganador!=8:
                dato=[]
                datobuffer=[]
                datobuffer=Client_conn.recv(buffer_size)
                dato=pickle.loads(datobuffer)
                print(dato)
                turno=dato[0]
                
                while turno=="1":
                    print("puntajeganador: "+str(puntajeganador))
                    
                    print("validando datos del cliente......")
                    #print("TURNO DEL SERVIDOR")
                    xp1=dato[1][0]
                    yp1=dato[1][1]
                    xp2=dato[1][2]
                    yp2=dato[1][3]

                
                    memoramafacilprint[xp1][yp1]=memoramafacil[xp1][yp1]
                    par1=memoramafacilprint[xp1][yp1]
                    memoramafacilprint[xp2][yp2]=memoramafacil[xp2][yp2]
                    par2=memoramafacilprint[xp2][yp2]    
                    #imprimirmatriz(memoramafacilprint)
                    datoenv.append("0")
                    datoenv.append(memoramafacilprint)

                    print(datoenv)
                    
                    if par1==par2:
                        print("obtuvo un punto el cliente!")
                        datoenv.append("1")
                        datoenv.append("0")
                        datoenv.append("0")
                        
                        
                        puntajeganador=puntajeganador+1
                        puntoscliente=puntoscliente+1
                    else:
                       
                        
                        print("el cliente envio una respuesta equivocada")
                        datoenv.append("0")
                        cordenadas=[]
                        for i in range(4):
                             num=random.randint(0,3)
                             cordenadas.append(num)
                        print(cordenadas)
                        xs1=cordenadas[0]
                        ys1=cordenadas[1]
                        xs2=cordenadas[2]
                        ys2=cordenadas[3]
                        memoramafacilprintserver[xs1][ys1]=memoramafacil[xs1][ys1]
                        memoramafacilprintserver[xs2][ys2]=memoramafacil[xs2][ys2]
                        
                        print("el servidor selecciono las siguientes casillas")
                        ps1=memoramafacilprintserver[xs1][ys1]
                        ps2=memoramafacilprintserver[xs2][ys2]
                        imprimirmatriz(memoramafacilprintserver)
                        datoenv.append(memoramafacilprintserver)
                        print(datoenv)
                        if ps1==ps2:
                            print("el servidor obtuvo un punto")
                            
                            datoenv.append("1")
                            puntajeganador=puntajeganador+1
                            puntosservidor=puntosservidor+1
                    
                        else:
                            print("el servidor se equivoco")
                            datoenv.append("0")
                        
                        #memoramafacilprint[xp1][yp1]="0"
                        #memoramafacilprint[xp2][yp2]="0" 
                     
                    datoenv.append(puntajeganador)
                    print(datoenv)
                    datoenvbuffer=pickle.dumps(datoenv)
                    Client_conn.send(datoenvbuffer)
                    memoramafacilprint[xp1][yp1]="0"
                    memoramafacilprint[xp2][yp2]="0" 
                    datobuffer=[]
                    datoenv=[]
                    turno="0"
            print(f"puntos del cliente:{puntoscliente}")
            print(f"puntos del servidor:{puntosservidor}")

            fin=time.time()
            tiempo=fin-inicio
            if puntoscliente>puntosservidor:
                ganador="el ganador es el cliente con "+str(puntoscliente)+" puntos"
            elif puntosservidor>puntoscliente:
                ganador="el ganador es el servidor con "+str(puntosservidor)+" puntos"
            else:
                ganador="empate"

            puntajefinal=ganador+" y el tiempo que tardo la partida es : "+str(tiempo)+" segundos"
            Client_conn.send(puntajefinal.encode())     
            print("TERMINO EL JUEGO")      

        elif dificultad.decode()=="2":
            generartablero(memoramadificil,palabrasdificil)
            datosiniciales=[]
            datosiniciales.append("elegiste dificil")
            datosiniciales.append(memoramadificil)
            datosiniciales.append(16)
            print(datosiniciales)
            print(type(memoramadificil))
            datosinicialesbuffer=pickle.dumps(datosiniciales)
            Client_conn.send(datosinicialesbuffer)
            puntajeganador=0
            while puntajeganador!=16:
                dato=[]
                datobuffer=[]
                datobuffer=Client_conn.recv(buffer_size)
                dato=pickle.loads(datobuffer)
                print(dato)
                turno=dato[0]
                
                while turno=="1":
                    print("puntajeganador: "+str(puntajeganador))
                    
                    print("validando datos del cliente......")
                    #print("TURNO DEL SERVIDOR")
                    xp1=dato[1][0]
                    yp1=dato[1][1]
                    xp2=dato[1][2]
                    yp2=dato[1][3]

                
                    memoramadificilprint[xp1][yp1]=memoramadificil[xp1][yp1]
                    par1=memoramadificilprint[xp1][yp1]
                    memoramadificilprint[xp2][yp2]=memoramadificil[xp2][yp2]
                    par2=memoramadificilprint[xp2][yp2]    
                    #imprimirmatriz(memoramadificilprint)
                    datoenv.append("0")
                    datoenv.append(memoramadificilprint)

                    print(datoenv)
                    
                    if par1==par2:
                        print("obtuvo un punto el cliente!")
                        datoenv.append("1")
                        datoenv.append("0")
                        datoenv.append("0")
                        
                        
                        puntajeganador=puntajeganador+1
                        puntoscliente=puntoscliente+1
                    else:
                       
                        
                        print("el cliente envio una respuesta equivocada")
                        datoenv.append("0")
                        cordenadas=[]
                        for i in range(4):
                             num=random.randint(0,3)
                             cordenadas.append(num)
                        print(cordenadas)
                        xs1=cordenadas[0]
                        ys1=cordenadas[1]
                        xs2=cordenadas[2]
                        ys2=cordenadas[3]
                        memoramadificilprintserver[xs1][ys1]=memoramadificil[xs1][ys1]
                        memoramadificilprintserver[xs2][ys2]=memoramadificil[xs2][ys2]
                        
                        print("el servidor selecciono las siguientes casillas")
                        ps1=memoramadificilprintserver[xs1][ys1]
                        ps2=memoramadificilprintserver[xs2][ys2]
                        imprimirmatriz(memoramadificilprintserver)
                        datoenv.append(memoramadificilprintserver)
                        print(datoenv)
                        if ps1==ps2:
                            print("el servidor obtuvo un punto")
                            
                            datoenv.append("1")
                            puntajeganador=puntajeganador+1
                            puntosservidor=puntosservidor+1
                    
                        else:
                            print("el servidor se equivoco")
                            datoenv.append("0")
                        
                        #memoramadificilprint[xp1][yp1]="0"
                        #memoramadificilprint[xp2][yp2]="0" 
                     
                    datoenv.append(puntajeganador)
                    print(datoenv)
                    datoenvbuffer=pickle.dumps(datoenv)
                    Client_conn.send(datoenvbuffer)
                    memoramadificilprint[xp1][yp1]="0"
                    memoramadificilprint[xp2][yp2]="0" 
                    datobuffer=[]
                    datoenv=[]
                    turno="0"
            print(f"puntos del cliente:{puntoscliente}")
            print(f"puntos del servidor:{puntosservidor}")

            fin=time.time()
            tiempo=fin-inicio
            if puntoscliente>puntosservidor:
                ganador="el ganador es el cliente con "+str(puntoscliente)+" puntos"
            elif puntosservidor>puntoscliente:
                ganador="el ganador es el servidor con "+str(puntosservidor)+" puntos"
            else:
                ganador="empate"

            puntajefinal=ganador+" y el tiempo que tardo la partida es : "+str(tiempo)+" segundos"
            Client_conn.send(puntajefinal.encode())     
            print("TERMINO EL JUEGO")
        else:
            Client_conn.sendall(b"selecciona una dificultad valida")
        #while True:
            
            #if not dificultad:
             #   break
            
	      
           
            








